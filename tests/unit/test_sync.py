from types import SimpleNamespace

from raindrop_enhancer.services.sync import compute_content_hash, enrich_link


def test_compute_content_hash_is_stable():
    h1 = compute_content_hash("hello world")
    h2 = compute_content_hash("hello world")
    assert h1 == h2


def test_enrich_link_with_content(monkeypatch):
    html = "<html><head></head><body><h1>Title</h1><p>This is some content that is long enough to avoid manual review.</p></body></html>"

    def fake_get(url, timeout=0):
        return SimpleNamespace(
            status_code=200, text=html, raise_for_status=lambda: None
        )

    monkeypatch.setattr("raindrop_enhancer.services.sync.requests.get", fake_get)

    link = {"url": "http://example.com/page"}
    enriched = enrich_link(link)
    assert "content" in enriched
    assert enriched["manual_review"] in (True, False)
