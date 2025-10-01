import pytest
from raindrop_enhancer.services.tagging import suggest_tags_for_content


def test_tagging_adapter_batch_and_confidence():
    """
    Unit: Tagging adapter should batch, filter by confidence, and handle errors (TDD red phase).
    """
    with pytest.raises(NotImplementedError):
        suggest_tags_for_content("hello world")
