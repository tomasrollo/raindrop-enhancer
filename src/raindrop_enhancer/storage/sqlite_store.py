"""SQLite storage implementation for Raindrop archive.

Provides schema creation, WAL mode enablement, batch inserts, sync_state management,
and basic corruption checks via PRAGMA quick_check.
"""

from __future__ import annotations

import sqlite3
from dataclasses import dataclass
from datetime import datetime
from pathlib import Path
from typing import Iterable, List, Optional

from ..models import RaindropLink, SyncState


DB_SCHEMA = """
CREATE TABLE IF NOT EXISTS raindrop_links (
    raindrop_id INTEGER PRIMARY KEY,
    collection_id INTEGER NOT NULL,
    collection_title TEXT NOT NULL,
    title TEXT NOT NULL,
    url TEXT NOT NULL,
    created_at TEXT NOT NULL,
    synced_at TEXT NOT NULL,
    tags_json TEXT NOT NULL,
    raw_payload TEXT NOT NULL
);
CREATE INDEX IF NOT EXISTS idx_links_created_at ON raindrop_links(created_at);
CREATE INDEX IF NOT EXISTS idx_links_collection_created ON raindrop_links(collection_id, created_at);

CREATE TABLE IF NOT EXISTS sync_state (
    id INTEGER PRIMARY KEY CHECK (id = 1),
    last_cursor_iso TEXT NOT NULL,
    last_run_at TEXT NOT NULL,
    db_version INTEGER NOT NULL,
    last_full_refresh TEXT NOT NULL
);
PRAGMA user_version = 1;
"""


class SQLiteStore:
    def __init__(self, path: Path | str):
        self.path = Path(path)
        self.path.parent.mkdir(parents=True, exist_ok=True)
        self.conn: Optional[sqlite3.Connection] = None

    def connect(self) -> None:
        if self.conn is not None:
            return
        self.conn = sqlite3.connect(
            str(self.path), detect_types=sqlite3.PARSE_DECLTYPES
        )
        self.conn.row_factory = sqlite3.Row
        self._enable_wal()
        self._ensure_schema()

    def close(self) -> None:
        if self.conn:
            try:
                self.conn.close()
            finally:
                self.conn = None

    def _enable_wal(self) -> None:
        assert self.conn
        cur = self.conn.cursor()
        cur.execute("PRAGMA journal_mode=WAL")
        cur.close()

    def _ensure_schema(self) -> None:
        assert self.conn
        cur = self.conn.cursor()
        cur.executescript(DB_SCHEMA)
        self.conn.commit()
        cur.close()

    def quick_check(self) -> bool:
        """Run PRAGMA quick_check and return True if OK."""
        assert self.conn
        cur = self.conn.cursor()
        try:
            cur.execute("PRAGMA quick_check")
            rows = cur.fetchall()
            return all(r[0] == "ok" for r in rows)
        finally:
            cur.close()

    def insert_batch(self, links: Iterable[RaindropLink]) -> int:
        """Insert multiple RaindropLink records atomically. Returns number inserted."""
        assert self.conn
        to_insert = [
            (
                l.raindrop_id,
                l.collection_id,
                l.collection_title,
                l.title,
                l.url,
                l.created_at,
                l.synced_at,
                l.tags_json,
                l.raw_payload,
            )
            for l in links
        ]
        if not to_insert:
            return 0
        cur = self.conn.cursor()
        try:
            cur.execute("BEGIN")
            # count before
            cur.execute("SELECT COUNT(*) FROM raindrop_links")
            before = int(cur.fetchone()[0])
            cur.executemany(
                "INSERT OR IGNORE INTO raindrop_links (raindrop_id, collection_id, collection_title, title, url, created_at, synced_at, tags_json, raw_payload) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)",
                to_insert,
            )
            # count after (within same transaction)
            cur.execute("SELECT COUNT(*) FROM raindrop_links")
            after = int(cur.fetchone()[0])
            inserted = after - before
            self.conn.commit()
            return inserted
        except Exception:
            self.conn.rollback()
            raise
        finally:
            cur.close()

    def get_sync_state(self) -> Optional[SyncState]:
        assert self.conn
        cur = self.conn.cursor()
        try:
            cur.execute(
                "SELECT last_cursor_iso, last_run_at, db_version, last_full_refresh FROM sync_state WHERE id = 1"
            )
            row = cur.fetchone()
            if not row:
                return None
            return SyncState(
                last_cursor_iso=row[0],
                last_run_at=row[1],
                db_version=int(row[2]),
                last_full_refresh=row[3],
            )
        finally:
            cur.close()

    def upsert_sync_state(self, state: SyncState) -> None:
        assert self.conn
        cur = self.conn.cursor()
        try:
            cur.execute(
                "INSERT OR REPLACE INTO sync_state (id, last_cursor_iso, last_run_at, db_version, last_full_refresh) VALUES (1, ?, ?, ?, ?)",
                (
                    state.last_cursor_iso,
                    state.last_run_at,
                    state.db_version,
                    state.last_full_refresh,
                ),
            )
            self.conn.commit()
        finally:
            cur.close()

    def backup_db(self) -> Path:
        """Create a timestamped backup of the DB file and return the backup path."""
        # If DB isn't on disk yet, return original path
        if not self.path.exists():
            return self.path
        bak = self.path.with_suffix(self.path.suffix + ".bak")
        # if bak exists, append timestamp
        if bak.exists():
            bak = self.path.with_suffix(
                self.path.suffix + f".{int(datetime.utcnow().timestamp())}.bak"
            )
        from shutil import copy2

        self.close()
        copy2(self.path, bak)
        return bak

    def count_links(self) -> int:
        assert self.conn
        cur = self.conn.cursor()
        try:
            cur.execute("SELECT COUNT(*) FROM raindrop_links")
            return int(cur.fetchone()[0])
        finally:
            cur.close()
