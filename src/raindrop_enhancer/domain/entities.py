"""Domain entities implemented with SQLModel for persistence.

These follow the data-model.md specification: LinkRecord, Collection,
TagSuggestion, SyncRun and ConfigSettings.
"""

from datetime import datetime, timezone
from typing import Optional, List

from sqlmodel import SQLModel, Field, Relationship


class LinkCollectionLink(SQLModel, table=True):
    link_id: Optional[int] = Field(
        default=None, foreign_key="linkrecord.id", primary_key=True
    )
    collection_id: Optional[int] = Field(
        default=None, foreign_key="collection.id", primary_key=True
    )


class LinkRecord(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    raindrop_id: str = Field(index=True)
    url: str
    title: Optional[str] = None
    description: Optional[str] = None
    content_hash: Optional[str] = None
    status: str = Field(default="pending", index=True)
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None
    processed_at: Optional[datetime] = None
    llm_version: Optional[str] = None

    collections: List["Collection"] = Relationship(
        back_populates="links", link_model=LinkCollectionLink
    )
    tags: List["TagSuggestion"] = Relationship(back_populates="link")


class Collection(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    collection_id: str = Field(index=True)
    title: Optional[str] = None
    color: Optional[str] = None
    parent_id: Optional[str] = None
    last_sync_timestamp: Optional[datetime] = None

    links: List[LinkRecord] = Relationship(
        back_populates="collections", link_model=LinkCollectionLink
    )


class TagSuggestion(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    raindrop_id: Optional[str] = Field(index=True)
    tag: str
    confidence: float = Field(default=0.0)
    source: Optional[str] = None
    suggested_at: Optional[datetime] = None

    link_id: Optional[int] = Field(default=None, foreign_key="linkrecord.id")
    link: Optional[LinkRecord] = Relationship(back_populates="tags")


class SyncRun(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    run_id: str = Field(index=True)
    started_at: Optional[datetime] = None
    completed_at: Optional[datetime] = None
    mode: str = Field(default="full")
    links_processed: int = Field(default=0)
    links_skipped: int = Field(default=0)
    manual_review: int = Field(default=0)
    failures: int = Field(default=0)
    output_path: Optional[str] = None
    status_code: Optional[int] = None
    rate_limit_remaining: Optional[int] = None
    rate_limit_reset: Optional[int] = None


class ConfigSettings(SQLModel, table=True):
    id: Optional[int] = Field(default=1, primary_key=True)
    data_dir: Optional[str] = None
    token_path: Optional[str] = None
    llm_api_base: Optional[str] = None
    llm_api_key: Optional[str] = None
    tag_confidence_threshold: float = Field(default=0.6)
    max_tags: int = Field(default=10)
