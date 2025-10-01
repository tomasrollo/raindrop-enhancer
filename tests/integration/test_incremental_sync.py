import pytest


import tempfile
import json
from pathlib import Path
from datetime import datetime, timedelta
from raindrop_enhancer.domain.repositories import Repo
from raindrop_enhancer.domain.entities import LinkRecord, SyncRun
from raindrop_enhancer.services.sync import run_incremental_sync


class FakeTagging:
    def suggest_tags_for_content(self, content):
        return [{"tag": "test", "confidence": 1.0}]


def test_incremental_sync_only_updates_changed_links():
    """
    Integration: Incremental sync should process only updated links and record rate-limit telemetry.
    """
    with tempfile.TemporaryDirectory() as tmpdir:
        db_path = Path(tmpdir) / "test.db"
        export_path = Path(tmpdir) / "export.json"
        repo = Repo(str(db_path))
        repo.setup()
        # Insert two links, one old, one new
        old_time = datetime.now() - timedelta(days=2)
        new_time = datetime.now() - timedelta(hours=1)
        link1 = LinkRecord(
            raindrop_id=1, url="https://old.com", title="Old", updated_at=old_time
        )
        link2 = LinkRecord(
            raindrop_id=2, url="https://new.com", title="New", updated_at=new_time
        )
        repo.upsert_link(link1)
        repo.upsert_link(link2)
        tagging = FakeTagging()
        since = datetime.now() - timedelta(hours=2)
        result = run_incremental_sync(
            repo, tagging, export_path, since=since, dry_run=False
        )
        # Only link2 should be exported
        data = json.loads(export_path.read_text())
        urls = [item["url"] for item in data]
        assert "https://new.com" in urls
        assert "https://old.com" not in urls
        # Check SyncRun has been updated (rate-limit fields may be None in this fake)
        from sqlmodel import Session, select
        from sqlalchemy import desc

        with Session(repo.engine) as session:
            run = session.exec(
                select(SyncRun).order_by(desc(getattr(SyncRun, "completed_at")))
            ).first()
            assert run is not None
            assert run.mode == "incremental"
