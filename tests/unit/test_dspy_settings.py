import os

import pytest

from raindrop_enhancer.content.dspy_settings import get_dspy_model, DSPyConfigError


def test_missing_model_env_raises():
    # Ensure env var not set
    if "RAINDROP_DSPY_MODEL" in os.environ:
        del os.environ["RAINDROP_DSPY_MODEL"]

    with pytest.raises(DSPyConfigError):
        get_dspy_model()
