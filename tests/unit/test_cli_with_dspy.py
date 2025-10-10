import os

from click.testing import CliRunner


def test_cli_with_dspy_callable_predictor(monkeypatch, tmp_path):
    """Simulate DSPy being present: Predictor is callable and returns tags; CLI should exit 0."""
    # Ensure configure_dspy returns a fake predictor for the test
    from raindrop_enhancer.content import dspy_settings as ds

    class FakePrediction:
        def __init__(self, tags):
            self.tags = tags

        def get_lm_usage(self):
            return None

    class FakePredict:
        def __call__(self, prompt: str):
            return FakePrediction(["alpha", "beta"])

    monkeypatch.setattr(ds, "configure_dspy", lambda: FakePredict())
    monkeypatch.setattr(ds, "get_dspy_model", lambda: "test:model")

    # Ensure CLI will process at least one item
    from raindrop_enhancer.storage.sqlite_store import SQLiteStore as StoreClass

    monkeypatch.setattr(
        StoreClass,
        "fetch_untagged_links",
        lambda self, limit=None: [(1, "Title", "http://", "content")],
    )

    # Run CLI with dry-run to avoid writing DB
    from raindrop_enhancer import cli as cli_mod

    runner = CliRunner()
    db_file = tmp_path / "links.db"

    result = runner.invoke(
        cli_mod.tags, ["generate", "--db-path", str(db_file), "--dry-run"]
    )

    assert result.exit_code == 0
    # Output should indicate at least one processed link
    out = (result.output or "") + (result.stderr or "")
    assert "Processed:" in out or "processed" in out.lower()
