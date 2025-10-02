"""Configuration manager for reading/writing config.toml with 0600 permissions and threshold access."""

from pathlib import Path
import toml
import os
from typing import Any, Dict, Optional


def enforce_permissions(path: Path):
    # Set file permissions to 0600 (owner read/write only)
    try:
        os.chmod(path, 0o600)
    except Exception:
        pass  # On Windows or error, ignore


class ConfigManager:
    def __init__(self, config_path: Path):
        self.config_path = config_path

    def write(self, data: Dict[str, Any]):
        self.config_path.parent.mkdir(parents=True, exist_ok=True)
        self.config_path.write_text(toml.dumps(data), encoding="utf-8")
        enforce_permissions(self.config_path)

    def read(self) -> Dict[str, Any]:
        if not self.config_path.exists():
            return {}
        enforce_permissions(self.config_path)
        return toml.loads(self.config_path.read_text(encoding="utf-8"))

    def get_threshold(self, key: str, default: Optional[Any] = None) -> Any:
        config = self.read()
        thresholds = config.get("thresholds", {})
        return thresholds.get(key, default)


# Legacy functions for compatibility
def write_config(path: Path, data: dict):
    ConfigManager(path).write(data)


def read_config(path: Path):
    return ConfigManager(path).read()
