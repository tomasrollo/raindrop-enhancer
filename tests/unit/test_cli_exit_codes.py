import json

from click.testing import CliRunner


def test_persistence_failure_returns_3(monkeypatch, tmp_path):
    """If the DB write fails while persisting tags, CLI should exit with code 3."""
    from raindrop_enhancer import cli as cli_mod

    # Ensure DSPy configured by providing a fake predictor
    from raindrop_enhancer.content import dspy_settings as ds

    class FakePrediction:
        def __init__(self, tags):
            self.tags = tags

        def get_lm_usage(self):
            return None

    class FakePredict:
        def __call__(self, prompt: str):
            return FakePrediction(["tag"])

    monkeypatch.setattr(ds, "configure_dspy", lambda: FakePredict())
    monkeypatch.setattr(ds, "get_dspy_model", lambda: "test:model")

    # Make run_batch emit one successful generated entry so collected is non-empty
    def fake_run_batch(self, items, on_result):
        for i, it in enumerate(items, start=1):
            on_result(
                {
                    "raindrop_id": i,
                    "tags_json": json.dumps(["tag"]),
                    "meta_json": json.dumps({}),
                }
            )

    # Ensure the CLI will process at least one item by patching fetch_untagged_links
    from raindrop_enhancer.storage.sqlite_store import SQLiteStore as StoreClass

    monkeypatch.setattr(
        StoreClass,
        "fetch_untagged_links",
        lambda self, limit=None: [(1, "T", "http://", "c")],
    )

    # Patch the TagGenerationRunner implementation used by the CLI
    from raindrop_enhancer.content.tag_generator import TagGenerationRunner

    monkeypatch.setattr(TagGenerationRunner, "run_batch", fake_run_batch)

    # Patch SQLiteStore.write_auto_tags_batch to raise
    from raindrop_enhancer.storage.sqlite_store import SQLiteStore

    def raise_on_write(self, tuples):
        raise RuntimeError("simulated disk error")

    monkeypatch.setattr(SQLiteStore, "write_auto_tags_batch", raise_on_write)

    runner = CliRunner()
    db_file = tmp_path / "links.db"
    result = runner.invoke(cli_mod.tags, ["generate", "--db-path", str(db_file)])

    assert result.exit_code == 3
    assert "persist" in (result.stderr or "") or "persist" in (result.output or "")


def test_fail_on_error_returns_4(monkeypatch, tmp_path):
    """When --fail-on-error is set and any link generation failed, CLI should exit 4."""
    from raindrop_enhancer import cli as cli_mod

    # Provide a fake DSPy predictor so DSPy requirement is satisfied
    from raindrop_enhancer.content import dspy_settings as ds

    class FakePrediction:
        def __init__(self, tags):
            self.tags = tags

        def get_lm_usage(self):
            return None

    class FakePredict:
        def __call__(self, prompt: str):
            return FakePrediction([])

    monkeypatch.setattr(ds, "configure_dspy", lambda: FakePredict())
    monkeypatch.setattr(ds, "get_dspy_model", lambda: "test:model")

    # Make run_batch emit one failed entry (empty tags)
    def fake_run_batch_fail(self, items, on_result):
        for i, it in enumerate(items, start=1):
            on_result({"raindrop_id": i, "tags_json": "[]", "meta_json": json.dumps({})})

    from raindrop_enhancer.content.tag_generator import TagGenerationRunner as TGR

    # Ensure CLI will process one item
    from raindrop_enhancer.storage.sqlite_store import SQLiteStore as StoreClass2

    monkeypatch.setattr(
        StoreClass2,
        "fetch_untagged_links",
        lambda self, limit=None: [(1, "T", "http://", "c")],
    )

    monkeypatch.setattr(TGR, "run_batch", fake_run_batch_fail)

    runner = CliRunner()
    db_file = tmp_path / "links.db"

    # Use --dry-run to avoid persistence and --json to exercise JSON path
    result = runner.invoke(
        cli_mod.tags,
        [
            "generate",
            "--db-path",
            str(db_file),
            "--fail-on-error",
            "--dry-run",
            "--json",
        ],
    )

    assert result.exit_code == 4
    # JSON should have processed/failed keys
    assert "failed" in (result.output or "")
