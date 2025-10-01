"""Unit tests for the LLM tagging adapter."""

from __future__ import annotations

from datetime import datetime, timezone

import pytest

from raindrop_enhancer.services.tagging import TaggingService


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
