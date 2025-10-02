"""Performance benchmark harness for the Raindrop Link Enhancer CLI."""

from __future__ import annotations

import argparse
import json
import logging
import math
import random
import shutil
import sys
import time
from datetime import datetime, timedelta, timezone
from pathlib import Path
from tempfile import TemporaryDirectory
from typing import Any

from raindrop_enhancer.services import sync
from raindrop_enhancer.util.logging import configure_logging, get_metrics


def main() -> None:
    args = _parse_args()
    configure_logging(logging.ERROR if args.quiet else logging.INFO)

    temp_dir: TemporaryDirectory[str] | None = None
    if args.data_dir:
        data_dir = Path(args.data_dir).expanduser().resolve()
        data_dir.mkdir(parents=True, exist_ok=True)
    else:
        temp_dir = TemporaryDirectory()
        data_dir = Path(temp_dir.name)

    try:
        result = _run_benchmark(
            data_dir=data_dir,
            total_links=args.links,
            collections=args.collections,
            batch_size=args.batch_size,
            seed=args.seed,
        )
        result["sla_seconds"] = args.sla
        result["status"] = "pass" if result["duration_seconds"] <= args.sla else "fail"
        result["data_dir"] = str(data_dir)

        print(json.dumps(result, indent=2), file=sys.stdout)

        sys.exit(0 if result["status"] == "pass" else 1)
    finally:
        if temp_dir is not None:
            temp_dir.cleanup()


def _parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Benchmark full sync throughput")
    parser.add_argument(
        "--data-dir", type=str, help="Optional directory for benchmark artifacts"
    )
    parser.add_argument(
        "--links", type=int, default=1000, help="Total links to generate in fixture"
    )
    parser.add_argument(
        "--collections",
        type=int,
        default=10,
        help="Number of collections to spread links across",
    )
    parser.add_argument(
        "--batch-size",
        type=int,
        default=50,
        help="Batch size forwarded to sync pipeline",
    )
    parser.add_argument(
        "--sla",
        type=float,
        default=60.0,
        help="Target completion time in seconds",
    )
    parser.add_argument(
        "--seed", type=int, default=0, help="Seed for deterministic fixtures"
    )
    parser.add_argument("--quiet", action="store_true", help="Suppress INFO logs")
    return parser.parse_args()


def _run_benchmark(
    *,
    data_dir: Path,
    total_links: int,
    collections: int,
    batch_size: int,
    seed: int,
) -> dict[str, Any]:
    _reset_data_dir(data_dir)
    random.seed(seed)

    client = BenchmarkRaindropClient(
        total_links=total_links, collection_count=collections
    )
    tagging_service = BenchmarkTaggingService()
    now = _monotonic_clock()

    start = time.perf_counter()
    summary = sync.run_full_sync(
        data_dir=data_dir,
        api_client=client,
        tagging_service=tagging_service,
        content_fetcher=_content_fetcher,
        now=now,
        batch_size=batch_size,
        dry_run=False,
    )
    duration = time.perf_counter() - start

    metrics_snapshot = get_metrics().snapshot()

    return {
        "links": total_links,
        "collections": collections,
        "batch_size": batch_size,
        "duration_seconds": duration,
        "sync_summary": summary,
        "metrics": metrics_snapshot,
    }


def _reset_data_dir(data_dir: Path) -> None:
    if not data_dir.exists():
        data_dir.mkdir(parents=True, exist_ok=True)
        return

    for pattern in ["raindrop.sqlite", "exports", "config.toml"]:
        target = data_dir / pattern
        if target.is_file():
            target.unlink()
        elif target.is_dir():
            shutil.rmtree(target)


class BenchmarkRaindropClient:
    """Deterministic Raindrop client fixture used for benchmarks."""

    def __init__(self, *, total_links: int, collection_count: int) -> None:
        self.collection_count = max(1, collection_count)
        self.total_links = max(1, total_links)
        self.limit = 120
        self.remaining = 120
        self.reset_epoch = int(time.time()) + 60

        self._collections: list[dict[str, Any]] = []
        self._items: dict[int, list[dict[str, Any]]] = {}

        links_per_collection = math.ceil(self.total_links / self.collection_count)
        raindrop_id = 1

        for index in range(self.collection_count):
            collection_id = index + 1
            self._collections.append(
                {
                    "id": collection_id,
                    "title": f"Collection {collection_id}",
                    "color": None,
                    "lastUpdate": "2025-01-01T00:00:00Z",
                }
            )
            items: list[dict[str, Any]] = []
            for _ in range(links_per_collection):
                if raindrop_id > self.total_links:
                    break
                items.append(
                    {
                        "id": raindrop_id,
                        "collectionId": collection_id,
                        "title": f"Benchmark Link {raindrop_id}",
                        "link": f"https://example.com/{raindrop_id}",
                        "excerpt": f"Summary for {raindrop_id}",
                        "tags": ["benchmark"],
                        "created": "2025-01-01T00:00:00Z",
                        "lastUpdate": "2025-01-02T00:00:00Z",
                    }
                )
                raindrop_id += 1
            self._items[collection_id] = items

    def list_collections(self) -> tuple[list[dict[str, Any]], dict[str, str]]:
        self._consume_rate_limit()
        return self._collections, self._headers()

    def list_raindrops(
        self,
        collection_id: int,
        *,
        last_update: str | None = None,
        per_page: int = 50,
    ) -> tuple[list[dict[str, Any]], dict[str, str]]:
        self._consume_rate_limit()
        return list(self._items.get(collection_id, [])), self._headers()

    def fetch_raindrop(self, raindrop_id: int) -> tuple[dict[str, Any], dict[str, str]]:
        self._consume_rate_limit()
        for items in self._items.values():
            for item in items:
                if item["id"] == raindrop_id:
                    return item, self._headers()
        raise KeyError(raindrop_id)

    def close(self) -> None:  # pragma: no cover - compatibility shim
        return None

    def _headers(self) -> dict[str, str]:
        return {
            "X-RateLimit-Limit": str(self.limit),
            "X-RateLimit-Remaining": str(max(0, self.remaining)),
            "X-RateLimit-Reset": str(self.reset_epoch),
        }

    def _consume_rate_limit(self) -> None:
        self.remaining = max(0, self.remaining - 1)


class BenchmarkTaggingService:
    """Synthetic tagging service returning deterministic suggestions."""

    def __init__(self) -> None:
        self.calls: list[list[int]] = []

    def generate(self, documents: list[dict[str, Any]]) -> dict[str, Any]:
        self.calls.append([doc["raindrop_id"] for doc in documents])
        suggestions: dict[int, list[dict[str, Any]]] = {}
        for doc in documents:
            suggestions[doc["raindrop_id"]] = [
                {
                    "tag": f"topic-{doc['raindrop_id'] % 10}",
                    "confidence": 0.9,
                    "source": "benchmark",
                }
            ]
        return {"suggestions": suggestions, "failures": {}}


def _content_fetcher(url: str) -> str:
    return f"content:{url}"


def _monotonic_clock():
    current = datetime(2025, 1, 1, 12, 0, tzinfo=timezone.utc)

    def _next() -> datetime:
        nonlocal current
        stamp = current
        current = current + timedelta(seconds=1)
        return stamp

    return _next


if __name__ == "__main__":
    main()
