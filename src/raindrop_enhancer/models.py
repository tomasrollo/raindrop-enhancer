"""Data models for raindrop_enhancer.

This file will contain dataclasses / TypedDicts for Collection and Raindrop.
"""

from dataclasses import dataclass
from datetime import datetime
from typing import List, Optional, Iterable
from urllib.parse import urlparse
from pathlib import Path
import json


@dataclass
class Collection:
    id: int
    title: str
    count: int
    parent_id: Optional[int]
    color: Optional[str]
    created_at: datetime
    last_updated_at: datetime
    access_level: int

    @staticmethod
    def from_api(payload: dict) -> "Collection":
        """Create Collection from API payload (best-effort).

        Expects fields like `_id`, `title`, `count`, `parent`, `color`, `created`, `lastUpdate`, `access`.
        """
        return Collection(
            id=int(payload.get("_id", 0)),
            title=str(payload.get("title", "")),
            count=int(payload.get("count", 0)),
            parent_id=payload.get("parent"),
            color=payload.get("color"),
            created_at=_parse_ts(payload.get("created")),
            last_updated_at=_parse_ts(payload.get("lastUpdate")),
            access_level=int(payload.get("access", 1)),
        )


@dataclass
class Raindrop:
    id: int
    collection_id: int
    collection_title: str
    title: str
    url: str
    excerpt: Optional[str]
    created_at: datetime
    last_updated_at: datetime
    tags: List[str]
    cover: Optional[str]

    @staticmethod
    def from_api(payload: dict, collection_title: str = "") -> "Raindrop":
        """Create Raindrop from API payload.

        Performs basic validation (URL scheme) and normalization.
        """
        url = payload.get("link") or payload.get("url") or ""
        return Raindrop(
            id=int(payload.get("_id", 0)),
            collection_id=int(payload.get("collectionId", payload.get("collection_id", 0))),
            collection_title=collection_title,
            title=str(payload.get("title", "")),
            url=str(url),
            excerpt=payload.get("excerpt"),
            created_at=_parse_ts(payload.get("created")),
            last_updated_at=_parse_ts(payload.get("lastUpdate")),
            tags=list(payload.get("tags", [])),
            cover=payload.get("cover"),
        )


@dataclass
class RaindropLink:
    raindrop_id: int
    collection_id: int
    collection_title: str
    title: str
    url: str
    created_at: str  # ISO8601
    synced_at: str  # ISO8601
    tags_json: str
    raw_payload: str
    # New content fields
    content_markdown: Optional[str] = None
    content_fetched_at: Optional[str] = None
    content_source: Optional[str] = None

    @staticmethod
    def from_raindrop(r: "Raindrop", synced_at: datetime) -> "RaindropLink":
        return RaindropLink(
            raindrop_id=r.id,
            collection_id=r.collection_id,
            collection_title=r.collection_title,
            title=r.title,
            url=r.url,
            created_at=r.created_at.isoformat(),
            synced_at=synced_at.isoformat(),
            tags_json=json.dumps(sorted(r.tags)),
            raw_payload=json.dumps({"id": r.id, "title": r.title, "url": r.url}),
        )


@dataclass
class LinkCaptureAttempt:
    link_id: int
    attempted_at: datetime
    status: str  # success|skipped|failed
    retry_count: int = 0
    error_type: Optional[str] = None


@dataclass
class ContentCaptureSession:
    started_at: datetime
    completed_at: Optional[datetime]
    links_processed: int
    links_succeeded: int
    links_skipped: int
    links_failed: int
    errors: Optional[List[dict]] = None
    exit_code: int = 0


@dataclass
class SyncState:
    last_cursor_iso: str
    last_run_at: str
    db_version: int
    last_full_refresh: str


@dataclass
class SyncOutcome:
    run_started_at: datetime
    run_finished_at: datetime
    new_links: int
    total_links: int
    was_full_refresh: bool
    db_path: Path
    requests_count: int = 0
    retries_count: int = 0


def _parse_ts(value) -> datetime:
    if value is None:
        return datetime.fromtimestamp(0)
    # API may return int timestamp or ISO string
    try:
        if isinstance(value, (int, float)):
            return datetime.fromtimestamp(int(value))
        return datetime.fromisoformat(str(value))
    except Exception:
        return datetime.fromtimestamp(0)


def is_valid_url(u: str) -> bool:
    try:
        parsed = urlparse(u)
        return parsed.scheme in ("http", "https") and parsed.netloc != ""
    except Exception:
        return False


def filter_active_raindrops(items: Iterable[dict]) -> List["Raindrop"]:
    """Filter API raindrop payloads keeping only active/valid raindrops.

    Rules (from data-model): exclude removed, duplicate, broken; require valid URL.
    """
    result: List[Raindrop] = []
    for payload in items:
        flags = {k: payload.get(k) for k in ("removed", "duplicate", "broken")}
        if any(flags.values()):
            continue
        url = payload.get("link") or payload.get("url") or ""
        if not is_valid_url(url):
            continue
        result.append(Raindrop.from_api(payload))
    return result
