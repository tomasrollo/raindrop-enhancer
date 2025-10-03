import pytest


def test_raindrop_incremental_request_contract(monkeypatch):
    """Ensure the client issues incremental requests with sort=created, perpage=200 and search filter.

    We patch RaindropClient._request_with_retry to return sequential pages. The iterator must
    stop when an item's created timestamp is <= provided cursor.
    """
    from raindrop_enhancer.api.raindrop_client import RaindropClient

    client = RaindropClient(token="x")

    pages = [
        [
            {"_id": 1, "created": "2025-10-01T00:00:00Z"},
            {"_id": 2, "created": "2025-09-20T00:00:00Z"},
        ],
        [
            {"_id": 3, "created": "2025-09-10T00:00:00Z"},
        ],
        [],
    ]

    calls = []

    def fake_request(self, method, url, params=None):
        # record the params for assertions
        calls.append(dict(params or {}))

        class Resp:
            def __init__(self, items):
                self._items = items

            def json(self):
                return {"items": self._items}

        return Resp(pages.pop(0))

    from raindrop_enhancer.api import raindrop_client

    monkeypatch.setattr(
        raindrop_client.RaindropClient, "_request_with_retry", fake_request
    )

    # Use a cursor that should exclude the item with 2025-09-10 and include the earlier two
    cursor = "2025-09-15T00:00:00Z"
    results = list(client.list_raindrops_since(1, iso_cursor=cursor))

    # Should yield only the two items with created > cursor
    assert [r["_id"] for r in results] == [1, 2]

    # Validate query parameters used
    assert any(p.get("perpage") == 200 for p in calls), "perpage=200 not used"
    assert any(p.get("sort") == "created" for p in calls), "sort=created not used"
    assert any(
        "search" in p and f"created:>={cursor}" in p.get("search", "") for p in calls
    ), "search filter with cursor not present"
    # Ensure pagination used (page parameter should increment from 0)
    assert calls[0].get("page", 0) == 0
    # second call should have page=1
    assert len(calls) >= 2 and calls[1].get("page", 1) == 1
