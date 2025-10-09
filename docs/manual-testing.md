Manual testing and validation steps for the Unified Raindrop Export CLI

Purpose

This document lists manual validation steps to reproduce key scenarios described in the feature spec. It is intended for reviewers and maintainers to verify the CLI behavior without running automated tests.

Prerequisites

- A valid Raindrop API token with read access saved to `.env` at the repository root:
  RAINDROP_TOKEN=your_token_here
- `uv` toolchain available and the project dependencies installed via `uv sync`.

Manual test steps

1. Dry run (connectivity + token validation)

- Command:
  uv run raindrop-export --dry-run --verbose
- Expected:
  - CLI loads `.env` and validates the token.
  - Prints a list of collections with counts and exits with code 0.

2. Successful export to stdout

- Command:
  uv run raindrop-export --verbose
- Expected:
  - CLI shows progress bars for collections and items.
  - Outputs a JSON array to stdout with raindrop objects containing required fields: id, collection_id, title, url, created_at, last_updated_at, tags.
  - Exit code 0.

3. Export to file

- Command:
  uv run raindrop-export --output exported.json --verbose
- Expected:
  - File `exported.json` is created with the JSON array.
  - File is valid JSON (parse with `jq '.' exported.json`).

4. Missing token error handling

- Command (with `.env` removed or empty):
  uv run raindrop-export
- Expected:
  - CLI writes an error to stderr explaining missing/invalid token and exits with non-zero exit code.

5. Rate-limit retry scenario (manual)

- Method: simulate repeated runs to provoke 429, or use controlled network shaping to cause 429 responses from a test proxy.
- Expected:
  - CLI logs retry attempts (when `--verbose`) and eventually succeeds or exits with informative error if retries exhausted.
  - Retry delays exponential backoff: 1s, 2s, 4s, 8s (cap at 8s) up to total allowed wait (~60s)

Collecting logs

- For review attach stdout and stderr from runs; when troubleshooting include `--verbose` so structured logs and retry details are visible.

Notes

- For reproducible perf tests, use the planned performance fixture (tests/perf) to simulate large counts; the smoke test will be added to CI when available.

6. Sync command (local SQLite storage)

- Baseline sync (first run creates DB):

  ```bash
  uv run raindrop-sync --db-path ./tmp/raindrops.db --json
  ```

  Expected:
  - Creates the SQLite DB at the provided path and writes all active raindrops.
  - Outputs a JSON summary with `new_links` and `total_links`.

- Incremental sync (no new items):

  ```bash
  uv run raindrop-sync --db-path ./tmp/raindrops.db --json
  ```

  Expected:
  - Reads sync cursor from DB and exits quickly when no new links are found; `new_links` should be 0.

- Full refresh (rebuild):

  ```bash
  uv run raindrop-sync --db-path ./tmp/raindrops.db --full-refresh --json
  ```

  Expected:
  - Backup existing DB to `raindrops.db.bak`, recreate schema, and perform a baseline export.

7. Capture content command (manual testing)

- Dry-run preview (no mutations):

  ```bash
  uv run capture-content --dry-run --limit 5 --verbose
  ```

  Expected:
  - Lists which links would be processed and exits with code 0.

- Execute capture (writes Markdown into DB):

  ```bash
  uv run capture-content --limit 100
  ```

  Expected:
  - Persists `content_markdown` and `content_fetched_at` for successfully captured links.
  - Exits `0` when at least one link succeeded; exits `1` when all attempted links fail.

- Refresh existing content (overwrite):

  ```bash
  uv run capture-content --refresh --limit 10
  ```

  Expected:
  - Overwrites existing `content_markdown` fields for the targeted links.

Migration

If your DB predates this feature you must add the new columns. A one-off migration helper is available (Python API) until a `migrate` CLI command is added:

```bash
uv run python - <<'PY'
from raindrop_enhancer.storage.sqlite_store import SQLiteStore
from raindrop_enhancer.sync.orchestrator import default_db_path

store = SQLiteStore(default_db_path())
store.connect()
store._ensure_content_columns()
print('Migration applied')
PY
```

After migration, validate columns exist:

```bash
uv run python - <<'PY'
import sqlite3
from raindrop_enhancer.sync.orchestrator import default_db_path

db = default_db_path()
conn = sqlite3.connect(db)
print([r[1] for r in conn.execute("PRAGMA table_info(raindrop_links)")])
PY

8. Auto-tagging (LLM-assisted) manual validation

- Prerequisites: set `RAINDROP_DSPY_MODEL` in `.env` or export in your shell. For dry-run testing you can omit it.

- Dry-run (no DB writes):

```bash
uv run raindrop-enhancer tags generate --db-path ./tmp/raindrops.db --dry-run --verbose
```

Expected:
- CLI lists how many links will be processed and prints a short summary. Exit code 0.

- Persist generated tags (writes to DB):

```bash
uv run raindrop-enhancer tags generate --db-path ./tmp/raindrops.db
```

Expected:
- Writes `auto_tags_json` and `auto_tags_meta_json` columns in `raindrop_links` for updated links. Exit code 0 on success.

- CI-style run (fail if DSPy missing):

```bash
uv run raindrop-enhancer tags generate --db-path ./tmp/raindrops.db --require-dspy --json
```

Expected:
- If `RAINDROP_DSPY_MODEL` is missing, exit code 2 and an error message. If present, emits JSON summary.

## Quickstart run: LLM-assisted tagging (T021)

I performed the end-to-end quickstart locally using a temporary SQLite DB and a deterministic fake DSPy predictor to validate the dry-run -> persist -> idempotency flows.

Summary (deterministic fake predictor):

- Dry-run: exit code 0
- Dry-run JSON summary: {"processed": 5, "generated": 5, "failed": 0, "db": "<tmp db>", "model": "unknown"}
- Persist run: exit code 0
- Persist JSON summary: {"processed": 5, "generated": 5, "failed": 0, "db": "<tmp db>", "model": "unknown"}
- Re-run (idempotency): exit code 0; JSON: {"processed": 0, "generated": 0, "failed": 0, "db": "<tmp db>", "model": "unknown"}

Notes:

- The run used a fake predictor by monkeypatching `raindrop_enhancer.content.dspy_settings.configure_dspy` to return a simple fast callable. This avoids external API calls and makes the run deterministic for reviewers.
- The `model` field shows `unknown` when using the fallback predictor; with a real DSPy-backed model (set `RAINDROP_DSPY_MODEL`) the CLI reports the configured model name.
- Use the CLI commands in the spec/quickstart to reproduce against a real model and your DB; the quickstart in `specs/005-add-llm-tagging/quickstart.md` documents the exact commands.
