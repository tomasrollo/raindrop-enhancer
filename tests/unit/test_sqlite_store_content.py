from pathlib import Path
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


def test_select_uncaptured_fallback(tmp_path: Path):
    db = tmp_path / "test.db"
    store = SQLiteStore(db)
    store.connect()
    # Insert entries
    store.insert_batch([_make_link(1, "https://example.org/a1")])
    rows = store.select_uncaptured()
    assert len(rows) >= 1


def test_update_and_clear_content(tmp_path: Path):
    db = tmp_path / "test.db"
    store = SQLiteStore(db)
    store.connect()
    store.insert_batch([_make_link(2, "https://example.org/a2")])
    store._ensure_content_columns()
    store.update_content(2, "MD CONTENT", source="test")
    cur = store.conn.cursor()
    cur.execute("SELECT content_markdown FROM raindrop_links WHERE raindrop_id = 2")
    row = cur.fetchone()
    assert row[0] == "MD CONTENT"
    store.clear_content_for_link(2)
    cur.execute("SELECT content_markdown FROM raindrop_links WHERE raindrop_id = 2")
    row2 = cur.fetchone()
    assert row2[0] is None
