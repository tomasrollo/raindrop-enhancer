from raindrop_enhancer.services.tagging import suggest_tags_for_content


def test_suggest_tags_not_implemented():
    res = suggest_tags_for_content("hello world")
    assert isinstance(res, list)
