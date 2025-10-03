from datetime import datetime, timedelta
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
    start = start or datetime.utcnow() - timedelta(seconds=n)
    out = []
    for i in range(n):
        created = (start + timedelta(seconds=i)).isoformat() + "Z"
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
