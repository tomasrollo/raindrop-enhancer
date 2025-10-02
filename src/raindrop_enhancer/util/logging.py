"""Logging utilities: provide a configured logger for the project.

This module configures a logger named `raindrop_enhancer` and exposes a
convenience `structured` helper to emit simple dict-based logs when needed.
"""

import logging
import json
from typing import Any, Dict


logger = logging.getLogger("raindrop_enhancer")
if not logger.handlers:
    handler = logging.StreamHandler()
    fmt = logging.Formatter("%(asctime)s %(levelname)s %(name)s: %(message)s")
    handler.setFormatter(fmt)
    logger.addHandler(handler)
    logger.setLevel(logging.INFO)


def structured(msg: str, **kwargs: Any) -> None:
    """Emit a JSON-like structured log to the logger at INFO level."""
    payload: Dict[str, Any] = {"message": msg, **kwargs}
    logger.info(json.dumps(payload))
