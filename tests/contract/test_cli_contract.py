import pytest
from click.testing import CliRunner
from raindrop_enhancer.cli.main import app


def test_cli_contract_sync_command():
    runner = CliRunner()
    result = runner.invoke(app, ["--help"])
    # Contract: sync command must be present in help output
    assert "sync" in result.output, (
        "CLI 'sync' command should be present in help (TDD red phase)"
    )
