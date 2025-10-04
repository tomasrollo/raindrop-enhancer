import json
from click.testing import CliRunner
from datetime import datetime, timedelta, timezone

from raindrop_enhancer.cli import sync


class StubClient:
    payloads = []

    def __init__(self, token=None, **kwargs):
        pass

    def list_collections(self):
        return [{"_id": 1, "title": "Test"}]

    def list_raindrops_since(self, collection_id: int, iso_cursor: str | None = None):
        for p in StubClient.payloads:
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


def test_cli_baseline_and_incremental(tmp_path, monkeypatch):
    runner = CliRunner()
    db = tmp_path / "test.db"
    # monkeypatch RaindropClient in cli module
    monkeypatch.setattr("raindrop_enhancer.cli.RaindropClient", StubClient)
    # baseline run
    StubClient.payloads = _make_payloads(5)
    result = runner.invoke(
        sync, ["--db-path", str(db), "--json"], env={"RAINDROP_TOKEN": "x"}
    )
    assert result.exit_code == 0
    out = json.loads(result.output)
    assert out["new_links"] == 5
    assert out["total_links"] == 5

    # ensure DB file exists and contains 5 links
    from raindrop_enhancer.storage.sqlite_store import SQLiteStore

    store = SQLiteStore(db)
    store.connect()
    assert store.count_links() == 5

    # incremental run: no new items
    StubClient.payloads = []
    result2 = runner.invoke(
        sync, ["--db-path", str(db), "--json"], env={"RAINDROP_TOKEN": "x"}
    )
    assert result2.exit_code == 0
    out2 = json.loads(result2.output)
    assert out2["new_links"] == 0

    # DB still has 5 links
    assert store.count_links() == 5


def test_cli_full_refresh_and_dry_run(tmp_path, monkeypatch):
    runner = CliRunner()
    db = tmp_path / "test.db"
    monkeypatch.setattr("raindrop_enhancer.cli.RaindropClient", StubClient)
    StubClient.payloads = _make_payloads(3)
    # dry-run with full-refresh should not error and should return JSON
    result = runner.invoke(
        sync,
        ["--db-path", str(db), "--full-refresh", "--dry-run", "--json"],
        env={"RAINDROP_TOKEN": "x"},
    )
    assert result.exit_code == 0
    out = json.loads(result.output)
    # dry-run currently doesn't perform inserts, so new_links may be 0; ensure command succeeds
    assert "new_links" in out

    # ensure DB file was not created by dry-run
    assert not db.exists()
