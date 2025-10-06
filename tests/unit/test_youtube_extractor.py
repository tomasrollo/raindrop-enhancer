from __future__ import annotations

from raindrop_enhancer.content import youtube_extractor as ye


def test_is_youtube_url_positive():
    assert ye.is_youtube_url("https://www.youtube.com/watch?v=dQw4w9WgXcQ")
    assert ye.is_youtube_url("https://youtu.be/dQw4w9WgXcQ")


def test_is_youtube_url_negative():
    assert not ye.is_youtube_url("")
    assert not ye.is_youtube_url("https://example.com/watch?v=123")


def test_extract_metadata_not_youtube():
    res = ye.extract_metadata("https://example.com/abc")
    assert res["error"] == "not_youtube"
    assert res["title"] is None


def test_extract_metadata_when_yt_dlp_missing(monkeypatch):
    # Ensure importlib fails to find yt_dlp
    monkeypatch.setattr(
        "importlib.import_module",
        lambda name: (_ for _ in ()).throw(ImportError("not found")),
    )
    res = ye.extract_metadata("https://youtu.be/dQw4w9WgXcQ")
    assert res["error"].startswith("yt_dlp_missing")


def test_extract_metadata_success(monkeypatch):
    class DummyYDL:
        def __init__(self, opts):
            self.opts = opts

        def __enter__(self):
            return self

        def __exit__(self, exc_type, exc, tb):
            return False

        def extract_info(self, url, download=False):
            return {"title": "Test Title", "description": "Desc"}

    class DummyModule:
        YoutubeDL = DummyYDL

    monkeypatch.setattr("importlib.import_module", lambda name: DummyModule())
    res = ye.extract_metadata("https://youtu.be/dQw4w9WgXcQ")
    assert res["error"] is None
    assert res["title"] == "Test Title"
    assert res["description"] == "Desc"
