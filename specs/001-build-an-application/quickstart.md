# Quickstart — Raindrop Link Enhancer CLI

_Date: 2025-10-01_

## Prerequisites
- Python 3.13 installed
- `uv` available on PATH (`pipx install uv` if needed)
- Raindrop Test token or OAuth access token (see [Raindrop authentication docs](https://developer.raindrop.io/v1/authentication))
- LLM tagging API credentials (HTTP JSON endpoint)


## 1. Clone & Environment Setup
```bash
uv sync
uv run python --version
```

> **Note:** All CLI commands accept a global `--config <path>` option to specify the config file location. If omitted, the default is `$RAINDROP_ENHANCER_DATA/config.toml`.

## 2. Configure Data Directory
```bash
export RAINDROP_ENHANCER_DATA=~/raindrop-data
mkdir -p "$RAINDROP_ENHANCER_DATA"
chmod 700 "$RAINDROP_ENHANCER_DATA"
```

## 3. First-Time Configuration
```bash
uv run raindrop-enhancer configure \
  --token "$RAINDROP_TOKEN" \
  --data-dir "$RAINDROP_ENHANCER_DATA" \
  --llm-api-base "https://api.example.com/tag" \
  --llm-api-key "$LLM_API_KEY" \
  --tag-threshold 0.6 \
  --max-tags 10
```
- Creates `config.toml` with `0600` permissions inside data dir.


## 4. Run Full Sync (TDD Red → Green)
1. Execute tests first (expected to fail until implementation completes):
   ```bash
   uv run pytest tests/contract -k "raindrop_api or cli_contract"
   ```
2. After implementing failing tests, run full suite:
   ```bash
   uv run pytest
   ```
3. Execute full sync:
   ```bash
   uv run raindrop-enhancer sync --mode full --json-output --config "$RAINDROP_ENHANCER_DATA/config.toml"
   ```
   - Use `--dry-run` to test API fetches without writing outputs.
4. Inspect generated JSON export in `$RAINDROP_ENHANCER_DATA/exports/latest.json`, verify tags/status fields, and confirm `rate_limit_remaining` / `rate_limit_reset` values reflect the documented 120-requests-per-minute window.


## 5. Incremental Sync
```bash
uv run raindrop-enhancer sync --mode incremental --since last --config "$RAINDROP_ENHANCER_DATA/config.toml"
```
- Uses collection-level timestamps to fetch only updated links.
- `--dry-run` is supported here as well.

## 6. Reprocess Specific Link
```bash
uv run raindrop-enhancer reprocess --id 123456789 --reason "content fixed"
```

## 7. Status & Audit Trail
```bash
uv run raindrop-enhancer status --json
```
- Displays latest `SyncRun` entries, pending manual reviews, and export path.

## 8. Performance Smoke (10% dataset)
```bash
uv run python scripts/perf/benchmark_sync.py --fixtures fixtures/links_1k.json
```
- Ensure run completes within 6 seconds (10% of 60s budget).

## 9. Cleanup / Token Rotation
```bash
rm "$RAINDROP_ENHANCER_DATA/config.toml"
rm -rf "$RAINDROP_ENHANCER_DATA"/exports/*
```
- On next run, CLI will prompt for new token or use `configure` command.


## Rate Limit & Troubleshooting
- **Rate limits:** The CLI automatically retries with exponential backoff up to 60s and reports Raindrop `X-RateLimit-*` headers. If you hit the 120-requests-per-minute limit, wait until `rate_limit_reset` before rerunning.
- **Content extraction failures:** Logged to `$DATA/manual_review.log`; use `reprocess` after manual checks.
- **Config file issues:** Ensure the config path is correct and permissions are 0600. Use `configure` to regenerate if needed.
- **Token expired:** Delete or edit your config file and rerun `configure`.
- **Dry run:** Use `--dry-run` to exercise API fetches without writing JSON export.
