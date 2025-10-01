from types import SimpleNamespace
from pathlib import Path

from raindrop_enhancer.services.sync import run_full_sync
from raindrop_enhancer.services.tagging import TaggingAdapter
from raindrop_enhancer.domain.repositories import Repo


class FakeClient:
    def __init__(self):
        self.last_rate_limit = {"limit": 120, "remaining": 100, "reset": 0}

    def list_collections(self):
        return {"result": True, "items": [{"id": 1, "title": "col1"}]}

    def list_raindrops(self, collection_id, perpage=50):
        yield {
            "result": True,
            "items": [
                {
                    "id": 10,
                    "link": "http://example.com/1",
                    "title": "t1",
                    "excerpt": "hello world content",
                }
            ],
        }


def test_full_sync_with_tagging(tmp_path, monkeypatch):
    # monkeypatch requests.get to return simple HTML
    html = "<html><body><p>Example content for tagging adapter</p></body></html>"

    def fake_get(url, timeout=0):
        return SimpleNamespace(
            status_code=200, text=html, raise_for_status=lambda: None
        )

    monkeypatch.setattr("raindrop_enhancer.services.sync.requests.get", fake_get)

    repo = Repo(path=str(tmp_path / "db.sqlite"))
    repo.setup()
    client = FakeClient()
    tagging = TaggingAdapter()

    result = run_full_sync(
        repo=repo,
        client=client,
        tagging_adapter=tagging,
        export_path=tmp_path / "export.json",
        dry_run=True,
    )
    assert result["processed"] == 1
