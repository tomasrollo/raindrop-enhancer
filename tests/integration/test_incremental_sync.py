"""Integration coverage for incremental sync behavior."""

from __future__ import annotations

import json
import sqlite3
from datetime import datetime, timedelta, timezone
from pathlib import Path

from raindrop_enhancer.services import sync


class IncrementalRaindropClient:
    def __init__(self, stage: str) -> None:
        self.stage = stage
        self.calls: list[tuple[str, dict]] = []
        self.rate_limit_remaining = 42
        self.rate_limit_reset = 1700000456

        if stage == "full":
            self._collections = [
                {"id": 10, "title": "Inbox", "lastUpdate": "2024-01-05T00:00:00Z"}
            ]
            self._items = {
                10: [
                    {
                        "id": 201,
                        "collectionId": 10,
                        "title": "Baseline",
                        "link": "https://example.com/baseline",
                        "created": "2024-01-01T00:00:00Z",
                        "lastUpdate": "2024-01-05T00:00:00Z",
                        "tags": [],
                    }
                ]
            }
        else:  # incremental stage
            self._collections = [
                {"id": 10, "title": "Inbox", "lastUpdate": "2024-01-07T00:00:00Z"}
            ]
            self._items = {
                10: [
                    {
                        "id": 202,
                        "collectionId": 10,
                        "title": "New Link",
                        "link": "https://example.com/new",
                        "created": "2024-01-06T00:00:00Z",
                        "lastUpdate": "2024-01-07T00:00:00Z",
                        "tags": [],
                    },
                    {
                        "id": 201,
                        "collectionId": 10,
                        "title": "Baseline Updated",
                        "link": "https://example.com/baseline",
                        "created": "2024-01-01T00:00:00Z",
                        "lastUpdate": "2024-01-07T00:00:00Z",
                        "tags": ["updated"],
                    },
                ]
            }

        self.last_update_params: list[str | None] = []

    def list_collections(self):
        self.calls.append(("collections", {}))
        return self._collections, self._headers()

    def list_raindrops(self, collection_id: int, *, last_update: str | None = None):
        self.calls.append(
            ("raindrops", {"collection_id": collection_id, "last_update": last_update})
        )
        self.last_update_params.append(last_update)
        return self._items[collection_id], self._headers()

    def _headers(self) -> dict[str, str]:
        return {
            "X-RateLimit-Remaining": str(self.rate_limit_remaining),
            "X-RateLimit-Reset": str(self.rate_limit_reset),
        }


class StaticTagger:
    def __init__(self) -> None:
        self.calls: list[list[int]] = []

    def generate(self, documents: list[dict]) -> dict:
        self.calls.append([doc["raindrop_id"] for doc in documents])
        suggestions = {}
        for doc in documents:
            suggestions[doc["raindrop_id"]] = [
                {
                    "tag": f"tag-{doc['raindrop_id']}",
                    "confidence": 0.85,
                    "source": "llm",
                }
            ]
        return {"suggestions": suggestions, "failures": {}}


def _content_fetcher(url: str) -> str:
    return f"payload:{url}"


def _now_generator(start: datetime):
    current = start

    def _inner() -> datetime:
        nonlocal current
        value = current
        current = current + timedelta(minutes=5)
        return value

    return _inner


def test_incremental_sync_only_processes_updates(tmp_path):
    data_dir = tmp_path / "workspace"
    data_dir.mkdir()
    now = _now_generator(datetime(2025, 1, 1, 12, 0, tzinfo=timezone.utc))

    # Seed baseline with a full sync
    full_client = IncrementalRaindropClient(stage="full")
    tagger = StaticTagger()
    sync.run_full_sync(
        data_dir=data_dir,
        api_client=full_client,
        tagging_service=tagger,
        content_fetcher=_content_fetcher,
        now=now,
    )

    incremental_client = IncrementalRaindropClient(stage="incremental")
    summary = sync.run_incremental_sync(
        data_dir=data_dir,
        api_client=incremental_client,
        tagging_service=tagger,
        content_fetcher=_content_fetcher,
        now=now,
    )

    assert summary["mode"] == "incremental"
    assert summary["processed"] == 2  # one new + one updated existing
    assert summary["skipped"] == 0
    assert summary["rate_limit_remaining"] == incremental_client.rate_limit_remaining

    # Ensure lastUpdate filter applied
    assert incremental_client.last_update_params[-1] is not None

    db_path = data_dir / "raindrop.sqlite"
    conn = sqlite3.connect(db_path)
    try:
        rows = conn.execute("SELECT COUNT(*) FROM links").fetchone()[0]
        assert rows == 2  # still two unique links (deduped)
        titles = dict(conn.execute("SELECT raindrop_id, title FROM links"))
        assert titles[201] == "Baseline Updated"
        assert titles[202] == "New Link"
        sync_run_modes = [
            row[0]
            for row in conn.execute(
                "SELECT mode FROM sync_runs ORDER BY started_at"
            ).fetchall()
        ]
        assert sync_run_modes == ["full", "incremental"]
    finally:
        conn.close()

    export_path = Path(summary["export_path"])
    payload = json.loads(export_path.read_text(encoding="utf-8"))
    assert {link["raindrop_id"] for link in payload["links"]} == {201, 202}
