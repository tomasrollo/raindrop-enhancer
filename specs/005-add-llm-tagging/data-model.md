# Phase 1 Data Model — LLM-Assisted Link Tagging

## Updated Entity: `RaindropLink`
- **Table**: `raindrop_links`
- **New Column**: `auto_tags_json` (`TEXT`, nullable)
  - Stores a JSON array of generated tag strings (Title Case, ≤20 characters each).
  - Populated only by the DSPy tagging command; manual tagging workflows remain in `tags_json`.
  - `NULL` indicates tags have not been generated or were cleared.
- **Constraints & Validation**:
  - Deserialized list must contain at most 10 unique strings.
  - Strings are normalized to Title Case ASCII and trimmed; blank entries are discarded before persistence.
  - Column updated atomically alongside `tags_generation_metadata` (see below) to avoid partial writes.

## New Entity: `TagGenerationMetadata`
- **Representation**: Stored as a JSON object in new column `auto_tags_meta_json` (`TEXT`, nullable) on `raindrop_links`.
- **Fields**:
  - `generated_at` (ISO8601): UTC timestamp of LLM completion.
  - `model` (str): Identifier from `RAINDROP_DSPY_MODEL` or DSPy settings (`openai:gpt-4o-mini` etc.).
  - `tokens_used` (int, optional): Total tokens reported by LLM provider if available.
  - `status` (str): `success` or `failed` — `failed` indicates the link was attempted but produced no tags (also stores `failure_reason`).
  - `failure_reason` (str, optional): Short machine-readable reason (e.g., `empty_content`, `llm_error`).
- **Rationale**: Enables idempotent re-runs, auditability, and future performance analytics without another table.

## New Value Object: `GeneratedTag`
- **Purpose**: Internal dataclass used in tagging module.
- **Fields**:
  - `value` (str)
  - `confidence` (float, optional; defaults to 1.0 when not provided by LLM)
  - `source` (Literal[`dspy`, `manual`]) — primarily `dspy` for this feature, but allows merges later.
- **Validation Rules**:
  - `value` normalized via slugify-then-Title Case pipeline; duplicates deduplicated ignoring case.
  - `confidence` must be within `[0.0, 1.0]`.

## Relationships & Lifecycle
- `RaindropLink.auto_tags_json` is independent from `tags_json`; existing sync and content capture pipelines only read/write manual tags, so migrations must be backward compatible.
- The DSPy tagging command:
  1. Loads candidate links where `auto_tags_json IS NULL` (or `status != success`).
  2. Generates tags and writes both `auto_tags_json` and `auto_tags_meta_json` in a single `UPDATE`.
  3. Emits progress events including timestamp and counts for success/skip/failure.
- Clearing tags (`--dry-run` or `--reset`) will set both columns to `NULL` and record action in CLI output rather than deleting manual tags.

## Migration Notes
- Add helper `_ensure_tagging_columns()` invoked during `SQLiteStore.connect()` alongside existing content-column checks.
- Update user version pragma to `3` once the migration runs to avoid re-applying.
- Provide SQL scripts and tests to confirm columns exist and default to `NULL`.
