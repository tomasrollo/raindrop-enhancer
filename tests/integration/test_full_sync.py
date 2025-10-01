import pytest


import tempfile
import json
from pathlib import Path
from raindrop_enhancer.domain.repositories import Repo
from raindrop_enhancer.domain.entities import LinkRecord
from raindrop_enhancer.services.sync import run_full_sync
from raindrop_enhancer.services.tagging import TaggingService


class FakeTagging:
    def suggest_tags_for_content(self, content):
        return [{"tag": "test", "confidence": 1.0}]


def test_full_sync_happy_path():
    """
    Integration: Full sync should export JSON, persist to SQLite, and tag links.
    """
    with tempfile.TemporaryDirectory() as tmpdir:
        db_path = Path(tmpdir) / "test.db"
        export_path = Path(tmpdir) / "export.json"
        repo = Repo(str(db_path))
        repo.setup()
        # Insert a fake link
        link = LinkRecord(raindrop_id=1, url="https://example.com", title="Test")
        repo.upsert_link(link)
        tagging = FakeTagging()
        result = run_full_sync(repo, tagging, export_path, dry_run=False)
        # Check export file
        assert export_path.exists()
        data = json.loads(export_path.read_text())
        assert isinstance(data, list)
        assert data[0]["url"] == "https://example.com"
        assert data[0]["tags"][0]["tag"] == "test"
        # Check DB persistence
        fetched = repo.get_link(1)
        assert fetched is not None
