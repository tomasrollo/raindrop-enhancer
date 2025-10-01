import pytest


import tempfile
from pathlib import Path
from raindrop_enhancer.domain.repositories import Repo
from raindrop_enhancer.domain.entities import LinkRecord
from raindrop_enhancer.services.sync import enrich_metadata


def fake_reprocess(repo: Repo):
    # Mark all links with manual_review as reprocessed (clear the flag)
    links = repo.list_links()
    for link in links:
        data = link.model_dump()
        if data.get("manual_review"):
            # Simulate reprocessing by clearing the flag
            data["manual_review"] = False
            repo.upsert_link(LinkRecord(**data))


def test_reprocess_status_not_implemented():
    with tempfile.TemporaryDirectory() as tmpdir:
        db_path = Path(tmpdir) / "test.db"
        repo = Repo(str(db_path))
        repo.setup()
        # Insert links, some flagged for manual review
        link1 = LinkRecord(raindrop_id=1, url="https://manual.com", title="Manual")
        link2 = LinkRecord(raindrop_id=2, url="https://ok.com", title="OK")
        repo.upsert_link(link1)
        repo.upsert_link(link2)
        # Simulate enrichment: mark link1 as manual_review
        enriched1 = enrich_metadata(link1.model_dump(), None)
        repo.upsert_link(LinkRecord(**enriched1))
        # Reprocess
        fake_reprocess(repo)
        # Status summary: count links needing review
        links = repo.list_links()
        needs_review = [l for l in links if getattr(l, "manual_review", False)]
        assert len(needs_review) == 0
