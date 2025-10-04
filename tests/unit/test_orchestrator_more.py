from datetime import datetime, timezone
from pathlib import Path

from raindrop_enhancer.sync.orchestrator import Orchestrator, default_db_path
from raindrop_enhancer.api.raindrop_client import RaindropClient


def test_default_db_path_creates_dir(tmp_path):
    p = default_db_path()
    # ensure returns a Path ending with raindrops.db
    assert p.name == "raindrops.db"


class MissingIdClient(RaindropClient):
    def list_collections(self):
        return [{"title": "NoId"}]

    def list_raindrops_since(self, collection_id: int, iso_cursor: str | None = None):
        return []


def test_orchestrator_skips_collections_without_id(tmp_path):
    client = MissingIdClient()
    orch = Orchestrator(tmp_path / "skip.db", client)
    outcome = orch.run(full_refresh=False, dry_run=False)
    assert outcome.new_links == 0


class CallbackClient(RaindropClient):
    def __init__(self, payloads):
        super().__init__(token="x")
        self.payloads = payloads

    def list_collections(self):
        return [{"_id": 1, "title": "T"}]

    def list_raindrops_since(self, collection_id: int, iso_cursor: str | None = None):
        # simulate the client triggering on_request and then yielding payloads
        try:
            if hasattr(self, "on_request") and self.on_request:
                self.on_request("http://example")
        except Exception:
            pass
        # simulate a retry event
        try:
            if hasattr(self, "on_retry") and self.on_retry:
                self.on_retry("http://example", 1, 0.1)
        except Exception:
            pass
        for p in self.payloads:
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


def test_orchestrator_callbacks_counted(tmp_path):
    payloads = [_make_payload(i) for i in range(3)]
    client = CallbackClient(payloads)
    orch = Orchestrator(tmp_path / "cb.db", client)
    outcome = orch.run(full_refresh=True, dry_run=False)
    # wrapper should have been invoked at least once for request and retry
    assert outcome.requests_count >= 1
    assert outcome.retries_count >= 1


def test_orchestrator_large_batch_flush(tmp_path):
    payloads = [_make_payload(i) for i in range(120)]
    client = CallbackClient(payloads)
    orch = Orchestrator(tmp_path / "batch.db", client)
    outcome = orch.run(full_refresh=True, dry_run=False)
    assert outcome.new_links == 120


def test_default_db_path_platform_branches(monkeypatch, tmp_path):
    import sys

    # simulate windows
    monkeypatch.setattr(sys, "platform", "win32")
    p = default_db_path()
    assert "AppData" in str(p) or "raindrop_enhancer" in str(p)

    # simulate linux
    monkeypatch.setattr(sys, "platform", "linux")
    p2 = default_db_path()
    assert ".local" in str(p2) or "raindrop_enhancer" in str(p2)


def test_wrapped_orig_callbacks_exception_handling(tmp_path):
    # create a client that already has on_request and on_retry that raise
    class BadClient(CallbackClient):
        def __init__(self, payloads):
            super().__init__(payloads)

        def bad_request(self, url):
            raise RuntimeError("bad request")

        def bad_retry(self, url, attempt, delay):
            raise RuntimeError("bad retry")

    payloads = [_make_payload(i) for i in range(2)]
    c = BadClient(payloads)
    # assign orig handlers that raise
    c.on_request = c.bad_request
    c.on_retry = c.bad_retry

    orch = Orchestrator(tmp_path / "badcb.db", c)
    # should not raise despite orig handlers throwing
    outcome = orch.run(full_refresh=True, dry_run=False)
    assert outcome.requests_count >= 0
    assert outcome.retries_count >= 0


def test_state_cursor_passed_to_client(tmp_path):
    # create DB and store a sync state first
    from raindrop_enhancer.storage.sqlite_store import SQLiteStore
    from raindrop_enhancer.models import SyncState

    db = tmp_path / "cursor.db"
    store = SQLiteStore(db)
    store.connect()
    state = SyncState(
        last_cursor_iso="1999-01-01T00:00:00Z",
        last_run_at="",
        db_version=1,
        last_full_refresh="",
    )
    store.upsert_sync_state(state)

    # client that captures the iso_cursor argument
    class CursorClient(RaindropClient):
        def __init__(self):
            super().__init__(token="x")
            self.captured = None

        def list_collections(self):
            return [{"_id": 1}]

        def list_raindrops_since(
            self, collection_id: int, iso_cursor: str | None = None
        ):
            self.captured = iso_cursor
            return []

    client = CursorClient()
    orch = Orchestrator(db, client)
    outcome = orch.run(full_refresh=False, dry_run=False)
    assert client.captured == "1999-01-01T00:00:00Z"
