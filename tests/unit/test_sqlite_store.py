import sqlite3
from datetime import datetime
from pathlib import Path

from raindrop_enhancer.storage.sqlite_store import SQLiteStore
from raindrop_enhancer.models import RaindropLink


def _make_link(i: int) -> RaindropLink:
    now = datetime.utcnow()
    return RaindropLink(
        raindrop_id=1000 + i,
        collection_id=1,
        collection_title="Test",
        title=f"T{i}",
        url=f"https://example.test/{i}",
        created_at=now.isoformat() + "Z",
        synced_at=now.isoformat() + "Z",
        tags_json="[]",
        raw_payload="{}",
    )


def test_schema_creation(tmp_path: Path):
    db = tmp_path / "test.db"
    store = SQLiteStore(db)
    store.connect()
    # Ensure tables exist
    cur = store.conn.cursor()
    cur.execute("SELECT name FROM sqlite_master WHERE type='table'")
    names = {r[0] for r in cur.fetchall()}
    assert "raindrop_links" in names
    assert "sync_state" in names
    # user_version should be 1
    cur.execute("PRAGMA user_version")
    uv = cur.fetchone()[0]
    assert int(uv) == 1
    cur.close()


def test_insert_batch_and_append_only(tmp_path: Path):
    db = tmp_path / "test.db"
    store = SQLiteStore(db)
    store.connect()
    links = [_make_link(i) for i in range(3)]
    inserted = store.insert_batch(links)
    assert inserted == 3
    count = store.count_links()
    assert count == 3

    # Insert same links again -> should be ignored (append-only)
    inserted2 = store.insert_batch(links)
    assert inserted2 == 0
    assert store.count_links() == 3


def test_corruption_detection(tmp_path: Path):
    db = tmp_path / "test.db"
    store = SQLiteStore(db)
    store.connect()
    ok = store.quick_check()
    assert ok is True
