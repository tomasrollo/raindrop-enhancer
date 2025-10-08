from __future__ import annotations

import os
from functools import lru_cache
from typing import Optional, Callable, List

import dspy


class DSPyConfigError(Exception):
    pass


def get_dspy_model() -> str:
    """Return the DSPy model identifier from environment.

    Raises DSPyConfigError if not configured.
    """
    model = os.environ.get("RAINDROP_DSPY_MODEL")
    if not model:
        raise DSPyConfigError(
            "RAINDROP_DSPY_MODEL is not set; please set it to a DSPy model identifier, e.g. 'openai:gpt-4o-mini'"
        )
    return model


@lru_cache(maxsize=1)
def configure_dspy() -> Callable[[str], List[str]]:
    """Configure DSPy and return a simple predictor callable: prompt -> list[str].

    This wrapper normalizes several DSPy predictor interfaces and returns a
    function that accepts a prompt string and yields a list of tag strings.
    """
    model = get_dspy_model()
    try:
        # Attempt to configure global settings if available
        try:
            dspy.settings.configure(lm=model)
        except Exception:
            # Not all backends require this; ignore failures here
            pass

        pred = dspy.Predictor(model)

        def predictor(prompt: str) -> List[str]:
            # DSPy predictors vary: try call, then predict, then generate
            if callable(pred):
                res = pred(prompt)
            elif hasattr(pred, "predict"):
                res = pred.predict(prompt)
            elif hasattr(pred, "generate"):
                res = pred.generate(prompt)
            else:
                raise DSPyConfigError("Unsupported DSPy predictor interface")

            # Normalize result to list[str]
            if isinstance(res, str):
                return [res]
            if isinstance(res, list):
                return [str(r) for r in res]
            # Attempt to coerce from other structures
            try:
                return [str(r) for r in list(res)]
            except Exception:
                return []

        return predictor
    except Exception as e:
        raise DSPyConfigError(f"Failed to configure DSPy predictor: {e}")
