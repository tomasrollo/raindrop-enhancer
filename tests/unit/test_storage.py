from raindrop_enhancer.domain.repositories import Repo


def test_repo_setup_raises_not_implemented():
    repo = Repo(path=":memory:")
    # should not raise and should prepare an engine
    repo.setup()
    assert repo.engine is not None
