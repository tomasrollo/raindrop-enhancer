import types
import pytest


def test_trafilatura_fetcher_timeout_and_extract(monkeypatch):
    # Patch trafilatura.fetch_url and extract to simulate timeout and successful extract
    fake_module = types.SimpleNamespace()

    def fake_fetch_url(url, timeout=10.0):
        if "slow" in url:
            raise TimeoutError("timeout")
        return "<html>content</html>"

    def fake_extract(html, output_format="markdown"):
        return "# Title\n\nBody"

    monkeypatch.setitem(__import__("sys").modules, "trafilatura", fake_module)
    fake_module.fetch_url = fake_fetch_url
    fake_module.extract = fake_extract

    from raindrop_enhancer.content.fetcher import TrafilaturaFetcher

    f = TrafilaturaFetcher(timeout=0.01)
    # fast URL returns markdown
    r = f.fetch("https://example.org/fast")
    assert r.markdown is not None
    # slow URL returns error but handled
    r2 = f.fetch("https://example.org/slow")
    assert r2.markdown is None
    assert r2.error is not None
