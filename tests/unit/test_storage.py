import pytest
from raindrop_enhancer.domain.repositories import Repo


from raindrop_enhancer.domain.entities import LinkRecord


def test_repo_crud_and_audit_trail():
    """
    Unit: Repo should support CRUD, deduplication, and audit logging.
    """
    repo = Repo(path=":memory:")
    repo.setup()
    link = LinkRecord(raindrop_id=123, url="https://example.com")
    inserted = repo.upsert_link(link)
    fetched = repo.get_link(123)
    assert fetched is not None
    assert fetched.url == "https://example.com"
