"""Raindrop API client with basic pagination and rate-limit header capture.

This client intentionally keeps a small surface area: it exposes
`list_collections()` and `list_raindrops()` and returns Python dicts matching
the OpenAPI contract used in contract tests. It also exposes the latest
rate-limit headers alongside responses so callers can make throttling
decisions.
"""

from typing import Dict, Any, Iterator, Optional
import requests
from dataclasses import dataclass

from raindrop_enhancer.util.retry import retryable


@dataclass
class APIResult:
    body: Dict[str, Any]
    rate_limit_limit: Optional[int] = None
    rate_limit_remaining: Optional[int] = None
    rate_limit_reset: Optional[int] = None


class RaindropClient:
    def __init__(
        self,
        token: str,
        base: str | None = None,
        session: Optional[requests.Session] = None,
    ):
        self.token = token
        self.base = base or "https://api.raindrop.io/rest/v1"
        self.session = session or requests.Session()
        self.session.headers.update(
            {"Authorization": f"Bearer {token}", "Accept": "application/json"}
        )
        # Store last observed rate limit headers for callers who want telemetry
        self.last_rate_limit: Dict[str, Optional[int]] = {
            "limit": None,
            "remaining": None,
            "reset": None,
        }

    def _capture_headers(self, response: requests.Response) -> Dict[str, Optional[int]]:
        def _int_header(name: str) -> Optional[int]:
            v = response.headers.get(name)
            try:
                return int(v) if v is not None else None
            except Exception:
                return None

        return {
            "limit": _int_header("X-RateLimit-Limit"),
            "remaining": _int_header("X-RateLimit-Remaining"),
            "reset": _int_header("X-RateLimit-Reset"),
        }

    @retryable()
    def _get(self, path: str, **params) -> APIResult:
        url = f"{self.base}{path}"
        resp = self.session.get(url, params=params, timeout=30)
        # Raise for non-2xx to allow retry semantics to trigger on server errors
        resp.raise_for_status()
        headers = self._capture_headers(resp)
        return APIResult(
            body=resp.json(),
            rate_limit_limit=headers["limit"],
            rate_limit_remaining=headers["remaining"],
            rate_limit_reset=headers["reset"],
        )

    def list_collections(self) -> Dict[str, Any]:
        """Return collections response along with captured rate-limit headers."""
        try:
            res = self._get("/collections")
            # expose headers for callers
            self.last_rate_limit = {
                "limit": res.rate_limit_limit,
                "remaining": res.rate_limit_remaining,
                "reset": res.rate_limit_reset,
            }
            return res.body
        except Exception as exc:
            body = {"result": False, "items": [], "error": str(exc)}
            self.last_rate_limit = {"limit": None, "remaining": None, "reset": None}
            return body

    def list_raindrops(
        self, collection_id: int, perpage: int = 50, max_pages: int = 100, **extra
    ) -> Iterator[Dict[str, Any]]:
        """Yield APIResult per page for raindrops in a collection.

        This returns an iterator of per-page results so callers can stream and
        merge items without loading everything into memory.
        """
        page = 0
        while page < max_pages:
            params = {"page": page, "perpage": perpage, **extra}
            path = f"/raindrops/{collection_id}"
            try:
                res = self._get(path, **params)
            except Exception as exc:
                yield {"result": False, "items": [], "error": str(exc)}
                return

            # surface telemetry
            self.last_rate_limit = {
                "limit": res.rate_limit_limit,
                "remaining": res.rate_limit_remaining,
                "reset": res.rate_limit_reset,
            }
            yield res.body
            items = res.body.get("items") or []
            if not items or len(items) < perpage:
                break
            page += 1
