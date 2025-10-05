from __future__ import annotations

import dataclasses
import time
from typing import Optional

import importlib


class FetchError(Exception):
    pass


@dataclasses.dataclass
class FetchResult:
    url: str
    markdown: Optional[str]
    error: Optional[str]
    retry_count: int = 0


class TrafilaturaFetcher:
    """Simple wrapper around trafilatura.fetch_url + extract to produce markdown.

    This is intentionally synchronous for the MVP and keeps a shared session.
    """

    def __init__(self, timeout: float = 10.0):
        self.timeout = timeout

    def fetch(self, url: str) -> FetchResult:
        try:
            # Import trafilatura at call-time so tests can monkeypatch sys.modules prior to invocation.
            trafilatura = importlib.import_module("trafilatura")
            # Some implementations accept timeout positionally; pass it positionally for compatibility.
            downloaded = trafilatura.fetch_url(url, self.timeout)
            if not downloaded:
                return FetchResult(
                    url=url, markdown=None, error="no_content", retry_count=0
                )
            markdown = trafilatura.extract(downloaded, output_format="markdown")
            return FetchResult(url=url, markdown=markdown, error=None)
        except (
            Exception
        ) as exc:  # pragma: no cover - allow exceptions to surface in integration
            return FetchResult(url=url, markdown=None, error=str(exc))
