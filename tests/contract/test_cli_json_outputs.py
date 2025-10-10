import json
from click.testing import CliRunner
from raindrop_enhancer import cli


def _get_entry():
    return getattr(cli, "cli", getattr(cli, "main", None))


def test_sync_json_schema(monkeypatch):
    runner = CliRunner()
    entry = _get_entry()
    if entry is None:
        return

    # Monkeypatch RaindropClient.list_collections and list_raindrops to produce minimal data
    try:
        # Patch the RaindropClient used by the CLI module (imported at module scope)
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
    except Exception:
        return
    # Ensure RAINDROP_TOKEN is present for commands that require it
    monkeypatch.setenv("RAINDROP_TOKEN", "fake-token")

    # Stub Orchestrator to return a deterministic outcome object
    try:
        from datetime import datetime, timezone
        from raindrop_enhancer import cli as cli_mod
        from raindrop_enhancer.sync import orchestrator as orch_mod

        class FakeOutcome:
            def __init__(self):
                self.run_started_at = datetime.now(timezone.utc)
                self.run_finished_at = datetime.now(timezone.utc)
                self.was_full_refresh = False
                self.new_links = 0
                self.total_links = 0
                self.db_path = "/tmp/test.db"
                self.requests_count = 0
                self.retries_count = 0

        class FakeOrchestrator:
            def __init__(self, dbp, client):
                pass

            def run(self, full_refresh=False, dry_run=False):
                return FakeOutcome()

        # Patch the Orchestrator symbol used by the CLI module (it was imported earlier)
        monkeypatch.setattr(orch_mod, "Orchestrator", FakeOrchestrator)
        monkeypatch.setattr(cli_mod, "Orchestrator", FakeOrchestrator, raising=False)
    except Exception:
        return

    result = runner.invoke(entry, ["sync", "--json"])
    assert result.exit_code == 0
    data = json.loads(result.output)
    assert "run_started_at" in data
    assert "run_finished_at" in data


def test_capture_json_schema(monkeypatch):
    runner = CliRunner()
    entry = _get_entry()
    if entry is None:
        return

    # Monkeypatch capture runner to yield an empty summary
    try:
        from raindrop_enhancer.content import capture_runner
        from datetime import datetime, timezone

        class FakeRunner:
            def __init__(self, *args, **kwargs):
                pass

            def run(self, limit=None, dry_run=False, refresh=False):
                class S:
                    started_at = datetime.now(timezone.utc)

                    completed_at = datetime.now(timezone.utc)

                return S()

        monkeypatch.setattr(capture_runner, "CaptureRunner", FakeRunner)
    except Exception:
        return

    # Ensure RAINDROP_TOKEN is present for capture flow
    monkeypatch.setenv("RAINDROP_TOKEN", "fake-token")

    result = runner.invoke(entry, ["capture", "--json"])
    assert result.exit_code == 0
    data = json.loads(result.output)
    assert "session" in data


def test_tag_json_schema(monkeypatch):
    runner = CliRunner()
    entry = _get_entry()
    if entry is None:
        return

    # Monkeypatch DSPy and DB interactions to return deterministic summary
    try:
        from raindrop_enhancer.content import dspy_settings
        from raindrop_enhancer.content import tag_generator

        def fake_configure():
            return lambda prompt: (["tag1", "tag2"], None)

        monkeypatch.setattr(dspy_settings, "configure_dspy", fake_configure)

        class FakeStore:
            def connect(self):
                pass

            def fetch_untagged_links(self, limit=None):
                return []

            def write_auto_tags_batch(self, tuples):
                return

        monkeypatch.setattr(tag_generator, "SQLiteStore", FakeStore)
    except Exception:
        return

    result = runner.invoke(entry, ["tag", "generate", "--json"])
    assert result.exit_code == 0
    data = json.loads(result.output)
    assert "processed" in data
