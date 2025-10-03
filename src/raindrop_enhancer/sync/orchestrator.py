"""Sync orchestrator: baseline and incremental flows for Raindrop archive."""

from __future__ import annotations

from datetime import datetime
from pathlib import Path
from typing import Iterable

from ..api.raindrop_client import RaindropClient
from ..models import Raindrop, RaindropLink, SyncOutcome, SyncState
from ..storage.sqlite_store import SQLiteStore
from typing import Optional


def default_db_path() -> Path:
    # Platform-specific default paths per spec (minimal mapping)
    from sys import platform

    if platform.startswith("darwin"):
        base = Path.home() / "Library" / "Application Support" / "raindrop_enhancer"
    elif platform.startswith("win"):
        base = Path.home() / "AppData" / "Roaming" / "raindrop_enhancer"
    else:
        base = Path.home() / ".local" / "share" / "raindrop_enhancer"
    base.mkdir(parents=True, exist_ok=True)
    return base / "raindrops.db"


def _now_iso() -> str:
    return datetime.utcnow().isoformat() + "Z"


class Orchestrator:
    def __init__(self, db_path: Path | str, client: RaindropClient):
        self.db_path = Path(db_path)
        self.client = client
        self.store = SQLiteStore(self.db_path)

    def run(self, full_refresh: bool = False, dry_run: bool = False) -> SyncOutcome:
        started = datetime.utcnow()
        self.store.connect()

        if not self.store.quick_check():
            raise RuntimeError("Database integrity check failed")
        state = self.store.get_sync_state()

        was_full = False
        if full_refresh or state is None:
            # baseline: no state or full refresh requested
            was_full = True
            if not dry_run:
                # create a backup first
                _ = self.store.backup_db()
                # recreate db file (store.backup_db closes the connection)
                if self.db_path.exists():
                    try:
                        self.db_path.unlink()
                    except Exception:
                        pass
                self.store = SQLiteStore(self.db_path)
                self.store.connect()

        # metrics and tracking
        total_inserted = 0
        total_seen = 0
        requests_count = 0
        retries_count = 0
        max_created_iso: Optional[str] = None

        # wrap client's callbacks to count requests/retries without clobbering existing handlers
        orig_on_request = getattr(self.client, "on_request", None)
        orig_on_retry = getattr(self.client, "on_retry", None)

        def _on_request(url: str) -> None:
            nonlocal requests_count
            requests_count += 1
            if orig_on_request:
                try:
                    orig_on_request(url)
                except Exception:
                    pass

        def _on_retry(url: str, attempt: int, delay: float) -> None:
            nonlocal retries_count
            retries_count += 1
            if orig_on_retry:
                try:
                    orig_on_retry(url, attempt, delay)
                except Exception:
                    pass

        self.client.on_request = _on_request
        self.client.on_retry = _on_retry

        for coll in self.client.list_collections():
            cid = coll.get("_id") or coll.get("id")
            if cid is None:
                continue
            iterator = self.client.list_raindrops_since(
                int(cid), state.last_cursor_iso if state else None
            )
            batch = []
            for item in iterator:
                total_seen += 1
                r = Raindrop.from_api(item, collection_title=coll.get("title", ""))
                # track max created timestamp seen
                try:
                    created_iso = r.created_at.isoformat()
                except Exception:
                    created_iso = None
                if created_iso:
                    if max_created_iso is None or created_iso > max_created_iso:
                        max_created_iso = created_iso
                link = RaindropLink.from_raindrop(r, synced_at=datetime.utcnow())
                batch.append(link)
                if len(batch) >= 100:
                    if not dry_run:
                        inserted = self.store.insert_batch(batch)
                        total_inserted += inserted
                    batch = []
            if batch:
                if not dry_run:
                    inserted = self.store.insert_batch(batch)
                    total_inserted += inserted

        # compute total_links
        total_links = 0
        if not dry_run:
            total_links = self.store.count_links()

        # update sync state
        now_iso = _now_iso()
        if not dry_run:
            # set last_cursor_iso to observed max_created_iso if available, otherwise now
            cursor = max_created_iso or _now_iso()
            new_state = SyncState(
                last_cursor_iso=cursor,
                last_run_at=now_iso,
                db_version=1,
                last_full_refresh=now_iso if was_full else "",
            )
            self.store.upsert_sync_state(new_state)

        finished = datetime.utcnow()
        outcome = SyncOutcome(
            run_started_at=started,
            run_finished_at=finished,
            new_links=total_inserted,
            total_links=total_links,
            was_full_refresh=was_full,
            db_path=self.db_path,
        )
        outcome.requests_count = requests_count
        outcome.retries_count = retries_count
        return outcome
