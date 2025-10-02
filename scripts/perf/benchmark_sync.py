"""Performance benchmark scaffold for the Raindrop Link Enhancer CLI."""

import json
from pathlib import Path


import time
import tempfile
from raindrop_enhancer.domain.repositories import Repo
from raindrop_enhancer.domain.entities import LinkRecord
from raindrop_enhancer.services.sync import run_full_sync


class FakeTagging:
    def suggest_tags_for_content(self, content):
        return [{"tag": "bench", "confidence": 1.0}]


def main():
    print("Benchmark: 1k-link full sync (target: ≤60s)")
    with tempfile.TemporaryDirectory() as tmpdir:
        db_path = Path(tmpdir) / "bench.db"
        export_path = Path(tmpdir) / "bench_export.json"
        repo = Repo(str(db_path))
        repo.setup()
        # Insert 1k links
        for i in range(1000):
            repo.upsert_link(
                LinkRecord(
                    raindrop_id=i, url=f"https://bench{i}.com", title=f"Bench {i}"
                )
            )
        tagging = FakeTagging()
        start = time.time()
        result = run_full_sync(repo, tagging, export_path, dry_run=False)
        elapsed = time.time() - start
        print(f"Processed: {result['processed']} links in {elapsed:.2f}s")
        if elapsed <= 60:
            print("[PASS] Benchmark met SLA (≤60s)")
        else:
            print("[FAIL] Benchmark exceeded SLA (>60s)")


if __name__ == "__main__":
    main()
