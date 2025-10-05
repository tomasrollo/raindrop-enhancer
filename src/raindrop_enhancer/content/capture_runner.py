from __future__ import annotations

import dataclasses
import datetime
from datetime import timezone
from typing import Iterable, List, Optional

from raindrop_enhancer.storage.sqlite_store import SQLiteStore
from .fetcher import TrafilaturaFetcher, FetchResult


@dataclasses.dataclass
class LinkAttemptSummary:
    """Summary of a single link capture attempt.

    Fields mirror the information useful for CLI output and tests.
    - link_id: internal DB id for the raindrop link row
    - url: the original link URL
    - status: one of 'skipped', 'success', or 'failed'
    - retry_count: reserved for future retry/backoff metrics
    - error_type/error_message: textual error details on failure
    """

    link_id: int
    url: str
    status: str
    retry_count: int = 0
    error_type: Optional[str] = None
    error_message: Optional[str] = None


@dataclasses.dataclass
class SessionSummary:
    """High-level summary of a capture session.

    - started_at/completed_at: timezone-aware UTC datetimes
    - attempts: list of LinkAttemptSummary entries in processed order
    """

    started_at: datetime.datetime
    completed_at: Optional[datetime.datetime] = None
    attempts: List[LinkAttemptSummary] = dataclasses.field(default_factory=list)


class CaptureRunner:
    """Coordinates fetching content for a set of links and persists results.

    Responsibilities and behavior:
    - Selects the set of links to process using `store.select_uncaptured` or
      `store.select_all_links` when `refresh=True`.
    - Honors `dry_run=True` by not modifying the DB and recording `skipped`
      attempts for visibility.
    - When `refresh=True`, clears existing content for the link before
      attempting a new fetch (via `store.clear_content_for_link`).
    - Uses `TrafilaturaFetcher.fetch` and writes successful markdown to the
      DB through `store.update_content`.

    Notes / extension points:
    - Retries, concurrency, and rate-limiting are intentionally not part of
      the MVP; these can be added here (or delegated to the fetcher) later.
    - The runner intentionally returns a plain data structure (SessionSummary)
      to keep CLI and higher-level orchestration logic easy to test.
    """

    def __init__(self, store: SQLiteStore, fetcher: TrafilaturaFetcher):
        self.store = store
        self.fetcher = fetcher

    def run(
        self, limit: Optional[int] = None, dry_run: bool = True, refresh: bool = False
    ) -> SessionSummary:
        """Run a single capture session.

        Parameters:
        - limit: optional maximum number of links to process
        - dry_run: if True, do not write changes to the DB; produce 'skipped'
          attempt entries for each considered link.
        - refresh: if True, process all links (not only uncaptured), and
          clear existing content before fetching.

        Returns a SessionSummary describing timing and per-link outcomes.
        """
        started = datetime.datetime.now(timezone.utc)
        attempts: List[LinkAttemptSummary] = []

        # Choose which links to process. Use `refresh` to re-fetch existing
        # captures (useful for backfilling or refreshing stale content).
        if refresh:
            links = self.store.select_all_links(limit=limit)
        else:
            links = self.store.select_uncaptured(limit=limit)

        for link in links:
            # Link rows are returned as simple tuples (id, url, ...). We keep
            # this logic minimal here and let the storage layer govern shapes.
            if dry_run:
                # Do not mutate DB on dry runs; record intention instead.
                attempts.append(
                    LinkAttemptSummary(link_id=link[0], url=link[1], status="skipped")
                )
                continue

            if refresh:
                # Clear existing content before re-capturing to ensure the
                # runner writes fresh content regardless of previous state.
                self.store.clear_content_for_link(link_id=link[0])

            # Perform the fetch and persist successful results.
            result: FetchResult = self.fetcher.fetch(link[1])
            if result.markdown:
                # Persist the captured markdown. The store layer is responsible
                # for updating timestamps and source metadata.
                self.store.update_content(link_id=link[0], markdown=result.markdown)
                attempts.append(
                    LinkAttemptSummary(link_id=link[0], url=link[1], status="success")
                )
            else:
                # On failure, keep the error text for debugging and CLI output.
                attempts.append(
                    LinkAttemptSummary(
                        link_id=link[0],
                        url=link[1],
                        status="failed",
                        error_type=result.error,
                        error_message=result.error,
                    )
                )

        return SessionSummary(
            started_at=started,
            completed_at=datetime.datetime.now(timezone.utc),
            attempts=attempts,
        )
