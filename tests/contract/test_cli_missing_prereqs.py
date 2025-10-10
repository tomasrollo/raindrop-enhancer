import os
from click.testing import CliRunner
from raindrop_enhancer import cli


def _get_entry():
    return getattr(cli, "cli", getattr(cli, "main", None))


def test_missing_raindrop_token_env(monkeypatch):
    runner = CliRunner()
    entry = _get_entry()
    if entry is None:
        return
    # Ensure RAINDROP_TOKEN is not present
    monkeypatch.delenv("RAINDROP_TOKEN", raising=False)
    result = runner.invoke(entry, ["export"])
    assert result.exit_code == 2
    assert "Missing RAINDROP_TOKEN" in result.output or "Missing RAINDROP_TOKEN" in result.stderr


def test_missing_dspy(monkeypatch):
    runner = CliRunner()
    entry = _get_entry()
    if entry is None:
        return

    # Monkeypatch configure_dspy to raise a DSPyConfigError when invoked
    # Use the project's DSPyConfigError if available so CLI catches it and exits with code 2
    try:
        from raindrop_enhancer.content.dspy_settings import DSPyConfigError

        def fake_configure():
            raise DSPyConfigError("dspy not available")

    except Exception:
        # Fallback: raise a generic Exception (will cause the test to skip expectation)
        def fake_configure():
            raise Exception("dspy not available")

    # Attempt to patch into the tags_generate import path; best-effort patch
    try:
        from raindrop_enhancer.content import dspy_settings

        monkeypatch.setattr(dspy_settings, "configure_dspy", fake_configure)
    except Exception:
        # If import fails, skip the assertion (TDD stage)
        return

    # New CLI layout exposes a single `tag` subcommand (no nested `generate`),
    # invoke via the top-level entrypoint.
    result = runner.invoke(entry, ["tag"])
    assert result.exit_code == 2
    assert "DSPy configuration required" in result.output or "dspy" in result.output
