"""Unit tests for retry/backoff helper."""

from __future__ import annotations

from types import SimpleNamespace

import pytest

from raindrop_enhancer.util import retry


def test_backoff_grows_exponentially_until_cap(monkeypatch):
    monkeypatch.setattr(
        retry,
        "random",
        SimpleNamespace(uniform=lambda _low, high: high),
    )

    delays = [retry.backoff(attempt=i, base=1.0, cap=10.0) for i in range(5)]

    assert delays[0] == pytest.approx(1.0)
    assert delays[1] == pytest.approx(2.0)
    assert delays[2] == pytest.approx(4.0)
    assert delays[3] == pytest.approx(8.0)
    assert delays[4] == pytest.approx(10.0)


def test_backoff_honors_retry_after(monkeypatch):
    monkeypatch.setattr(
        retry,
        "random",
        SimpleNamespace(uniform=lambda _low, high: high / 2),
    )

    delay = retry.backoff(attempt=1, base=1.0, cap=60.0, retry_after=42)
    assert delay == pytest.approx(42)


def test_backoff_uses_full_jitter(monkeypatch):
    calls: list[tuple[float, float]] = []

    def fake_uniform(low: float, high: float) -> float:
        calls.append((low, high))
        return high

    monkeypatch.setattr(
        retry,
        "random",
        SimpleNamespace(uniform=fake_uniform),
    )

    retry.backoff(attempt=3, base=1.0, cap=60.0)

    assert calls == [(0, 8.0)]


def test_retry_retries_on_retryable_error(monkeypatch):
    attempts: list[int] = []
    events: list[retry.RetryEvent] = []

    def operation() -> str:
        attempts.append(len(attempts))
        if len(attempts) < 3:
            raise retry.RetryableError(
                "temporary",
                retry_after=None,
                context={"component": "test"},
            )
        return "success"

    monkeypatch.setattr(retry, "time", SimpleNamespace(sleep=lambda _delay: None))

    result = retry.retry(operation, on_retry=events.append)

    assert result == "success"
    assert len(attempts) == 3
    assert len(events) == 2
    assert events[0].context["component"] == "test"


def test_retry_raises_after_exhausting_attempts(monkeypatch):
    monkeypatch.setattr(retry, "time", SimpleNamespace(sleep=lambda _delay: None))

    def operation() -> None:
        raise retry.RetryableError("always failing", retry_after=0.1)

    with pytest.raises(retry.RetryableError):
        retry.retry(operation, attempts=2)


def test_retry_bubbles_non_retryable_errors(monkeypatch):
    monkeypatch.setattr(retry, "time", SimpleNamespace(sleep=lambda _delay: None))

    def operation() -> None:
        raise ValueError("boom")

    with pytest.raises(ValueError):
        retry.retry(operation)
