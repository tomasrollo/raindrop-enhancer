# Data Model: Persistent Storage and Incremental Sync for Raindrop Links

## Entities

### RaindropLink
- **Description**: Represents a single Raindrop item stored locally for long-term reference.
- **Storage**: `raindrop_links` SQLite table (append-only).
- **Fields**:
  - `raindrop_id: INTEGER PRIMARY KEY` — Unique identifier from Raindrop API (`_id`).
  - `collection_id: INTEGER NOT NULL` — Owning collection identifier (can be `-1` for Unsorted).
  - `collection_title: TEXT NOT NULL` — Collection label at time of capture.
  - `title: TEXT NOT NULL` — Bookmark title.
  - `url: TEXT NOT NULL` — Bookmark URL; validated as HTTP/HTTPS.
  - `created_at: TEXT NOT NULL` — ISO8601 timestamp from Raindrop `created` field.
  - `synced_at: TEXT NOT NULL` — ISO8601 timestamp when the local sync captured the record.
  - `tags_json: TEXT NOT NULL` — JSON-encoded array of tags (empty array `[]` if none).
  - `raw_payload: TEXT NOT NULL` — JSON-serialized subset of the original API payload for forwards compatibility.
- **Indexes**:
  - Primary key on `raindrop_id` prevents duplicates.
  - Secondary index on `created_at` accelerates incremental queries.
  - Composite index on `(collection_id, created_at)` supports per-collection filtering.
- **Validation Rules**:
  - Reject inserts where `raindrop_id` already exists (append-only constraint).
  - Only accept URLs beginning with `http://` or `https://`.
  - Normalize `tags_json` to canonical JSON (sorted strings) before storage.
- **State Transitions**:
  - Baseline sync inserts all active links with current `synced_at`.
  - Incremental sync inserts new rows only; existing rows remain untouched.

### SyncState
- **Description**: Tracks metadata required to drive incremental syncs and detect corruption.
- **Storage**: `sync_state` SQLite table with a single row (`id = 1`).
- **Fields**:
  - `id: INTEGER PRIMARY KEY CHECK (id = 1)` — Ensures singleton row.
  - `last_cursor_iso: TEXT NOT NULL` — Highest `created_at` ISO timestamp captured.
  - `last_run_at: TEXT NOT NULL` — Timestamp when the last successful sync finished.
  - `db_version: INTEGER NOT NULL` — Schema version for future migrations (initially `1`).
  - `last_full_refresh: TEXT NOT NULL` — Timestamp of last run with `--full-refresh` (set equal to `last_run_at` during baseline or reset).
- **Validation Rules**:
  - `last_cursor_iso` must be monotonically increasing; updates rejected if older than stored value.
  - `db_version` must match application constant; mismatch triggers migration or full refresh.
- **State Transitions**:
  - **Initialization**: Create row with cursor equal to newest `created_at` inserted during baseline.
  - **Incremental Sync**: Update `last_cursor_iso` and `last_run_at` only after transaction commits successfully.
  - **Full Refresh**: Reset both tables, rewrite row with new timestamps, increment `db_version` when schema changes.

### SyncOutcome (in-memory helper)
- **Description**: Captures a summary of a sync run for user messaging and telemetry.
- **Fields**:
  - `run_started_at: datetime`
  - `run_finished_at: datetime`
  - `new_links: int`
  - `total_links: int`
  - `was_full_refresh: bool`
  - `db_path: Path`
- **Usage**: Returned by orchestrator for CLI rendering and optional JSON summary output. Not persisted to the database.

## Relationships
- `SyncState` has a one-to-many conceptual relationship to `RaindropLink` through the cursor (each run references all rows inserted at or before the cursor).
- No cascading deletes; append-only archive keeps historical records even if Raindrop data changes upstream.

## Integrity & Recovery Rules
- On CLI start, the orchestrator verifies schema via `PRAGMA user_version` (mirrors `db_version`) and `PRAGMA quick_check`.
- If verification fails, CLI aborts with instructions to rerun using `--full-refresh`, which:
  1. Backs up the existing DB (copy to `<db_path>.bak` if not already present).
  2. Drops tables (if present) and recreates schema.
  3. Performs baseline sync, replacing `SyncState` row.
- Transactions: Baseline and incremental syncs wrap DB modifications in a single transaction to avoid partial state.

```sql
CREATE TABLE raindrop_links (
    raindrop_id INTEGER PRIMARY KEY,
    collection_id INTEGER NOT NULL,
    collection_title TEXT NOT NULL,
    title TEXT NOT NULL,
    url TEXT NOT NULL,
    created_at TEXT NOT NULL,
    synced_at TEXT NOT NULL,
    tags_json TEXT NOT NULL,
    raw_payload TEXT NOT NULL
);
CREATE INDEX idx_links_created_at ON raindrop_links(created_at);
CREATE INDEX idx_links_collection_created ON raindrop_links(collection_id, created_at);

CREATE TABLE sync_state (
    id INTEGER PRIMARY KEY CHECK (id = 1),
    last_cursor_iso TEXT NOT NULL,
    last_run_at TEXT NOT NULL,
    db_version INTEGER NOT NULL,
    last_full_refresh TEXT NOT NULL
);

PRAGMA user_version = 1;
```
