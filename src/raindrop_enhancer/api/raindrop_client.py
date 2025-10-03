"""Raindrop API client using httpx (Gracy compatible patterns).

Provides simple pagination, auth from env, and retry/backoff for 429s.
"""

from __future__ import annotations

import logging
import os
import random
import time
from typing import Callable, Iterator, List, Optional

import httpx

from ..models import Raindrop


DEFAULT_BASE = "https://api.raindrop.io/rest/v1"

Logger = logging.getLogger(__name__)


class RaindropClient:
    def __init__(
        self,
        token: Optional[str] = None,
        base_url: str = DEFAULT_BASE,
        per_page: int = 50,
        *,
        rate_limit_per_min: int = 120,
        enforce_rate_limit: bool = False,
        on_retry: Optional[Callable[[str, int, float], None]] = None,
        on_request: Optional[Callable[[str], None]] = None,
    ) -> None:
        """Create a RaindropClient.

        - rate_limit_per_min: allowed requests per minute when enforcement is enabled.
        - enforce_rate_limit: if True, enforces spacing between requests to honor rate limit.
        - on_retry: optional callback called on retry attempts: (url, attempt, delay)
        - on_request: optional callback called before each request with the url.
        """
        self.token = token or os.getenv("RAINDROP_TOKEN")
        self.base_url = base_url.rstrip("/")
        self.per_page = per_page
        self.rate_limit_per_min = rate_limit_per_min
        self.enforce_rate_limit = enforce_rate_limit
        self.on_retry = on_retry
        self.on_request = on_request

        self._client = httpx.Client(timeout=30.0)
        self._last_request_ts: float = 0.0

    def _headers(self) -> dict:
        headers = {"Accept": "application/json"}
        if self.token:
            headers["Authorization"] = f"Bearer {self.token}"
        return headers

    def list_collections(self) -> List[dict]:
        url = f"{self.base_url}/collections"
        resp = self._request_with_retry("GET", url)
        data = resp.json()
        return data.get("items", [])

    def list_raindrops(self, collection_id: int) -> Iterator[dict]:
        page = 0
        while True:
            url = f"{self.base_url}/raindrops/{collection_id}"
            params = {"page": page, "perpage": self.per_page}
            resp = self._request_with_retry("GET", url, params=params)
            data = resp.json()
            items = data.get("items", [])
            for it in items:
                yield it
            if not items or len(items) < self.per_page:
                break
            page += 1

    def _enforce_rate_limit_if_needed(self) -> None:
        if not self.enforce_rate_limit or self.rate_limit_per_min <= 0:
            return
        min_interval = 60.0 / float(self.rate_limit_per_min)
        now = time.monotonic()
        elapsed = now - self._last_request_ts
        if elapsed < min_interval:
            to_sleep = min_interval - elapsed
            Logger.debug("Enforcing rate limit: sleeping %.3fs", to_sleep)
            time.sleep(to_sleep)

    def _request_with_retry(
        self, method: str, url: str, params: dict | None = None
    ) -> httpx.Response:
        attempts = 0
        delay = 1.0
        max_delay = 30.0
        while True:
            attempts += 1
            # Rate limit spacing
            self._enforce_rate_limit_if_needed()

            if self.on_request:
                try:
                    self.on_request(url)
                except Exception:
                    Logger.exception("on_request callback raised an exception")

            Logger.debug("Requesting %s %s (attempt %d)", method, url, attempts)
            resp = self._client.request(
                method, url, headers=self._headers(), params=params
            )
            self._last_request_ts = time.monotonic()

            if resp.status_code == 429:
                # Exponential backoff + jitter
                jitter = random.uniform(0, 0.25 * delay)
                to_sleep = min(delay + jitter, max_delay)
                Logger.warning(
                    "Received 429 for %s, backing off %.2fs (attempt %d)",
                    url,
                    to_sleep,
                    attempts,
                )
                if self.on_retry:
                    try:
                        self.on_retry(url, attempts, to_sleep)
                    except Exception:
                        Logger.exception("on_retry callback raised an exception")
                time.sleep(to_sleep)
                delay = min(delay * 2, max_delay)
                continue

            resp.raise_for_status()
            return resp

    def close(self) -> None:
        try:
            self._client.close()
        except Exception:
            pass
