"""Unit tests for the SQLite repository layer."""

from __future__ import annotations

from datetime import datetime, timezone

import pytest

from raindrop_enhancer.domain.entities import Collection, LinkRecord, SyncRun
from raindrop_enhancer.domain.repositories import SQLiteRepository


@pytest.fixture()
def repo(tmp_path):
    db_path = tmp_path / "raindrop.sqlite"
    repository = SQLiteRepository(db_path)
    repository.setup()
    return repository


def _link(**overrides) -> LinkRecord:
    record = LinkRecord(
        raindrop_id=overrides.get("raindrop_id", 101),
        url=overrides.get("url", "https://example.com/a"),
        title=overrides.get("title", "Example A"),
        created_at=overrides.get(
            "created_at", datetime(2024, 1, 1, tzinfo=timezone.utc)
        ),
        updated_at=overrides.get(
            "updated_at", datetime(2024, 1, 2, tzinfo=timezone.utc)
        ),
    )
    # Attach additional attributes anticipated by SQLModel entities
    for key, value in {
        "description": "first link",
        "status": "pending",
        "processed_at": None,
        "content_hash": "hash-a",
        "llm_version": "v1",
    }.items():
        setattr(record, key, overrides.get(key, value))
    return record


def _collection(collection_id: int, title: str) -> Collection:
    obj = Collection(collection_id=collection_id, title=title)
    for key, value in {
        "color": None,
        "parent_id": None,
        "last_sync_timestamp": None,
    }.items():
        setattr(obj, key, value)
    return obj


def test_upsert_link_merges_collections_and_updates_metadata(repo):
    first = _link()
    repo.upsert_link(
        first,
        collections=[_collection(1, "Inbox")],
        tag_suggestions=[{"tag": "research", "confidence": 0.91, "source": "llm"}],
    )

    updated = _link(
        title="Example A Updated",
        updated_at=datetime(2024, 1, 5, tzinfo=timezone.utc),
        status="processed",
        processed_at=datetime(2024, 1, 5, tzinfo=timezone.utc),
        content_hash="hash-b",
    )
    repo.upsert_link(
        updated,
        collections=[
            _collection(1, "Inbox"),
            _collection(2, "AI"),
        ],
        tag_suggestions=[{"tag": "python", "confidence": 0.88, "source": "llm"}],
    )

    stored = repo.get_link(101)
    assert stored.title == "Example A Updated"
    assert stored.status == "processed"
    assert stored.content_hash == "hash-b"
    assert {c.collection_id for c in stored.collections} == {1, 2}
    tags = repo.get_tag_suggestions(101)
    assert {tag["tag"] for tag in tags} == {"python"}


def test_list_pending_links_excludes_processed(repo):
    repo.upsert_link(
        _link(raindrop_id=201, url="https://example.com/pending"),
        collections=[_collection(3, "Pending")],
        tag_suggestions=[],
    )
    repo.upsert_link(
        _link(
            raindrop_id=202,
            url="https://example.com/processed",
            status="processed",
            processed_at=datetime(2024, 1, 6, tzinfo=timezone.utc),
        ),
        collections=[_collection(4, "Done")],
        tag_suggestions=[],
    )

    pending = repo.list_pending_links()
    assert {item.raindrop_id for item in pending} == {201}


def test_record_sync_run_persists_audit_history(repo):
    run = SyncRun(
        run_id="run-1",
        started_at=datetime(2024, 1, 10, 12, 0, tzinfo=timezone.utc),
        completed_at=datetime(2024, 1, 10, 12, 5, tzinfo=timezone.utc),
        mode="full",
        links_processed=3,
    )
    for key, value in {
        "links_skipped": 1,
        "manual_review": 0,
        "failures": 0,
        "output_path": "/tmp/export.json",
        "rate_limit_remaining": 90,
        "rate_limit_reset": 1700000123,
    }.items():
        setattr(run, key, value)
    repo.record_sync_run(run)

    history = repo.list_sync_runs()
    assert history[0].run_id == "run-1"
    assert history[0].mode == "full"
    assert history[0].links_processed == 3
