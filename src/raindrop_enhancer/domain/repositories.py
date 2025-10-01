"""SQLite repository implementation for Raindrop Enhancer."""

from __future__ import annotations

from contextlib import contextmanager
from datetime import datetime, timezone
from pathlib import Path
from typing import Any, Iterator, Sequence, cast

from sqlmodel import Session, SQLModel, create_engine, select

from .entities import Collection, LinkRecord, SyncRun, TagSuggestion


class SQLiteRepository:
    """Persistence layer backed by SQLite."""

    def __init__(self, db_path: Path | str) -> None:
        self.database_path = Path(db_path)
        self._engine = create_engine(
            f"sqlite:///{self.database_path}",
            connect_args={"check_same_thread": False},
            pool_pre_ping=True,
        )

    def setup(self) -> None:
        """Create database schema and enable recommended pragmas."""

        self.database_path.parent.mkdir(parents=True, exist_ok=True)
        SQLModel.metadata.create_all(self._engine)
        with self._engine.connect() as connection:
            connection.exec_driver_sql("PRAGMA foreign_keys=ON;")
            connection.exec_driver_sql("PRAGMA journal_mode=WAL;")

    @contextmanager
    def session(self) -> Iterator[Session]:
        session = Session(self._engine)
        try:
            yield session
        finally:
            session.close()

    # ------------------------------------------------------------------
    # Link operations
    # ------------------------------------------------------------------
    def upsert_link(
        self,
        link: LinkRecord,
        *,
        collections: Sequence[Collection],
        tag_suggestions: Sequence[dict],
    ) -> None:
        """Insert or update a link, its collections, and tag suggestions."""

        with self.session() as session:
            existing = session.get(LinkRecord, link.raindrop_id)
            link_data = _link_payload(link)
            if existing is None:
                existing = LinkRecord(**link_data)
            else:
                for field, value in link_data.items():
                    setattr(existing, field, value)

            session.add(existing)

            # Upsert collections and attach relationship
            attached_collections: list[Collection] = []
            for incoming in collections:
                data = _collection_payload(incoming)
                stored = session.get(Collection, data["collection_id"])
                if stored is None:
                    stored = Collection(**data)
                else:
                    for field, value in data.items():
                        setattr(stored, field, value)
                session.add(stored)
                attached_collections.append(stored)

            existing.collections = attached_collections

            # Replace tag suggestions atomically
            replacements: list[TagSuggestion] = []
            for suggestion in tag_suggestions:
                replacements.append(
                    TagSuggestion(
                        raindrop_id=existing.raindrop_id,
                        tag=suggestion["tag"],
                        confidence=float(suggestion.get("confidence", 0.0)),
                        source=suggestion.get("source", "metadata"),
                        suggested_at=suggestion.get(
                            "suggested_at", datetime.now(tz=timezone.utc)
                        ),
                    )
                )
            existing.tag_suggestions = replacements

            session.commit()

    def get_link(self, raindrop_id: int) -> LinkRecord | None:
        """Fetch a link by Raindrop ID including relationships."""

        with self.session() as session:
            record = session.get(LinkRecord, raindrop_id)
            if record is None:
                return None
            _load_relationships(record)
            return record

    def get_tag_suggestions(self, raindrop_id: int) -> list[dict]:
        with self.session() as session:
            statement = select(TagSuggestion).where(
                TagSuggestion.raindrop_id == raindrop_id
            )
            results = session.exec(statement).all()
            suggestions: list[dict] = []
            for item in results:
                suggestions.append(
                    {
                        "tag": item.tag,
                        "confidence": item.confidence,
                        "source": item.source,
                        "suggested_at": item.suggested_at,
                    }
                )
            return suggestions

    def list_pending_links(self, *, limit: int | None = None) -> list[LinkRecord]:
        with self.session() as session:
            statement = (
                select(LinkRecord)
                .where(LinkRecord.status == "pending")
                .order_by(cast(Any, LinkRecord).updated_at)
            )
            if limit is not None:
                statement = statement.limit(limit)
            records = list(session.exec(statement).all())
            for record in records:
                _load_relationships(record)
            return records

    def list_all_links(self) -> list[LinkRecord]:
        """Return all links with eager loaded relationships."""

        with self.session() as session:
            records = list(session.exec(select(LinkRecord)).all())
            for record in records:
                _load_relationships(record)
                session.expunge(record)
            return records

    def get_collection(self, collection_id: int) -> Collection | None:
        with self.session() as session:
            record = session.get(Collection, collection_id)
            if record is None:
                return None
            session.expunge(record)
            return record

    # ------------------------------------------------------------------
    # Sync run audit log operations
    # ------------------------------------------------------------------
    def record_sync_run(self, run: SyncRun) -> None:
        with self.session() as session:
            existing = session.get(SyncRun, run.run_id)
            payload = _sync_run_payload(run)
            if existing is None:
                existing = SyncRun(**payload)
            else:
                for field, value in payload.items():
                    setattr(existing, field, value)
            session.add(existing)
            session.commit()

    def list_sync_runs(self, *, limit: int | None = None) -> list[SyncRun]:
        with self.session() as session:
            statement = select(SyncRun).order_by(cast(Any, SyncRun).started_at.desc())
            if limit is not None:
                statement = statement.limit(limit)
            runs = list(session.exec(statement).all())
            for run in runs:
                session.expunge(run)
            return runs


# ----------------------------------------------------------------------
# Helper utilities
# ----------------------------------------------------------------------


def _link_payload(link: LinkRecord) -> dict:
    return {
        "raindrop_id": link.raindrop_id,
        "url": link.url,
        "title": link.title,
        "description": link.description,
        "created_at": link.created_at,
        "updated_at": link.updated_at,
        "processed_at": link.processed_at,
        "content_hash": link.content_hash,
        "status": link.status,
        "llm_version": link.llm_version,
    }


def _collection_payload(collection: Collection) -> dict:
    return {
        "collection_id": collection.collection_id,
        "title": collection.title,
        "color": getattr(collection, "color", None),
        "parent_id": getattr(collection, "parent_id", None),
        "last_sync_timestamp": getattr(collection, "last_sync_timestamp", None),
    }


def _sync_run_payload(run: SyncRun) -> dict:
    return {
        "run_id": run.run_id,
        "started_at": run.started_at,
        "completed_at": run.completed_at,
        "mode": run.mode,
        "links_processed": run.links_processed,
        "links_skipped": run.links_skipped,
        "manual_review": run.manual_review,
        "failures": run.failures,
        "output_path": run.output_path,
        "status_code": run.status_code,
        "rate_limit_remaining": run.rate_limit_remaining,
        "rate_limit_reset": run.rate_limit_reset,
    }


def _load_relationships(record: LinkRecord) -> None:
    # Access relationships to ensure they are loaded before detaching
    _ = list(record.collections)
    _ = list(record.tag_suggestions)
