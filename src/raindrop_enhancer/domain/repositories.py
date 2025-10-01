"""SQLite repository implementation using SQLModel."""

from sqlmodel import SQLModel, Session, create_engine, select
from .entities import (
    LinkRecord,
    Collection,
    TagSuggestion,
    SyncRun,
    ConfigSettings,
    LinkCollectionLink,
)
from typing import Optional, List
from datetime import datetime
import os


class Repo:
    def __init__(self, path: str):
        self.path = path
        self.engine = create_engine(
            f"sqlite:///{path}", echo=False, connect_args={"check_same_thread": False}
        )

    def setup(self):
        # Enable WAL mode and create tables
        with self.engine.connect() as conn:
            conn.exec_driver_sql("PRAGMA journal_mode=WAL;")
        SQLModel.metadata.create_all(self.engine)

    def upsert_link(self, link: LinkRecord) -> LinkRecord:
        with Session(self.engine) as session:
            existing = session.exec(
                select(LinkRecord).where(LinkRecord.raindrop_id == link.raindrop_id)
            ).first()
            if existing:
                for field, value in link.model_dump(exclude_unset=True).items():
                    setattr(existing, field, value)
                session.add(existing)
                session.commit()
                session.refresh(existing)
                return existing
            else:
                session.add(link)
                session.commit()
                session.refresh(link)
                return link

    def get_link(self, raindrop_id: int) -> Optional[LinkRecord]:
        with Session(self.engine) as session:
            return session.exec(
                select(LinkRecord).where(LinkRecord.raindrop_id == raindrop_id)
            ).first()

    def list_links(self) -> List[LinkRecord]:
        with Session(self.engine) as session:
            return list(session.exec(select(LinkRecord)))

    def upsert_collection(self, collection: Collection) -> Collection:
        with Session(self.engine) as session:
            existing = session.exec(
                select(Collection).where(Collection.id == collection.id)
            ).first()
            if existing:
                for field, value in collection.model_dump(exclude_unset=True).items():
                    setattr(existing, field, value)
                session.add(existing)
                session.commit()
                session.refresh(existing)
                return existing
            else:
                session.add(collection)
                session.commit()
                session.refresh(collection)
                return collection

    def upsert_tag_suggestion(self, tag: TagSuggestion) -> TagSuggestion:
        with Session(self.engine) as session:
            session.add(tag)
            session.commit()
            session.refresh(tag)
            return tag

    def upsert_sync_run(self, run: SyncRun) -> SyncRun:
        with Session(self.engine) as session:
            existing = session.exec(
                select(SyncRun).where(SyncRun.run_id == run.run_id)
            ).first()
            if existing:
                for field, value in run.model_dump(exclude_unset=True).items():
                    setattr(existing, field, value)
                session.add(existing)
                session.commit()
                session.refresh(existing)
                return existing
            else:
                session.add(run)
                session.commit()
                session.refresh(run)
                return run

    def upsert_config(self, config: ConfigSettings) -> ConfigSettings:
        with Session(self.engine) as session:
            existing = session.exec(
                select(ConfigSettings).where(ConfigSettings.key == config.key)
            ).first()
            if existing:
                existing.value = config.value
                session.add(existing)
                session.commit()
                session.refresh(existing)
                return existing
            else:
                session.add(config)
                session.commit()
                session.refresh(config)
                return config

    # Incremental queries and audit logging stubs
    def get_links_updated_since(self, dt: datetime) -> List[LinkRecord]:
        with Session(self.engine) as session:
            return list(
                session.exec(select(LinkRecord).where(LinkRecord.updated_at > dt))
            )

    def log_audit_event(self, event: str, details: str = ""):
        # TODO: Implement audit logging table and logic
        pass
