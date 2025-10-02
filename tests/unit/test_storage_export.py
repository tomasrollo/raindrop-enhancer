from pathlib import Path
import json

from raindrop_enhancer.services.storage import write_export


def test_write_export_creates_wrapped_json(tmp_path):
    path = tmp_path / "out.json"
    data = [{"id": 1, "url": "http://example.com"}]
    metadata = {"run_id": "r1"}
    write_export(path, data, metadata=metadata, schema_version="2.0")
    assert path.exists()
    obj = json.loads(path.read_text(encoding="utf-8"))
    assert obj["schema_version"] == "2.0"
    assert obj["metadata"]["run_id"] == "r1"
    assert isinstance(obj["items"], list)
