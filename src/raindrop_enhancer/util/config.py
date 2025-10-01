"""Configuration manager stub."""

from pathlib import Path
import toml


def write_config(path: Path, data: dict):
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(toml.dumps(data), encoding="utf-8")


def read_config(path: Path):
    return toml.loads(path.read_text(encoding="utf-8"))
