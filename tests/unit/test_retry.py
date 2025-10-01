from raindrop_enhancer.util.retry import backoff


def test_backoff_returns_number():
    val = backoff(1)
    if not isinstance(val, float):
        raise AssertionError("backoff should return a float")
