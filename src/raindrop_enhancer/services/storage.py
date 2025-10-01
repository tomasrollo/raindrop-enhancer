"""Storage helpers and JSON export writer stub."""

import json
from pathlib import Path
from typing import Any, Dict, Optional


def write_export(
    path: Path,
    data: Any,
    *,
    metadata: Optional[Dict[str, Any]] = None,
    schema_version: str = "1.0",
) -> None:
    """Write export JSON with schema version and metadata.

    The function writes atomically via a temporary file and then replaces the
    destination. `metadata` is merged into the top-level object under
    `metadata` key.
    """
    path.parent.mkdir(parents=True, exist_ok=True)
    wrapper: Dict[str, Any] = {"schema_version": schema_version, "items": data}
    if metadata:
        wrapper["metadata"] = metadata

    # idempotent write: write to temp and move
    tmp = path.with_suffix(path.suffix + ".tmp")
    with tmp.open("w", encoding="utf-8") as f:
        # compact representation by default; caller can pretty-print later
        json.dump(wrapper, f, ensure_ascii=False)
    tmp.replace(path)
