import os
import sys
import pytest


def test_perf_cli_tags_generate_dryrun_50(tmp_path, monkeypatch):
    """Performance smoke test: 50-link dry-run of `tags generate` should complete quickly.

    Skips by default unless ENABLE_PERF=1 is set in the environment (same pattern as
    other perf tests in this repo).
    """
    if not (os.environ.get("ENABLE_PERF") == "1"):
        pytest.skip("Perf tests disabled by default")

    # Import perf utils by file path to avoid package import issues
    from pathlib import Path
    import importlib.util

    repo_root = Path(__file__).resolve().parents[2]
    utils_path = repo_root / "tests" / "perf" / "utils.py"

    spec = importlib.util.spec_from_file_location("perf_utils", str(utils_path))
    if spec is None or spec.loader is None:
        pytest.skip("Could not load perf utils")
    perf_utils = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(perf_utils)  # type: ignore
    make_raindrop_payloads = perf_utils.make_raindrop_payloads
    Timer = perf_utils.Timer

    # Build 50 synthetic raindrops
    count = int(os.environ.get("PERF_CLI_TAGS_COUNT", "50"))
    payloads = make_raindrop_payloads(count)

    # Create and seed temporary DB
    db_path = tmp_path / "perf_tags.db"
    from raindrop_enhancer.storage.sqlite_store import SQLiteStore
    from raindrop_enhancer.models import Raindrop, RaindropLink
    from datetime import datetime, timezone

    store = SQLiteStore(db_path)
    store.connect()

    now = datetime.now(timezone.utc)
    links = [RaindropLink.from_raindrop(Raindrop.from_api(p), now) for p in payloads]
    inserted = store.insert_batch(links)
    assert inserted == count

    # Monkeypatch DSPy configuration to a fast deterministic predictor
    def fake_predictor(prompt: str):
        # Return a couple of simple tags deterministically
        return ["alpha", "beta"]

    monkeypatch.setenv("RAINDROP_DSPY_MODEL", "dummy:model")
    import raindrop_enhancer.content.dspy_settings as ds

    monkeypatch.setattr(ds, "configure_dspy", lambda: fake_predictor)

    # Run CLI tags_generate as a dry-run and measure elapsed time and memory
    from click.testing import CliRunner
    from raindrop_enhancer.cli import tags_generate

    max_seconds = float(os.environ.get("PERF_CLI_TAGS_MAX_SECONDS", "3.0"))
    # memory threshold in bytes (50 MB default)
    max_mem_bytes = int(
        os.environ.get("PERF_CLI_TAGS_MAX_MEM_BYTES", str(50 * 1024 * 1024))
    )

    # Try to measure peak RSS using resource (best-effort; units differ by platform)
    try:
        import resource

        have_resource = True
    except Exception:
        resource = None
        have_resource = False

    runner = CliRunner()

    if have_resource:
        before = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss

    with Timer() as t:
        res = runner.invoke(
            tags_generate, ["--db-path", str(db_path), "--dry-run", "--quiet"]
        )

    if have_resource:
        after = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss
        # Normalize units: macOS returns bytes, Linux returns kilobytes
        if sys.platform.startswith("darwin"):
            mem_delta = after - before
        elif sys.platform.startswith("linux"):
            mem_delta = (after - before) * 1024
        else:
            mem_delta = after - before

        assert mem_delta <= max_mem_bytes, (
            f"Memory growth too large: {mem_delta} bytes > {max_mem_bytes} bytes"
        )

    # CLI should exit cleanly
    assert res.exit_code == 0, (
        f"tags_generate failed: {res.exit_code} stdout={res.output}"
    )

    # Check time threshold
    assert t.elapsed <= max_seconds, (
        f"tags generate too slow: {t.elapsed}s > {max_seconds}s"
    )

    store.close()
