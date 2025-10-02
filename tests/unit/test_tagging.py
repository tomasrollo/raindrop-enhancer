"""Unit tests for the LLM tagging adapter."""

from __future__ import annotations

from datetime import datetime, timezone
from types import SimpleNamespace
from typing import Any

import pytest

from raindrop_enhancer.util import retry as retry_module
from raindrop_enhancer.services.tagging import TaggingService


class DummyResponse:
    def __init__(self, status_code: int, payload: dict | None = None, headers=None):
        self.status_code = status_code
        self._payload = payload or {}
        self.headers = headers or {}

    def json(self) -> dict:
        return self._payload

    def raise_for_status(self) -> None:
        if self.status_code >= 400 and self.status_code not in {429, 500}:
            raise RuntimeError(f"HTTP {self.status_code}")


def _docs(count: int) -> list[dict]:
    now = datetime(2025, 1, 1, tzinfo=timezone.utc)
    documents: list[dict] = []
    for idx in range(count):
        documents.append(
            {
                "raindrop_id": 100 + idx,
                "url": f"https://example.com/{idx}",
                "title": f"Doc {idx}",
                "content": f"Content for {idx}",
                "created_at": now,
            }
        )
    return documents


def test_generate_tags_batches_requests(monkeypatch):
    batches: list[list[int]] = []

    def fake_transport(documents: list[dict]) -> list[dict]:
        batches.append([doc["raindrop_id"] for doc in documents])
        payload = []
        for doc in documents:
            payload.append(
                {
                    "raindrop_id": doc["raindrop_id"],
                    "suggestions": [
                        {
                            "tag": f"tag-{doc['raindrop_id']}",
                            "confidence": 0.9,
                            "source": "llm",
                        }
                    ],
                }
            )
        return payload

    service = TaggingService(
        api_base="https://llm.example.com",
        api_key="key-123",
        batch_size=2,
        confidence_threshold=0.5,
        max_tags=3,
        transport=fake_transport,
    )

    docs = _docs(3)
    result = service.generate(docs)

    assert batches == [[100, 101], [102]]
    assert result["failures"] == {}
    assert result["suggestions"][100][0]["tag"] == "tag-100"


def test_generate_tags_filters_by_confidence_and_truncates():
    def fake_transport(documents: list[dict]) -> list[dict]:
        responses = []
        for doc in documents:
            responses.append(
                {
                    "raindrop_id": doc["raindrop_id"],
                    "suggestions": [
                        {"tag": "keep", "confidence": 0.9, "source": "llm"},
                        {"tag": "drop", "confidence": 0.2, "source": "llm"},
                    ],
                }
            )
        return responses

    service = TaggingService(
        api_base="https://llm.example.com",
        api_key="key-123",
        batch_size=5,
        confidence_threshold=0.5,
        max_tags=1,
        transport=fake_transport,
    )

    docs = _docs(1)
    result = service.generate(docs)

    assert list(result["suggestions"].keys()) == [100]
    assert result["suggestions"][100] == [
        {"tag": "keep", "confidence": 0.9, "source": "llm"}
    ]


def test_generate_tags_records_failures_and_continues():
    def flaky_transport(documents: list[dict]) -> list[dict]:
        if any(doc["raindrop_id"] == 102 for doc in documents):
            raise RuntimeError("LLM offline")
        return [
            {
                "raindrop_id": doc["raindrop_id"],
                "suggestions": [{"tag": "ok", "confidence": 0.7, "source": "llm"}],
            }
            for doc in documents
        ]

    service = TaggingService(
        api_base="https://llm.example.com",
        api_key="key-123",
        batch_size=2,
        confidence_threshold=0.5,
        max_tags=5,
        transport=flaky_transport,
    )

    docs = _docs(3)
    result = service.generate(docs)

    assert 102 in result["failures"]
    assert result["failures"][102].startswith("LLM offline")
    assert 100 in result["suggestions"]
    assert 101 in result["suggestions"]


def test_http_transport_posts_documents(monkeypatch):
    captured: dict[str, Any] = {}

    def fake_post(url, *, json, headers, timeout):  # type: ignore[override]
        captured["url"] = url
        captured["json"] = json
        captured["headers"] = headers
        captured["timeout"] = timeout
        return DummyResponse(
            200,
            payload={
                "results": [
                    {
                        "raindrop_id": entry["raindrop_id"],
                        "suggestions": entry.get("suggestions", []),
                    }
                    for entry in json["documents"]
                ]
            },
        )

    monkeypatch.setattr(
        "raindrop_enhancer.services.tagging.requests.post",
        fake_post,
    )

    service = TaggingService(
        api_base="https://llm.example.com",
        api_key="key-123",
    )

    documents = [{"raindrop_id": 1, "content": "hello"}]
    result = service._http_transport(documents)

    assert captured["url"] == "https://llm.example.com"
    assert captured["headers"]["Authorization"] == "Bearer key-123"
    assert result[0]["raindrop_id"] == 1


def test_http_transport_retries_on_server_error(monkeypatch):
    responses = [
        DummyResponse(500),
        DummyResponse(
            200,
            payload={"results": [{"raindrop_id": 1, "suggestions": []}]},
        ),
    ]
    events: list[retry_module.RetryEvent] = []

    def fake_post(url, *, json, headers, timeout):  # type: ignore[override]
        _ = (url, json, headers, timeout)
        return responses.pop(0)

    monkeypatch.setattr(
        "raindrop_enhancer.services.tagging.requests.post",
        fake_post,
    )
    monkeypatch.setattr(
        retry_module,
        "time",
        SimpleNamespace(sleep=lambda _delay: None),
    )

    service = TaggingService(
        api_base="https://llm.example.com",
        api_key="key-123",
        on_retry=events.append,
    )

    result = service._http_transport([{"raindrop_id": 1}])

    assert result[0]["raindrop_id"] == 1
    assert len(events) == 1


def test_http_transport_retries_on_rate_limit(monkeypatch):
    responses = [
        DummyResponse(429, headers={"Retry-After": "1"}),
        DummyResponse(
            200,
            payload={"results": [{"raindrop_id": 2, "suggestions": []}]},
        ),
    ]

    def fake_post(url, *, json, headers, timeout):  # type: ignore[override]
        _ = (url, json, headers, timeout)
        return responses.pop(0)

    monkeypatch.setattr(
        "raindrop_enhancer.services.tagging.requests.post",
        fake_post,
    )
    monkeypatch.setattr(
        retry_module,
        "time",
        SimpleNamespace(sleep=lambda _delay: None),
    )

    service = TaggingService(
        api_base="https://llm.example.com",
        api_key="key-123",
    )

    result = service._http_transport([{"raindrop_id": 2}])

    assert result[0]["raindrop_id"] == 2
