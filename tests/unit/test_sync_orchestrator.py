import pytest


def test_baseline_sync_behavior(tmp_path):
    """Baseline sync should populate DB when no sync_state exists."""
    pytest.fail("Unit test skeleton — failing by design to enforce TDD")


def test_incremental_sync_cursor_updates(tmp_path):
    """Incremental sync should only insert items with created > last_cursor_iso."""
    pytest.fail("Unit test skeleton — failing by design to enforce TDD")


def test_full_refresh_flag_resets_db(tmp_path):
    """Full refresh should backup and recreate DB schema before baseline."""
    pytest.fail("Unit test skeleton — failing by design to enforce TDD")
