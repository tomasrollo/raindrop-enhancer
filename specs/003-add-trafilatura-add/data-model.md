# Data Model: Full-Text Capture Enhancements

## Entity: SavedLink (Updated)
- **Primary Key**: `id` (INTEGER)
- **Fields**:
  - `url` (TEXT, required, unique index) – existing canonical link identifier
  - `title` (TEXT, optional) – stored metadata from Raindrop
  - `collection_id` (INTEGER, optional) – existing grouping metadata
  - `tags` (TEXT, optional) – serialized tag list
  - `excerpt` (TEXT, optional) – short description currently stored
  - `content_markdown` (TEXT, nullable, default NULL) – newly captured article content in Markdown
  - `content_fetched_at` (TIMESTAMP, nullable, default NULL) – UTC timestamp of last successful capture
  - `content_source` (TEXT, nullable, default 'trafilatura') – origin of captured content for future provenance
- **Relationships**:
  - 1-to-many with `LinkCaptureAttempt` (conceptual, for diagnostics)
- **Validation Rules**:
  - `content_markdown` only populated when capture succeeds
  - When `content_markdown` is set, `content_fetched_at` MUST also be set
  - Refresh operations overwrite `content_markdown` only when `--refresh` flag supplied

## Entity: LinkCaptureAttempt (Logical Record)
- **Primary Key**: ephemeral (not stored persistently; represented in CLI summaries/tests)
- **Fields**:
  - `link_id` (INTEGER, required)
  - `attempted_at` (TIMESTAMP, required)
  - `status` (ENUM: `success`, `skipped`, `failed`)
  - `retry_count` (INTEGER, default 0, max 1)
  - `error_type` (TEXT, nullable) – populated for failed attempts
- **Purpose**: shapes CLI JSON output and logging; may later be persisted but initially remains in-process structure backing summaries.
- **Relationships**:
  - References `SavedLink`

## Entity: ContentCaptureSession (Summary Object)
- **Primary Key**: generated per command invocation (UUID in-memory)
- **Fields**:
  - `started_at` (TIMESTAMP)
  - `completed_at` (TIMESTAMP)
  - `links_processed` (INTEGER)
  - `links_succeeded` (INTEGER)
  - `links_skipped` (INTEGER)
  - `links_failed` (INTEGER)
  - `errors` (ARRAY of {`link_id`, `error_type`, `message`})
  - `exit_code` (INTEGER: 0 success/partial, 1 all failed)
- **Relationships**:
  - Aggregates many `LinkCaptureAttempt`

## Derived Relationships & Behaviors
- Selecting uncaptured links: `SELECT * FROM saved_links WHERE content_markdown IS NULL ORDER BY updated_at LIMIT :limit`
- Refresh flow: when `--refresh` set, clear `content_markdown`/`content_fetched_at` before recapturing for targeted links.
- JSON output structure mirrors `ContentCaptureSession` with nested `attempts`, enabling deterministic contract tests.
