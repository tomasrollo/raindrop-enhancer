# Data Model: Unified Raindrop Export CLI

## Entities

### Collection
- **Description**: Represents a Raindrop collection accessible to the authenticated user.
- **Fields**:
  - `id: int` — Collection identifier (`_id`).
  - `title: str` — Display name.
  - `count: int` — Number of active raindrops (may differ from raw API count; adjust after filtering).
  - `parent_id: Optional[int]` — Identifier of parent collection (if nested).
  - `color: Optional[str]` — Hex color metadata (used only for context, not output).
  - `created_at: datetime` — ISO timestamp from API `created`.
  - `last_updated_at: datetime` — Timestamp from API `lastUpdate`.
  - `access_level: int` — Access value (1-4) to determine ownership if needed for filtering.
- **Validation Rules**:
  - `title` must be non-empty.
  - Collections with `access_level < 1` are ignored (no access).
- **Relationships**:
  - One-to-many with `Raindrop` via `collection_id`.

### Raindrop
- **Description**: Active bookmark item returned from Raindrop API.
- **Fields**:
  - `id: int` — Raindrop identifier (`_id`).
  - `collection_id: int` — Owning collection id.
  - `collection_title: str` — Human-readable collection name (from parent collection for output convenience).
  - `title: str` — Bookmark title.
  - `url: str` — Destination URL.
  - `excerpt: Optional[str]` — Short description (if provided).
  - `created_at: datetime` — Saved timestamp (`created`).
  - `last_updated_at: datetime` — Last update timestamp (`lastUpdate`).
  - `tags: List[str]` — Associated tags.
  - `cover: Optional[str]` — Thumbnail URL (optional for output, may include).
- **Validation Rules**:
  - Exclude raindrops where API flags `important=false` and status indicates archived/duplicate. (Filter by `removed`, `duplicate`, `broken`, `important` fields.)
  - Ensure `url` parses as valid HTTP(S) URL.
- **Relationships**:
  - Belongs to exactly one `Collection` (per `collection_id`).

### ExportResult
- **Description**: In-memory representation of final export payload for serialization.
- **Fields**:
  - `raindrops: List[Raindrop]` — Ordered list of active items sorted by collection then created date.
  - `exported_at: datetime` — Timestamp when export completed.
  - `total_collections: int`
  - `total_raindrops: int`
- **Validation Rules**:
  - `total_raindrops` must equal `len(raindrops)`.

## Derived/Helper Structures
- **PaginationState**: tracks `collection_id`, `page`, `per_page`, `total` to drive loops.
- **RateLimitState**: stores last retry delay and elapsed wait for logging/backoff decisions.

## State Transitions
1. **Collection discovery**: Start with empty list → fetch root collections → append to list → expand nested collections if present.
2. **Raindrop retrieval**: For each collection, iterate pages; accumulate raindrops matching filters.
3. **Export assembly**: Combine raindrops into `ExportResult`, compute totals, and pass to exporter for JSON serialization.
