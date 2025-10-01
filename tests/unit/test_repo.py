from raindrop_enhancer.domain.repositories import Repo
from raindrop_enhancer.domain.entities import LinkRecord
import tempfile
from pathlib import Path


def test_repo_incremental_and_dedupe():
    with tempfile.TemporaryDirectory() as tmpdir:
        db_path = Path(tmpdir) / "test.db"
        repo = Repo(str(db_path))
        repo.setup()
        link = LinkRecord(raindrop_id=1, url="https://a.com")
        repo.upsert_link(link)
        # Update same raindrop_id
        link2 = LinkRecord(raindrop_id=1, url="https://b.com")
        repo.upsert_link(link2)
        fetched = repo.get_link(1)
        assert fetched.url == "https://b.com"
        # Test get_links_updated_since
        import datetime

        all_links = repo.list_links()
        since = datetime.datetime.now(datetime.UTC)
        updated = repo.get_links_updated_since(since)
        assert isinstance(updated, list)
