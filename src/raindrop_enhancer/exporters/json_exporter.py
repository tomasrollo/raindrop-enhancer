"""JSON exporter for raindrop_enhancer."""

from __future__ import annotations

import json
from dataclasses import asdict, is_dataclass
from datetime import datetime
from typing import Iterable, Any, IO


def _serialize_item(item: Any) -> dict:
    if is_dataclass(item):
        return _make_jsonable(asdict(item))
    if isinstance(item, dict):
        return _make_jsonable(item)
    raise TypeError("Unsupported item type for JSON exporter")


def _make_jsonable(obj: Any) -> Any:
    if isinstance(obj, dict):
        return {k: _make_jsonable(v) for k, v in obj.items()}
    if isinstance(obj, list):
        return [_make_jsonable(v) for v in obj]
    if isinstance(obj, datetime):
        return obj.isoformat()
    return obj


def export_to_file(items: Iterable[Any], fh: IO[str], pretty: bool = False) -> None:
    """Write items as a JSON array to the given file handle.

    Items may be dataclasses or dicts.
    """
    arr = [_serialize_item(i) for i in items]
    if pretty:
        json.dump(arr, fh, indent=2, ensure_ascii=False)
    else:
        json.dump(arr, fh, separators=(",", ":"), ensure_ascii=False)
    fh.write("\n")
