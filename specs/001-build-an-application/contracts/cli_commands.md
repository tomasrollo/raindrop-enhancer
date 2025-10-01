# CLI Contract — Raindrop Link Enhancer

_Date: 2025-10-01_

## Command Group
`raindrop-enhancer [OPTIONS] COMMAND [ARGS]...`

Global options:
- `--json` (flag): Output machine-readable status payloads; disables rich progress.
- `--verbose`/`--quiet` (mutually exclusive): Control log verbosity; default INFO.
- `--dry-run` (flag): Fetch data but skip writes (SQLite, JSON export).
- `--data-dir PATH`: Override configured data directory.
- Exit codes: 0 success, 2 validation error (bad args/bad token), 3 external dependency failure (Raindrop/LLM), 4 internal error.

## Commands

### `configure`
- **Options**: `--token`, `--data-dir`, `--llm-api-base`, `--llm-api-key`, `--tag-threshold`, `--max-tags`
- **Behavior**: Writes/updates `config.toml` with `0600` permissions, verifying directories exist. Returns JSON summary when `--json` is active. Documentation references the Raindrop App Management Console for retrieving Test tokens or OAuth credentials.

### `sync`
- **Options**:
  - `--mode [full|incremental]` (required)
  - `--collection-id INT` (optional, repeats allowed)
  - `--since TIMESTAMP` (optional ISO8601 override for incremental runs)
  - `--batch-size INT` (default 50, max 100)
- **Output**: Rich progress bar per collection unless `--json/--quiet`; JSON summary includes counts (`processed`, `skipped`, `manual_review`, `failures`), export path, run ID, and latest Raindrop rate-limit telemetry (`rate_limit_remaining`, `rate_limit_reset`).
- **Error Handling**: On authentication failure exit code 2; on repeated rate-limit exhaustion exit code 3 with failure summary.

### `reprocess`
- **Options**: `--id INT` (required); `--collection-id INT` (optional); `--reason TEXT` (optional)
- **Behavior**: Clears existing tag suggestions, re-fetches content, re-runs tagging pipeline.
- **Output**: JSON object with `status`, `previous_status`, `new_tags`, `manual_review` flag.

### `status`
- **Options**: `--limit INT` (default 10)
- **Behavior**: Displays latest sync runs, pending manual reviews, and export metadata.
- **Output**: Table via `rich` or JSON array when `--json`.

## JSON Output Schema (shared)
```
{
  "run_id": "uuid",
  "mode": "full" | "incremental" | "reprocess",
  "processed": int,
  "skipped": int,
  "manual_review": int,
  "failures": [
    {
      "link_id": int,
      "reason": "string"
    }
  ],
  "export_path": "string",
  "timestamp": "ISO-8601",
  "duration_seconds": float
}
```

## Contract Tests (planned)
- `tests/contract/test_cli_contract.py` will assert flag availability, mutual exclusivity, and JSON schema.
- `tests/integration/test_full_sync.py` will validate summary totals align with SQLite contents.
