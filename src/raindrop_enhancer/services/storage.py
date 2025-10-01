"""Storage helpers and JSON export writer stub."""

import json
from pathlib import Path


def write_export(path: Path, data):
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8") as f:
        json.dump(data, f)
