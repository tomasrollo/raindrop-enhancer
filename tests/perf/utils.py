"""Performance test utilities: synthetic data builders and timing helpers."""

from __future__ import annotations

import time
from datetime import datetime, timedelta, timezone
from typing import Iterable, Dict, List


def make_raindrop_payloads(count: int, start: datetime | None = None) -> List[Dict]:
    """Generate synthetic Raindrop API payloads with monotonically increasing created timestamps."""
    # Use timezone-aware UTC datetimes to avoid deprecation warnings
    start = start or (datetime.now(timezone.utc) - timedelta(seconds=count))
    out: List[Dict] = []
    for i in range(count):
        # Ensure ISO8601 UTC with 'Z' suffix
        created_dt = (start + timedelta(seconds=i)).astimezone(timezone.utc)
        created = created_dt.isoformat().replace("+00:00", "Z")
        out.append(
            {
                "_id": 100000 + i,
                "collectionId": 1,
                "title": f"Title {i}",
                "link": f"https://example.invalid/{i}",
                "created": created,
                "tags": [f"tag{i % 5}"],
            }
        )
    return out


class Timer:
    def __init__(self):
        self.start = 0.0
        self.elapsed = 0.0

    def __enter__(self):
        self.start = time.perf_counter()
        return self

    def __exit__(self, exc_type, exc, tb):
        self.elapsed = time.perf_counter() - self.start
