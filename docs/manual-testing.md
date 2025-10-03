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
