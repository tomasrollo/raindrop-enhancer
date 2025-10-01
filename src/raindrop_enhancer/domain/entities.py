"""SQLModel domain entities for Raindrop Enhancer."""

from datetime import datetime, timezone
from typing import ClassVar, Optional

from sqlalchemy.orm import Mapped
from sqlmodel import Field, Relationship, SQLModel


class LinkCollectionLink(SQLModel, table=True):
    """Association table between links and collections."""

    __tablename__: ClassVar[str] = "link_collections"

    link_id: Optional[int] = Field(
        default=None,
        foreign_key="link_records.raindrop_id",
        primary_key=True,
    )
    collection_id: Optional[int] = Field(
        default=None,
        foreign_key="collections.collection_id",
        primary_key=True,
    )


class LinkRecord(SQLModel, table=True):
    """Persisted metadata about a Raindrop link and its processing state."""

    __tablename__: ClassVar[str] = "link_records"

    raindrop_id: int = Field(primary_key=True, index=True)
    url: str = Field()
    title: str = Field(default="")
    description: Optional[str] = Field(default=None)
    created_at: datetime = Field(index=True)
    updated_at: datetime = Field(index=True)
    processed_at: Optional[datetime] = Field(default=None, index=True)
    content_hash: Optional[str] = Field(default=None)
    status: str = Field(default="pending", index=True)
    llm_version: Optional[str] = Field(default=None)

    collections: Mapped[list["Collection"]] = Relationship(
        back_populates="links",
        link_model=LinkCollectionLink,
        sa_relationship_kwargs={"lazy": "selectin"},
    )
    tag_suggestions: Mapped[list["TagSuggestion"]] = Relationship(
        back_populates="link",
        sa_relationship_kwargs={"lazy": "selectin", "cascade": "all, delete-orphan"},
    )


class Collection(SQLModel, table=True):
    """Raindrop collection metadata."""

    __tablename__: ClassVar[str] = "collections"

    collection_id: int = Field(primary_key=True)
    title: str = Field()
    color: Optional[str] = Field(default=None)
    parent_id: Optional[int] = Field(
        default=None,
        foreign_key="collections.collection_id",
    )
    last_sync_timestamp: Optional[datetime] = Field(default=None, index=True)

    links: Mapped[list[LinkRecord]] = Relationship(
        back_populates="collections",
        link_model=LinkCollectionLink,
        sa_relationship_kwargs={"lazy": "selectin"},
    )


class TagSuggestion(SQLModel, table=True):
    """Tag recommendations generated for a link."""

    __tablename__: ClassVar[str] = "tag_suggestions"

    raindrop_id: int = Field(
        foreign_key="link_records.raindrop_id",
        primary_key=True,
    )
    tag: str = Field(default="", primary_key=True)
    confidence: float = Field(default=0.0, ge=0.0, le=1.0)
    source: str = Field(default="metadata")
    suggested_at: datetime = Field(
        default_factory=lambda: datetime.now(tz=timezone.utc),
        index=True,
    )

    link: Mapped[LinkRecord] = Relationship(back_populates="tag_suggestions")


class SyncRun(SQLModel, table=True):
    """Audit trail entry for a sync execution."""

    __tablename__: ClassVar[str] = "sync_runs"

    run_id: str = Field(primary_key=True)
    started_at: datetime = Field(index=True)
    completed_at: Optional[datetime] = Field(default=None)
    mode: str = Field(index=True)
    links_processed: int = Field(default=0, ge=0)
    links_skipped: int = Field(default=0, ge=0)
    manual_review: int = Field(default=0, ge=0)
    failures: int = Field(default=0, ge=0)
    output_path: Optional[str] = Field(default=None)
    status_code: Optional[int] = Field(default=None)
    rate_limit_remaining: Optional[int] = Field(default=None)
    rate_limit_reset: Optional[int] = Field(default=None)


class ConfigSettings(SQLModel, table=True):
    """Persisted CLI configuration state."""

    __tablename__: ClassVar[str] = "config_settings"

    id: int = Field(default=1, primary_key=True)
    data_dir: Optional[str] = Field(default=None)
    token_path: Optional[str] = Field(default=None)
    llm_api_base: Optional[str] = Field(default=None)
    llm_api_key: Optional[str] = Field(default=None)
    tag_confidence_threshold: float = Field(
        default=0.5,
        ge=0.0,
        le=1.0,
    )
    max_tags: int = Field(default=5, ge=0)


__all__ = [
    "LinkCollectionLink",
    "LinkRecord",
    "Collection",
    "TagSuggestion",
    "SyncRun",
    "ConfigSettings",
]
