import pytest
from raindrop_enhancer.api.client import RaindropClient


import types


def test_list_collections_contract(monkeypatch):
    """
    Contract: RaindropClient.list_collections should return collections in OpenAPI schema shape and surface X-RateLimit-* headers.
    """
    client = RaindropClient(token="test-token")

    # Monkeypatch the session.get to return a fake response
    class FakeResp:
        def __init__(self):
            self.headers = {
                "X-RateLimit-Limit": "1000",
                "X-RateLimit-Remaining": "999",
                "X-RateLimit-Reset": "1234567890",
            }

        def raise_for_status(self):
            pass

        def json(self):
            return {"result": True, "items": [{"_id": 1, "title": "Test Collection"}]}

    monkeypatch.setattr(client.session, "get", lambda url: FakeResp())
    result = client.list_collections()
    assert "items" in result
    assert isinstance(result["items"], list)
    assert client.last_rate_limit["X-RateLimit-Limit"] == "1000"
