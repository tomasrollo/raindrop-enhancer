import pytest
from raindrop_enhancer.util.retry import backoff


def test_retry_backoff_and_retry_after():
    """
    Unit: Retry helper should implement exponential backoff, jitter, and Retry-After handling (TDD red phase).
    """
    with pytest.raises(NotImplementedError):
        backoff(1)
