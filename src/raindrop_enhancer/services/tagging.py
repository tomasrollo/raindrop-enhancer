"""Tagging adapter and helpers.

Provides a small adapter that can batch multiple content items and return
tag suggestions with confidences. The implementation includes a deterministic
mock mode (no network calls) useful for tests and early integration; a real
HTTP adapter can be plugged in later.
"""

from typing import List, Dict, Iterable, Optional, Any
import re

from raindrop_enhancer.util.retry import retryable


class TaggingAdapter:
    """Adapter to obtain tag suggestions for content.

    The current implementation ships a deterministic, local mocker that
    generates tags from content words (useful for tests). The adapter can be
    configured with `max_tags` and `confidence_threshold` to filter results.
    """

    def __init__(
        self,
        llm_api_base: Optional[str] = None,
        llm_api_key: Optional[str] = None,
        *,
        max_tags: int = 10,
        confidence_threshold: float = 0.6,
    ):
        self.llm_api_base = llm_api_base
        self.llm_api_key = llm_api_key
        self.max_tags = int(max_tags)
        self.confidence_threshold = float(confidence_threshold)

    def _mock_tags_from_text(self, text: str) -> List[Dict[str, Any]]:
        # Deterministic tokenization: take unique words longer than 4 chars
        words = re.findall(r"[a-zA-Z]{5,}", text)
        seen = []
        for w in words:
            lw = w.lower()
            if lw not in seen:
                seen.append(lw)

        tags = []
        for w in seen[: self.max_tags]:
            # deterministic confidence from word length
            confidence = min(1.0, 0.5 + (len(w) / 20.0))
            tags.append(
                {"tag": w, "confidence": round(confidence, 3), "source": "mock-llm"}
            )
        return tags

    @retryable()
    def suggest_for_batch(self, texts: Iterable[str]) -> List[List[Dict[str, Any]]]:
        """Return per-text list of tag suggestion dicts.

        If an external llm_api_base is configured, this method would call the
        remote endpoint. For now we use the deterministic mock implementation.
        """
        out = []
        for t in texts:
            tags = self._mock_tags_from_text(t or "")
            # apply confidence threshold
            tags = [
                tg
                for tg in tags
                if float(tg.get("confidence", 0.0)) >= self.confidence_threshold
            ]
            out.append(tags)
        return out


_default_adapter = TaggingAdapter()


def suggest_tags_for_content(content: str) -> List[Dict[str, Any]]:
    """Convenience function used by existing tests and callers.

    Returns a list of tag dicts with `tag`, `confidence`, and `source`.
    """
    return _default_adapter.suggest_for_batch([content])[0]
