# Phase 1 Data Model — Raindrop Link Enhancer CLI

_Date: 2025-10-01_

## Entity Overview

### LinkRecord
- **Primary Key**: `raindrop_id` (string/UUID from Raindrop)
- **Fields**: `url`, `title`, `description`, `created_at`, `updated_at`, `processed_at`, `content_hash`, `status` (`pending` | `processed` | `manual_review`), `llm_version`
- **Relationships**: many-to-many with `Collection` via `link_collections`; one-to-many with `TagSuggestion`
- **Indexes**: `(updated_at)`, `(processed_at)`, `(status)`
- **Notes**: Deduplicate by `raindrop_id`; track `content_hash` to detect content changes.

### Collection
- **Primary Key**: `collection_id`
- **Fields**: `title`, `color`, `parent_id`, `last_sync_timestamp`
- **Relationships**: many-to-many with `LinkRecord`
- **Indexes**: `(last_sync_timestamp)` for incremental sync per clarification.

### TagSuggestion
- **Primary Key**: composite (`raindrop_id`, `tag`)
- **Fields**: `tag`, `confidence`, `source` (enum: `llm`, `metadata`, `manual`), `suggested_at`
- **Relationships**: belongs to `LinkRecord`
- **Indexes**: `(confidence DESC)` for filtering by threshold.

### SyncRun
- **Primary Key**: `run_id` (UUID)
- **Fields**: `started_at`, `completed_at`, `mode` (`full` | `incremental` | `reprocess`), `links_processed`, `links_skipped`, `manual_review`, `failures`, `output_path`, `status_code`, `rate_limit_remaining`, `rate_limit_reset`
- **Relationships**: none; aggregated stats appended per run
- **Notes**: Supports audit trail requirement FR-014 and captures latest Raindrop API rate-limit telemetry.

### ConfigSettings
- **Primary Key**: singleton row (id=1)
- **Fields**: `data_dir`, `token_path`, `llm_api_base`, `llm_api_key`, `tag_confidence_threshold`, `max_tags`
- **Notes**: Persist CLI preferences and thresholds; ensure encryption not required but enforce permissions.

## State & Lifecycle
- **Link processing**: `pending` → `processed` once tagging succeeds; if trafilatura fails, set to `manual_review` with failure reason stored in auxiliary table/log.
- **Incremental sync**: for each `Collection`, compare last sync timestamp; fetch Raindrop links with `lastUpdate` greater, merge into SQLite, mark `processed_at=NULL` to queue for tagging.
- **Tag suggestions**: store latest set per LLM invocation; versioned by `llm_version` to support future retraining.
- **Audit trail**: each `SyncRun` appended with summary, referencing produced JSON path and recording final `rate_limit_remaining`/`rate_limit_reset` headers.

## Validation Rules
- `confidence` between 0.0 and 1.0.
- `tag` must be lowercase alphanumeric + hyphen/underscore.
- `status` transitions only forward (pending → processed/manual_review; manual_review can transition to processed via reprocess command).
- `output_path` directories must exist; `token_path` must resolve within data directory.

## Diagram (textual)
```
Collection 1---* LinkCollections *---1 LinkRecord 1---* TagSuggestion
LinkRecord 1---* SyncRun (via run entries)
ConfigSettings (singleton) -> controls thresholds for LinkRecord processing
```

## Open Questions
_None — all clarifications resolved during Phase 0._
