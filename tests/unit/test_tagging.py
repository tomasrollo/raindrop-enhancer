from raindrop_enhancer.services.tagging import suggest_tags_for_content


def test_suggest_tags_not_implemented():
    try:
        suggest_tags_for_content("hello world")
    except NotImplementedError:
        raise
    else:
        raise AssertionError("suggest_tags_for_content should raise NotImplementedError until implemented")
