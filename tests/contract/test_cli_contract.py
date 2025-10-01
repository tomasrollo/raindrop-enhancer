import click
from click.testing import CliRunner

from raindrop_enhancer.cli.main import app


def test_cli_has_sync_command():
    runner = CliRunner()
    result = runner.invoke(app, ["--help"])
    # Expect the sync command to be present in help; failing until implemented
    if "sync" not in result.output:
        raise AssertionError("CLI 'sync' command should be present in help")
