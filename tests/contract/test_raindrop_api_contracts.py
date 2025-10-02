from raindrop_enhancer.api.client import RaindropClient


def test_list_collections_raises_not_implemented():
    """Contract: RaindropClient.list_collections should return a dict with items key."""
    client = RaindropClient(token="test-token")
    resp = client.list_collections()
    assert isinstance(resp, dict)
    assert "items" in resp
