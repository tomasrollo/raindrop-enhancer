"""Sync helpers: content extraction, enrichment, and lightweight orchestration.

This module focuses on content fetch and enrichment helpers used by the
sync orchestration in later tasks. It prefers `trafilatura` when available
for higher-quality extraction but falls back to a simple requests-based
extractor.
"""

from typing import Dict, Any, Optional, List
from hashlib import sha256
from pathlib import Path
from datetime import datetime, timezone
import uuid

import requests

try:
    import trafilatura

    _HAS_TRAFILATURA = True
except Exception:
    _HAS_TRAFILATURA = False

from raindrop_enhancer.util.logging import logger, structured


def fetch_content(url: str, timeout: int = 15) -> Optional[str]:
    """Fetch URL content and extract main text. Returns None on failure."""
    try:
        resp = requests.get(url, timeout=timeout)
        resp.raise_for_status()
        html = resp.text
        if _HAS_TRAFILATURA:
            text = trafilatura.extract(html) or ""
        else:
            # very small fallback: strip tags naively
            text = _naive_text_extract(html)
        return text.strip() if text else None
    except Exception:
        return None


def _naive_text_extract(html: str) -> str:
    # Remove script/style blocks crudely and then tags
    import re

    s = re.sub(r"(?s)<(script|style).*?>.*?</\1>", " ", html)
    s = re.sub(r"<[^>]+>", " ", s)
    s = re.sub(r"\s+", " ", s)
    return s.strip()


def compute_content_hash(content: str) -> str:
    return sha256(content.encode("utf-8")).hexdigest()


def enrich_link(link: Dict[str, Any]) -> Dict[str, Any]:
    """Given a link dict with 'url', fetch content, compute hash and flag manual_review.

    Adds keys: `content`, `content_hash`, `manual_review` (bool).
    """
    url = link.get("url")
    content = None
    if url:
        content = fetch_content(url)

    if content:
        link["content"] = content
        link["content_hash"] = compute_content_hash(content)
        link["manual_review"] = False if len(content) > 200 else True
    else:
        link["content"] = None
        link["content_hash"] = None
        link["manual_review"] = True

    return link


def run_full_sync(
    repo,
    client,
    tagging_adapter=None,
    export_path: Optional[Path] = None,
    dry_run: bool = False,
    perpage: int = 50,
):
    """Minimal orchestration for a full sync.

    - Uses `client` to list collections and raindrops
    - Enriches content, upserts into `repo` and writes a JSON export
    Returns a summary dict with processed counts and rate-limit telemetry.
    """
    if repo is None or client is None:
        return {"processed": 0, "error": "missing dependencies"}

    run_id = str(uuid.uuid4())
    started_at = datetime.now(timezone.utc)

    processed = 0
    export_items = []

    collections = client.list_collections() or {}
    for col in collections.get("items", []):
        col_id = col.get("id") or col.get("collection_id")
        # iterate pages
        for page in client.list_raindrops(col_id, perpage=perpage):
            items = page.get("items") or []
            for rd in items:
                # Map minimal raindrop fields
                link = {
                    "url": rd.get("link") or rd.get("url"),
                    "title": rd.get("title"),
                    "description": rd.get("excerpt") or rd.get("note"),
                }
                enriched = enrich_link(link)

                # Build LinkRecord entity if repo expects domain model
                try:
                    from raindrop_enhancer.domain.entities import LinkRecord

                    lr = LinkRecord(
                        raindrop_id=str(rd.get("id")),
                        url=str(enriched.get("url") or ""),
                        title=str(enriched.get("title") or ""),
                        description=str(enriched.get("description") or ""),
                        content_hash=enriched.get("content_hash"),
                        status=(
                            "processed"
                            if not enriched.get("manual_review")
                            else "manual_review"
                        ),
                    )
                    repo.upsert_link(lr)
                except Exception:
                    # If repo doesn't accept model, skip persistence but continue
                    pass

                export_items.append({"raindrop_id": rd.get("id"), **enriched})
                processed += 1

    # Tagging: batch through tagging_adapter if provided
    if tagging_adapter and export_items:
        contents = [it.get("content") or "" for it in export_items]
        try:
            tag_lists: List[List[dict]] = tagging_adapter.suggest_for_batch(contents)
            for item, tags in zip(export_items, tag_lists):
                item["tags_suggested"] = tags
                try:
                    repo.upsert_tag_suggestions(item.get("raindrop_id"), tags)
                except Exception:
                    logger.exception("Failed to persist tag suggestions")
        except Exception:
            logger.exception("Tagging adapter failed")

    # write export
    if not dry_run and export_path:
        try:
            from raindrop_enhancer.services.storage import write_export

            write_export(Path(export_path), export_items)
        except Exception:
            logger.exception("Failed to write export")

    completed_at = datetime.now(timezone.utc)
    duration = (completed_at - started_at).total_seconds()

    result = {
        "run_id": run_id,
        "started_at": started_at.isoformat(),
        "completed_at": completed_at.isoformat(),
        "duration_seconds": duration,
        "processed": processed,
        "export_count": len(export_items),
        "rate_limit": getattr(client, "last_rate_limit", None),
    }

    # Emit structured summary
    try:
        structured(
            "sync.complete",
            run_id=run_id,
            processed=processed,
            export_count=len(export_items),
            duration_seconds=duration,
            rate_limit=getattr(client, "last_rate_limit", None),
        )
    except Exception:
        logger.info("sync complete", extra={"run_id": run_id, "processed": processed})

    # Persist SyncRun summary if repo supports it
    try:
        repo.upsert_sync_run(
            {
                "run_id": run_id,
                "started_at": started_at,
                "completed_at": completed_at,
                "mode": "full",
                "processed": processed,
                "export_count": len(export_items),
                "rate_limit": getattr(client, "last_rate_limit", None),
                "output_path": str(export_path) if export_path is not None else None,
            }
        )
    except Exception:
        logger.exception("Failed to persist SyncRun summary")

    return result


def run_incremental_sync():
    return {"processed": 0}
