"""Raindrop API client stubs."""

import requests


class RaindropClient:
    def __init__(self, token: str):
        self.token = token
        self.base = "https://api.raindrop.io/rest/v1"
        self.session = requests.Session()
        self.session.headers.update({"Authorization": f"Bearer {token}"})
        self.last_rate_limit = {}

    def _capture_rate_limit(self, resp):
        self.last_rate_limit = {
            "X-RateLimit-Limit": resp.headers.get("X-RateLimit-Limit"),
            "X-RateLimit-Remaining": resp.headers.get("X-RateLimit-Remaining"),
            "X-RateLimit-Reset": resp.headers.get("X-RateLimit-Reset"),
        }

    def list_collections(self):
        url = f"{self.base}/collections"
        resp = self.session.get(url)
        self._capture_rate_limit(resp)
        resp.raise_for_status()
        return resp.json()

    def list_raindrops(self, collection_id: int, **params):
        url = f"{self.base}/raindrop/{collection_id}"
        all_items = []
        page = 0
        while True:
            page += 1
            req_params = params.copy()
            req_params["page"] = page
            resp = self.session.get(url, params=req_params)
            self._capture_rate_limit(resp)
            resp.raise_for_status()
            data = resp.json()
            items = data.get("items", [])
            all_items.extend(items)
            if (
                not data.get("result")
                or not items
                or len(items) < data.get("count", 50)
            ):
                break
        return {"result": True, "items": all_items}
