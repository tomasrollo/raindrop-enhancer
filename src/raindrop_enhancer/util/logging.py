"""Structured logging and metrics for raindrop_enhancer."""

import logging
import json
import sys
from collections import defaultdict


class JsonFormatter(logging.Formatter):
    def format(self, record):
        log_record = {
            "level": record.levelname,
            "time": self.formatTime(record, self.datefmt),
            "name": record.name,
            "msg": record.getMessage(),
        }
        return json.dumps(log_record)


def setup_logging(json_logs: bool = False, level: int = logging.INFO):
    logger = logging.getLogger("raindrop_enhancer")
    logger.setLevel(level)
    handler = logging.StreamHandler(sys.stdout)
    if json_logs:
        handler.setFormatter(JsonFormatter())
    else:
        handler.setFormatter(logging.Formatter("[%(levelname)s] %(name)s: %(message)s"))
    logger.handlers = [handler]
    return logger


logger = setup_logging()

# Simple in-memory metrics
_metrics = defaultdict(int)


def inc_metric(name: str, value: int = 1):
    _metrics[name] += value


def get_metrics():
    return dict(_metrics)
