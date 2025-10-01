"""Sync orchestration for the Raindrop Enhancer CLI."""

from __future__ import annotations

import hashlib
import shutil
from dataclasses import dataclass, field
from datetime import datetime, timezone
from pathlib import Path
from typing import Any, Callable, Iterable, Sequence
from uuid import uuid4

from raindrop_enhancer.domain.entities import Collection, LinkRecord, SyncRun
from raindrop_enhancer.domain.repositories import SQLiteRepository
from raindrop_enhancer.services.storage import write_export

SCHEMA_VERSION = "1.0"
EXPORT_DIRNAME = "exports"


# ---------------------------------------------------------------------------
# Public entry points
# ---------------------------------------------------------------------------


def run_full_sync(
    *,
    data_dir: Path,
    api_client,
    tagging_service,
    content_fetcher: Callable[[str], str],
    now: Callable[[], datetime],
    collection_ids: Sequence[int] | None = None,
    batch_size: int = 50,
    dry_run: bool = False,
) -> dict[str, Any]:
    """Execute a full synchronisation across all collections."""

    return _run_sync(
        mode="full",
        data_dir=data_dir,
        api_client=api_client,
        tagging_service=tagging_service,
        content_fetcher=content_fetcher,
        now=now,
        collection_ids=collection_ids,
        since_override=None,
        batch_size=batch_size,
        dry_run=dry_run,
    )


def run_incremental_sync(
    *,
    data_dir: Path,
    api_client,
    tagging_service,
    content_fetcher: Callable[[str], str],
    now: Callable[[], datetime],
    collection_ids: Sequence[int] | None = None,
    since: datetime | str | None = None,
    batch_size: int = 50,
    dry_run: bool = False,
) -> dict[str, Any]:
    """Execute an incremental synchronisation using stored timestamps."""

    return _run_sync(
        mode="incremental",
        data_dir=data_dir,
        api_client=api_client,
        tagging_service=tagging_service,
        content_fetcher=content_fetcher,
        now=now,
        collection_ids=collection_ids,
        since_override=since,
        batch_size=batch_size,
        dry_run=dry_run,
    )


def run_reprocess(
    *,
    data_dir: Path,
    raindrop_id: int,
    api_client,
    tagging_service,
    content_fetcher: Callable[[str], str],
    now: Callable[[], datetime],
    dry_run: bool = False,
) -> dict[str, Any]:
    """Re-run enrichment for a specific Raindrop link."""

    repo = _prepare_repository(data_dir)
    context = SyncExecution(
        mode="reprocess",
        data_dir=data_dir,
        repo=repo,
        now=now,
        dry_run=dry_run,
    )

    existing = repo.get_link(raindrop_id)
    previous_status = existing.status if existing else "missing"

    item, headers = api_client.fetch_raindrop(raindrop_id)
    context.update_rate_limit(headers)

    collection_meta = {
        "id": item.get("collectionId") or item.get("collection", {}).get("id"),
        "title": item.get("collection", {}).get("title", ""),
        "color": item.get("collection", {}).get("color"),
        "lastUpdate": item.get("lastUpdate"),
    }

    pending = _build_pending_link(
        item,
        collection_meta,
        repo=repo,
        content_fetcher=content_fetcher,
        context=context,
    )

    if pending is None:
        raise RuntimeError(f"Raindrop {raindrop_id} is unchanged; nothing to reprocess")

    tagging_result = (
        tagging_service.generate(_documents_for([pending]))
        if pending.content is not None
        else {"suggestions": {}, "failures": {}}
    )

    processed_payload = _apply_tagging_results(
        [pending],
        tagging_result,
        context=context,
        tagging_service=tagging_service,
    )

    export_path = _finalise_run(context, processed_payload)

    summary = _build_summary(context, export_path)
    summary.update(
        {
            "previous_status": previous_status,
            "new_status": processed_payload[0]["record"].status,
            "new_tags": processed_payload[0]["tags"],
        }
    )
    return summary


