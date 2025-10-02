"""Storage helpers and JSON export writer utilities."""

from __future__ import annotations

import json
from datetime import datetime
from pathlib import Path
from typing import Any


def write_export(
    path: Path,
    data: Any,
    *,
    schema_version: str | None = None,
    indent: int = 2,
) -> bool:
    """Write JSON export to ``path`` atomically.

    Returns ``True`` when the on-disk payload changed. The function ensures
    deterministic ordering so repeated calls with identical data are
    idempotent and avoid unnecessary filesystem writes.
    """

    payload = data
    if isinstance(data, dict) and schema_version and "schema_version" not in data:
        payload = dict(data)
        payload["schema_version"] = schema_version

    serialized = json.dumps(
        payload,
        indent=indent,
        sort_keys=True,
        ensure_ascii=False,
        default=_json_default,
    )
    if not serialized.endswith("\n"):
        serialized += "\n"

    path.parent.mkdir(parents=True, exist_ok=True)

    if path.exists():
        try:
            if path.read_text(encoding="utf-8") == serialized:
                return False
        except OSError:
            pass

    temp_path = path.with_suffix(path.suffix + ".tmp")
    temp_path.write_text(serialized, encoding="utf-8")
    temp_path.replace(path)
    return True


def _json_default(value: Any) -> Any:
    if isinstance(value, datetime):
        return value.isoformat()
    if isinstance(value, Path):
        return str(value)
    return str(value)
