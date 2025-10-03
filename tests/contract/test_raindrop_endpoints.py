from raindrop_enhancer.api.raindrop_client import RaindropClient


def test_list_collections_contract(httpx_mock):
    """Client should call collections endpoint and return items."""
    httpx_mock.add_response(
        method="GET", url="https://api.raindrop.io/rest/v1/collections", json={"items": [{"_id": 1, "title": "c"}]}
    )
    c = RaindropClient(token="x")
    items = c.list_collections()
    assert isinstance(items, list)
    assert items[0]["_id"] == 1
    c.close()


def test_list_raindrops_contract(httpx_mock):
    """Client should iterate raindrops with pagination params."""
    httpx_mock.add_response(
        method="GET",
        url="https://api.raindrop.io/rest/v1/raindrops/1?page=0&perpage=50",
        json={"items": [{"_id": 10, "link": "https://a"}]},
    )
    c = RaindropClient(token="x")
    items = list(c.list_raindrops(1))
    assert len(items) == 1
    assert items[0]["_id"] == 10
    c.close()
