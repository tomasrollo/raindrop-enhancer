import json
from click.testing import CliRunner
from raindrop_enhancer import cli


def _get_entry():
    return getattr(cli, "cli", getattr(cli, "main", None))


def test_export_integration(monkeypatch):
    runner = CliRunner()
    entry = _get_entry()
    if entry is None:
        return

    # Patch RaindropClient to return one collection and no raindrops
    from raindrop_enhancer import cli as cli_mod

    class FakeClient:
        def __init__(self, *args, **kwargs):
            pass

        def list_collections(self):
            return [{"_id": 1}]

        def list_raindrops(self, cid):
            return [{"id": 10, "title": "Test", "link": "https://x/"}]

        def close(self):
            pass

    monkeypatch.setattr(cli_mod, "RaindropClient", FakeClient, raising=False)

    # Patch export_to_file as referenced by the CLI module to avoid writing; ensure it's called
    called = {}

    def fake_export_to_file(items, fh, pretty=False):
        called["count"] = len(items)
        fh.write("[]")

    monkeypatch.setattr(cli_mod, "export_to_file", fake_export_to_file, raising=False)
    monkeypatch.setenv("RAINDROP_TOKEN", "fake-token")

    result = runner.invoke(entry, ["export", "--output", "-"])
    assert result.exit_code == 0
    assert called.get("count", 0) >= 1


def test_sync_integration(monkeypatch):
    runner = CliRunner()
    entry = _get_entry()
    if entry is None:
        return

    # Patch Orchestrator to return deterministic outcome
    from datetime import datetime, timezone
    from raindrop_enhancer import cli as cli_mod

    class FakeOutcome:
        def __init__(self):
            self.run_started_at = datetime.now(timezone.utc)
            self.run_finished_at = datetime.now(timezone.utc)
            self.was_full_refresh = False
            self.new_links = 1
            self.total_links = 1
            self.db_path = "/tmp/test.db"
            self.requests_count = 0
            self.retries_count = 0

    class FakeOrchestrator:
        def __init__(self, dbp, client):
            pass

        def run(self, full_refresh=False, dry_run=False):
            return FakeOutcome()

    monkeypatch.setattr(cli_mod, "Orchestrator", FakeOrchestrator, raising=False)
    monkeypatch.setenv("RAINDROP_TOKEN", "fake-token")

    result = runner.invoke(entry, ["sync", "--dry-run"])
    assert result.exit_code == 0
    assert "Dry run" in result.output or "Synced" in result.output


def test_capture_integration(monkeypatch):
    runner = CliRunner()
    entry = _get_entry()
    if entry is None:
        return

    # Patch CaptureRunner to return summary with attempts
    from datetime import datetime, timezone
    from raindrop_enhancer.content import capture_runner

    class FakeSummary:
        def __init__(self):
            self.started_at = datetime.now(timezone.utc)
            self.completed_at = datetime.now(timezone.utc)
            self.attempts = []

    class FakeRunner:
        def __init__(self, *args, **kwargs):
            pass

        def run(self, limit=None, dry_run=False, refresh=False):
            return FakeSummary()

    monkeypatch.setattr(capture_runner, "CaptureRunner", FakeRunner)
    monkeypatch.setenv("RAINDROP_TOKEN", "fake-token")

    result = runner.invoke(entry, ["capture", "--dry-run"])
    assert result.exit_code == 0
    assert "Processed" in result.output or "Dry run" in result.output
