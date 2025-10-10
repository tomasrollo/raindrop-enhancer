"""SQLite storage implementation for Raindrop archive.

Provides schema creation, WAL mode enablement, batch inserts, sync_state management,
and basic corruption checks via PRAGMA quick_check.
"""

from __future__ import annotations

import sqlite3
from dataclasses import dataclass
import logging
from datetime import datetime, timezone
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


Logger = logging.getLogger(__name__)
Logger.debug("Started logging in sqlite_store.py")


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

    # --- Migration helpers -------------------------------------------------
    def _ensure_content_columns(self) -> None:
        """Ensure new columns for content capture exist; add them if missing.

        This method is idempotent and safe to call on every connect.
        """
        assert self.conn
        cur = self.conn.cursor()
        try:
            cur.execute("PRAGMA table_info(raindrop_links)")
            cols = {r[1] for r in cur.fetchall()}
            to_add = []
            if "content_markdown" not in cols:
                to_add.append(
                    "ALTER TABLE raindrop_links ADD COLUMN content_markdown TEXT DEFAULT NULL"
                )
            if "content_fetched_at" not in cols:
                to_add.append(
                    "ALTER TABLE raindrop_links ADD COLUMN content_fetched_at TEXT DEFAULT NULL"
                )
            if "content_source" not in cols:
                to_add.append(
                    "ALTER TABLE raindrop_links ADD COLUMN content_source TEXT DEFAULT 'trafilatura'"
                )

            for stmt in to_add:
                cur.execute(stmt)
            if to_add:
                # bump user_version to indicate migration
                cur.execute("PRAGMA user_version = 2")
                self.conn.commit()
        finally:
            cur.close()

    def _ensure_tagging_columns(self) -> None:
        """Ensure columns for auto-generated tags exist on raindrop_links.

        Adds `auto_tags_json` and `auto_tags_meta_json` as nullable TEXT columns.
        This method is idempotent and will bump PRAGMA user_version to 3 when applied.
        """
        assert self.conn
        cur = self.conn.cursor()
        try:
            cur.execute("PRAGMA table_info(raindrop_links)")
            cols = {r[1] for r in cur.fetchall()}
            to_add = []
            if "auto_tags_json" not in cols:
                to_add.append(
                    "ALTER TABLE raindrop_links ADD COLUMN auto_tags_json TEXT DEFAULT NULL"
                )
            if "auto_tags_meta_json" not in cols:
                to_add.append(
                    "ALTER TABLE raindrop_links ADD COLUMN auto_tags_meta_json TEXT DEFAULT NULL"
                )

            for stmt in to_add:
                cur.execute(stmt)
            if to_add:
                # bump user_version to indicate migration applied
                cur.execute("PRAGMA user_version = 3")
                self.conn.commit()
        finally:
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

    # --- Content selection / update helpers -------------------------------
    def select_uncaptured(self, limit: Optional[int] = None) -> List[tuple]:
        """Return list of (raindrop_id, url) for links without content_markdown.

        Ordered by synced_at ascending to pick oldest first.
        """
        assert self.conn
        cur = self.conn.cursor()
        try:
            q = "SELECT raindrop_id, url FROM raindrop_links WHERE content_markdown IS NULL ORDER BY synced_at"
            try:
                if limit:
                    q = q + " LIMIT ?"
                    cur.execute(q, (limit,))
                else:
                    cur.execute(q)
            except sqlite3.OperationalError as e:
                # Fallback for databases that don't have the content_* columns yet
                msg = str(e).lower()
                if "no such column" in msg:
                    q2 = (
                        "SELECT raindrop_id, url FROM raindrop_links ORDER BY synced_at"
                    )
                    if limit:
                        q2 = q2 + " LIMIT ?"
                        cur.execute(q2, (limit,))
                    else:
                        cur.execute(q2)
                else:
                    raise
            return [(int(r[0]), r[1]) for r in cur.fetchall()]
        finally:
            cur.close()

    def select_all_links(self, limit: Optional[int] = None) -> List[tuple]:
        """Return list of (raindrop_id, url) for all links ordered by synced_at."""
        assert self.conn
        cur = self.conn.cursor()
        try:
            q = "SELECT raindrop_id, url FROM raindrop_links ORDER BY synced_at"
            if limit:
                q = q + " LIMIT ?"
                cur.execute(q, (limit,))
            else:
                cur.execute(q)
            return [(int(r[0]), r[1]) for r in cur.fetchall()]
        finally:
            cur.close()

    def update_content(
        self, link_id: int, markdown: str, source: str = "trafilatura"
    ) -> None:
        assert self.conn
        cur = self.conn.cursor()
        try:
            cur.execute(
                "UPDATE raindrop_links SET content_markdown = ?, content_fetched_at = ?, content_source = ? WHERE raindrop_id = ?",
                (markdown, datetime.now(timezone.utc).isoformat(), source, link_id),
            )
            self.conn.commit()
        finally:
            cur.close()

    def clear_content_for_link(self, link_id: int) -> None:
        assert self.conn
        cur = self.conn.cursor()
        try:
            cur.execute(
                "UPDATE raindrop_links SET content_markdown = NULL, content_fetched_at = NULL WHERE raindrop_id = ?",
                (link_id,),
            )
            self.conn.commit()
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
            # Determine which raindrop_ids already exist to provide deterministic
            # inserted count and helpful debug information.
            ids = [int(t[0]) for t in to_insert]
            # Prepare a safe parameter list for IN clause
            placeholders = ",".join(["?" for _ in ids]) if ids else ""
            existing_ids = set()
            if ids:
                cur.execute(
                    f"SELECT raindrop_id FROM raindrop_links WHERE raindrop_id IN ({placeholders})",
                    ids,
                )
                rows = cur.fetchall()
                existing_ids = {int(r[0]) for r in rows}

            new_ids = [i for i in ids if i not in existing_ids]
            Logger.debug(
                "Inserting batch: total=%d, existing=%d, new=%d",
                len(ids),
                len(existing_ids),
                len(new_ids),
            )

            cur.execute("BEGIN")
            cur.executemany(
                "INSERT OR IGNORE INTO raindrop_links (raindrop_id, collection_id, collection_title, title, url, created_at, synced_at, tags_json, raw_payload) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)",
                to_insert,
            )
            # count after (within same transaction)
            cur.execute("SELECT COUNT(*) FROM raindrop_links")
            after = int(cur.fetchone()[0])
            # count before is after - number inserted by this exec
            inserted = len(new_ids)
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
                self.path.suffix + f".{int(datetime.now(timezone.utc).timestamp())}.bak"
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

    # --- Tagging helpers -------------------------------------------------
    def fetch_untagged_links(self, limit: Optional[int] = None) -> List[tuple]:
        """Return list of (raindrop_id, title, url, content_markdown) for links with no auto_tags_json.

        Ordered by synced_at ascending.
        """
        assert self.conn
        cur = self.conn.cursor()
        try:
            # Inspect columns to handle older DBs without migration columns
            cur.execute("PRAGMA table_info(raindrop_links)")
            cols = {r[1] for r in cur.fetchall()}

            select_fields = ["raindrop_id", "title", "url"]
            if "content_markdown" in cols:
                select_fields.append("content_markdown")
            else:
                select_fields.append("NULL as content_markdown")

            # If auto_tags_json doesn't exist, treat all rows as untagged.
            # If the column exists, consider rows untagged when the column is NULL,
            # empty, or contains an empty list literal '[]'. This handles cases
            # where tags were written as an empty JSON array or an empty string.
            if "auto_tags_json" in cols:
                where = "(auto_tags_json IS NULL OR trim(auto_tags_json) = '' OR trim(auto_tags_json) = '[]')"
            else:
                where = "1=1"

            q = f"SELECT {', '.join(select_fields)} FROM raindrop_links WHERE {where} ORDER BY synced_at"
            if limit:
                q = q + " LIMIT ?"
                cur.execute(q, (limit,))
            else:
                cur.execute(q)

            rows = cur.fetchall()
            Logger.debug(
                "fetch_untagged_links: query=%s limit=%r returned=%d rows",
                q,
                limit,
                len(rows),
            )
            return [(int(r[0]), r[1], r[2], r[3]) for r in rows]
        finally:
            cur.close()

    def write_auto_tags_batch(self, entries: List[tuple]) -> None:
        """Write auto_tags_json and auto_tags_meta_json for multiple links in a single transaction.

        entries: List of (raindrop_id, auto_tags_json_str, auto_tags_meta_json_str)
        """
        assert self.conn
        cur = self.conn.cursor()
        try:
            # Ensure tagging columns exist (safe to call multiple times)
            cur.execute("PRAGMA table_info(raindrop_links)")
            cols = {r[1] for r in cur.fetchall()}
            to_add = []
            if "auto_tags_json" not in cols:
                to_add.append(
                    "ALTER TABLE raindrop_links ADD COLUMN auto_tags_json TEXT DEFAULT NULL"
                )
            if "auto_tags_meta_json" not in cols:
                to_add.append(
                    "ALTER TABLE raindrop_links ADD COLUMN auto_tags_meta_json TEXT DEFAULT NULL"
                )
            for stmt in to_add:
                cur.execute(stmt)

            cur.execute("BEGIN")
            cur.executemany(
                "UPDATE raindrop_links SET auto_tags_json = ?, auto_tags_meta_json = ? WHERE raindrop_id = ?",
                [(e[1], e[2], e[0]) for e in entries],
            )
            self.conn.commit()
        except Exception:
            self.conn.rollback()
            raise
        finally:
            cur.close()
