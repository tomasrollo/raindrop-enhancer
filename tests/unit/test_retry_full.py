import pytest
from raindrop_enhancer.util.retry import Retry
import time


def test_retry_decorator_success():
    calls = []

    @Retry(max_attempts=3)
    def ok():
        calls.append(1)
        return 42

    assert ok() == 42
    assert len(calls) == 1


def test_retry_decorator_with_failures():
    calls = []

    class DummyExc(Exception):
        pass

    @Retry(max_attempts=3, base=0.01)
    def flaky():
        calls.append(1)
        if len(calls) < 3:
            raise DummyExc()
        return 99

    assert flaky() == 99
    assert len(calls) == 3


def test_retry_after(monkeypatch):
    class DummyResp:
        headers = {"Retry-After": "0.01"}

    class DummyExc(Exception):
        def __init__(self):
            self.response = DummyResp()

    called = []

    @Retry(max_attempts=2, base=0.01)
    def func():
        called.append(1)
        if len(called) == 1:
            raise DummyExc()
        return 1

    assert func() == 1
    assert len(called) == 2
