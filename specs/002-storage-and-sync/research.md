# Research Log: Persistent Storage and Incremental Sync for Raindrop Links

## Decision 1: Incremental cursor from Raindrop API
- **Decision**: Use the raindrop `created` timestamp and `sort=created` query parameter with `page`/`perpage` pagination to request only links created after the last stored ISO timestamp. When the API lacks direct `after` filters, fetch pages in chronological order and stop once `created <= last_cursor` to avoid duplicates.
- **Rationale**: The Raindrop REST API exposes stable ISO8601 `created` values and supports chronological sorting. Tracking the maximum `created` value per sync run meets the requirement to ignore edits/deletes while capturing newly added links.
- **Alternatives Considered**:
  - Relying on `lastUpdate`: rejected because edits trigger updates that would force reprocessing existing links.
  - Using Raindrop backup export API: rejected; asynchronous delivery and full dataset each time contradict incremental goal.

## Decision 2: SQLite schema and durability settings
- **Decision**: Create two tables: `raindrop_links` (primary key `raindrop_id`, metadata columns, `created_at`, `synced_at`, JSON tags) and `sync_state` (singleton row storing `last_cursor_iso`, `last_run_at`, `db_version`, `last_full_refresh`). Enable WAL journal mode and wrap batch inserts in a single transaction per sync run.
- **Rationale**: A single-writer CLI benefits from WAL for crash safety while allowing fast reads. Separate state table isolates sync metadata from link records and simplifies future migrations. Primary key constraint prevents duplicates when incremental runs overlap.
- **Alternatives Considered**:
  - Normalizing tags into a join table: rejected as overkill for read-mostly archive; JSON text sufficient for search/export use.
  - Storing sync metadata in a JSON blob: rejected; harder to evolve and validate fields.

## Decision 3: Database file location
- **Decision**: Default DB path to `<platform data dir>/raindrop_enhancer/raindrops.db` using manual path rules: macOS `~/Library/Application Support/raindrop_enhancer`, Linux `~/.local/share/raindrop_enhancer`, Windows `%APPDATA%\raindrop_enhancer`. Allow override via `--db-path` CLI flag.
- **Rationale**: Keeps user data in conventional locations without adding dependencies. Manual mapping covers primary platforms and still allows explicit override for custom workflows or testing.
- **Alternatives Considered**:
  - Introducing `platformdirs` dependency: rejected to avoid additional third-party requirement per constitution preference unless necessary.
  - Storing alongside project repo: rejected; breaks multi-directory execution and clutters working tree.

## Decision 4: Corruption detection & recovery
- **Decision**: On startup, open SQLite in `PRAGMA quick_check` mode; if it fails or schema version mismatches expected, prompt user to run with `--full-refresh` (which drops and recreates tables) after backing up the corrupted file. During sync, wrap transactions in try/except and roll back on failure without updating `sync_state`.
- **Rationale**: `PRAGMA quick_check` is lightweight and detects most corruption scenarios. Coupling with explicit `--full-refresh` command satisfies spec requirement to rebuild archives safely.
- **Alternatives Considered**:
  - Automatically deleting corrupted DB: rejected; risks data loss without confirmation.
  - Implementing full migration framework now: deferred until schema evolution required; version column prepares for future migrations.

## Decision 5: Performance validation strategy
- **Decision**: Seed benchmark fixtures that emulate 10k inserts and 500 incremental inserts against temporary SQLite files, timing operations to ensure baseline ≤60s and incremental ≤5s. Log inserted rows per second and include assertions in performance smoke tests.
- **Rationale**: Constitution demands explicit performance targets. Synthetic fixtures allow deterministic measurement without live API dependency.
- **Alternatives Considered**:
  - Measuring only live API sync: rejected; network variability would make results unreliable.
  - Skipping incremental benchmark: rejected; requirement explicitly calls for efficient incremental runs.
