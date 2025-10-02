"""Structured logging utilities and lightweight metrics recorder."""

from __future__ import annotations

import json
import logging
import sys
from dataclasses import dataclass, field
from datetime import datetime, timezone
from pathlib import Path
from typing import Any, Iterable, Mapping, MutableMapping

from raindrop_enhancer.util.retry import RetryEvent

LOGGER_NAME = "raindrop_enhancer"
STANDARD_LOG_FIELDS = {
    "name",
    "msg",
    "args",
    "levelname",
    "levelno",
    "pathname",
    "filename",
    "module",
    "exc_info",
    "exc_text",
    "stack_info",
    "lineno",
    "funcName",
    "created",
    "msecs",
    "relativeCreated",
    "thread",
    "threadName",
    "processName",
    "process",
}


class JsonFormatter(logging.Formatter):
    """Format log records as structured JSON."""

    def format(
        self, record: logging.LogRecord
    ) -> str:  # pragma: no cover - exercised via CLI
        payload: dict[str, Any] = {
            "timestamp": datetime.fromtimestamp(record.created, tz=timezone.utc)
            .isoformat()
            .replace("+00:00", "Z"),
            "level": record.levelname.lower(),
            "logger": record.name,
            "message": record.getMessage(),
        }

        context: dict[str, Any] = {}
        for key, value in record.__dict__.items():
            if key in STANDARD_LOG_FIELDS:
                continue
            context[key] = _serialize(value)

        if context:
            payload["context"] = context

        if record.exc_info:
            payload["exception"] = self.formatException(record.exc_info)
        if record.stack_info:
            payload["stack"] = self.formatStack(record.stack_info)

        return json.dumps(payload, separators=(",", ":"))


_CONFIGURED = False


def configure_logging(level: int | str = logging.INFO) -> logging.Logger:
    """Configure application-wide logging with JSON formatting."""

    global _CONFIGURED

    resolved_level = _resolve_level(level)
    root = logging.getLogger()

    if _CONFIGURED:
        root.setLevel(resolved_level)
        return root

    root.handlers.clear()
    handler = logging.StreamHandler(stream=sys.stderr)
    handler.setFormatter(JsonFormatter())
    root.addHandler(handler)
    root.setLevel(resolved_level)

    logging.getLogger("urllib3").setLevel(logging.WARNING)
    logging.getLogger("requests").setLevel(logging.WARNING)

    _CONFIGURED = True
    return root


def get_logger(name: str | None = None) -> logging.Logger:
    """Return a logger configured for structured output."""

    if not _CONFIGURED:
        configure_logging()
    return logging.getLogger(name or LOGGER_NAME)


def _resolve_level(level: int | str) -> int:
    if isinstance(level, int):
        return level
    value = logging.getLevelName(str(level).upper())
    if isinstance(value, int):
        return value
    raise ValueError(f"Unknown log level: {level}")


def _serialize(value: Any) -> Any:
    if isinstance(value, (str, int, float, bool)) or value is None:
        return value
    if isinstance(value, datetime):
        return value.astimezone(timezone.utc).isoformat().replace("+00:00", "Z")
    if isinstance(value, Path):
        return str(value)
    if isinstance(value, Mapping):
        return {key: _serialize(inner) for key, inner in value.items()}
    if isinstance(value, Iterable) and not isinstance(value, (bytes, bytearray)):
        return [_serialize(item) for item in value]
    return str(value)


@dataclass(slots=True)
class MetricsRecorder:
    """Minimal in-process metrics aggregator for counters and gauges."""

    counters: MutableMapping[str, float] = field(default_factory=dict)
    gauges: MutableMapping[str, float] = field(default_factory=dict)
    timers: MutableMapping[str, list[float]] = field(default_factory=dict)

    def increment(self, name: str, value: float = 1.0, **labels: Any) -> None:
        key = _metric_key(name, labels)
        self.counters[key] = self.counters.get(key, 0.0) + value

    def set_gauge(self, name: str, value: float, **labels: Any) -> None:
        key = _metric_key(name, labels)
        self.gauges[key] = value

    def observe(self, name: str, value: float, **labels: Any) -> None:
        key = _metric_key(name, labels)
        bucket = self.timers.setdefault(key, [])
        bucket.append(value)

    def snapshot(self) -> dict[str, Any]:
        return {
            "counters": dict(self.counters),
            "gauges": dict(self.gauges),
            "timers": {key: list(values) for key, values in self.timers.items()},
        }

    def clear(self) -> None:
        self.counters.clear()
        self.gauges.clear()
        self.timers.clear()


def _metric_key(name: str, labels: Mapping[str, Any]) -> str:
    if not labels:
        return name
    parts = [name]
    for key in sorted(labels):
        value = labels[key]
        parts.append(f"{key}={value}")
    return "|".join(parts)


_METRICS = MetricsRecorder()


def get_metrics() -> MetricsRecorder:
    """Return the singleton metrics recorder."""

    return _METRICS


def log_retry_event(event: RetryEvent) -> None:
    """Emit structured telemetry for retry/backoff attempts."""

    logger = get_logger(f"{LOGGER_NAME}.retry")
    payload = {
        "attempt": event.attempt + 1,
        "delay_seconds": round(event.delay, 3),
        "retry_after": event.retry_after,
        "context": event.context,
    }
    logger.warning("retry_scheduled", extra={"event": "retry", **payload})

    metrics = get_metrics()
    metrics.increment(
        "retry.attempts", component=event.context.get("component", "unknown")
    )
    metrics.observe(
        "retry.delay_seconds",
        event.delay,
        component=event.context.get("component", "unknown"),
    )
