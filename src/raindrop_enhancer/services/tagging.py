"""Tagging adapter: LLM batch requests, confidence filtering, error handling, retry support."""

from typing import List, Dict, Any, Optional
from ..util.retry import Retry


class TaggingService:
    def __init__(
        self,
        llm_client,
        confidence_threshold: float = 0.5,
        max_batch: int = 10,
        retry: Optional[Retry] = None,
    ):
        self.llm_client = llm_client
        self.confidence_threshold = confidence_threshold
        self.max_batch = max_batch
        self.retry = retry or Retry()

    def batch_suggest_tags(self, contents: List[str]) -> List[List[Dict[str, Any]]]:
        results = []
        for i in range(0, len(contents), self.max_batch):
            batch = contents[i : i + self.max_batch]
            try:
                tags_batch = self.retry(self.llm_client.suggest_tags)(batch)
            except Exception as e:
                # Tag all failed with error
                tags_batch = [
                    [{"tag": "error", "confidence": 0.0, "error": str(e)}]
                    for _ in batch
                ]
            # Filter by confidence
            filtered = [
                [
                    t
                    for t in tags
                    if t.get("confidence", 0.0) >= self.confidence_threshold
                ]
                for tags in tags_batch
            ]
            results.extend(filtered)
        return results

    def suggest_tags_for_content(self, content: str) -> List[Dict[str, Any]]:
        return self.batch_suggest_tags([content])[0]


# Simple wrapper for legacy usage
def suggest_tags_for_content(content: str):
    # This should be replaced with a real LLM client instance
    class DummyLLM:
        def suggest_tags(self, batch):
            # Fake: returns a single tag with random confidence
            import random

            return [
                [{"tag": "example", "confidence": random.uniform(0, 1)}] for _ in batch
            ]

    service = TaggingService(DummyLLM())
    return service.suggest_tags_for_content(content)
