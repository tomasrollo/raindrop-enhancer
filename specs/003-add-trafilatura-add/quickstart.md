# Quickstart: Capture Markdown Content for Saved Links

## Prerequisites
1. Install uv (per project README) and sync environment:
   ```bash
   uv sync
   ```
2. Apply dependency update for Trafilatura (one-time):
   ```bash
   uv add trafilatura
   uv lock
   uv sync
   ```
3. Ensure Raindrop API token and config are already set (existing CLI requirements). Optional: export via `.env` file.
4. Verify sqlite database exists or run the existing sync command to populate baseline links.

## Database Migration
1. Run schema migration to add Markdown columns (implementation task will supply command). For now, validate migration script once available:
   ```bash
   uv run raindrop-enhancer migrate --target content-markdown
   ```
2. Confirm columns exist:
   ```bash
   uv run python - <<'PY'
   import sqlite3, os
   from raindrop_enhancer.storage.sqlite_store import get_db_path

   conn = sqlite3.connect(get_db_path())
   cursor = conn.execute("PRAGMA table_info(saved_links)")
   print([row[1] for row in cursor.fetchall()])
   PY
   ```

## Run the Capture Command
1. Dry-run preview (no mutations):
   ```bash
   uv run raindrop-enhancer capture-content --dry-run --limit 5 --verbose
   ```
   - Expect summary showing which links would be processed.
2. Execute content capture:
   ```bash
   uv run raindrop-enhancer capture-content --limit 100
   ```
   - Command exits `0` when at least one link succeeded.
3. Refresh existing content (explicit opt-in):
   ```bash
   uv run raindrop-enhancer capture-content --refresh --limit 10
   ```

## JSON Output Workflow
1. Capture with machine-readable summary:
   ```bash
   uv run raindrop-enhancer capture-content --json --limit 10 > capture_results.json
   ```
2. Inspect failures:
   ```bash
   jq '.attempts[] | select(.status == "failed")' capture_results.json
   ```

## Validation Steps
1. Spot-check database to confirm Markdown stored:
   ```bash
   uv run python - <<'PY'
   import sqlite3
   from raindrop_enhancer.storage.sqlite_store import get_db_path

   conn = sqlite3.connect(get_db_path())
   cursor = conn.execute(
       "SELECT url, substr(content_markdown, 1, 120), content_fetched_at FROM saved_links WHERE content_markdown IS NOT NULL LIMIT 3"
   )
   for row in cursor:
       print(row)
   PY
   ```
2. Run automated tests:
   ```bash
   uv run pytest tests/contract/test_cli_content_capture.py tests/integration/test_cli_content_capture.py
   ```
3. Execute performance baseline once dataset prepared:
   ```bash
   uv run pytest tests/perf/test_content_capture.py -k "baseline"
   ```
