````markdown
# Quickstart: Persistent Storage and Incremental Sync

## Prerequisites
- Dependencies managed via `uv` (`uv` already documented in repository README).
- Valid Raindrop API token stored in `.env` (`RAINDROP_TOKEN=...`).
- SQLite is bundled with Python 3.13; no extra installation required.

## Environment Setup
1. Install/update dependencies:
   ```bash
   uv sync
   ```
2. Optional: create default data directory (CLI will create automatically if missing):
   ```bash
   mkdir -p "${HOME}/.local/share/raindrop_enhancer"
   ```

## Baseline Sync (first run)
```bash
uv run raindrop-sync --verbose
```
- Creates the SQLite database at the default location.
- Fetches all active raindrops, writes them to `raindrop_links`, and records the sync cursor.
- Emits summary to stdout and detailed progress to stderr when `--verbose`.

## Incremental Sync (subsequent runs)
```bash
uv run raindrop-sync
```
- Reads existing cursor, fetches only new raindrops, and appends them.
- Summary indicates `(+N new)` count; exits quickly when no new links.

## Full Refresh / Recovery
```bash
uv run raindrop-sync --full-refresh
```
- Backs up existing DB to `<db_path>.bak`, recreates schema, and performs full export.
- Use when schema version changes or corruption detected.

## Dry Run & Diagnostics
```bash
uv run raindrop-sync --dry-run --json --verbose
```
- Simulates a sync without touching the database.
- Outputs JSON summary to stdout (safe for automation) and diagnostics to stderr.

## Custom Database Location
```bash
uv run raindrop-sync --db-path "$(pwd)/tmp/raindrops.db"
```
- Useful for testing; integration tests will rely on temporary paths.

## Test Suite
1. Unit tests (storage + orchestration):
   ```bash
   uv run pytest tests/unit/test_sqlite_store.py tests/unit/test_sync_orchestrator.py
   ```
2. Contract tests (API usage):
   ```bash
   uv run pytest tests/contract/test_raindrop_incremental_contract.py
   ```
3. Integration tests (CLI end-to-end):
   ```bash
   uv run pytest tests/integration/test_cli_sync.py
   ```
4. Coverage target (≥90% on changed code):
   ```bash
   uv run pytest --cov=raindrop_enhancer --cov-report=term-missing
   ```

## Performance Smoke Tests
- Baseline benchmark (10k synthetic links):
  ```bash
  uv run pytest tests/perf/test_sync_baseline.py
  ```
- Incremental benchmark (500 new links):
  ```bash
  uv run pytest tests/perf/test_sync_incremental.py
  ```
  > These tests will be added during implementation; ensure runtime ≤60s and ≤5s respectively.

## Troubleshooting
- **Missing token**: CLI exits with code 2 and message `Missing RAINDROP_TOKEN`; ensure `.env` is present.
- **Database corruption**: CLI detects via `PRAGMA quick_check` and asks for `--full-refresh`; the command automatically creates a `.bak` before rebuilding.
- **Rate limit issues**: Built-in retries back off for up to 60s; re-run with `--verbose` to inspect attempts.
- **Different storage location needed**: Use `--db-path` or set `RAINDROP_ENHANCER_DB_PATH`; document in future tasks if env var support added.
````
