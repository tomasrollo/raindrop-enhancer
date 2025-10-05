import json
import sqlite3
from pathlib import Path

import pytest
from click.testing import CliRunner

from raindrop_enhancer.cli import capture_content
from raindrop_enhancer.storage.sqlite_store import SQLiteStore
from raindrop_enhancer.models import RaindropLink
from datetime import datetime, timezone


def _make_link(rid: int, url: str) -> RaindropLink:
    return RaindropLink(
        raindrop_id=rid,
        collection_id=0,
        collection_title="",
        title=f"title-{rid}",
        url=url,
        created_at=datetime.now(timezone.utc).isoformat(),
        synced_at=datetime.now(timezone.utc).isoformat(),
        tags_json="[]",
        raw_payload="{}",
    )


def test_capture_fresh_dry_run(tmp_path: Path, monkeypatch):
    db = tmp_path / "test.db"
    store = SQLiteStore(db)
    store.connect()
    # insert two links
    store.insert_batch([_make_link(1, "https://example.org/a1"), _make_link(2, "https://example.org/a2")])

    runner = CliRunner()
    result = runner.invoke(capture_content, ["--db-path", str(db), "--dry-run", "--limit", "2"])
    assert result.exit_code == 0
    assert "Processed" in result.output or "Dry run" in result.output


def test_capture_refresh_and_persistence(tmp_path: Path, monkeypatch):
    db = tmp_path / "test.db"
    store = SQLiteStore(db)
    store.connect()
    # insert link and set content_markdown manually (simulate previous capture)
    store.insert_batch([_make_link(3, "https://example.org/a3")])
    # Ensure content columns exist for update
    store._ensure_content_columns()
    store.update_content(3, "OLD MARKDOWN", source="test")

    # Patch fetcher to return new markdown
    class FakeFetcher:
        def __init__(self, timeout=10.0):
            pass

        def fetch(self, url: str):
            class R:
                markdown = "NEW MARKDOWN"

            return R()

    monkeypatch.setattr("raindrop_enhancer.content.fetcher.TrafilaturaFetcher", FakeFetcher)

    runner = CliRunner()
    # run with refresh to overwrite content
    result = runner.invoke(capture_content, ["--db-path", str(db), "--limit", "1", "--refresh"])
    assert result.exit_code == 0

    # verify DB was updated
    cur = store.conn.cursor()
    cur.execute("SELECT content_markdown FROM raindrop_links WHERE raindrop_id = 3")
    row = cur.fetchone()
    assert row is not None
    assert row[0] == "NEW MARKDOWN"


def test_partial_failure_exit_code_all_fail(tmp_path: Path, monkeypatch):
    # This test expects the CLI to exit with code 1 when all captures fail.
    # As part of TDD this may be failing until exit-code logic is implemented.
    db = tmp_path / "test.db"
    store = SQLiteStore(db)
    store.connect()
    store.insert_batch([_make_link(4, "https://example.org/a4"), _make_link(5, "https://example.org/a5")])

    class AlwaysFailFetcher:
        def __init__(self, timeout=10.0):
            pass

        def fetch(self, url: str):
            class R:
                markdown = None
                error = "network"

            return R()

    monkeypatch.setattr("raindrop_enhancer.content.fetcher.TrafilaturaFetcher", AlwaysFailFetcher)

    runner = CliRunner()
    result = runner.invoke(capture_content, ["--db-path", str(db), "--limit", "2"])

    # TDD expectation: when all fail, exit_code should be 1 per contract. If not implemented yet, this will fail.
    assert result.exit_code == 1
