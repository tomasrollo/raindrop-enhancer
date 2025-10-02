"""CLI contract tests derived from `contracts/cli_commands.md`."""

from __future__ import annotations

import json

import pytest
from click.testing import CliRunner

from raindrop_enhancer.cli import main


@pytest.fixture()
def runner() -> CliRunner:
    return CliRunner()


def test_cli_help_exposes_expected_commands_and_options(runner: CliRunner) -> None:
    result = runner.invoke(main.app, ["--help"])
    assert result.exit_code == 0
    output = result.output
    for command in ["configure", "sync", "reprocess", "status"]:
        assert command in output, f"Expected `{command}` to be listed in help"
    for option in ["--json", "--verbose", "--quiet", "--dry-run", "--data-dir"]:
        assert option in output, f"Global option {option} missing from help"


def test_verbose_and_quiet_are_mutually_exclusive(runner: CliRunner) -> None:
    result = runner.invoke(main.app, ["--verbose", "--quiet", "sync", "--mode", "full"])
    assert result.exit_code != 0
    assert "mutually exclusive" in result.output.lower()


def test_sync_requires_mode_option(runner: CliRunner) -> None:
    result = runner.invoke(main.app, ["sync"])
    assert result.exit_code != 0
    assert "--mode" in result.output


def test_sync_json_payload_matches_contract(monkeypatch, runner: CliRunner) -> None:
    fake_payload = {
        "run_id": "uuid-1234",
        "mode": "full",
        "processed": 10,
        "skipped": 2,
        "manual_review": 1,
        "failures": [],
        "export_path": "/tmp/export.json",
        "timestamp": "2025-10-01T12:00:00Z",
        "duration_seconds": 12.5,
        "rate_limit_remaining": 80,
        "rate_limit_reset": 1700000000,
    }

    monkeypatch.setattr(
        main, "perform_sync", lambda **kwargs: fake_payload, raising=False
    )

    result = runner.invoke(
        main.app,
        ["--json", "sync", "--mode", "full"],
    )
    assert result.exit_code == 0
    payload = json.loads(result.stdout)
    for key in fake_payload:
        assert key in payload, f"Missing contract field `{key}`"
    assert payload["rate_limit_remaining"] == 80
    assert payload["mode"] == "full"
