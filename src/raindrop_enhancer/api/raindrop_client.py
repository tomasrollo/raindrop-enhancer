"""Raindrop API client using httpx (Gracy compatible patterns).

Provides simple pagination, auth from env, and retry/backoff for 429s.
"""

from __future__ import annotations

import logging
import os
import random
import time
from typing import Callable, Iterator, List, Optional
from datetime import datetime, date, timezone

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

    def list_raindrops_since(
        self, collection_id: int, iso_cursor: str | None = None
    ) -> Iterator[dict]:
        """Iterate raindrops sorted by created date; stop when created <= iso_cursor.

        Uses perpage=200 and sort=created per contract.
        """
        page = 0
        perpage = 200

        # Robust parser for timestamps -> timezone-aware datetimes
        def _parse_ts_to_dt(value) -> Optional[datetime]:
            if value is None:
                return None
            # Accept epoch seconds
            try:
                if isinstance(value, (int, float)):
                    return datetime.fromtimestamp(int(value), tz=timezone.utc)
            except Exception:
                pass
            s = str(value)
            # Normalize trailing Z to +00:00 for fromisoformat
            if s.endswith("Z"):
                s = s[:-1] + "+00:00"
            try:
                dt = datetime.fromisoformat(s)
                if dt.tzinfo is None:
                    # Assume UTC for naive timestamps
                    return dt.replace(tzinfo=timezone.utc)
                return dt
            except Exception:
                return None

        # Parse iso_cursor once for comparisons
        iso_dt: Optional[datetime] = _parse_ts_to_dt(iso_cursor) if iso_cursor else None
        while True:
            url = f"{self.base_url}/raindrops/{collection_id}"
            params = {"page": page, "perpage": perpage, "sort": "created"}
            if iso_cursor:
                # The Raindrop API only accepts a YYYY-MM-DD date for the `created`
                # search field and supports only '<' and '>' operators. Use the
                # parsed iso_dt to derive a date; fall back to the raw date part
                # if parsing failed.
                if iso_dt:
                    date_str = iso_dt.date().isoformat()
                    params["search"] = f"created:>{date_str}"
                else:
                    try:
                        date_str = iso_cursor.split("T")[0]
                        params["search"] = f"created:>{date_str}"
                    except Exception:
                        Logger.debug(
                            "Could not parse iso_cursor %r for search", iso_cursor
                        )
            resp = self._request_with_retry("GET", url, params=params)
            data = resp.json()
            items = data.get("items", [])
            Logger.debug("Fetched items: %d", len(items))
            if not items:
                break
            for it in items:
                # Yield all returned items; the DB enforces uniqueness so
                # duplicates won't be stored. This avoids client-side stopping
                # which can be brittle when the API only supports date-granular
                # search filters.
                yield it
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
