import pytest
from raindrop_enhancer.api.client import RaindropClient


class FakeResp:
    def __init__(self, json_data=None, headers=None, status=200):
        self._json = json_data or {"result": True, "items": []}
        self.headers = headers or {}
        self._status = status

    def raise_for_status(self):
        if self._status >= 400:
            raise Exception("HTTP error")

    def json(self):
        return self._json


def test_list_collections_and_rate_limit(monkeypatch):
    client = RaindropClient(token="fake")
    monkeypatch.setattr(
        client.session,
        "get",
        lambda url: FakeResp(
            headers={"X-RateLimit-Limit": "100", "X-RateLimit-Remaining": "99", "X-RateLimit-Reset": "123"}
        ),
    )
    result = client.list_collections()
    assert "items" in result
    assert client.last_rate_limit["X-RateLimit-Limit"] == "100"


def test_list_raindrops_pagination(monkeypatch):
    client = RaindropClient(token="fake")
    calls = []

    def fake_get(url, params=None):
        params = params or {}
        calls.append(params.get("page"))
        if params.get("page") == 1:
            return FakeResp(json_data={"result": True, "items": [1, 2], "count": 2})
        return FakeResp(json_data={"result": True, "items": [], "count": 2})

    monkeypatch.setattr(client.session, "get", fake_get)
    result = client.list_raindrops(123)
    assert result["items"] == [1, 2]
    assert calls == [1, 2]
