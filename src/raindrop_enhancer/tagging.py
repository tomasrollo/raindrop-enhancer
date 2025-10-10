from __future__ import annotations

from dataclasses import dataclass
from typing import Literal, Optional


@dataclass
class GeneratedTag:
    value: str
    confidence: float = 1.0
    source: Literal["dspy", "manual"] = "dspy"


@dataclass
class TagGenerationMetadata:
    generated_at: str  # ISO8601 UTC
    model: str
    tokens_used: Optional[int] = None
    status: str = "success"  # or 'failed'
    failure_reason: Optional[str] = None
