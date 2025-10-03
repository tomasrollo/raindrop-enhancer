# Contract: `raindrop-sync` CLI Command

## Overview
- **Command**: `uv run raindrop-sync`
- **Purpose**: Populate and update a local SQLite archive of Raindrop links.
- **Idempotency**: Running multiple times without new links leaves the DB unchanged and returns `new_links = 0`.
- **Scope**: Append-only archive; upstream edits/deletes are ignored.

## Arguments & Flags
| Flag | Required | Default | Description |
|------|----------|---------|-------------|
| `--db-path PATH` | No | Platform-specific default (`~/Library/Application Support/raindrop_enhancer/raindrops.db` on macOS, `~/.local/share/raindrop_enhancer/raindrops.db` on Linux, `%APPDATA%\raindrop_enhancer\raindrops.db` on Windows) | Overrides database file location. |
| `--full-refresh` | No | `False` | Drops existing archive after creating a timestamped backup copy (`<db>.bak`) and rebuilds from scratch. |
| `--dry-run` | No | `False` | Performs all remote requests and validation but skips database writes; reports projected counts. |
| `--json` | No | `False` | Prints run summary as JSON to stdout; human-readable text goes to stderr if `--quiet` not set. |
| `--quiet` | No | `False` | Suppresses non-error stdout/stderr output (summary still emitted when `--json`). |
| `--verbose` | No | `False` | Enables detailed logging (API requests, retry timing, DB operations) to stderr. |
| `--rate-limit INTEGER` | No | `120` | Requests-per-minute budget; enforced only when paired with `--enforce-rate-limit` for compatibility with existing CLI behavior. |
| `--enforce-rate-limit/--no-enforce-rate-limit` | No | `True` | When true, spaces requests to respect rate limit; must remain default true for sync command. |

## Environment Requirements
- `RAINDROP_TOKEN` must be available in environment or `.env`. Absent token → exit code `2` with error message to stderr.

## Exit Codes
| Code | Meaning |
|------|---------|
| `0` | Sync succeeded; summary emitted. |
| `1` | Unrecoverable error (network failure after retries, DB corruption not fixed by full refresh, SQLite write failure). |
| `2` | Configuration error (missing token, invalid DB path, schema mismatch without `--full-refresh`). |

## Output Contract
### Text Mode (`--json` not provided)
- **stdout**:
  - On success: human-readable summary lines, e.g. `Synced 125 total links (+5 new)`.
  - On dry-run: `Dry run: would add X new links; archive currently Y entries`.
- **stderr**:
  - Informational logs (progress, retry notices when `--verbose`).
  - Error messages prefixed with `ERROR:`.

### JSON Mode (`--json`)
- **stdout**: single JSON object adhering to schema below.

```json
{
  "run_started_at": "2025-10-03T10:15:00Z",
  "run_finished_at": "2025-10-03T10:15:04Z",
  "was_full_refresh": false,
  "new_links": 42,
  "total_links": 1050,
  "db_path": "/Users/name/Library/Application Support/raindrop_enhancer/raindrops.db"
}
```

- **stderr**: only logs when `--verbose` (unless `--quiet`).

### Failures
- On DB corruption detection without `--full-refresh`, CLI exits `1` and prints guidance: `Detected database corruption. Re-run with --full-refresh to rebuild archive.`
- On network failure after retries, CLI reports the failing endpoint and total retries before exiting `1`.

## Database Side Effects
- Baseline run creates directory if missing, initializes schema, populates tables within a transaction, and writes `sync_state` row with `last_cursor_iso` equal to latest `created` value.
- Incremental run inserts only links with `created` strictly greater than `last_cursor_iso`; duplicates are skipped silently.
- `--full-refresh` performs backup (`<db>.bak`), drops tables, recreates schema, and runs baseline logic.
- `--dry-run` leaves database untouched.

## External API Calls
- `GET /rest/v1/collections` — same as existing exporter contract; used to discover collection IDs.
- `GET /rest/v1/raindrops/{collectionId}` with query parameters:
  - `perpage=200`
  - `page=<0..N>`
  - `sort=created`
  - `search=created:>=${iso_cursor} -is:archived -is:duplicate`
- Stop requesting additional pages when `items` empty or all `created` timestamps ≤ stored cursor.
- Honor HTTP 429 handling with exponential backoff (initial 1s, max 16s, total ≤60s).

## Observability
- Every run logs: total API requests, retries, new link count, elapsed time. Logs go to stderr unless `--quiet`.
- Store `synced_at` timestamp for each link to allow future audit queries.

## Preconditions & Assumptions
- Only one sync runs at a time per token (single-device assumption). Concurrent runs may be blocked in future via DB lock file but are currently unsupported.
- SQLite file may be manually backed up or inspected; schema changes require bumping `db_version` and `PRAGMA user_version`.
