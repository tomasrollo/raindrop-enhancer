"""Performance benchmark for the Raindrop Link Enhancer CLI.

This script runs a dry-run full sync against a FakeClient and a lightweight
in-memory repository to measure throughput (links processed / second).

Usage: run from project root with the workspace Python environment, for
example:

    uv run python scripts/perf/benchmark_sync.py

The benchmark is intentionally simple and deterministic so it can be used
to compare changes over time.
"""

import time
import json
from pathlib import Path
from typing import Iterator, Dict, Any

from raindrop_enhancer.services.sync import run_full_sync


class FakeClient:
    def __init__(self, collections=1, per_collection=100):
        self._collections = collections
        self._per_collection = per_collection
        self.last_rate_limit = None

    def list_collections(self) -> Dict[str, Any]:
        return {
            "items": [
                {"id": f"c{i}", "title": f"col{i}"} for i in range(self._collections)
            ]
        }

    def list_raindrops(
        self, collection_id: str, perpage: int = 50
    ) -> Iterator[Dict[str, Any]]:
        # yield pages of fake raindrop items
        total = self._per_collection
        page = 0
        while page * perpage < total:
            start = page * perpage
            end = min(total, start + perpage)
            items = [
                {
                    "id": f"{collection_id}-{i}",
                    "link": f"https://example.com/{collection_id}/{i}",
                    "title": f"Title {i}",
                }
                for i in range(start, end)
            ]
            yield {"items": items}
            page += 1


class InMemoryRepo:
    def __init__(self):
        self.links = {}

    def upsert_link(self, lr):
        # accept dict-like or model-like objects
        try:
            rid = getattr(lr, "raindrop_id", None) or lr.get("raindrop_id")
        except Exception:
            rid = None
        if rid is None:
            rid = getattr(lr, "url", None) or (
                lr.get("url") if isinstance(lr, dict) else None
            )
        self.links[rid] = lr

    def upsert_tag_suggestions(self, raindrop_id, tags):
        # no-op for benchmark
        return


def main():
    # Configure benchmark parameters
    collections = 2
    per_collection = 100
    perpage = 50

    client = FakeClient(collections=collections, per_collection=per_collection)
    repo = InMemoryRepo()

    start = time.time()
    result = run_full_sync(
        repo=repo,
        client=client,
        tagging_adapter=None,
        export_path=None,
        dry_run=True,
        perpage=perpage,
    )
    elapsed = time.time() - start

    processed = result.get("processed") or 0
    throughput = processed / elapsed if elapsed > 0 else 0

    out = {
        "processed": processed,
        "elapsed_seconds": elapsed,
        "throughput_rps": throughput,
        "result": result,
    }

    print(json.dumps(out, indent=2))


if __name__ == "__main__":
    main()
