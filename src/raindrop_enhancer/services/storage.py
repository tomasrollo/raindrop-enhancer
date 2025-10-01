"""Storage helpers and JSON export writer stub."""

import json
from pathlib import Path


SCHEMA_VERSION = "1.0.0"


def write_export(path: Path, data, schema_version: str = SCHEMA_VERSION):
    """
    Write JSON export with schema versioning. Idempotent: only updates if content changes.
    """
    path.parent.mkdir(parents=True, exist_ok=True)
    export = {
        "schema_version": schema_version,
        "exported_at": __import__("datetime").datetime.now().isoformat(),
        "data": data,
    }
    # Check if file exists and is identical
    if path.exists():
        try:
            existing = json.loads(path.read_text(encoding="utf-8"))
            if existing == export:
                return False  # No update needed
        except Exception:
            pass
    with path.open("w", encoding="utf-8") as f:
        json.dump(export, f, ensure_ascii=False, indent=2)
    return True
