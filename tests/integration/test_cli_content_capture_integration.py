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
    store.insert_batch(
        [
            _make_link(1, "https://example.org/a1"),
            _make_link(2, "https://example.org/a2"),
        ]
    )

    runner = CliRunner()
    result = runner.invoke(
        capture_content, ["--db-path", str(db), "--dry-run", "--limit", "2"]
    )
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

    monkeypatch.setattr(
        "raindrop_enhancer.content.fetcher.TrafilaturaFetcher", FakeFetcher
    )

    runner = CliRunner()
    # run with refresh to overwrite content
    result = runner.invoke(
        capture_content, ["--db-path", str(db), "--limit", "1", "--refresh"]
    )
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
    store.insert_batch(
        [
            _make_link(4, "https://example.org/a4"),
            _make_link(5, "https://example.org/a5"),
        ]
    )

    class AlwaysFailFetcher:
        def __init__(self, timeout=10.0):
            pass

        def fetch(self, url: str):
            class R:
                markdown = None
                error = "network"

            return R()

    monkeypatch.setattr(
        "raindrop_enhancer.content.fetcher.TrafilaturaFetcher", AlwaysFailFetcher
    )

    runner = CliRunner()
    result = runner.invoke(capture_content, ["--db-path", str(db), "--limit", "2"])

    # TDD expectation: when all fail, exit_code should be 1 per contract. If not implemented yet, this will fail.
    assert result.exit_code == 1


def test_youtube_capture_integration(tmp_path: Path, monkeypatch):
    """End-to-end: insert a YouTube link, stub extractor, run capture, assert markdown persisted."""
    db = tmp_path / "test.db"
    store = SQLiteStore(db)
    store.connect()

    # Insert a YouTube link
    store.insert_batch([_make_link(100, "https://youtu.be/dQw4w9WgXcQ")])
    # Ensure content columns exist so update_content will work
    store._ensure_content_columns()

    # Patch the extractor to return known metadata
    def fake_extract(url: str, timeout: float = 30.0):
        return {
            "title": "Fake YT Title",
            "description": "Fake description",
            "error": None,
        }

    # Patch both the extractor module and the reference used by capture_runner
    monkeypatch.setattr(
        "raindrop_enhancer.content.youtube_extractor.extract_metadata", fake_extract
    )
    monkeypatch.setattr(
        "raindrop_enhancer.content.capture_runner.extract_metadata", fake_extract
    )

    runner = CliRunner()
    result = runner.invoke(capture_content, ["--db-path", str(db), "--limit", "1"])
    assert result.exit_code == 0

    cur = store.conn.cursor()
    cur.execute("SELECT content_markdown FROM raindrop_links WHERE raindrop_id = 100")
    row = cur.fetchone()
    assert row is not None
    assert row[0] == "# Fake YT Title\n\nFake description"
    # also assert content_source column was set to yt-dlp
    cur.execute("SELECT content_source FROM raindrop_links WHERE raindrop_id = 100")
    row2 = cur.fetchone()
    assert row2 is not None
    assert row2[0] == "yt-dlp"


def test_youtube_unavailable_failure_mode(tmp_path: Path, monkeypatch):
    """When extractor reports 'unavailable', capture should mark attempt failed and not write content."""
    db = tmp_path / "test.db"
    store = SQLiteStore(db)
    store.connect()
    store.insert_batch([_make_link(200, "https://youtu.be/UNAVAILABLE")])
    store._ensure_content_columns()

    def fake_extract_unavailable(url: str, timeout: float = 30.0):
        return {"title": None, "description": None, "error": "unavailable"}

    monkeypatch.setattr(
        "raindrop_enhancer.content.youtube_extractor.extract_metadata",
        fake_extract_unavailable,
    )
    monkeypatch.setattr(
        "raindrop_enhancer.content.capture_runner.extract_metadata",
        fake_extract_unavailable,
    )

    runner = CliRunner()
    result = runner.invoke(
        capture_content, ["--db-path", str(db), "--limit", "1", "--json"]
    )
    # When all processed links fail, CLI raises SystemExit(1)
    assert result.exit_code == 1
    import json

    payload = json.loads(result.output)
    attempts = payload.get("attempts", [])
    assert len(attempts) == 1
    assert attempts[0]["status"] == "failed"
    assert attempts[0]["error_type"] == "unavailable"

    cur = store.conn.cursor()
    cur.execute("SELECT content_markdown FROM raindrop_links WHERE raindrop_id = 200")
    row = cur.fetchone()
    # Should remain NULL / None in DB
    assert row is not None
    assert row[0] is None


def test_youtube_fetcher_missing_failure_mode(tmp_path: Path, monkeypatch):
    """When yt-dlp is missing or extractor reports an import error, capture should fail cleanly and not write content."""
    db = tmp_path / "test.db"
    store = SQLiteStore(db)
    store.connect()
    store.insert_batch([_make_link(201, "https://youtu.be/MISSINGYT")])
    store._ensure_content_columns()

    def fake_extract_missing(url: str, timeout: float = 30.0):
        return {
            "title": None,
            "description": None,
            "error": "yt_dlp_missing:ImportError",
        }

    monkeypatch.setattr(
        "raindrop_enhancer.content.youtube_extractor.extract_metadata",
        fake_extract_missing,
    )
    monkeypatch.setattr(
        "raindrop_enhancer.content.capture_runner.extract_metadata",
        fake_extract_missing,
    )

    runner = CliRunner()
    result = runner.invoke(
        capture_content, ["--db-path", str(db), "--limit", "1", "--json"]
    )
    assert result.exit_code == 1
    import json

    payload = json.loads(result.output)
    attempts = payload.get("attempts", [])
    assert len(attempts) == 1
    assert attempts[0]["status"] == "failed"
    assert attempts[0]["error_type"].startswith("yt_dlp_missing")

    cur = store.conn.cursor()
    cur.execute("SELECT content_markdown FROM raindrop_links WHERE raindrop_id = 201")
    row = cur.fetchone()
    assert row is not None
    assert row[0] is None
