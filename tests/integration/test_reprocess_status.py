"""Integration coverage for reprocess command and status summary."""

from __future__ import annotations

import json
import sqlite3
from datetime import datetime, timedelta, timezone
from pathlib import Path
from typing import Callable

from raindrop_enhancer.services import sync


class SeedClient:
    def __init__(self) -> None:
        self.calls: list[tuple[str, dict]] = []
        self._collections = [
            {"id": 55, "title": "Manual Review", "lastUpdate": "2024-02-01T00:00:00Z"}
        ]
        self._items = {
            55: [
                {
                    "id": 301,
                    "collectionId": 55,
                    "title": "Needs review",
                    "link": "https://example.com/review",
                    "created": "2024-01-30T00:00:00Z",
                    "lastUpdate": "2024-02-01T00:00:00Z",
                    "tags": [],
                }
            ]
        }
        self.rate_limit_remaining = 77
        self.rate_limit_reset = 1700000789

    def list_collections(self):
        self.calls.append(("collections", {}))
        return self._collections, self._headers()

    def list_raindrops(self, collection_id: int, *, last_update: str | None = None):
        self.calls.append(
            ("raindrops", {"collection_id": collection_id, "last_update": last_update})
        )
        return self._items[collection_id], self._headers()

    def fetch_raindrop(self, raindrop_id: int) -> tuple[dict, dict]:
        self.calls.append(("raindrop", {"id": raindrop_id}))
        for items in self._items.values():
            for item in items:
                if item["id"] == raindrop_id:
                    return item, self._headers()
        raise KeyError(raindrop_id)

    def _headers(self) -> dict[str, str]:
        return {
            "X-RateLimit-Remaining": str(self.rate_limit_remaining),
            "X-RateLimit-Reset": str(self.rate_limit_reset),
        }


class ReprocessTagger:
    def __init__(self) -> None:
        self.calls: list[list[int]] = []

    def generate(self, documents: list[dict]) -> dict:
        self.calls.append([doc["raindrop_id"] for doc in documents])
        suggestions = {
            doc["raindrop_id"]: [
                {"tag": "fixed", "confidence": 0.95, "source": "llm"},
                {"tag": "quality", "confidence": 0.7, "source": "metadata"},
            ]
            for doc in documents
        }
        return {"suggestions": suggestions, "failures": {}}


def _content_fetch(url: str) -> str:
    return f"reprocessed:{url}"


def _clock() -> Callable[[], datetime]:
    current = datetime(2025, 1, 2, 12, 0, tzinfo=timezone.utc)

    def _next() -> datetime:
        nonlocal current
        stamp = current
        current = current + timedelta(minutes=10)
        return stamp

    return _next


def test_reprocess_updates_manual_review_and_status_summary(tmp_path):
    data_dir = tmp_path / "state"
    data_dir.mkdir()
    clock = _clock()

    client = SeedClient()
    tagger = ReprocessTagger()
    sync.run_full_sync(
        data_dir=data_dir,
        api_client=client,
        tagging_service=tagger,
        content_fetcher=_content_fetch,
        now=clock,
    )

    db_path = data_dir / "raindrop.sqlite"
    conn = sqlite3.connect(db_path)
    try:
        conn.execute(
            "UPDATE links SET status='manual_review', processed_at=NULL WHERE raindrop_id=?",
            (301,),
        )
        conn.commit()
    finally:
        conn.close()

    summary = sync.run_reprocess(
        data_dir=data_dir,
        raindrop_id=301,
        api_client=client,
        tagging_service=tagger,
        content_fetcher=_content_fetch,
        now=clock,
    )

    assert summary["mode"] == "reprocess"
    assert summary["previous_status"] == "manual_review"
    assert summary["new_status"] == "processed"
    assert summary["new_tags"][0]["tag"] == "fixed"

    export_path = Path(summary["export_path"])
    payload = json.loads(export_path.read_text(encoding="utf-8"))
    entry = next(item for item in payload["links"] if item["raindrop_id"] == 301)
    assert entry["status"] == "processed"
    assert {tag["tag"] for tag in entry["tags"]} == {"fixed", "quality"}

    conn = sqlite3.connect(db_path)
    try:
        status = conn.execute(
            "SELECT status FROM links WHERE raindrop_id=?", (301,)
        ).fetchone()[0]
        assert status == "processed"
        runs = conn.execute(
            "SELECT mode, links_processed FROM sync_runs ORDER BY started_at"
        ).fetchall()
        assert [row[0] for row in runs] == ["full", "reprocess"]
    finally:
        conn.close()

    status_summary = sync.status_summary(data_dir=data_dir, limit=5)
    assert status_summary[0]["mode"] == "reprocess"
    assert status_summary[0]["links_processed"] == 1
    assert status_summary[0]["manual_review"] == 0
