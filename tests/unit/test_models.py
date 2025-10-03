from raindrop_enhancer.models import filter_active_raindrops, Raindrop


def test_model_validation_rules():
    """Model validation should filter out removed/invalid items and keep valid ones."""
    payloads = [
        {"_id": 1, "link": "https://example.com/1", "removed": False},
        {"_id": 2, "link": "not-a-url", "removed": False},
        {"_id": 3, "link": "https://example.com/3", "removed": True},
    ]

    active = filter_active_raindrops(payloads)
    assert isinstance(active, list)
    assert len(active) == 1
    assert isinstance(active[0], Raindrop)
    assert active[0].id == 1
    assert active[0].url == "https://example.com/1"
