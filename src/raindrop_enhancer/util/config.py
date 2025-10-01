"""Configuration manager.

Provides read/write helpers for a TOML-backed config file. Enforces POSIX
permissions (0600) when writing the file to keep tokens/config private.
Also includes minimal validation helpers used by the CLI and tests.
"""

from pathlib import Path
import os
import stat
from typing import Dict, Any

import toml


def default_config() -> Dict[str, Any]:
    return {
        "data_dir": str(Path.home() / ".raindrop_enhancer"),
        "token_path": "config-token",
        "llm_api_base": None,
        "llm_api_key": None,
        "tag_confidence_threshold": 0.6,
        "max_tags": 10,
    }


def write_config(path: Path, data: Dict[str, Any], enforce_mode: bool = True) -> None:
    """Write the given dict to `path` as TOML and set file mode to 0600.

    If `enforce_mode` is False, the chmod step is skipped (useful for
    non-POSIX platforms or tests that don't support permissions).
    """
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(toml.dumps(data), encoding="utf-8")

    # Try to set file permissions to 0600 on POSIX systems.
    if enforce_mode and os.name == "posix":
        try:
            path.chmod(stat.S_IRUSR | stat.S_IWUSR)
        except Exception:
            # If chmod fails, don't crash the application; callers may
            # opt to validate permissions separately.
            pass


def read_config(path: Path) -> Dict[str, Any]:
    """Read TOML config from `path` and return as a dict.

    Raises FileNotFoundError if the file does not exist.
    """
    if not path.exists():
        raise FileNotFoundError(f"Config file not found: {path}")
    return toml.loads(path.read_text(encoding="utf-8"))


def get_or_create_config(
    path: Path, defaults: Dict[str, Any] | None = None
) -> Dict[str, Any]:
    """Return config dict, creating a file with defaults if missing."""
    if defaults is None:
        defaults = default_config()
    if not path.exists():
        write_config(path, defaults)
        return defaults
    cfg = read_config(path)
    # Merge with defaults to ensure keys exist
    merged = {**defaults, **(cfg or {})}
    return merged


def validate_config(cfg: Dict[str, Any]) -> None:
    """Raise ValueError when config values are invalid.

    Currently validates `tag_confidence_threshold` and `max_tags`.
    """
    thr = cfg.get("tag_confidence_threshold")
    if thr is not None and not (0.0 <= float(thr) <= 1.0):
        raise ValueError("tag_confidence_threshold must be between 0.0 and 1.0")
    max_tags = cfg.get("max_tags")
    if max_tags is not None and int(max_tags) <= 0:
        raise ValueError("max_tags must be a positive integer")
