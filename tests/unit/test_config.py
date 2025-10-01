import tempfile
from pathlib import Path

from raindrop_enhancer.util.config import (
    default_config,
    write_config,
    read_config,
    get_or_create_config,
    validate_config,
)


def test_default_and_write_read(tmp_path: Path):
    cfg = default_config()
    p = tmp_path / "cfg.toml"
    write_config(p, cfg, enforce_mode=False)
    read = read_config(p)
    assert read.get("data_dir") == cfg.get("data_dir")


def test_get_or_create_config_creates(tmp_path: Path):
    p = tmp_path / "cfg.toml"
    got = get_or_create_config(p)
    assert isinstance(got, dict)
    assert p.exists()


def test_validate_config_pass_and_fail():
    good = {"tag_confidence_threshold": 0.5, "max_tags": 3}
    validate_config(good)  # should not raise

    bad_thr = {"tag_confidence_threshold": 1.5, "max_tags": 3}
    try:
        validate_config(bad_thr)
        assert False, "Expected ValueError for threshold"
    except ValueError:
        pass

    bad_max = {"tag_confidence_threshold": 0.5, "max_tags": 0}
    try:
        validate_config(bad_max)
        assert False, "Expected ValueError for max_tags"
    except ValueError:
        pass


import os
from pathlib import Path

from raindrop_enhancer.util.config import (
    write_config,
    read_config,
    get_or_create_config,
    validate_config,
    default_config,
)


def test_write_and_read_config(tmp_path):
    cfg_path = tmp_path / "config.toml"
    data = {"tag_confidence_threshold": 0.7, "max_tags": 5}
    write_config(cfg_path, data, enforce_mode=False)
    read = read_config(cfg_path)
    assert float(read["tag_confidence_threshold"]) == 0.7
    assert int(read["max_tags"]) == 5


def test_get_or_create_creates_file(tmp_path):
    cfg_path = tmp_path / "cfg.toml"
    cfg = get_or_create_config(cfg_path)
    assert cfg_path.exists()
    # defaults should be present
    defaults = default_config()
    assert "tag_confidence_threshold" in cfg
    assert cfg["tag_confidence_threshold"] == defaults["tag_confidence_threshold"]


def test_validate_config_rejects_invalid_values():
    bad = {"tag_confidence_threshold": 1.5, "max_tags": 0}
    try:
        validate_config(bad)
    except ValueError:
        return
    raise AssertionError("validate_config should have raised ValueError")
