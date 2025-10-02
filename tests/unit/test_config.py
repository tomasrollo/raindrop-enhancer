"""Tests for the configuration manager utilities."""

from __future__ import annotations

import os
import stat
from pathlib import Path

import pytest

from raindrop_enhancer.util.config import (
    CONFIG_FILENAME,
    ConfigManager,
    ConfigState,
    resolve_data_dir,
)


def test_resolve_data_dir_prefers_environment(monkeypatch, tmp_path):
    env_path = tmp_path / "from_env"
    monkeypatch.setenv("RAINDROP_ENHANCER_DATA", str(env_path))

    resolved = resolve_data_dir(None)

    assert resolved == env_path


def test_load_returns_defaults_when_missing(tmp_path):
    manager = ConfigManager(tmp_path)

    state = manager.load()

    assert state.data_dir == tmp_path
    assert state.raindrop_token is None
    assert state.extra == {}


def test_save_round_trip_and_permissions(tmp_path):
    manager = ConfigManager(tmp_path)
    state = ConfigState(
        data_dir=tmp_path,
        raindrop_token="secret-token",
        llm_api_base="https://llm.example.com",
        llm_api_key="llm-key",
    )
    state.extra["feature_flag"] = True

    manager.save(state)
    loaded = manager.load()

    assert loaded.raindrop_token == "secret-token"
    assert loaded.llm_api_base == "https://llm.example.com"
    assert loaded.extra == {"feature_flag": True}

    config_path = tmp_path / CONFIG_FILENAME
    assert config_path.exists()
    if os.name != "nt":
        mode = stat.S_IMODE(config_path.stat().st_mode)
        assert mode == 0o600


def test_update_handles_known_and_extra_fields(tmp_path):
    manager = ConfigManager(tmp_path)

    updated = manager.update(
        raindrop_token="new-token",
        llm_api_base="https://tags.local",
        llm_api_key=None,
        custom_cache="enabled",
    )

    assert updated.raindrop_token == "new-token"
    assert updated.llm_api_base == "https://tags.local"
    assert updated.extra == {"custom_cache": "enabled"}

    reloaded = manager.load()
    assert reloaded.raindrop_token == "new-token"
    assert reloaded.extra == {"custom_cache": "enabled"}


def test_thresholds_reflect_persisted_values(tmp_path):
    manager = ConfigManager(tmp_path)
    manager.update(
        tag_confidence_threshold=0.75,
        max_tags=7,
    )

    assert manager.thresholds() == {"confidence": 0.75, "max_tags": 7}


def test_require_token_raises_when_missing(tmp_path):
    manager = ConfigManager(tmp_path)

    with pytest.raises(RuntimeError):
        manager.require_token()
