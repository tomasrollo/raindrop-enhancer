"""LLM tagging adapter used to enrich Raindrop links."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Callable, Iterable

import requests

from raindrop_enhancer.util import retry


def _chunked(items: list[dict], size: int) -> Iterable[list[dict]]:
    for index in range(0, len(items), size):
        yield items[index : index + size]


@dataclass(slots=True)
class TaggingService:
    """High-level interface for generating tag suggestions via an LLM API."""

    api_base: str
    api_key: str
    batch_size: int = 25
    confidence_threshold: float = 0.5
    max_tags: int = 5
    timeout: float = 30.0
    transport: Callable[[list[dict]], list[dict]] | None = None

    def __post_init__(self) -> None:
        if self.batch_size <= 0:
            raise ValueError("batch_size must be positive")
        if not (0.0 <= self.confidence_threshold <= 1.0):
            raise ValueError("confidence_threshold must be between 0 and 1")
        if self.max_tags < 0:
            raise ValueError("max_tags must be >= 0")

    # ------------------------------------------------------------------
    def generate(self, documents: list[dict]) -> dict:
        """Generate tag suggestions for the supplied documents.

        Returns a mapping with ``suggestions`` and ``failures`` keys. Failures
        are recorded per ``raindrop_id`` with an explanatory message.
        """

        if not documents:
            return {"suggestions": {}, "failures": {}}

        effective_transport = self.transport or self._http_transport
        suggestions: dict[int, list[dict]] = {}
        failures: dict[int, str] = {}

        for batch in _chunked(documents, self.batch_size):
            try:
                responses = effective_transport(batch)
            except Exception as exc:  # pragma: no cover - exercised in tests
                message = str(exc) or exc.__class__.__name__
                for doc in batch:
                    failures[doc["raindrop_id"]] = message
                continue

            index = {
                entry["raindrop_id"]: entry.get("suggestions", [])
                for entry in responses or []
                if "raindrop_id" in entry
            }

            for doc in batch:
                raindrop_id = doc["raindrop_id"]
                raw_suggestions = list(index.get(raindrop_id, []))
                filtered = [
                    {
                        "tag": item.get("tag"),
                        "confidence": float(item.get("confidence", 0.0)),
                        "source": item.get("source", "llm"),
                    }
                    for item in raw_suggestions
                    if float(item.get("confidence", 0.0)) >= self.confidence_threshold
                ]
                filtered.sort(
                    key=lambda item: item.get("confidence", 0.0), reverse=True
                )
                if self.max_tags:
                    filtered = filtered[: self.max_tags]
                suggestions[raindrop_id] = filtered

        return {"suggestions": suggestions, "failures": failures}

    # ------------------------------------------------------------------
    def _http_transport(self, documents: list[dict]) -> list[dict]:
        """Default HTTP transport implementation using ``requests``."""

        headers = {
            "Authorization": f"Bearer {self.api_key}",
            "Content-Type": "application/json",
            "Accept": "application/json",
        }
        payload = {"documents": documents}

        def _call() -> list[dict]:
            response = requests.post(
                self.api_base,
                json=payload,
                headers=headers,
                timeout=self.timeout,
            )
            if response.status_code >= 500:
                raise retry.RetryableError(
                    f"LLM API returned {response.status_code}",
                    context={"status_code": response.status_code},
                )
            if response.status_code == 429:
                retry_after = response.headers.get("Retry-After")
                raise retry.RetryableError(
                    "LLM API rate limited",
                    retry_after=float(retry_after) if retry_after else None,
                    context={"status_code": response.status_code},
                )
            response.raise_for_status()
            body = response.json()
            return body.get("results", body.get("data", body))

        return retry.retry(_call)
