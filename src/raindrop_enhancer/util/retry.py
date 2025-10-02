"""Retry/backoff helper.

Provides a small backoff function used by the service layer and a simple
decorator to apply retries to callables. The implementation is intentionally
small and deterministic-friendly for unit tests.
"""

import time
import random
from typing import Callable, Type, Tuple


def backoff(attempt: int, base: float = 1.0, cap: float = 60.0) -> float:
    """Return a jittered exponential backoff delay in seconds.

    attempt: 0-based retry attempt number
    """
    # exponential factor
    delay = min(cap, base * (2**attempt))
    # full jitter between 0 and delay
    return float(random.uniform(0, delay))


def retryable(
    exceptions: Tuple[Type[BaseException], ...] = (Exception,),
    max_attempts: int = 3,
    base: float = 1.0,
    cap: float = 60.0,
):
    """Simple retry decorator.

    Retries the wrapped callable when one of `exceptions` is raised.
    """

    def _decorator(fn: Callable):
        def _wrapped(*args, **kwargs):
            attempt = 0
            while True:
                try:
                    return fn(*args, **kwargs)
                except exceptions:
                    attempt += 1
                    if attempt >= max_attempts:
                        raise
                    delay = backoff(attempt - 1, base=base, cap=cap)
                    time.sleep(delay)

        return _wrapped

    return _decorator
