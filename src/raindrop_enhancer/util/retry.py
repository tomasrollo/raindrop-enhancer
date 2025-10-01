"""Retry/backoff helper stub."""

import time
import random


def backoff(attempt: int, base: float = 1.0, cap: float = 60.0):
    delay = min(cap, base * (2**attempt))
    # full jitter
    return random.uniform(0, delay)
