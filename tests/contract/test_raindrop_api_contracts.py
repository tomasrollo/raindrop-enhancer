from raindrop_enhancer.api.client import RaindropClient


def test_list_collections_raises_not_implemented():
    """Contract: RaindropClient.list_collections should be implemented later. This test fails now as TDD requires."""
    client = RaindropClient(token="test-token")
    try:
        client.list_collections()
    except NotImplementedError:
        # Expected for TDD red state
        raise
    else:
        raise AssertionError("list_collections should raise NotImplementedError until implemented")
