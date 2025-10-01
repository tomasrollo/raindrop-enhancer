"""Retry/backoff helper with exponential backoff, jitter, Retry-After support, and telemetry hooks."""

import time
import random
from typing import Callable, Any, Optional


def backoff(attempt: int, base: float = 1.0, cap: float = 60.0) -> float:
    delay = min(cap, base * (2**attempt))
    # full jitter
    return random.uniform(0, delay)


class Retry:
    def __init__(
        self,
        max_attempts: int = 5,
        base: float = 1.0,
        cap: float = 60.0,
        on_telemetry: Optional[Callable[[str, dict], None]] = None,
    ):
        self.max_attempts = max_attempts
        self.base = base
        self.cap = cap
        self.on_telemetry = on_telemetry

    def emit(self, event: str, data: dict):
        if self.on_telemetry:
            self.on_telemetry(event, data)

    def __call__(self, func: Callable):
        def wrapper(*args, **kwargs):
            attempt = 0
            while attempt < self.max_attempts:
                try:
                    return func(*args, **kwargs)
                except Exception as e:
                    retry_after = self._extract_retry_after(e)
                    if retry_after is not None:
                        delay = retry_after
                        self.emit(
                            "retry_after",
                            {"attempt": attempt, "delay": delay, "error": str(e)},
                        )
                    else:
                        delay = backoff(attempt, self.base, self.cap)
                        self.emit(
                            "backoff",
                            {"attempt": attempt, "delay": delay, "error": str(e)},
                        )
                    time.sleep(delay)
                    attempt += 1
            self.emit("fail", {"attempts": attempt})
            raise RuntimeError(f"Max retry attempts ({self.max_attempts}) exceeded.")

        return wrapper

    @staticmethod
    def _extract_retry_after(exc: Exception) -> Optional[float]:
        # Look for 'Retry-After' in exception attributes or response headers
        retry_after = None
        if hasattr(exc, "response"):
            resp = getattr(exc, "response")
            if hasattr(resp, "headers"):
                ra = resp.headers.get("Retry-After")
                if ra is not None:
                    try:
                        retry_after = float(ra)
                    except Exception:
                        pass
        return retry_after


# Example usage:
# @Retry(max_attempts=3, on_telemetry=lambda event, data: print(event, data))
# def flaky(): ...
