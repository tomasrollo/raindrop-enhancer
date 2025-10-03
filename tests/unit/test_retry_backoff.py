from raindrop_enhancer.api.raindrop_client import RaindropClient


def test_retry_triggers_on_retry_and_succeeds(httpx_mock):
    calls = []

    def on_retry(url: str, attempt: int, delay: float):
        calls.append((url, attempt, delay))

    client = RaindropClient(token="x", enforce_rate_limit=False)
    client.on_retry = on_retry

    # First response: 429 (will cause a retry), second: success
    httpx_mock.add_response(method="GET", url="https://api.raindrop.io/rest/v1/collections", status_code=429)
    httpx_mock.add_response(method="GET", url="https://api.raindrop.io/rest/v1/collections", json={"items": []})

    items = client.list_collections()
    assert items == []
    assert len(calls) >= 1
    # first retry attempt should be recorded with attempt number 1
    assert calls[0][1] >= 1
    assert isinstance(calls[0][2], float)


def test_retry_backoff_increases_delay(httpx_mock):
    calls = []

    def on_retry(url: str, attempt: int, delay: float):
        calls.append((url, attempt, delay))

    client = RaindropClient(token="x", enforce_rate_limit=False)
    client.on_retry = on_retry

    # Simulate two 429 responses so we have two retries, then a success
    httpx_mock.add_response(method="GET", url="https://api.raindrop.io/rest/v1/collections", status_code=429)
    httpx_mock.add_response(method="GET", url="https://api.raindrop.io/rest/v1/collections", status_code=429)
    httpx_mock.add_response(method="GET", url="https://api.raindrop.io/rest/v1/collections", json={"items": []})

    items = client.list_collections()
    assert items == []
    # Expect two recorded retries
    assert len(calls) >= 2
    assert calls[0][1] < calls[1][1]
    assert calls[1][2] >= calls[0][2]