"""Performance test utilities: synthetic data builders and timing helpers."""

from __future__ import annotations

import time
from datetime import datetime, timedelta
from typing import Iterable, Dict, List


def make_raindrop_payloads(count: int, start: datetime | None = None) -> List[Dict]:
    """Generate synthetic Raindrop API payloads with monotonically increasing created timestamps."""
    start = start or datetime.utcnow() - timedelta(seconds=count)
    out: List[Dict] = []
    for i in range(count):
        created = (start + timedelta(seconds=i)).isoformat() + "Z"
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
