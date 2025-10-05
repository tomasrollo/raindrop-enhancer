from __future__ import annotations

import dataclasses
import datetime
from typing import Iterable, List, Optional

from raindrop_enhancer.storage.sqlite_store import SQLiteStore
from .fetcher import TrafilaturaFetcher, FetchResult


@dataclasses.dataclass
class LinkAttemptSummary:
    link_id: int
    url: str
    status: str
    retry_count: int = 0
    error_type: Optional[str] = None
    error_message: Optional[str] = None


@dataclasses.dataclass
class SessionSummary:
    started_at: datetime.datetime
    completed_at: Optional[datetime.datetime] = None
    attempts: List[LinkAttemptSummary] = dataclasses.field(default_factory=list)


class CaptureRunner:
    def __init__(self, store: SQLiteStore, fetcher: TrafilaturaFetcher):
        self.store = store
        self.fetcher = fetcher

    def run(self, limit: Optional[int] = None, dry_run: bool = True, refresh: bool = False) -> SessionSummary:
        started = datetime.datetime.utcnow()
        attempts: List[LinkAttemptSummary] = []

        if refresh:
            links = self.store.select_all_links(limit=limit)
        else:
            links = self.store.select_uncaptured(limit=limit)
        for link in links:
            if dry_run:
                attempts.append(LinkAttemptSummary(link_id=link[0], url=link[1], status="skipped"))
                continue

            if refresh:
                self.store.clear_content_for_link(link_id=link[0])

            result: FetchResult = self.fetcher.fetch(link[1])
            if result.markdown:
                self.store.update_content(link_id=link[0], markdown=result.markdown)
                attempts.append(LinkAttemptSummary(link_id=link[0], url=link[1], status="success"))
            else:
                attempts.append(
                    LinkAttemptSummary(
                        link_id=link[0],
                        url=link[1],
                        status="failed",
                        error_type=result.error,
                        error_message=result.error,
                    )
                )

        return SessionSummary(started_at=started, completed_at=datetime.datetime.utcnow(), attempts=attempts)
