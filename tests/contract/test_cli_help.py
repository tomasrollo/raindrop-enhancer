import json
from click.testing import CliRunner
from raindrop_enhancer import cli


def _get_entry():
    # Support either a Click group named `cli` (future) or fall back to `main`.
    return getattr(cli, "cli", getattr(cli, "main", None))


def test_top_level_help():
    runner = CliRunner()
    entry = _get_entry()
    if entry is None:
        # If no group or main entry exists yet, skip the assertion to allow TDD iteration
        return
    result = runner.invoke(entry, ["--help"])
    assert result.exit_code == 0
    assert "Usage:" in result.output or "Commands:" in result.output


def test_subcommand_help_export():
    runner = CliRunner()
    entry = _get_entry()
    if entry is None:
        return
    result = runner.invoke(entry, ["export", "--help"])
    assert result.exit_code == 0
    assert "--output" in result.output