def status_summary(*, data_dir: Path, limit: int = 10) -> list[dict[str, Any]]:
    """Return recent sync runs and their telemetry."""

    db_path = data_dir / "raindrop.sqlite"
    if not db_path.exists():
        return []

    repo = SQLiteRepository(db_path)
    runs = repo.list_sync_runs(limit=limit)
    summary: list[dict[str, Any]] = []
    for run in runs:
        summary.append(
            {
                "run_id": run.run_id,
                "mode": run.mode,
                "started_at": run.started_at.isoformat(),
                "completed_at": run.completed_at.isoformat()
                if run.completed_at
                else None,
                "links_processed": run.links_processed,
                "links_skipped": run.links_skipped,
                "manual_review": run.manual_review,
                "failures": run.failures,
                "rate_limit_remaining": run.rate_limit_remaining,
                "rate_limit_reset": run.rate_limit_reset,
                "export_path": run.output_path,
            }
        )
    return summary


# ---------------------------------------------------------------------------
# Internal execution helpers
# ---------------------------------------------------------------------------


@dataclass(slots=True)
class PendingLink:
    record: LinkRecord
    collections: list[Collection]
    content: str | None
    failure: str | None = None


@dataclass(slots=True)
class SyncExecution:
    mode: str
    data_dir: Path
    repo: SQLiteRepository
    now: Callable[[], datetime]
    dry_run: bool
    run_id: str = field(default_factory=lambda: uuid4().hex)
    processed: int = 0
    skipped: int = 0
    manual_review: int = 0
    failures: list[dict[str, Any]] = field(default_factory=list)
    rate_limit_remaining: int | None = None
    rate_limit_reset: int | None = None
    started_at: datetime = field(init=False)
    completed_at: datetime | None = None

    def __post_init__(self) -> None:
        self.started_at = self.timestamp()

    def timestamp(self) -> datetime:
        stamp = self.now()
        if stamp.tzinfo is None:
            stamp = stamp.replace(tzinfo=timezone.utc)
        return stamp.astimezone(timezone.utc)

    def update_rate_limit(self, headers: dict[str, str]) -> None:
        remaining = headers.get("X-RateLimit-Remaining")
        reset = headers.get("X-RateLimit-Reset")
        if remaining:
            try:
                self.rate_limit_remaining = int(remaining)
            except ValueError:
                pass
        if reset:
            try:
                self.rate_limit_reset = int(reset)
            except ValueError:
                pass

    def record_failure(self, raindrop_id: int, reason: str) -> None:
        self.manual_review += 1
        self.failures.append({"link_id": raindrop_id, "reason": reason})

    def mark_completed(self) -> None:
        self.completed_at = self.timestamp()


def _run_sync(
    *,
    mode: str,
    data_dir: Path,
    api_client,
    tagging_service,
    content_fetcher: Callable[[str], str],
    now: Callable[[], datetime],
    collection_ids: Sequence[int] | None,
    since_override: datetime | str | None,
    batch_size: int,
    dry_run: bool,
) -> dict[str, Any]:
    repo = _prepare_repository(data_dir)
    context = SyncExecution(
        mode=mode,
        data_dir=data_dir,
        repo=repo,
        now=now,
        dry_run=dry_run,
    )

    collections, headers = api_client.list_collections()
    context.update_rate_limit(headers)

    filter_set = set(collection_ids) if collection_ids else None
    pending_links: list[PendingLink] = []

    for collection in collections:
        collection_id = collection.get("id") or collection.get("_id")
        if not isinstance(collection_id, int):
            continue
        if filter_set and collection_id not in filter_set:
            continue

        last_update_param = _compute_last_update(
            mode=mode,
            repo=repo,
            collection_id=collection_id,
            since_override=since_override,
        )

        try:
            items, item_headers = api_client.list_raindrops(
                collection_id,
                last_update=last_update_param,
                per_page=batch_size,
            )
        except TypeError:
            if last_update_param is None:
                items, item_headers = api_client.list_raindrops(collection_id)
            else:
                items, item_headers = api_client.list_raindrops(
                    collection_id, last_update=last_update_param
                )
        context.update_rate_limit(item_headers)

        if not items:
            continue

        for item in items:
            pending = _build_pending_link(
                item,
                collection,
                repo=repo,
                content_fetcher=content_fetcher,
                context=context,
                incremental=(mode == "incremental"),
            )
            if pending is None:
                continue
            pending_links.append(pending)

    tagging_result = (
        tagging_service.generate(_documents_for(pending_links))
        if pending_links
        else {"suggestions": {}, "failures": {}}
    )

    processed_payload = _apply_tagging_results(
        pending_links,
        tagging_result,
        context=context,
        tagging_service=tagging_service,
    )

    export_path = _finalise_run(context, processed_payload)
    return _build_summary(context, export_path)


