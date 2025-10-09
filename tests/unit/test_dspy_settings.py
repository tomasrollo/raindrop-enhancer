import os
import types

import pytest


def _reload_module(module):
    # Helper to clear cached functions (lru_cache) by reloading the module
    import importlib

    importlib.reload(module)


def test_get_dspy_model_default_and_override(monkeypatch):
    # Ensure default is returned when env not set
    monkeypatch.delenv("RAINDROP_DSPY_MODEL", raising=False)
    import raindrop_enhancer.content.dspy_settings as ds

    # reload to pick up env change
    _reload_module(ds)
    assert ds.get_dspy_model() == "openai/gpt-4o-mini"

    # When env is set, that value is returned
    monkeypatch.setenv("RAINDROP_DSPY_MODEL", "customprovider/custom-model")
    _reload_module(ds)
    assert ds.get_dspy_model() == "customprovider/custom-model"


def test_configure_dspy_builds_lm_and_extracts_tokens(monkeypatch):
    # Prepare environment
    monkeypatch.setenv("RAINDROP_DSPY_MODEL", "openai/gpt-test")
    monkeypatch.setenv("RAINDROP_DSPY_OPENAI_API_KEY", "key-xyz")
    monkeypatch.setenv("RAINDROP_DSPY_API_BASE", "https://example.test")
    monkeypatch.setenv("RAINDROP_DSPY_TRACK_USAGE", "1")

    import raindrop_enhancer.content.dspy_settings as ds

    # Create a fake dspy module surface we can attach to the imported module
    class FakeUsage:
        def __init__(self, total_tokens=123):
            self.total_tokens = total_tokens

    class FakePrediction:
        def __init__(self, tags, usage):
            self.tags = tags
            self._usage = usage

        def get_lm_usage(self):
            return self._usage

        def toDict(self):
            return {"tags": self.tags}

    class FakePredict:
        def __init__(self, signature_or_model=None):
            self._sig = signature_or_model

        def __call__(self, text=None, prompt=None, **kwargs):
            # Accept named param used by configure_dspy
            return FakePrediction(["Alpha", "Beta"], FakeUsage(total_tokens=42))

    # Monkeypatch dspy.LM, dspy.settings.configure, dspy.Predict
    fake_lm_kwargs = {}

    def fake_LM(model, **kwargs):
        fake_lm_kwargs["model"] = model
        fake_lm_kwargs.update(kwargs)
        return object()

    class FakeSettings:
        def configure(self, lm=None, track_usage=False):
            # record for inspection if needed
            fake_lm_kwargs["configured_lm"] = lm
            fake_lm_kwargs["track_usage"] = track_usage

    monkeypatch.setattr(ds, "dspy", ds.dspy)
    monkeypatch.setattr(ds.dspy, "LM", fake_LM)
    monkeypatch.setattr(ds.dspy, "Predict", FakePredict)
    monkeypatch.setattr(ds.dspy, "settings", FakeSettings())

    # Clear cache and reload to ensure monkeypatching is used
    ds.configure_dspy.cache_clear()
    predictor = ds.configure_dspy()

    # Call the predictor
    tags, tokens = predictor("some text")
    assert tags == ["Alpha", "Beta"]
    assert tokens == 42

    # Confirm the LM was constructed with api_key and api_base
    assert fake_lm_kwargs.get("api_key") == "key-xyz"
    assert fake_lm_kwargs.get("api_base") == "https://example.test"


def test_configure_dspy_without_track_usage_returns_none(monkeypatch):
    # Without track usage, tokens should be None
    monkeypatch.setenv("RAINDROP_DSPY_MODEL", "openai/gpt-test")
    monkeypatch.setenv("RAINDROP_DSPY_OPENAI_API_KEY", "key-xyz")
    monkeypatch.delenv("RAINDROP_DSPY_TRACK_USAGE", raising=False)

    import raindrop_enhancer.content.dspy_settings as ds

    class FakePredictionNoUsage:
        def __init__(self, tags):
            self.tags = tags

        def toDict(self):
            return {"tags": self.tags}

    class FakePredictNoUsage:
        def __init__(self, signature_or_model=None):
            pass

        def __call__(self, text=None, **kwargs):
            return FakePredictionNoUsage(["X"])

    # Monkeypatch
    monkeypatch.setattr(ds.dspy, "Predict", FakePredictNoUsage)
    # Ensure LM constructor exists but do not inspect kwargs here
    monkeypatch.setattr(ds.dspy, "LM", lambda m, **k: object())
    monkeypatch.setattr(
        ds.dspy, "settings", type("S", (), {"configure": lambda self, **k: None})()
    )

    ds.configure_dspy.cache_clear()
    pred = ds.configure_dspy()
    tags, tokens = pred("t")
    assert tags == ["X"]
    assert tokens is None


import os

import pytest

from raindrop_enhancer.content.dspy_settings import get_dspy_model, DSPyConfigError


def test_missing_model_env_defaults():
    # If env var not set, get_dspy_model should return the default model id
    if "RAINDROP_DSPY_MODEL" in os.environ:
        del os.environ["RAINDROP_DSPY_MODEL"]

    assert get_dspy_model() == "openai/gpt-4o-mini"
