import os
import pytest


def test_perf_sync_incremental_small(tmp_path):
    """Performance smoke test placeholder for incremental sync (synthetic dataset)."""
    # Skip perf tests by default; enable by setting ENABLE_PERF=1 in environment
    if not (os.environ.get("ENABLE_PERF") == "1"):
        pytest.skip("Perf tests disabled by default")
    from pathlib import Path
    from raindrop_enhancer.storage.sqlite_store import SQLiteStore

    # Import perf utils by file path to avoid package import issues
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
    from datetime import datetime

    # prepare small baseline then incremental payload set
    baseline_count = int(os.environ.get("PERF_BASELINE_COUNT", "500"))
    incremental_count = int(os.environ.get("PERF_INCREMENTAL_COUNT", "50"))

    baseline = make_raindrop_payloads(baseline_count)
    incremental = make_raindrop_payloads(incremental_count, start=None)
    # Avoid ID collisions with baseline by offsetting incremental _id values
    id_offset = 1000000 + baseline_count
    for p in incremental:
        p["_id"] = int(p.get("_id", 0)) + id_offset

    db_path = tmp_path / "perf_incremental.db"
    store = SQLiteStore(db_path)
    store.connect()

    # insert baseline
    now = datetime.utcnow()
    base_links = [
        RaindropLink.from_raindrop(Raindrop.from_api(p), now) for p in baseline
    ]
    store.insert_batch(base_links)

    # prepare incremental links
    inc_links = [
        RaindropLink.from_raindrop(Raindrop.from_api(p), now) for p in incremental
    ]

    max_seconds = float(os.environ.get("PERF_INCREMENTAL_MAX_SECONDS", "0.5"))
    with Timer() as t:
        inserted = store.insert_batch(inc_links)

    assert inserted == incremental_count
    assert store.count_links() == baseline_count + incremental_count
    assert t.elapsed <= max_seconds, (
        f"Incremental insert too slow: {t.elapsed}s > {max_seconds}s"
    )
    store.close()
