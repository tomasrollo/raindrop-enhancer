import pytest
from raindrop_enhancer.api.client import RaindropClient


def test_list_collections_contract():
    """
    Contract: RaindropClient.list_collections should return collections in OpenAPI schema shape and surface X-RateLimit-* headers.
    This test is expected to fail until the client is implemented.
    """
    client = RaindropClient(token="test-token")
    with pytest.raises(NotImplementedError):
        client.list_collections()