def _prepare_repository(data_dir: Path) -> SQLiteRepository:
    db_path = data_dir / "raindrop.sqlite"
    repository = SQLiteRepository(db_path)
    repository.setup()
    return repository


def _compute_last_update(
    *,
    mode: str,
    repo: SQLiteRepository,
    collection_id: int,
    since_override: datetime | str | None,
) -> str | None:
    if mode != "incremental":
        return None

    if isinstance(since_override, datetime):
        return _format_timestamp(since_override)
    if isinstance(since_override, str):
        return since_override

    existing = repo.get_collection(collection_id)
    if existing and existing.last_sync_timestamp:
        return _format_timestamp(existing.last_sync_timestamp)
    return None


def _build_pending_link(
    item: dict,
    collection_meta: dict,
    *,
    repo: SQLiteRepository,
    content_fetcher: Callable[[str], str],
    context: SyncExecution,
    incremental: bool = False,
) -> PendingLink | None:
    raindrop_id = int(item["id"])
    updated_at = _parse_timestamp(item.get("lastUpdate"))

    existing = repo.get_link(raindrop_id)
    if incremental and existing is not None and existing.updated_at is not None:
        existing_updated = existing.updated_at
        if existing_updated.tzinfo is None:
            existing_updated = existing_updated.replace(tzinfo=timezone.utc)
        if existing_updated >= updated_at:
            context.skipped += 1
            return None

    link = _create_link_record(item, updated_at)

    collection = _create_collection(collection_meta)

    try:
        content = content_fetcher(link.url)
    except Exception as exc:  # pragma: no cover - exercised in integration tests
        link.status = "manual_review"
        link.processed_at = None
        link.content_hash = None
        return PendingLink(
            link, [collection], None, failure=str(exc) or exc.__class__.__name__
        )

    link.content_hash = hashlib.sha256(content.encode("utf-8")).hexdigest()
    return PendingLink(link, [collection], content)


def _documents_for(pending_links: Iterable[PendingLink]) -> list[dict]:
    documents: list[dict] = []
    for pending in pending_links:
        if pending.content is None:
            continue
        documents.append(
            {
                "raindrop_id": pending.record.raindrop_id,
                "url": pending.record.url,
                "title": pending.record.title,
                "content": pending.content,
                "created_at": pending.record.created_at,
            }
        )
    return documents


def _apply_tagging_results(
    pending_links: list[PendingLink],
    tagging_result: dict,
    *,
    context: SyncExecution,
    tagging_service,
) -> list[dict[str, Any]]:
    suggestions_map = tagging_result.get("suggestions", {})
    tagging_failures = tagging_result.get("failures", {})
    processed: list[dict[str, Any]] = []

    for pending in pending_links:
        link = pending.record
        raindrop_id = link.raindrop_id
        link_suggestions = suggestions_map.get(raindrop_id, [])

        if pending.failure is not None:
            context.record_failure(raindrop_id, pending.failure)
            link.status = "manual_review"
            link.processed_at = None
            tag_payload: list[dict] = []
        elif raindrop_id in tagging_failures:
            context.record_failure(raindrop_id, tagging_failures[raindrop_id])
            link.status = "manual_review"
            link.processed_at = None
            tag_payload = []
        else:
            link.status = "processed"
            link.processed_at = context.timestamp()
            context.processed += 1
            tag_payload = list(link_suggestions)

        if not context.dry_run:
            context.repo.upsert_link(
                link,
                collections=pending.collections,
                tag_suggestions=tag_payload,
            )

        processed.append({"record": link, "tags": tag_payload})

    context.mark_completed()
    return processed


def _finalise_run(context: SyncExecution, processed_payload: list[dict]) -> Path | None:
    export_path: Path | None = None
    if not context.dry_run:
        export_path = _write_export(context)
        _record_sync_run(context, export_path)
    else:
        context.mark_completed()
    return export_path


