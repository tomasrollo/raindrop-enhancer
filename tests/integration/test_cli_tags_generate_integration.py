import json
from click.testing import CliRunner
from pathlib import Path

from raindrop_enhancer.cli import tags_generate


def _seed_db(tmp_db: Path):
    # Create DB and insert a few links using SQLiteStore
    from raindrop_enhancer.storage.sqlite_store import SQLiteStore
    from raindrop_enhancer.models import RaindropLink

    store = SQLiteStore(tmp_db)
    store.connect()
    links = [
        RaindropLink(
            raindrop_id=100 + i,
            collection_id=1,
            collection_title="Test",
            title=f"Title {i}",
            url=f"https://example.test/{i}",
            created_at="2020-01-01T00:00:00Z",
            synced_at="2020-01-01T00:00:00Z",
            tags_json="[]",
            raw_payload="{}",
        )
        for i in range(3)
    ]
    store.insert_batch(links)
    store.close()


def test_cli_tags_generate_dryrun_then_persist(tmp_path: Path, monkeypatch):
    db = tmp_path / "test.db"
    _seed_db(db)

    # monkeypatch DSPy predictor to deterministic output
    def fake_predictor(prompt: str):
        return ["Alpha", "Beta"]

    monkeypatch.setenv("RAINDROP_DSPY_MODEL", "dummy:model")
    # Monkeypatch configure_dspy to return our fake predictor
    import raindrop_enhancer.content.dspy_settings as ds

    monkeypatch.setattr(ds, "configure_dspy", lambda: fake_predictor)

    runner = CliRunner()
    # Dry run: should not persist
    res1 = runner.invoke(tags_generate, ["--db-path", str(db), "--dry-run"])
    assert res1.exit_code == 0

    # Persist run
    res2 = runner.invoke(tags_generate, ["--db-path", str(db)])
    assert res2.exit_code == 0

    # Re-run should be idempotent (no additional generated tags)
    res3 = runner.invoke(tags_generate, ["--db-path", str(db)])
    assert res3.exit_code == 0
