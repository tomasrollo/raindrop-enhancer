import io
from datetime import datetime
from raindrop_enhancer.exporters.json_exporter import export_to_file
from raindrop_enhancer.models import Raindrop


def test_json_exporter_format():
    now = datetime.utcnow()
    r = Raindrop(
        id=1,
        collection_id=1,
        collection_title="c",
        title="t",
        url="https://x",
        excerpt=None,
        created_at=now,
        last_updated_at=now,
        tags=[],
        cover=None,
    )
    fh = io.StringIO()
    export_to_file([r], fh, pretty=True)
    out = fh.getvalue()
    assert out.strip().startswith("[") and out.strip().endswith("]")
    assert '"id": 1' in out
