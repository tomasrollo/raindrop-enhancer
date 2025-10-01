"""Integration tests for full sync orchestration."""

from __future__ import annotations

import json
import sqlite3
from datetime import datetime, timezone
from pathlib import Path

from raindrop_enhancer.services import sync


class FakeRaindropClient:
    def __init__(self) -> None:
        self._collections = [
            {
                "id": 1,
                "title": "Inbox",
                "color": None,
                "lastUpdate": "2024-01-01T00:00:00Z",
            },
            {
                "id": 2,
                "title": "AI",
                "color": "#fff",
                "lastUpdate": "2024-01-01T00:00:00Z",
            },
        ]
        self._items = {
            1: [
                {
                    "id": 101,
                    "collectionId": 1,
                    "title": "Link A",
                    "link": "https://example.com/a",
                    "excerpt": "A summary",
                    "tags": ["research"],
                    "created": "2024-01-01T00:00:00Z",
                    "lastUpdate": "2024-01-02T00:00:00Z",
                },
            ],
            2: [
                {
                    "id": 102,
                    "collectionId": 2,
                    "title": "Link B",
                    "link": "https://example.com/b",
                    "excerpt": "B summary",
                    "tags": ["ai"],
                    "created": "2024-01-01T00:00:00Z",
                    "lastUpdate": "2024-01-03T00:00:00Z",
                }
            ],
        }
        self.calls: list[tuple[str, dict]] = []
        self.rate_limit_remaining = 90
        self.rate_limit_reset = 1700000123

    def list_collections(self):
        self.calls.append(("collections", {}))
        return self._collections, self._headers()

    def list_raindrops(self, collection_id: int, *, last_update: str | None = None):
        self.calls.append(
            ("raindrops", {"collection_id": collection_id, "last_update": last_update})
        )
        return self._items[collection_id], self._headers()

    def _headers(self) -> dict[str, str]:
        return {
            "X-RateLimit-Remaining": str(self.rate_limit_remaining),
            "X-RateLimit-Reset": str(self.rate_limit_reset),
        }


class FakeTaggingService:
    def __init__(self) -> None:
        self.calls: list[list[int]] = []

    def generate(self, documents: list[dict]) -> dict:
        self.calls.append([doc["raindrop_id"] for doc in documents])
        suggestions: dict[int, list[dict]] = {}
        for doc in documents:
            suggestions[doc["raindrop_id"]] = [
                {"tag": f"tag-{doc['raindrop_id']}", "confidence": 0.9, "source": "llm"}
            ]
        return {"suggestions": suggestions, "failures": {}}


def _content_for(url: str) -> str:
    return f"content:{url}"


def _fixed_now() -> datetime:
    return datetime(2025, 1, 1, 12, 0, tzinfo=timezone.utc)


def test_full_sync_writes_database_and_json_export(tmp_path):
    data_dir = tmp_path / "data"
    data_dir.mkdir()
    client = FakeRaindropClient()
    tagging = FakeTaggingService()

    summary = sync.run_full_sync(
        data_dir=data_dir,
        api_client=client,
        tagging_service=tagging,
        content_fetcher=_content_for,
        now=_fixed_now,
    )

    assert summary["mode"] == "full"
    assert summary["processed"] == 2
    assert summary["skipped"] == 0
    assert summary["rate_limit_remaining"] == client.rate_limit_remaining

    export_path = Path(summary["export_path"])
    assert export_path.exists()
    payload = json.loads(export_path.read_text(encoding="utf-8"))
    assert payload["schema_version"] == "1.0"
    assert {link["raindrop_id"] for link in payload["links"]} == {101, 102}
    assert payload["links"][0]["tags"][0]["tag"].startswith("tag-")

    db_path = data_dir / "raindrop.sqlite"
    assert db_path.exists()
    conn = sqlite3.connect(db_path)
    try:
        link_rows = conn.execute("SELECT COUNT(*) FROM links").fetchone()[0]
        assert link_rows == 2
        sync_runs = conn.execute(
            "SELECT mode, links_processed, rate_limit_remaining FROM sync_runs ORDER BY started_at DESC LIMIT 1"
        ).fetchone()
        assert sync_runs[0] == "full"
        assert sync_runs[1] == 2
        assert sync_runs[2] == client.rate_limit_remaining
    finally:
        conn.close()

    assert client.calls[0][0] == "collections"
    assert len(tagging.calls) == 1
