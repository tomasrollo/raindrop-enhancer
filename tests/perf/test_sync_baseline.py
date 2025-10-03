import os
import pytest


def test_perf_sync_baseline_small(tmp_path):
    """Performance smoke test placeholder for baseline (synthetic dataset)."""
    # Skip perf tests by default; enable by setting ENABLE_PERF=1 in environment
    if not (os.environ.get("ENABLE_PERF") == "1"):
        pytest.skip("Perf tests disabled by default")
    pytest.fail("Perf test placeholder — implement benchmark")
