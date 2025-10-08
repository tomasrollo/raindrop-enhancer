import os

from click.testing import CliRunner


def test_cli_with_dspy_callable_predictor(monkeypatch, tmp_path):
    """Simulate DSPy being present: Predictor is callable and returns tags; CLI should exit 0."""
    # Ensure env var is set so configure_dspy will attempt to build a predictor
    monkeypatch.setenv("RAINDROP_DSPY_MODEL", "test:model")

    # Import the dspy_settings module and clear any cached configure_dspy
    from raindrop_enhancer.content import dspy_settings as ds

    try:
        ds.configure_dspy.cache_clear()
    except Exception:
        # If no cache attribute, ignore
        pass

    # Provide a fake dspy module with Predictor and settings.configure
    class FakePred:
        def __call__(self, prompt: str):
            return ["alpha", "beta"]

    class FakeSettings:
        def configure(self, lm=None):
            return None

    class FakeDspyModule:
        settings = FakeSettings()

        def Predictor(self, model):
            return FakePred()

    monkeypatch.setattr(ds, "dspy", FakeDspyModule())

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
