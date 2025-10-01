"""Minimal Raindrop API client with retry and pagination support."""

from __future__ import annotations

from datetime import datetime, timezone
from typing import Callable

import requests
from requests.structures import CaseInsensitiveDict

from raindrop_enhancer.util import retry

RATE_LIMIT_HEADERS = {
    "X-RateLimit-Limit",
    "X-RateLimit-Remaining",
    "X-RateLimit-Reset",
}


def _parse_retry_after(header: str | None) -> float | None:
    if header is None:
        return None
    header = header.strip()
    if not header:
        return None
    try:
        return float(header)
    except ValueError:
        try:
            reset = datetime.strptime(header, "%a, %d %b %Y %H:%M:%S %Z")
            return max(0.0, (reset - datetime.now(timezone.utc)).total_seconds())
        except ValueError:
            return None


class RaindropClient:
    """Typed wrapper over the Raindrop REST API."""

    def __init__(
        self,
        token: str,
        *,
        base_url: str = "https://api.raindrop.io/rest/v1",
        session: requests.Session | None = None,
        timeout: float = 30.0,
        on_retry: Callable[[retry.RetryEvent], None] | None = None,
    ) -> None:
        self.base_url = base_url.rstrip("/")
        self.session = session or requests.Session()
        self.session.headers.update(
            {
                "Authorization": f"Bearer {token}",
                "User-Agent": "raindrop-enhancer/0.1 (+https://github.com)",
                "Accept": "application/json",
            }
        )
        self.timeout = timeout
        self._on_retry = on_retry

    # ------------------------------------------------------------------
    def list_collections(self) -> tuple[list[dict], dict[str, str]]:
        payload, headers = self._request("GET", "collections")
        return payload.get("items", []), _extract_rate_limit(headers)

    def list_raindrops(
        self,
        collection_id: int,
        *,
        last_update: str | None = None,
        per_page: int = 50,
    ) -> tuple[list[dict], dict[str, str]]:
        page = 0
        params: dict[str, str] = {"perpage": str(per_page), "page": str(page)}
        if last_update:
            params["lastUpdate"] = last_update

        items: list[dict] = []
        headers: dict[str, str] = {}

        while True:
            path = f"raindrops/{collection_id}"
            payload, response_headers = self._request("GET", path, params=params)
            headers = _extract_rate_limit(response_headers)
            batch = payload.get("items", [])
            items.extend(batch)

            if not payload.get("result", True):
                break
            if len(batch) < per_page:
                break
            page += 1
            params["page"] = str(page)

        return items, headers

    def fetch_raindrop(self, raindrop_id: int) -> tuple[dict, dict[str, str]]:
        payload, headers = self._request("GET", f"raindrop/{raindrop_id}")
        item = payload.get("item") or payload
        return item, _extract_rate_limit(headers)

    def close(self) -> None:
        self.session.close()

    # ------------------------------------------------------------------
    def _request(
        self,
        method: str,
        path: str,
        *,
        params: dict[str, str] | None = None,
    ) -> tuple[dict, CaseInsensitiveDict[str]]:
        url = f"{self.base_url}/{path.lstrip('/')}"

        def _do_request() -> tuple[dict, CaseInsensitiveDict[str]]:
            response = self.session.request(
                method,
                url,
                params=params,
                timeout=self.timeout,
            )
            if response.status_code in {429, 500, 502, 503, 504}:
                retry_after = _parse_retry_after(response.headers.get("Retry-After"))
                raise retry.RetryableError(
                    f"Raindrop API {response.status_code}",
                    retry_after=retry_after,
                    context={
                        "url": url,
                        "status_code": response.status_code,
                    },
                )

            response.raise_for_status()
            return response.json(), response.headers

        payload, headers = retry.retry(
            _do_request,
            on_retry=self._on_retry,
        )
        return payload, headers


def _extract_rate_limit(headers: CaseInsensitiveDict[str]) -> dict[str, str]:
    return {key: headers.get(key, "") for key in RATE_LIMIT_HEADERS if key in headers}