def _write_export(context: SyncExecution) -> Path:
    export_dir = context.data_dir / EXPORT_DIRNAME
    export_dir.mkdir(parents=True, exist_ok=True)
    export_path = export_dir / f"sync-{context.run_id}.json"
    payload = _export_payload(context)
    write_export(export_path, payload)

    latest_path = export_dir / "latest.json"
    if latest_path != export_path:
        shutil.copyfile(export_path, latest_path)

    return export_path


def _export_payload(context: SyncExecution) -> dict[str, Any]:
    links = context.repo.list_all_links()
    entries: list[dict[str, Any]] = []
    for link in links:
        entries.append(
            {
                "raindrop_id": link.raindrop_id,
                "url": link.url,
                "title": link.title,
                "description": link.description,
                "created_at": link.created_at.isoformat(),
                "updated_at": link.updated_at.isoformat(),
                "processed_at": link.processed_at.isoformat()
                if link.processed_at
                else None,
                "status": link.status,
                "collections": [
                    {
                        "id": collection.collection_id,
                        "title": collection.title,
                    }
                    for collection in link.collections
                ],
                "tags": [
                    {
                        "tag": suggestion.tag,
                        "confidence": suggestion.confidence,
                        "source": suggestion.source,
                        "suggested_at": suggestion.suggested_at.isoformat(),
                    }
                    for suggestion in link.tag_suggestions
                ],
            }
        )

    return {
        "schema_version": SCHEMA_VERSION,
        "generated_at": context.completed_at.isoformat()
        if context.completed_at
        else context.timestamp().isoformat(),
        "links": entries,
    }


def _record_sync_run(context: SyncExecution, export_path: Path | None) -> None:
    run = SyncRun(
        run_id=context.run_id,
        started_at=context.started_at,
        completed_at=context.completed_at,
        mode=context.mode,
        links_processed=context.processed,
    )
    run.links_skipped = context.skipped
    run.manual_review = context.manual_review
    run.failures = len(context.failures)
    run.output_path = str(export_path) if export_path else None
    run.rate_limit_remaining = context.rate_limit_remaining
    run.rate_limit_reset = context.rate_limit_reset
    context.repo.record_sync_run(run)


def _build_summary(context: SyncExecution, export_path: Path | None) -> dict[str, Any]:
    duration_seconds = 0.0
    if context.completed_at is not None:
        duration_seconds = (context.completed_at - context.started_at).total_seconds()

    return {
        "run_id": context.run_id,
        "mode": context.mode,
        "processed": context.processed,
        "skipped": context.skipped,
        "manual_review": context.manual_review,
        "failures": context.failures,
        "export_path": str(export_path) if export_path else None,
        "timestamp": context.completed_at.isoformat()
        if context.completed_at
        else context.started_at.isoformat(),
        "duration_seconds": duration_seconds,
        "rate_limit_remaining": context.rate_limit_remaining,
        "rate_limit_reset": context.rate_limit_reset,
    }


def _create_link_record(item: dict, updated_at: datetime) -> LinkRecord:
    created_at = _parse_timestamp(item.get("created"))
    link = LinkRecord(
        raindrop_id=int(item["id"]),
        url=item.get("link") or item.get("url", ""),
        title=item.get("title", ""),
        created_at=created_at,
        updated_at=updated_at,
    )
    link.description = item.get("excerpt") or item.get("note")
    link.status = "pending"
    link.processed_at = None
    link.llm_version = item.get("llm_version")
    return link


def _create_collection(payload: dict) -> Collection:
    collection_id = payload.get("id") or payload.get("_id")
    if collection_id is None:
        raise ValueError("collection payload missing identifier")

    collection = Collection(
        collection_id=int(collection_id),
        title=payload.get("title", ""),
    )
    collection.color = payload.get("color")
    collection.parent_id = payload.get("parentId")
    collection.last_sync_timestamp = _parse_optional_timestamp(
        payload.get("lastUpdate")
    )
    return collection


def _parse_timestamp(value: str | None) -> datetime:
    if value is None:
        return datetime.now(timezone.utc)
    return datetime.fromisoformat(value.replace("Z", "+00:00"))


def _parse_optional_timestamp(value: str | None) -> datetime | None:
    if value is None:
        return None
    return _parse_timestamp(value)


def _format_timestamp(value: datetime) -> str:
    stamp = value.astimezone(timezone.utc)
    return stamp.isoformat().replace("+00:00", "Z")
