from datetime import datetime, timedelta, timezone
from pathlib import Path

from raindrop_enhancer.api.raindrop_client import RaindropClient
from raindrop_enhancer.sync.orchestrator import Orchestrator


class StubClient(RaindropClient):
    def __init__(self, payloads):
        super().__init__(token="stub")
        self._payloads = payloads

    def list_collections(self):
        return [{"_id": 1, "title": "Test"}]

    def list_raindrops_since(self, collection_id: int, iso_cursor: str | None = None):
        for p in self._payloads:
            yield p


def _make_payloads(n: int, start: datetime | None = None):
    start = start or (datetime.now(timezone.utc) - timedelta(seconds=n))
    out = []
    for i in range(n):
        created_dt = (start + timedelta(seconds=i)).astimezone(timezone.utc)
        created = created_dt.isoformat().replace("+00:00", "Z")
        out.append(
            {
                "_id": i + 1,
                "collectionId": 1,
                "title": f"T{i}",
                "link": f"https://x/{i}",
                "created": created,
                "tags": [],
            }
        )
    return out


def test_baseline_sync_behavior(tmp_path: Path):
    db = tmp_path / "test.db"
    payloads = _make_payloads(5)
    client = StubClient(payloads)
    orch = Orchestrator(db, client)
    outcome = orch.run(full_refresh=True, dry_run=False)
    assert outcome.new_links == 5
    assert outcome.total_links == 5


def test_full_refresh_flag_resets_db(tmp_path: Path):
    db = tmp_path / "test.db"
    payloads = _make_payloads(3)
    client = StubClient(payloads)
    orch = Orchestrator(db, client)
    outcome1 = orch.run(full_refresh=True, dry_run=False)
    assert outcome1.new_links == 3

    # Run again with different payloads and full_refresh -> should backup and recreate
    payloads2 = _make_payloads(2)
    client2 = StubClient(payloads2)
    orch2 = Orchestrator(db, client2)
    outcome2 = orch2.run(full_refresh=True, dry_run=False)
    assert outcome2.new_links == 2


def test_incremental_updates_cursor_and_dry_run(tmp_path: Path):
    db = tmp_path / "test.db"
    # initial payloads
    payloads = _make_payloads(3)
    client = StubClient(payloads)
    orch = Orchestrator(db, client)
    outcome1 = orch.run(full_refresh=True, dry_run=False)
    assert outcome1.new_links == 3

    # Now simulate new items but run as dry-run -> should not update sync_state
    new_payloads = _make_payloads(2, start=datetime.now(timezone.utc))
    # ensure new IDs that don't collide with the baseline (offset by 100)
    for idx, p in enumerate(new_payloads):
        p["_id"] = 100 + idx
    client2 = StubClient(new_payloads)
    orch2 = Orchestrator(db, client2)
    outcome_dry = orch2.run(full_refresh=False, dry_run=True)
    assert outcome_dry.new_links == 0

    # After a real run, the cursor updates and new items are inserted
    orch3 = Orchestrator(db, client2)
    outcome_real = orch3.run(full_refresh=False, dry_run=False)
    assert outcome_real.new_links == 2
