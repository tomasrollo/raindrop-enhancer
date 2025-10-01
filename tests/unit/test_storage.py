from raindrop_enhancer.domain.repositories import Repo


def test_repo_setup_raises_not_implemented():
    repo = Repo(path=":memory:")
    try:
        repo.setup()
    except NotImplementedError:
        raise
    else:
        raise AssertionError("Repo.setup should raise NotImplementedError until implemented")
