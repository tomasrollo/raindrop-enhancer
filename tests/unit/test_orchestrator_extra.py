import sqlite3
from datetime import datetime, timezone
from pathlib import Path

from raindrop_enhancer.sync.orchestrator import Orchestrator
from raindrop_enhancer.api.raindrop_client import RaindropClient


class EmptyClient(RaindropClient):
    def __init__(self):
        super().__init__(token="x")

    def list_collections(self):
        return []


class StubClient(RaindropClient):
    def __init__(self, payloads):
        super().__init__(token="x")
        self._payloads = payloads
        self._requests = 0

    def list_collections(self):
        return [{"_id": 1, "title": "Test"}]

    def list_raindrops_since(self, collection_id: int, iso_cursor: str | None = None):
        self._requests += 1
        for p in self._payloads:
            yield p


def _make_payload(i: int):
    created = datetime.now(timezone.utc).isoformat().replace("+00:00", "Z")
    return {
        "_id": i,
        "collectionId": 1,
        "title": f"T{i}",
        "link": "https://x",
        "created": created,
        "tags": [],
    }


def test_orchestrator_empty_collections(tmp_path):
    client = EmptyClient()
    orch = Orchestrator(tmp_path / "test_empty.db", client)
    outcome = orch.run(full_refresh=False, dry_run=False)
    assert outcome.new_links == 0


def test_orchestrator_dry_run_and_callbacks(tmp_path):
    payloads = [_make_payload(i) for i in range(3)]
    client = StubClient(payloads)
    db = tmp_path / "test_cb.db"
    orch = Orchestrator(db, client)

    # set a custom on_retry handler to ensure it doesn't break callback chaining
    def on_retry(url, attempt, delay):
        # no-op
        pass

    client.on_retry = on_retry

    outcome = orch.run(full_refresh=True, dry_run=True)
    # dry-run should not write DB
    assert not db.exists()
    # but outcome should be produced
    assert hasattr(outcome, "new_links")


def test_orchestrator_full_refresh_creates_backup(tmp_path):
    payloads = [_make_payload(i) for i in range(2)]
    client = StubClient(payloads)
    db = tmp_path / "test_full.db"
    orch = Orchestrator(db, client)

    # first run to create DB
    outcome1 = orch.run(full_refresh=True, dry_run=False)
    assert outcome1.new_links == 2

    # Running full_refresh again should create a backup of the previous DB and recreate
    outcome2 = orch.run(full_refresh=True, dry_run=False)
    assert db.exists()

    # Now simulate a corrupted file and ensure backup_db can be invoked without connecting
    orch.store.close()
    # corrupt underlying file
    db.write_bytes(b"corrupt")
    # call backup_db on a store instance that isn't connected; it should create a .bak
    s = orch.store
    bak = s.backup_db()
    assert bak.exists()
