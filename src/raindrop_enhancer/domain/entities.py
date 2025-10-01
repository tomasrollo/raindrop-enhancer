"""Domain entity stubs."""

from dataclasses import dataclass
from datetime import datetime
from typing import List


@dataclass
class LinkRecord:
    raindrop_id: int
    url: str
    title: str = ""
    tags: List[str] = None
    created_at: datetime = None
    updated_at: datetime = None


@dataclass
class Collection:
    collection_id: int
    title: str = ""


@dataclass
class TagSuggestion:
    tag: str
    confidence: float = 0.0


@dataclass
class SyncRun:
    run_id: str
    started_at: datetime = None
    completed_at: datetime = None
    mode: str = "full"
    links_processed: int = 0
