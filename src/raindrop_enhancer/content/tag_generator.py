from __future__ import annotations

from dataclasses import asdict
import json
from typing import List, Callable, Iterable, Optional, Tuple, Any
from datetime import datetime, timezone

from ..tagging import GeneratedTag, TagGenerationMetadata


# Predictor: legacy callable that accepts a prompt string and returns
# (list[str], Optional[int]). We also accept a `dspy.Predict` object which
# when called returns a `Prediction` object exposing `.tags` and optionally
# `.get_lm_usage()`. The runner normalizes both shapes to the legacy
# (list[str], Optional[int]) tuple for downstream processing.
Predictor = Callable[[str], Tuple[List[str], Optional[int]]]


def normalize_tag_value(s: str) -> str:
    s = s.strip()
    if not s:
        return ""
    # Simple Title Case normalization; real implementation should be locale-aware
    s = s.title()
    if len(s) > 40:
        s = s[:40]
    return s


def normalize_tags(raw: Iterable[str], limit: int = 10) -> List[GeneratedTag]:
    out: List[GeneratedTag] = []
    seen = set()
    for r in raw:
        v = normalize_tag_value(r)
        if not v:
            continue
        key = v.lower()
        if key in seen:
            continue
        seen.add(key)
        out.append(GeneratedTag(value=v))
        if len(out) >= limit:
            break
    return out


class TagGenerationRunner:
    def __init__(
        self,
        predictor: Any,
        *,
        model_name: Optional[str] = None,
        batch_size: int = 1,
    ):
        """Runner to generate tags for items.

        predictor: callable(prompt) -> (list[str], Optional[int]) or a
                   dspy.Predict object which returns Prediction objects.
        model_name: optional model identifier for metadata
        batch_size: number of items to process per internal batch (defaults to 1)
        """
        # predictor may be either the legacy callable or a `dspy.Predict` object.
        # We'll accept both and normalize at call time.
        self.predictor = predictor
        self.model_name = model_name or "unknown"
        self.batch_size = max(1, int(batch_size))

    def run_batch(self, items: Iterable[tuple], on_result: Optional[Callable[[dict], None]] = None) -> List[tuple]:
        """Process items and return list of (raindrop_id, tags_json_str, meta_json_str).

        items: Iterable of (raindrop_id, title, url, content_markdown)
        on_result: optional callback called with a dict for each processed link
        """
        results: List[tuple] = []
        batch = []

        def flush_batch(b):
            # Always call predictor per-item (do not rely on batch API).
            for rid, title, url, content in b:
                try:
                    prompt = f"Generate up to 10 concise tags for the following content:\nTitle: {title}\nContent: {content or ''}"
                    # Call predictor (expects a Prediction-like object)
                    out = self.predictor(prompt)
                    raw_tags = getattr(out, "tags", [])
                    tokens_used = None
                    try:
                        usage = out.get_lm_usage()
                        if hasattr(usage, "total_tokens"):
                            tokens_used = int(getattr(usage, "total_tokens"))
                        elif hasattr(usage, "tokens"):
                            tokens_used = int(getattr(usage, "tokens"))
                    except Exception:
                        tokens_used = None

                    tags = normalize_tags(raw_tags)
                    tags_json = json.dumps([t.value for t in tags])
                    meta = TagGenerationMetadata(
                        generated_at=datetime.now(timezone.utc).isoformat(),
                        model=self.model_name,
                        tokens_used=tokens_used,
                        status="success" if tags else "failed",
                        failure_reason=None if tags else "empty_result",
                    )
                    meta_json = json.dumps(asdict(meta))
                    res = (rid, tags_json, meta_json)
                except Exception as e:
                    meta = TagGenerationMetadata(
                        generated_at=datetime.now(timezone.utc).isoformat(),
                        model=self.model_name,
                        tokens_used=None,
                        status="failed",
                        failure_reason=str(e),
                    )
                    res = (rid, json.dumps([]), json.dumps(asdict(meta)))

                results.append(res)
                if on_result:
                    on_result(
                        {
                            "raindrop_id": res[0],
                            "tags_json": res[1],
                            "meta_json": res[2],
                        }
                    )

        for item in items:
            batch.append(item)
            if len(batch) >= self.batch_size:
                flush_batch(batch)
                batch = []

        if batch:
            flush_batch(batch)

        return results
