"""Reusable retry helpers for API calls and external integrations."""

from __future__ import annotations

import random
import time
from dataclasses import dataclass
from typing import Any, Callable, Protocol

DEFAULT_ATTEMPTS = 5
DEFAULT_BASE = 1.0
DEFAULT_CAP = 60.0


class SupportsRetryAfter(Protocol):
    """Protocol for exceptions exposing retry metadata."""

    @property
    def retry_after(self) -> float | None:  # pragma: no cover - protocol hook
        ...


@dataclass(slots=True)
class RetryEvent:
    """Telemetry payload describing a single retry attempt."""

    attempt: int
    delay: float
    retry_after: float | None
    error: Exception | None
    context: dict[str, Any]


class RetryableError(RuntimeError):
    """Raised when an operation should be retried with backoff."""

    def __init__(
        self,
        message: str,
        *,
        retry_after: float | None = None,
        context: dict[str, Any] | None = None,
    ) -> None:
        super().__init__(message)
        self.retry_after = retry_after
        self.context = context or {}


def backoff(
    *,
    attempt: int,
    base: float = DEFAULT_BASE,
    cap: float = DEFAULT_CAP,
    retry_after: float | None = None,
) -> float:
    """Compute a jittered backoff delay honoring ``Retry-After`` when present."""

    if retry_after is not None:
        return float(retry_after)

    delay = min(cap, base * (2**attempt))
    return random.uniform(0.0, delay)


def retry(
    operation: Callable[[], Any],
    *,
    attempts: int = DEFAULT_ATTEMPTS,
    base: float = DEFAULT_BASE,
    cap: float = DEFAULT_CAP,
    sleep: Callable[[float], None] = time.sleep,
    on_retry: Callable[[RetryEvent], None] | None = None,
) -> Any:
    """Execute ``operation`` with exponential backoff on ``RetryableError``.

    Parameters
    ----------
    operation:
        Callable that performs the work. It may raise :class:`RetryableError`
        to signal a transient failure that should be retried.
    attempts:
        Total number of attempts (initial try + retries). Defaults to ``5``.
    base / cap:
        Backoff parameters (in seconds) controlling the exponential growth.
    sleep:
        Function used to sleep between attempts. Primarily injected in tests.
    on_retry:
        Optional callback receiving :class:`RetryEvent` telemetry when a retry
        occurs, enabling metrics/structured logging.
    """

    last_error: Exception | None = None

    for attempt in range(attempts):
        try:
            return operation()
        except RetryableError as exc:
            last_error = exc
            if attempt == attempts - 1:
                break

            delay = backoff(
                attempt=attempt,
                base=base,
                cap=cap,
                retry_after=exc.retry_after,
            )
            if on_retry is not None:
                on_retry(
                    RetryEvent(
                        attempt=attempt,
                        delay=delay,
                        retry_after=exc.retry_after,
                        error=exc,
                        context=exc.context,
                    )
                )
            sleep(delay)
        except Exception as exc:  # pragma: no cover - unexpected failure
            last_error = exc
            break

    if last_error is not None:
        raise last_error

    raise RuntimeError("retry() finished without returning or raising")
