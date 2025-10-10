from click.testing import CliRunner
from raindrop_enhancer import cli


def _get_entry():
    return getattr(cli, "cli", getattr(cli, "main", None))


def test_quiet_and_verbose(monkeypatch):
    runner = CliRunner()
    entry = _get_entry()
    if entry is None:
        return

    # Patch RaindropClient to avoid network and provide minimal behavior
    from raindrop_enhancer import cli as cli_mod

    class FakeClient:
        def __init__(self, *args, **kwargs):
            pass

        def list_collections(self):
            return [{"_id": -1}]

        def list_raindrops(self, cid):
            return []

        def close(self):
            pass

    monkeypatch.setattr(cli_mod, "RaindropClient", FakeClient, raising=False)
    monkeypatch.setenv("RAINDROP_TOKEN", "fake-token")

    # Quiet: no summary output
    res = runner.invoke(entry, ["export", "--output", "-", "--quiet"])
    assert res.exit_code == 0
    assert "Exported" not in res.output

    # Verbose: logs to stderr; ensure exit_code 0
    res2 = runner.invoke(entry, ["export", "--output", "-", "--verbose"])
    assert res2.exit_code == 0


def test_dry_run(monkeypatch):
    runner = CliRunner()
    entry = _get_entry()
    if entry is None:
        return

    from raindrop_enhancer import cli as cli_mod

    class FakeClient:
        def __init__(self, *args, **kwargs):
            pass

        def list_collections(self):
            return [{"_id": -1}]

        def list_raindrops(self, cid):
            return []

        def close(self):
            pass

    monkeypatch.setattr(cli_mod, "RaindropClient", FakeClient, raising=False)
    monkeypatch.setenv("RAINDROP_TOKEN", "fake-token")

    res = runner.invoke(entry, ["export", "--dry-run"])
    assert res.exit_code == 0
    assert "Dry run" in res.output
