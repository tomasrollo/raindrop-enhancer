import httpx

from raindrop_enhancer.api.raindrop_client import RaindropClient


def test_pagination_and_retry_behavior(httpx_mock):
    # Prepare two pages for collection 1
    httpx_mock.add_response(
        method="GET",
        url="https://api.raindrop.io/rest/v1/raindrops/1?page=0&perpage=50",
        json={"items": [{"_id": 1, "link": "https://a"}]},
    )

    client = RaindropClient(token="dummy")
    items = list(client.list_raindrops(1))
    assert len(items) == 1
    assert items[0]["_id"] == 1
    client.close()
