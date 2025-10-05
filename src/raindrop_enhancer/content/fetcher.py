from __future__ import annotations

import dataclasses
import time
from typing import Optional

import importlib


class FetchError(Exception):
    """Domain-level fetch error for fetcher-specific failures.

    Currently unused (we return FetchResult.error for failures) but kept for
    future extension where callers may prefer exceptions.
    """


@dataclasses.dataclass
class FetchResult:
    """Result container for a single fetch attempt.

    Fields:
    - url: the target URL
    - markdown: the extracted markdown string on success (None on failure)
    - error: textual error description when markdown is None
    - retry_count: number of retries performed (reserved for future use)
    """

    url: str
    markdown: Optional[str]
    error: Optional[str]
    retry_count: int = 0


class TrafilaturaFetcher:
    """Thin wrapper around Trafilatura's `fetch_url` + `extract`.

    Implementation notes / assumptions:
    - synchronous by design for the MVP which keeps interactions simple and
      easy to test.
    - imports `trafilatura` at call-time so unit tests can monkeypatch
      `sys.modules['trafilatura']` to provide fake behaviour.
    - passes timeout positionally for compatibility with different
      trafilatura function signatures (some variants accept timeout
      as a positional argument).
    - All exceptions are captured and returned as `FetchResult.error` so
      the caller (CaptureRunner) can decide retry/skip semantics.

    Extension points:
    - Add shared HTTP session reuse (e.g., session pooling) to improve perf.
    - Implement retry/backoff logic here and populate `retry_count`.
    - Add logging hooks for observability on fetch start/finish/error.
    """

    def __init__(self, timeout: float = 10.0):
        # Per-link timeout in seconds (float)
        self.timeout = timeout

    def fetch(self, url: str) -> FetchResult:
        """Fetch the URL and return markdown or an error description.

        The function intentionally swallows exceptions and maps them to a
        FetchResult so callers can remain synchronous and decide how to
        treat failures (retry vs skip vs abort).
        """
        try:
            # Import trafilatura at call-time so tests can monkeypatch sys.modules prior to invocation.
            trafilatura = importlib.import_module("trafilatura")
            # Some implementations accept timeout positionally; pass it positionally for compatibility.
            downloaded = trafilatura.fetch_url(url, self.timeout)
            if not downloaded:
                # Trafilatura may return empty content for pages it cannot parse
                return FetchResult(
                    url=url, markdown=None, error="no_content", retry_count=0
                )
            # Extract markdown; `output_format="markdown"` chosen per spec
            markdown = trafilatura.extract(downloaded, output_format="markdown")
            return FetchResult(url=url, markdown=markdown, error=None)
        except (
            Exception
        ) as exc:  # pragma: no cover - allow exceptions to surface in integration
            # Return a structured error rather than raising to keep runner logic simple
            return FetchResult(url=url, markdown=None, error=str(exc))
