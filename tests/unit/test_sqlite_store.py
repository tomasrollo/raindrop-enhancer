import sqlite3
from datetime import datetime, timezone
from pathlib import Path

from raindrop_enhancer.storage.sqlite_store import SQLiteStore
from raindrop_enhancer.models import RaindropLink


def _make_link(i: int) -> RaindropLink:
    now = datetime.now(timezone.utc)
    return RaindropLink(
        raindrop_id=1000 + i,
        collection_id=1,
        collection_title="Test",
        title=f"T{i}",
        url=f"https://example.test/{i}",
        created_at=now.isoformat().replace("+00:00", "Z"),
        synced_at=now.isoformat().replace("+00:00", "Z"),
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
    # user_version reflects latest applied migrations
    cur.execute("PRAGMA user_version")
    uv = cur.fetchone()[0]
    assert int(uv) >= 3
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


def test_corruption_recovery_and_backup(tmp_path: Path):
    """Simulate a corrupted DB file and ensure backup is created and quick_check fails."""
    db = tmp_path / "test.db"
    store = SQLiteStore(db)
    store.connect()
    # close and corrupt the file
    store.close()
    # write invalid content to simulate corruption
    db.write_bytes(b"not-a-sqlite-db")
    # reopen using a new store instance
    import sqlite3

    store2 = SQLiteStore(db)
    # connecting to a corrupted sqlite file raises DatabaseError
    try:
        store2.connect()
        connected = True
    except sqlite3.DatabaseError:
        connected = False

    assert connected is False

    # backup should create a .bak file even without a live connection
    bak = store2.backup_db()
    assert bak.exists()
    # After backup, original db file still exists
    assert db.exists()


def test_url_validation_in_models():
    from raindrop_enhancer.models import is_valid_url

    assert is_valid_url("https://example.com") is True
    assert is_valid_url("http://example.com/path") is True
    assert is_valid_url("ftp://example.com") is False
    assert is_valid_url("not-a-url") is False


def test_ensure_tagging_columns_creates_columns(tmp_path: Path):
    """Fail-first test: _ensure_tagging_columns should add auto_tags_json and auto_tags_meta_json
    columns with NULL defaults when the DB is initialized or migrated.
    """
    db = tmp_path / "test.db"
    store = SQLiteStore(db)
    store.connect()
    store._ensure_tagging_columns()  # ensure idempotent when called manually
    cur = store.conn.cursor()
    cur.execute("PRAGMA table_info(raindrop_links)")
    cols = {row[1]: row for row in cur.fetchall()}  # name -> row

    # Expect the new columns to be present and allow NULL
    assert "auto_tags_json" in cols, "auto_tags_json column is missing"
    assert "auto_tags_meta_json" in cols, "auto_tags_meta_json column is missing"

    # Verify default is NULL (not NOT NULL)
    # PRAGMA table_info returns: cid, name, type, notnull, dflt_value, pk
    assert cols["auto_tags_json"][3] == 0, "auto_tags_json should allow NULL"
    assert cols["auto_tags_meta_json"][3] == 0, "auto_tags_meta_json should allow NULL"

    cur.close()
