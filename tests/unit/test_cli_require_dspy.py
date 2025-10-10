import os

from click.testing import CliRunner


def test_require_dspy_exits_when_missing(monkeypatch, tmp_path):
    """When --require-dspy is passed but DSPy is not configured, CLI should exit 2."""
    # Ensure DSPy model env is unset
    monkeypatch.delenv("RAINDROP_DSPY_MODEL", raising=False)

    # Import here so environment changes take effect before CLI loads modules
    from raindrop_enhancer.cli import tags

    runner = CliRunner()

    db_file = tmp_path / "links.db"

    # DSPy is now mandatory; running without configuration should exit 2
    result = runner.invoke(tags, ["generate", "--dry-run", "--db-path", str(db_file)])

    assert result.exit_code == 2
    combined = (result.stderr or "") + (result.output or "")
    assert "DSPy" in combined or "dspy" in combined
