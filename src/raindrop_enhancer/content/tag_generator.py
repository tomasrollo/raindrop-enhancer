from __future__ import annotations

from dataclasses import asdict
import json
from typing import List, Callable, Iterable, Optional, Tuple
from datetime import datetime, timezone

from ..tagging import GeneratedTag, TagGenerationMetadata


# Predictor: callable that accepts a prompt string and returns (list[str], Optional[int])
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
        predictor: Predictor,
        *,
        model_name: Optional[str] = None,
        batch_size: int = 1,
    ):
        """Runner to generate tags for items.

        predictor: callable(prompt) -> (list[str], Optional[int])
        model_name: optional model identifier for metadata
        batch_size: number of items to process per internal batch (defaults to 1)
        """
        # predictor is a callable: prompt -> (List[str], Optional[int])
        self.predictor = predictor
        self.model_name = model_name or "unknown"
        self.batch_size = max(1, int(batch_size))

    def run_batch(
        self, items: Iterable[tuple], on_result: Optional[Callable[[dict], None]] = None
    ) -> List[tuple]:
        """Process items and return list of (raindrop_id, tags_json_str, meta_json_str).

        items: Iterable of (raindrop_id, title, url, content_markdown)
        on_result: optional callback called with a dict for each processed link
        """
        results: List[tuple] = []
        batch = []

        def flush_batch(b):
            # Attempt batch prediction when underlying predictor exposes a batch API.
            if hasattr(self.predictor, "batch"):
                try:
                    # Build prompts for the batch
                    prompts = [
                        f"Generate up to 10 concise tags for the following content:\nTitle: {title}\nContent: {content or ''}"
                        for (_rid, title, _url, content) in b
                    ]

                    batch_out = self.predictor.batch(prompts)
                    # Expect batch_out to be an iterable of (list[str], Optional[int])
                    for item, out in zip(b, batch_out):
                        rid, title, url, content = item
                        try:
                            raw_tags, tokens_used = out
                        except Exception:
                            # If shape is unexpected, coerce best-effort
                            try:
                                raw_tags = out
                                tokens_used = None
                            except Exception:
                                raw_tags = []
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
                        results.append(res)
                        if on_result:
                            on_result(
                                {
                                    "raindrop_id": res[0],
                                    "tags_json": res[1],
                                    "meta_json": res[2],
                                }
                            )
                    return
                except Exception:
                    # Batch failed; fall back to per-item handling below
                    pass

            # Per-item fallback
            for rid, title, url, content in b:
                try:
                    prompt = f"Generate up to 10 concise tags for the following content:\nTitle: {title}\nContent: {content or ''}"
                    raw_tags, tokens_used = self.predictor(prompt)
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
