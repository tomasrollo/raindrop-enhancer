import os
import pytest


def test_perf_sync_baseline_small(tmp_path):
    """Performance smoke test placeholder for baseline (synthetic dataset)."""
    # Skip perf tests by default; enable by setting ENABLE_PERF=1 in environment
    if not (os.environ.get("ENABLE_PERF") == "1"):
        pytest.skip("Perf tests disabled by default")
    # Build synthetic dataset and measure baseline insert performance
    import sys
    from pathlib import Path
    from raindrop_enhancer.storage.sqlite_store import SQLiteStore

    # Import tests/perf/utils.py by file path to avoid package import issues
    repo_root = Path(__file__).resolve().parents[2]
    utils_path = repo_root / "tests" / "perf" / "utils.py"
    import importlib.util

    spec = importlib.util.spec_from_file_location("perf_utils", str(utils_path))
    if spec is None or spec.loader is None:
        pytest.skip("Could not load perf utils")
    perf_utils = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(perf_utils)  # type: ignore
    make_raindrop_payloads = perf_utils.make_raindrop_payloads
    Timer = perf_utils.Timer
    from raindrop_enhancer.models import Raindrop, RaindropLink
    import json
    from datetime import datetime, timezone

    # small benchmark size by default; can be scaled via PERF_COUNT env
    count = int(os.environ.get("PERF_COUNT", "1000"))
    payloads = make_raindrop_payloads(count)

    # create temp DB path
    db_path = tmp_path / "perf_baseline.db"
    store = SQLiteStore(db_path)
    store.connect()

    # convert payloads to Raindrop and then to RaindropLink
    links = []
    now = datetime.now(timezone.utc)
    for p in payloads:
        r = Raindrop.from_api(p)
        links.append(RaindropLink.from_raindrop(r, now))

    # run benchmark
    max_seconds = float(os.environ.get("PERF_MAX_SECONDS", "2.0"))
    with Timer() as t:
        inserted = store.insert_batch(links)

    # sanity checks
    assert inserted == count
    assert store.count_links() == count
    # assert performance threshold
    assert t.elapsed <= max_seconds, (
        f"Baseline insert too slow: {t.elapsed}s > {max_seconds}s"
    )
    store.close()
