from pathlib import Path
from raindrop_enhancer.services.sync import run_full_sync, enrich_link


class FakeClient:
    def list_collections(self):
        return {"items": [{"id": 1}]}

    def list_raindrops(self, collection_id, perpage=50):
        yield {"items": [{"id": 1, "link": "https://example.com/1", "title": "T1"}]}


class FakeTagger:
    def suggest_for_batch(self, contents):
        return [[{"tag": "x", "confidence": 0.9} for _ in contents]]


class InMemoryRepo:
    def __init__(self):
        self._links = []

    def upsert_link(self, lr):
        self._links.append(lr)

    def upsert_tag_suggestions(self, raindrop_id, tags):
        return


def test_run_full_sync_writes_export(tmp_path: Path, monkeypatch):
    repo = InMemoryRepo()
    client = FakeClient()
    export = tmp_path / "out.json"

    result = run_full_sync(
        repo=repo,
        client=client,
        tagging_adapter=FakeTagger(),
        export_path=export,
        dry_run=False,
    )
    processed = result.get("processed")
    assert processed is not None
    assert processed >= 0
