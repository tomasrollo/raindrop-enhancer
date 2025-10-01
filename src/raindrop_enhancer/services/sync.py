"""Sync service: content extraction, enrichment, manual-review flagging."""

import trafilatura
from typing import Dict, Any, Optional


def extract_content(url: str, timeout: int = 10) -> Optional[str]:
    # Fetch and extract main content from a URL using trafilatura
    try:
        downloaded = trafilatura.fetch_url(url, timeout=timeout)
        if not downloaded:
            return None
        return trafilatura.extract(downloaded)
    except Exception:
        return None


def enrich_metadata(link: Dict[str, Any], extracted: Optional[str]) -> Dict[str, Any]:
    # Merge extracted content and flag for manual review if missing
    enriched = dict(link)
    enriched["extracted_content"] = extracted
    enriched["manual_review"] = extracted is None
    return enriched


import json
from pathlib import Path
from ..domain.repositories import Repo
from ..services.tagging import TaggingService
from ..domain.entities import SyncRun, LinkRecord
from datetime import datetime, UTC


def _convert_datetimes(obj):
    if isinstance(obj, dict):
        return {k: _convert_datetimes(v) for k, v in obj.items()}
    elif isinstance(obj, list):
        return [_convert_datetimes(v) for v in obj]
    elif hasattr(obj, "isoformat") and callable(obj.isoformat):
        return obj.isoformat()
    else:
        return obj


def run_full_sync(
    repo: Repo,
    tagging,
    export_path: Path,
    dry_run: bool = False,
    batch_size: int = 20,
    sync_run_id: Optional[str] = None,
) -> dict:
    # Fetch all links (simulate API fetch)
    links = repo.list_links()
    processed = 0
    enriched_links = []
    for i in range(0, len(links), batch_size):
        batch = links[i : i + batch_size]
        urls = [l.url for l in batch]
        extracted = [extract_content(url) for url in urls]
        for link, content in zip(batch, extracted):
            enriched = enrich_metadata(link.model_dump(), content)
            tags = tagging.suggest_tags_for_content(content or "")
            enriched["tags"] = tags
            enriched_links.append(enriched)
            processed += 1
    if not dry_run:
        with export_path.open("w", encoding="utf-8") as f:
            json.dump(_convert_datetimes(enriched_links), f, ensure_ascii=False, indent=2)
    # Update SyncRun
    now = datetime.now(UTC)
    run_id = sync_run_id or f"full-{now.isoformat()}"
    repo.upsert_sync_run(
        SyncRun(
            run_id=run_id,
            started_at=now,
            completed_at=now,
            mode="full",
            links_processed=processed,
        )
    )
    return {"processed": processed, "exported": len(enriched_links), "dry_run": dry_run}


def run_incremental_sync(
    repo: Repo,
    tagging,
    export_path: Path,
    since: datetime,
    dry_run: bool = False,
    batch_size: int = 20,
    sync_run_id: Optional[str] = None,
) -> dict:
    # Fetch only links updated since 'since'
    links = repo.get_links_updated_since(since)
    processed = 0
    enriched_links = []
    for i in range(0, len(links), batch_size):
        batch = links[i : i + batch_size]
        urls = [l.url for l in batch]
        extracted = [extract_content(url) for url in urls]
        for link, content in zip(batch, extracted):
            enriched = enrich_metadata(link.model_dump(), content)
            tags = tagging.suggest_tags_for_content(content or "")
            enriched["tags"] = tags
            enriched_links.append(enriched)
            processed += 1
    if not dry_run:
        with export_path.open("w", encoding="utf-8") as f:
            json.dump(_convert_datetimes(enriched_links), f, ensure_ascii=False, indent=2)
    # Update SyncRun
    now = datetime.now(UTC)
    run_id = sync_run_id or f"incr-{now.isoformat()}"
    repo.upsert_sync_run(
        SyncRun(
            run_id=run_id,
            started_at=now,
            completed_at=now,
            mode="incremental",
            links_processed=processed,
        )
    )
    return {"processed": processed, "exported": len(enriched_links), "dry_run": dry_run}
