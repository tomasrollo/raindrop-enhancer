import os

from click.testing import CliRunner


def test_require_dspy_exits_when_missing(monkeypatch, tmp_path):
    """When --require-dspy is passed but DSPy is not configured, CLI should exit 2."""
    # Ensure DSPy model env and RAINDROP-scoped API keys are unset so DSPy is considered missing
    for v in (
        "RAINDROP_DSPY_MODEL",
        "RAINDROP_DSPY_API_KEY",
        "RAINDROP_DSPY_OPENAI_API_KEY",
        "RAINDROP_DSPY_ANTHROPIC_API_KEY",
        "RAINDROP_DSPY_GEMINI_API_KEY",
    ):
        monkeypatch.delenv(v, raising=False)

    # Import here so environment changes take effect before CLI loads modules
    from raindrop_enhancer.cli import tag

    runner = CliRunner()

    db_file = tmp_path / "links.db"

    # Ensure CLI behaves as if DSPy is missing by forcing configure_dspy to raise
    try:
        from raindrop_enhancer.content.dspy_settings import DSPyConfigError, configure_dspy

        def fake_configure():
            raise DSPyConfigError("dspy not available for test")

        monkeypatch.setattr(
            "raindrop_enhancer.content.dspy_settings.configure_dspy",
            fake_configure,
        )
    except Exception:
        # If DSPy settings module not importable, fall back to env-based approach
        pass

    # DSPy is now mandatory; running without configuration should exit 2
    result = runner.invoke(tag, ["generate", "--dry-run", "--db-path", str(db_file)])

    assert result.exit_code == 2
    combined = (result.stderr or "") + (result.output or "")
    assert "DSPy" in combined or "dspy" in combined
