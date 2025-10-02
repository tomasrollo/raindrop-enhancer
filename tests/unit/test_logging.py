"""Tests for structured logging utilities and metrics."""

from __future__ import annotations

import json
import logging
from datetime import datetime, timezone
from pathlib import Path

import pytest

from raindrop_enhancer.util import logging as log_util
from raindrop_enhancer.util.retry import RetryEvent


@pytest.fixture(autouse=True)
def reset_logging_state():
    """Ensure logging globals do not leak across tests."""

    log_util._CONFIGURED = False
    log_util.get_metrics().clear()
    root = logging.getLogger()
    for handler in list(root.handlers):
        root.removeHandler(handler)
    yield
    log_util._CONFIGURED = False
    log_util.get_metrics().clear()
    root = logging.getLogger()
    for handler in list(root.handlers):
        root.removeHandler(handler)


def test_configure_logging_installs_json_formatter():
    root = log_util.configure_logging("debug")

    assert root.level == logging.DEBUG
    assert len(root.handlers) == 1
    handler = root.handlers[0]
    assert isinstance(handler.formatter, log_util.JsonFormatter)

    # Updating the level should not duplicate handlers.
    second = log_util.configure_logging(logging.WARNING)
    assert second is root
    assert len(root.handlers) == 1
    assert root.level == logging.WARNING


def test_get_logger_auto_configures_root():
    logger = log_util.get_logger("raindrop_enhancer.tests")

    assert log_util._CONFIGURED is True
    assert logger.name == "raindrop_enhancer.tests"
    assert logging.getLogger().handlers, "configure_logging should attach a handler"


def test_json_formatter_serialises_context_values():
    formatter = log_util.JsonFormatter()
    record = logging.LogRecord(
        name="raindrop_enhancer.test",
        level=logging.INFO,
        pathname=__file__,
        lineno=42,
        msg="processed %s link",
        args=("example",),
        exc_info=None,
    )
    record.path = Path("/tmp/example.html")
    record.generated_at = datetime(2025, 1, 1, tzinfo=timezone.utc)
    record.metadata = {"tags": ["ai", Path("/tmp/tag.txt")]}

    payload = json.loads(formatter.format(record))

    assert payload["message"] == "processed example link"
    assert payload["context"]["path"] == "/tmp/example.html"
    assert payload["context"]["generated_at"] == "2025-01-01T00:00:00Z"
    assert payload["context"]["metadata"] == {"tags": ["ai", "/tmp/tag.txt"]}


def test_resolve_level_rejects_unknown_values():
    assert log_util._resolve_level("info") == logging.INFO
    assert log_util._resolve_level(logging.ERROR) == logging.ERROR
    with pytest.raises(ValueError):
        log_util._resolve_level("verbose")


def test_metrics_recorder_tracks_counters_gauges_and_timers():
    recorder = log_util.MetricsRecorder()

    recorder.increment("retry.attempts", component="raindrop")
    recorder.increment("retry.attempts", value=2, component="raindrop")
    recorder.set_gauge("rate_limit.remaining", 42, mode="full")
    recorder.observe("retry.delay", 0.5, component="raindrop")

    snapshot = recorder.snapshot()

    assert snapshot["counters"]["retry.attempts|component=raindrop"] == 3.0
    assert snapshot["gauges"]["rate_limit.remaining|mode=full"] == 42
    assert snapshot["timers"]["retry.delay|component=raindrop"] == [0.5]

    recorder.clear()
    cleared = recorder.snapshot()
    assert cleared == {"counters": {}, "gauges": {}, "timers": {}}


def test_log_retry_event_emits_structured_warning_and_metrics():
    log_util.configure_logging()
    log_util.get_metrics().clear()
    event = RetryEvent(
        attempt=0,
        delay=1.234,
        retry_after=5.0,
        error=None,
        context={"component": "raindrop", "operation": "list"},
    )

    captured: list[logging.LogRecord] = []

    class _Recorder(logging.Handler):
        def emit(self, record: logging.LogRecord) -> None:  # pragma: no cover - trivial
            captured.append(record)

    handler = _Recorder()
    logger = logging.getLogger("raindrop_enhancer.retry")
    logger.addHandler(handler)
    logger.setLevel(logging.WARNING)

    try:
        log_util.log_retry_event(event)
    finally:
        logger.removeHandler(handler)

    assert any(record.getMessage() == "retry_scheduled" for record in captured)
    snapshot = log_util.get_metrics().snapshot()
    assert snapshot["counters"]["retry.attempts|component=raindrop"] == 1.0
    delays = snapshot["timers"]["retry.delay_seconds|component=raindrop"]
    assert pytest.approx(delays[0], rel=1e-3) == 1.234
