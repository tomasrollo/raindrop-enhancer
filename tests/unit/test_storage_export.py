"""Unit tests covering JSON export writer behaviour."""

from __future__ import annotations

import json
from datetime import datetime, timezone
from pathlib import Path

from raindrop_enhancer.services.storage import _json_default, write_export


def test_write_export_injects_schema_and_is_idempotent(tmp_path) -> None:
    export_path = tmp_path / "exports" / "sync.json"
    payload = {"links": [{"raindrop_id": 1}]}

    changed = write_export(export_path, payload, schema_version="1.0")
    assert changed is True
    document = json.loads(export_path.read_text(encoding="utf-8"))
    assert document["schema_version"] == "1.0"

    first_mtime = export_path.stat().st_mtime_ns
    unchanged = write_export(
        export_path, {"links": [{"raindrop_id": 1}]}, schema_version="1.0"
    )
    second_mtime = export_path.stat().st_mtime_ns
    assert unchanged is False
    assert first_mtime == second_mtime


def test_write_export_detects_changes(tmp_path) -> None:
    export_path = tmp_path / "exports" / "sync.json"
    write_export(export_path, {"links": []}, schema_version="1.0")

    changed = write_export(
        export_path, {"links": [], "summary": {"processed": 1}}, schema_version="1.0"
    )
    assert changed is True
    document = json.loads(export_path.read_text(encoding="utf-8"))
    assert document["summary"]["processed"] == 1


def test_json_default_handles_datetime_and_path() -> None:
    now = datetime(2025, 1, 1, tzinfo=timezone.utc)
    path = Path("/tmp/export.json")

    assert _json_default(now).startswith("2025-01-01T00:00:00")
    assert _json_default(path) == "/tmp/export.json"
    assert _json_default(123) == "123"
