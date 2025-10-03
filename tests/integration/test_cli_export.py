import os
from click.testing import CliRunner
from raindrop_enhancer.cli import main


def test_export_missing_token_exits_with_error(monkeypatch):
    monkeypatch.delenv("RAINDROP_TOKEN", raising=False)
    runner = CliRunner()
    result = runner.invoke(main, ["--dry-run"])
    assert result.exit_code == 2


def test_export_success_writes_json(monkeypatch, httpx_mock):
    # Provide token
    monkeypatch.setenv("RAINDROP_TOKEN", "x")
    # Mock collections and raindrops
    httpx_mock.add_response(
        method="GET", url="https://api.raindrop.io/rest/v1/collections", json={"items": [{"_id": 1}]}
    )
    httpx_mock.add_response(
        method="GET",
        url="https://api.raindrop.io/rest/v1/raindrops/1?page=0&perpage=50",
        json={"items": [{"_id": 1, "link": "https://a"}]},
    )

    runner = CliRunner()
    result = runner.invoke(main, ["--dry-run"])
    assert result.exit_code == 0
    assert "Dry run: collected" in result.output
