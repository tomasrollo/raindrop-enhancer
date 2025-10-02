from types import SimpleNamespace
import json

import requests

from raindrop_enhancer.api.client import RaindropClient, APIResult


class DummyResp:
    def __init__(self, status=200, body=None, headers=None):
        self.status_code = status
        self._body = body or {"items": []}
        self.headers = headers or {}

    def raise_for_status(self):
        if self.status_code >= 400:
            raise requests.HTTPError(f"status {self.status_code}")

    def json(self):
        return self._body


def test_capture_headers_and_list_collections(monkeypatch):
    client = RaindropClient(token="t", base="http://example")

    def fake_get(url, params=None, timeout=None):
        return DummyResp(
            body={"items": [{"id": 1}]}, headers={"X-RateLimit-Remaining": "5"}
        )

    monkeypatch.setattr(client.session, "get", fake_get)
    res = client.list_collections()
    assert isinstance(res, dict)
    assert res.get("items")
    assert client.last_rate_limit.get("remaining") == 5


def test_list_raindrops_handles_error(monkeypatch):
    client = RaindropClient(token="t", base="http://example")

    def bad_get(url, params=None, timeout=None):
        return DummyResp(status=500)

    monkeypatch.setattr(client.session, "get", bad_get)
    pages = list(client.list_raindrops(1, perpage=10, max_pages=1))
    assert pages and pages[0].get("result") is False
