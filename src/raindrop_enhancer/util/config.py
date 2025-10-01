"""Configuration manager for the Raindrop Enhancer CLI.

This module centralises reading and writing the user configuration stored inside
``config.toml`` within the chosen data directory. The file retains secrets such
as the Raindrop API token, therefore it is created with ``0600`` permissions on
POSIX systems. The helper exposes a dataclass representation and a manager that
handles permission enforcement, defaults, and persistence.
"""

from __future__ import annotations

import os
import stat
from dataclasses import dataclass, field
from pathlib import Path
from typing import Any, Mapping

import toml

CONFIG_FILENAME = "config.toml"

DEFAULT_CONFIDENCE = 0.5
DEFAULT_MAX_TAGS = 5


@dataclass(slots=True)
class ConfigState:
    """In-memory representation of the persisted CLI configuration."""

    data_dir: Path
    raindrop_token: str | None = None
    llm_api_base: str | None = None
    llm_api_key: str | None = None
    tag_confidence_threshold: float = DEFAULT_CONFIDENCE
    max_tags: int = DEFAULT_MAX_TAGS
    extra: dict[str, Any] = field(default_factory=dict)

    def to_dict(self) -> dict[str, Any]:
        """Serialise the configuration for toml persistence."""

        payload: dict[str, Any] = {
            "data_dir": str(self.data_dir),
            "raindrop_token": self.raindrop_token,
            "llm_api_base": self.llm_api_base,
            "llm_api_key": self.llm_api_key,
            "tag_confidence_threshold": float(self.tag_confidence_threshold),
            "max_tags": int(self.max_tags),
        }
        payload.update(self.extra)
        return payload

    def thresholds(self) -> dict[str, Any]:
        """Return tagging thresholds consumed by the tagging adapter."""

        return {
            "confidence": float(self.tag_confidence_threshold),
            "max_tags": int(self.max_tags),
        }


def resolve_data_dir(candidate: Path | str | None) -> Path:
    """Resolve the effective data directory for configuration storage."""

    if candidate is not None:
        return Path(candidate).expanduser()

    env_dir = os.environ.get("RAINDROP_ENHANCER_DATA")
    if env_dir:
        return Path(env_dir).expanduser()

    # Fallback to a sensible default inside the user's home directory.
    return Path.home() / ".raindrop-enhancer"


class ConfigManager:
    """Handle reading, writing, and updating the CLI configuration file."""

    def __init__(self, data_dir: Path | str | None = None) -> None:
        self.data_dir = resolve_data_dir(data_dir)
        self.config_path = self.data_dir / CONFIG_FILENAME

    # ------------------------------------------------------------------
    # Public API
    # ------------------------------------------------------------------
    def load(self) -> ConfigState:
        """Load the current configuration, returning defaults when missing."""

        if not self.config_path.exists():
            return ConfigState(data_dir=self.data_dir)

        raw = toml.loads(self.config_path.read_text(encoding="utf-8"))
        return _state_from_mapping(raw, fallback_dir=self.data_dir)

    def save(self, state: ConfigState) -> ConfigState:
        """Persist the provided configuration and enforce permissions."""

        self.data_dir.mkdir(parents=True, exist_ok=True)

        # Merge extra keys while ensuring the canonical data_dir is stored.
        payload = state.to_dict()
        payload["data_dir"] = str(self.data_dir)

        self.config_path.write_text(toml.dumps(payload), encoding="utf-8")
        _ensure_private_permissions(self.config_path)
        return state

    def update(self, **updates: Any) -> ConfigState:
        """Update individual fields in the configuration file."""

        state = self.load()
        for key, value in updates.items():
            if value is None:
                continue
            if not hasattr(state, key):
                state.extra[key] = value
            else:
                setattr(state, key, value)
        return self.save(state)

    # Convenience accessors -------------------------------------------------
    def thresholds(self) -> dict[str, Any]:
        return self.load().thresholds()

    def require_token(self) -> str:
        """Return the persisted Raindrop token or raise an informative error."""

        token = self.load().raindrop_token
        if not token:
            raise RuntimeError(
                "Raindrop token missing from config. Run `raindrop-enhancer configure --token ...`."
            )
        return token


# ---------------------------------------------------------------------------
# Internal helpers
# ---------------------------------------------------------------------------


def _state_from_mapping(
    payload: Mapping[str, Any], *, fallback_dir: Path
) -> ConfigState:
    data_dir = Path(payload.get("data_dir", fallback_dir)).expanduser()
    extra = {
        key: value
        for key, value in payload.items()
        if key
        not in {
            "data_dir",
            "raindrop_token",
            "llm_api_base",
            "llm_api_key",
            "tag_confidence_threshold",
            "max_tags",
        }
    }

    return ConfigState(
        data_dir=data_dir,
        raindrop_token=payload.get("raindrop_token"),
        llm_api_base=payload.get("llm_api_base"),
        llm_api_key=payload.get("llm_api_key"),
        tag_confidence_threshold=float(
            payload.get("tag_confidence_threshold", DEFAULT_CONFIDENCE)
        ),
        max_tags=int(payload.get("max_tags", DEFAULT_MAX_TAGS)),
        extra=extra,
    )


def _ensure_private_permissions(path: Path) -> None:
    """Ensure the config file is readable and writable only by the owner."""

    if os.name == "nt":  # Windows permissions differ; rely on default ACLs
        return

    desired_mode = stat.S_IRUSR | stat.S_IWUSR
    try:
        os.chmod(path, desired_mode)
    except PermissionError as exc:  # pragma: no cover - unlikely but defensive
        raise RuntimeError(
            f"Failed to set permissions on config file {path}: {exc}"
        ) from exc
