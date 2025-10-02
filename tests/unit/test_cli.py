"""Focused unit tests for the CLI orchestration layer."""

from __future__ import annotations

import json
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

import click
import toml
from click.testing import CliRunner
import pytest

from raindrop_enhancer.cli import main
from raindrop_enhancer.util.config import ConfigManager


def test_configure_command_writes_config_and_outputs_json() -> None:
    runner = CliRunner()
    with runner.isolated_filesystem():
        data_dir = Path("cfg")
        result = runner.invoke(
            main.app,
            [
                "--json",
                "configure",
                "--token",
                "secret",
                "--data-dir",
                str(data_dir),
                "--llm-api-base",
                "https://llm.local",
                "--llm-api-key",
                "llm-key",
                "--tag-threshold",
                "0.7",
                "--max-tags",
                "4",
            ],
        )

        assert result.exit_code == 0, result.output
        payload = json.loads(result.output)
        assert payload["has_token"] is True
        config_path = data_dir / "config.toml"
        document = toml.loads(config_path.read_text(encoding="utf-8"))
        assert document["raindrop_token"] == "secret"
        assert document["tag_confidence_threshold"] == 0.7
        assert document["max_tags"] == 4


def test_sync_command_invokes_perform_sync_and_clears_metrics(monkeypatch) -> None:
    runner = CliRunner()
    with runner.isolated_filesystem():
        data_dir = Path("data")
        manager = ConfigManager(data_dir)
        manager.update(
            raindrop_token="token-123",
            llm_api_base="https://llm.local",
            llm_api_key="key-456",
            tag_confidence_threshold=0.6,
            max_tags=3,
        )

        summary = {
            "mode": "full",
            "processed": 10,
            "skipped": 1,
            "manual_review": 2,
            "rate_limit_remaining": 50,
            "rate_limit_reset": 1_700_000_000,
            "rate_limit_limit": 120,
            "export_path": str(data_dir / "exports/latest.json"),
        }
        captured: dict[str, Any] = {}

        def fake_perform(**kwargs):
            captured.update(kwargs)
            return summary

        monkeypatch.setattr(main, "perform_sync", fake_perform)

        metrics = main.get_metrics()
        metrics.increment("raindrop.api_request", component="prefill")

        result = runner.invoke(
            main.app,
            [
                "--json",
                "--dry-run",
                "--data-dir",
                str(data_dir),
                "sync",
                "--mode",
                "full",
                "--batch-size",
                "10",
            ],
        )

        assert result.exit_code == 0, result.output
        payload = json.loads(result.output)
        assert payload["processed"] == 10
        assert captured["batch_size"] == 10
        assert captured["dry_run"] is True
        assert captured["mode"] == "full"
        assert metrics.snapshot() == {"counters": {}, "gauges": {}, "timers": {}}


def test_status_command_renders_summary(monkeypatch) -> None:
    runner = CliRunner()
    summaries = [
        {
            "run_id": "abc123",
            "mode": "full",
            "links_processed": 5,
            "manual_review": 1,
            "rate_limit_remaining": 40,
            "rate_limit_limit": 120,
            "rate_limit_reset": 1_700_000_500,
            "completed_at": "2025-01-01T00:00:00Z",
        }
    ]

    def fake_status_summary(*, data_dir: Path, limit: int):
        assert limit == 5
        assert data_dir.name == "data"
        return summaries

    monkeypatch.setattr(main.sync_service, "status_summary", fake_status_summary)

    with runner.isolated_filesystem():
        data_dir = Path("data")
        result = runner.invoke(
            main.app,
            [
                "--data-dir",
                str(data_dir),
                "status",
                "--limit",
                "5",
            ],
        )

        assert result.exit_code == 0, result.output
        assert "Recent Sync Runs" in result.output
        assert "abc123" in result.output


def test_perform_sync_requires_token(tmp_path) -> None:
    manager = ConfigManager(tmp_path)

    with pytest.raises(click.ClickException):
        main.perform_sync(
            mode="full",
            config_manager=manager,
            data_dir_override=None,
            collection_ids=None,
            since=None,
            batch_size=10,
            dry_run=True,
        )


def test_perform_sync_requires_llm_credentials(tmp_path) -> None:
    manager = ConfigManager(tmp_path)
    manager.update(raindrop_token="token-123")

    with pytest.raises(click.ClickException):
        main.perform_sync(
            mode="full",
            config_manager=manager,
            data_dir_override=None,
            collection_ids=None,
            since=None,
            batch_size=5,
            dry_run=False,
        )


def test_perform_sync_invokes_services(monkeypatch, tmp_path) -> None:
    manager = ConfigManager(tmp_path)
    manager.update(
        raindrop_token="token-xyz",
        llm_api_base="https://llm.local",
        llm_api_key="key-789",
        tag_confidence_threshold=0.55,
        max_tags=7,
    )

    captured: dict[str, Any] = {}

    class DummyTagging:
        def __init__(self, **kwargs):
            captured["tagging"] = kwargs

    class DummyClient:
        def __init__(self, token, on_retry=None):
            captured["client"] = {"token": token, "on_retry": on_retry}

        def close(self):
            captured["closed"] = True

    def fake_run_full_sync(**kwargs):
        captured["sync_kwargs"] = kwargs
        return {
            "mode": "full",
            "processed": 1,
            "skipped": 0,
            "manual_review": 0,
            "export_path": str(tmp_path / "exports/latest.json"),
        }

    monkeypatch.setattr(main, "TaggingService", DummyTagging)
    monkeypatch.setattr(main, "RaindropClient", DummyClient)
    monkeypatch.setattr(main.sync_service, "run_full_sync", fake_run_full_sync)

    summary = main.perform_sync(
        mode="full",
        config_manager=manager,
        data_dir_override=tmp_path,
        collection_ids=[1],
        since=None,
        batch_size=25,
        dry_run=True,
    )

    assert summary["processed"] == 1
    assert captured["client"]["token"] == "token-xyz"
    assert captured.get("closed") is True
    sync_kwargs = captured["sync_kwargs"]
    assert sync_kwargs["batch_size"] == 25
    assert sync_kwargs["collection_ids"] == [1]
    assert sync_kwargs["dry_run"] is True


def test_format_rate_limit_reset_handles_values() -> None:
    assert main._format_rate_limit_reset(None) == "-"
    assert main._format_rate_limit_reset("oops") == "oops"
    timestamp = int(datetime(2025, 1, 1, tzinfo=timezone.utc).timestamp())
    formatted = main._format_rate_limit_reset(timestamp)
    assert formatted.endswith("UTC")
    assert "2025-01-01" in formatted
