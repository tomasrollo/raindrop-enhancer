"""Domain entity stubs."""

from datetime import datetime
from typing import List, Optional, TYPE_CHECKING

if TYPE_CHECKING:
    from .entities import Collection
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
    raindrop_id: int = Field(index=True, unique=True)
    url: str
    title: str = Field(default="")
    tags: Optional[str] = Field(default=None, description="Comma-separated tags")
    created_at: Optional[datetime] = Field(default=None)
    updated_at: Optional[datetime] = Field(default=None)
    collections: List["Collection"] = Relationship(
        back_populates="links", link_model=LinkCollectionLink
    )


class Collection(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    title: str = Field(default="")
    description: Optional[str] = Field(default=None)
    links: List[LinkRecord] = Relationship(
        back_populates="collections", link_model=LinkCollectionLink
    )


# ConfigSettings for storing configuration in the database
class ConfigSettings(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    key: str = Field(index=True, unique=True)
    value: str


# TagSuggestion SQLModel
class TagSuggestion(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    tag: str
    confidence: float = Field(default=0.0)


# SyncRun SQLModel with rate-limit fields
class SyncRun(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    run_id: str = Field(index=True, unique=True)
    started_at: Optional[datetime] = Field(default=None)
    completed_at: Optional[datetime] = Field(default=None)
    mode: str = Field(default="full")
    links_processed: int = Field(default=0)
    rate_limit_limit: Optional[int] = Field(
        default=None, description="X-RateLimit-Limit"
    )
    rate_limit_remaining: Optional[int] = Field(
        default=None, description="X-RateLimit-Remaining"
    )
    rate_limit_reset: Optional[int] = Field(
        default=None, description="X-RateLimit-Reset (epoch seconds)"
    )
