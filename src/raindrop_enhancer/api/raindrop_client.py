"""Raindrop API client using httpx (Gracy compatible patterns).

Provides simple pagination, auth from env, and retry/backoff for 429s.
"""

from __future__ import annotations

import os
import time
from typing import Iterator, List, Optional

import httpx

from ..models import Raindrop, Collection


DEFAULT_BASE = "https://api.raindrop.io/rest/v1"


class RaindropClient:
    def __init__(self, token: Optional[str] = None, base_url: str = DEFAULT_BASE, per_page: int = 50):
        self.token = token or os.getenv("RAINDROP_TOKEN")
        self.base_url = base_url.rstrip("/")
        self.per_page = per_page
        self._client = httpx.Client(timeout=30.0)

    def _headers(self):
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
            # pagination: stop when no more items
            if not items or len(items) < self.per_page:
                break
            page += 1

    def _request_with_retry(self, method: str, url: str, params: dict | None = None) -> httpx.Response:
        attempts = 0
        delay = 1.0
        while True:
            attempts += 1
            resp = self._client.request(method, url, headers=self._headers(), params=params)
            if resp.status_code == 429:
                # simple exponential backoff
                time.sleep(delay)
                delay = min(delay * 2, 30.0)
                continue
            resp.raise_for_status()
            return resp

    def close(self) -> None:
        try:
            self._client.close()
        except Exception:
            pass
