"""Unit tests for the Raindrop API client."""

from __future__ import annotations

from datetime import datetime, timedelta, timezone
from types import SimpleNamespace
from typing import Any, Callable

import pytest
import requests
from requests.structures import CaseInsensitiveDict

from raindrop_enhancer.api.client import RaindropClient, _parse_retry_after
from raindrop_enhancer.util import retry as retry_module


class FakeResponse:
    def __init__(
        self,
        status_code: int = 200,
        payload: dict[str, Any] | None = None,
        headers: dict[str, str] | None = None,
    ) -> None:
        self.status_code = status_code
        self._payload = payload or {}
        self.headers = CaseInsensitiveDict(headers or {})

    def json(self) -> dict[str, Any]:
        return self._payload

    def raise_for_status(self) -> None:
        if self.status_code >= 400:
            raise requests.HTTPError(f"HTTP {self.status_code}")


class FakeSession(requests.Session):
    def __init__(self, responses: list[FakeResponse]) -> None:
        super().__init__()
        self._responses = list(responses)
        self.requests: list[tuple[str, str, dict[str, str]]] = []

    def request(
        self,
        method: str,
        url: str,
        *,
        params: dict[str, str] | None = None,
        timeout: float | None = None,
    ) -> FakeResponse:
        params_copy = dict(params) if params is not None else {}
        self.requests.append((method, url, params_copy))
        if not self._responses:
            raise AssertionError("No fake responses remaining")
        return self._responses.pop(0)


@pytest.mark.parametrize(
    "header, expected",
    [("42", 42.0), ("", None), (None, None)],
)
def test_parse_retry_after_numeric(header: str | None, expected: float | None) -> None:
    assert _parse_retry_after(header) == expected


def test_parse_retry_after_http_date(monkeypatch) -> None:
    future = datetime.now(timezone.utc) + timedelta(seconds=5)
    header = future.strftime("%a, %d %b %Y %H:%M:%S GMT")

    class _AwareDatetime(datetime):
        @classmethod
        def strptime(cls, value: str, fmt: str):  # type: ignore[override]
            assert value == header
            return future

        @classmethod
        def now(cls, tz=None):  # type: ignore[override]
            return datetime.now(tz)

    monkeypatch.setattr("raindrop_enhancer.api.client.datetime", _AwareDatetime)

    result = _parse_retry_after(header)
    assert result is not None
    assert 0.0 <= result <= 5.0


def test_list_collections_returns_items_and_headers() -> None:
    session = FakeSession(
        [
            FakeResponse(
                payload={"items": [{"id": 1}, {"id": 2}]},
                headers={
                    "X-RateLimit-Remaining": "99",
                    "X-RateLimit-Reset": "12345",
                },
            )
        ]
    )
    client = RaindropClient("token", session=session)

    items, headers = client.list_collections()

    assert [item["id"] for item in items] == [1, 2]
    assert headers["X-RateLimit-Remaining"] == "99"
    assert session.requests[0][0] == "GET"


def test_list_raindrops_paginates_until_short_batch() -> None:
    session = FakeSession(
        [
            FakeResponse(payload={"items": [{"_id": 1}, {"_id": 2}], "result": True}),
            FakeResponse(
                payload={"items": [{"_id": 3}], "result": True},
                headers={"X-RateLimit-Limit": "120"},
            ),
        ]
    )
    client = RaindropClient("token", session=session)

    items, headers = client.list_raindrops(123, per_page=2)

    assert len(items) == 3
    assert headers.get("X-RateLimit-Limit") == "120"
    # Ensure pagination advanced page parameter
    first_call = session.requests[0]
    second_call = session.requests[1]
    assert first_call[2]["page"] == "0"
    assert second_call[2]["page"] == "1"


def test_list_raindrops_includes_last_update_parameter() -> None:
    session = FakeSession(
        [
            FakeResponse(
                payload={"items": [], "result": True},
            )
        ]
    )
    client = RaindropClient("token", session=session)

    client.list_raindrops(321, last_update="2025-01-01T00:00:00Z")

    params = session.requests[0][2]
    assert params["lastUpdate"] == "2025-01-01T00:00:00Z"


def test_fetch_raindrop_returns_wrapped_item() -> None:
    session = FakeSession(
        [
            FakeResponse(
                payload={"item": {"id": 42, "collection": {"id": 99}}},
                headers={"X-RateLimit-Remaining": "80"},
            )
        ]
    )
    client = RaindropClient("token", session=session)

    item, headers = client.fetch_raindrop(42)

    assert item["id"] == 42
    assert headers["X-RateLimit-Remaining"] == "80"


def test_request_retries_on_rate_limit(monkeypatch) -> None:
    session = FakeSession(
        [
            FakeResponse(status_code=429, headers={"Retry-After": "0"}),
            FakeResponse(payload={"items": []}),
        ]
    )
    events: list[retry_module.RetryEvent] = []
    client = RaindropClient("token", session=session, on_retry=events.append)

    monkeypatch.setattr(
        retry_module,
        "time",
        SimpleNamespace(sleep=lambda _delay: None),
    )

    items, _headers = client.list_collections()

    assert items == []
    assert len(events) == 1
    assert events[0].retry_after is None or events[0].retry_after == 0


def test_request_raises_for_non_retryable_error() -> None:
    session = FakeSession([FakeResponse(status_code=403)])
    client = RaindropClient("token", session=session)

    with pytest.raises(requests.HTTPError):
        client.list_collections()
