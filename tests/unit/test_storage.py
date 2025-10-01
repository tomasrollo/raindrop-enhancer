import pytest
from raindrop_enhancer.domain.repositories import Repo


def test_repo_crud_and_audit_trail():
    """
    Unit: Repo should support CRUD, deduplication, and audit logging (TDD red phase).
    """
    repo = Repo(path=":memory:")
    with pytest.raises(NotImplementedError):
        repo.setup()
