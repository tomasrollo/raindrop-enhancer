"""Repository implementation for SQLite using SQLModel.

This file provides a small convenience wrapper used by unit tests and the
sync implementation. It intentionally keeps the API lightweight: `setup()`
initialises the engine and tables, and `upsert_link()` performs an insert-or-
update using SQLModel session semantics. Additional helpers expose common
queries used by the service layer.
"""

from typing import Optional, Iterable
from pathlib import Path

from datetime import datetime, timezone

from sqlmodel import create_engine, SQLModel, Session, select

from raindrop_enhancer.domain import entities


class Repo:
    def __init__(self, path: str):
        # allow in-memory sqlite for tests
        self.path = path
        self.db_url = f"sqlite:///{path}"
        self.engine = None

    def setup(self):
        """Create the SQLite database file, enable WAL, and create tables."""
        db_path = Path(self.path)
        if db_path.parent and str(db_path.parent) != "":
            db_path.parent.mkdir(parents=True, exist_ok=True)

        # Create engine and enable WAL mode
        self.engine = create_engine(
            self.db_url, connect_args={"check_same_thread": False}
        )
        with self.engine.connect() as conn:
            # Use driver-level exec to run PRAGMA without SQLModel/SQLAlchemy typing issues
            conn.exec_driver_sql("PRAGMA journal_mode=WAL;")
            conn.commit()

        SQLModel.metadata.create_all(self.engine)

    def ensure_setup(self):
        if self.engine is None:
            raise RuntimeError("Repo not setup. Call setup() before using repo methods")

    def upsert_link(self, link: entities.LinkRecord) -> entities.LinkRecord:
        """Insert or update a LinkRecord. Returns the persisted instance."""
        self.ensure_setup()
        now = datetime.now(timezone.utc)
        # set created/updated timestamps if missing or update updated_at
        try:
            if getattr(link, "created_at", None) is None:
                link.created_at = now
            link.updated_at = now
            # if link marked as processed, set processed_at
            if getattr(link, "status", None) == "processed":
                if getattr(link, "processed_at", None) is None:
                    link.processed_at = now
        except Exception:
            # if link is not a model-like object, skip timestamp handling
            pass

        with Session(self.engine) as session:
            session.add(link)
            session.commit()
            session.refresh(link)
            return link

    def get_link_by_raindrop_id(
        self, raindrop_id: str
    ) -> Optional[entities.LinkRecord]:
        self.ensure_setup()
        with Session(self.engine) as session:
            statement = select(entities.LinkRecord).where(
                entities.LinkRecord.raindrop_id == raindrop_id
            )
            result = session.exec(statement).first()
            return result

    def list_pending_links(self, limit: int = 100) -> Iterable[entities.LinkRecord]:
        self.ensure_setup()
        with Session(self.engine) as session:
            statement = (
                select(entities.LinkRecord)
                .where(entities.LinkRecord.status == "pending")
                .limit(limit)
            )
            for row in session.exec(statement):
                yield row

    def upsert_tag_suggestions(self, raindrop_id: str, tags: Iterable[dict]):
        """Persist tag suggestions for a given raindrop id."""
        self.ensure_setup()
        now = datetime.now(timezone.utc)
        with Session(self.engine) as session:
            for tg in tags:
                ts = entities.TagSuggestion(
                    raindrop_id=str(raindrop_id),
                    tag=str(tg.get("tag")),
                    confidence=float(tg.get("confidence", 0.0)),
                    source=str(tg.get("source", "llm")),
                    suggested_at=now,
                )
                session.add(ts)
            session.commit()

    def upsert_sync_run(self, run: entities.SyncRun | dict):
        """Persist a SyncRun record created after a sync run.

        Accepts either an entities.SyncRun instance or a dict containing
        fields compatible with the SyncRun model.
        """
        self.ensure_setup()
        now = datetime.now(timezone.utc)
        # Normalize input into a SyncRun model
        if isinstance(run, dict):
            sr = entities.SyncRun(
                run_id=str(run.get("run_id") or run.get("id") or now.isoformat()),
                started_at=run.get("started_at")
                if run.get("started_at") is not None
                else now,
                completed_at=run.get("completed_at")
                if run.get("completed_at") is not None
                else now,
                mode=str(run.get("mode", "full")),
                links_processed=int(
                    run.get("processed", run.get("links_processed", 0)) or 0
                ),
                links_skipped=int(run.get("links_skipped", 0) or 0),
                manual_review=int(run.get("manual_review", 0) or 0),
                failures=int(run.get("failures", 0) or 0),
                output_path=str(run.get("output_path"))
                if run.get("output_path")
                else None,
                status_code=run.get("status_code"),
                rate_limit_remaining=(
                    run.get("rate_limit", {}).get("remaining")
                    if isinstance(run.get("rate_limit"), dict)
                    else None
                ),
                rate_limit_reset=(
                    run.get("rate_limit", {}).get("reset")
                    if isinstance(run.get("rate_limit"), dict)
                    else None
                ),
            )
        else:
            sr = run

        with Session(self.engine) as session:
            session.add(sr)
            session.commit()
            session.refresh(sr)
            return sr
