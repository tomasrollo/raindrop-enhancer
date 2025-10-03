import pytest


def test_cli_baseline_and_incremental(tmp_path, monkeypatch):
    """CLI should perform baseline and incremental runs; use temp DB path."""
    pytest.fail("Integration test skeleton — failing by design to enforce TDD")


def test_cli_full_refresh_and_dry_run(tmp_path):
    """CLI --full-refresh should backup and rebuild; --dry-run should not modify DB."""
    pytest.fail("Integration test skeleton — failing by design to enforce TDD")
