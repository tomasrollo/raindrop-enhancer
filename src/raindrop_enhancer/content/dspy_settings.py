from __future__ import annotations

import os
from functools import lru_cache
from typing import Optional, Callable, List, Tuple

import dspy


class DSPyConfigError(Exception):
    pass


def get_dspy_model() -> str:
    """Return the DSPy model identifier from environment.

    Raises DSPyConfigError if not configured.
    """
    # Default to a sensible OpenAI model when not configured explicitly.
    # Users may override by setting RAINDROP_DSPY_MODEL in their env or .env.
    model = os.environ.get("RAINDROP_DSPY_MODEL")
    if not model:
        return "openai/gpt-4o-mini"
    return model


@lru_cache(maxsize=1)
def configure_dspy() -> Callable[[str], Tuple[List[str], Optional[int]]]:
    """Configure DSPy and return a predictor wrapper: prompt -> (list[str], tokens_used).

    The wrapper attempts to instantiate a DSPy predictor using the documented
    entrypoints (`dspy.Predict` preferred) and normalizes `dspy.Prediction`
    objects to plain Python lists of strings. It also attempts to extract
    LM usage (tokens) when `track_usage` is enabled.
    """
    track_usage = os.environ.get("RAINDROP_DSPY_TRACK_USAGE", "0") == "1"
    try:
        # Basic configuration presence checks: if the user hasn't explicitly set a
        # RAINDROP_DSPY_MODEL and no plausible API key env var is present, treat
        # DSPy as "not configured" so callers can opt-in to failing fast.
        model_env = os.environ.get("RAINDROP_DSPY_MODEL")
        # Prefer RAINDROP-scoped API key env vars for determinism in user projects and tests.
        # Do not treat common global keys like OPENAI_API_KEY as sufficient unless an
        # explicit RAINDROP_DSPY_MODEL is also provided. This prevents leaking local
        # developer credentials into test runs which expect DSPy to be 'missing'.
        raindrop_scoped_keys = [
            os.environ.get("RAINDROP_DSPY_API_KEY"),
            os.environ.get("RAINDROP_DSPY_OPENAI_API_KEY"),
            os.environ.get("RAINDROP_DSPY_ANTHROPIC_API_KEY"),
            os.environ.get("RAINDROP_DSPY_GEMINI_API_KEY"),
        ]

        # Consider DSPy configured when either an explicit model is set, or a
        # RAINDROP-prefixed API key is provided. Global keys like OPENAI_API_KEY
        # are only used as fallbacks later when resolving provider credentials.
        if model_env is None and not any(raindrop_scoped_keys):
            # No explicit model and no RAINDROP-prefixed API keys -> consider DSPy unconfigured
            raise DSPyConfigError("DSPy not configured: set RAINDROP_DSPY_MODEL or provide a RAINDROP_DSPY_* API key")

        # Configure LM with provider API key / api_base when present
        model = get_dspy_model()
        provider = model.split("/")[0].lower() if "/" in model else model.lower()

        # Resolve API key: prefer RAINDROP_DSPY_{PROVIDER}_API_KEY, then PROVIDER_API_KEY,
        # then RAINDROP_DSPY_API_KEY, then common env names like OPENAI_API_KEY.
        api_key = os.environ.get(f"RAINDROP_DSPY_{provider.upper()}_API_KEY")
        if not api_key:
            api_key = os.environ.get(f"{provider.upper()}_API_KEY")
        if not api_key:
            api_key = os.environ.get("RAINDROP_DSPY_API_KEY")
        # provider-specific common fallbacks
        if not api_key:
            if provider == "openai":
                api_key = os.environ.get("OPENAI_API_KEY")
            elif provider == "anthropic":
                api_key = os.environ.get("ANTHROPIC_API_KEY")
            elif provider == "gemini":
                api_key = os.environ.get("GEMINI_API_KEY")

        # Optional custom API base (for OpenAI-compatible provider endpoints)
        api_base = os.environ.get("RAINDROP_DSPY_API_BASE") or os.environ.get(f"{provider.upper()}_API_BASE")

        lm_kwargs = {}
        if api_key:
            lm_kwargs["api_key"] = api_key
        if api_base:
            lm_kwargs["api_base"] = api_base
        lm = dspy.LM(model, **lm_kwargs)
        dspy.settings.configure(lm=lm, track_usage=track_usage)

        # Build a small Signature class
        class _TagSignature(dspy.Signature):
            """Generate tags for input text."""

            text: str = dspy.InputField(description="Input text for tag generation.")
            tags: List[str] = dspy.OutputField(description="List of tags most relevant to the input text.")

        pred = dspy.Predict(_TagSignature)

        def predictor(text: str) -> Tuple[List[str], Optional[int]]:
            prediction = pred(text=text)
            tokens_used: Optional[int] = None
            if track_usage:
                try:
                    usage = prediction.get_lm_usage()
                    if hasattr(usage, "total_tokens"):
                        tokens_used = int(getattr(usage, "total_tokens"))
                    elif hasattr(usage, "tokens"):
                        tokens_used = int(getattr(usage, "tokens"))
                except Exception:
                    tokens_used = None

            return prediction.tags, tokens_used

        return predictor
    except Exception as e:
        raise DSPyConfigError(f"Failed to configure DSPy predictor: {e}")
