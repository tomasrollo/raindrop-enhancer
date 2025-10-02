# Quickstart — Raindrop Link Enhancer CLI

_Date: 2025-10-02_

## Prerequisites

- Python 3.13
- [`uv`](https://github.com/astral-sh/uv) on your `PATH`
- Raindrop API token (test token or OAuth) – see the [official docs](https://developer.raindrop.io/v1/authentication)
- LLM tagging endpoint and API key (HTTPS JSON service)

## 1. Bootstrap the Environment

```bash
uv sync
uv run python --version
```

Optionally pin the working data directory:

```bash
export RAINDROP_ENHANCER_DATA=~/raindrop-enhancer
mkdir -p "$RAINDROP_ENHANCER_DATA"
chmod 700 "$RAINDROP_ENHANCER_DATA"
```

## 2. Configure Credentials and Thresholds

Create the initial `config.toml` (permissions automatically enforced to `0600`):

```bash
uv run raindrop-enhancer configure \
  --token "$RAINDROP_TOKEN" \
  --data-dir "${RAINDROP_ENHANCER_DATA:-$HOME/.raindrop-enhancer}" \
  --llm-api-base "https://llm.example.com/tag" \
  --llm-api-key "$LLM_API_KEY" \
  --tag-threshold 0.65 \
  --max-tags 8
```

You can rerun `configure` at any time to rotate tokens or tweak thresholds.

## 3. Run Syncs

### Full sync

```bash
uv run raindrop-enhancer sync --mode full --batch-size 50
```

### Incremental sync

```bash
uv run raindrop-enhancer sync --mode incremental --since last
```

### Dry-run / JSON summary

```bash
uv run raindrop-enhancer --json --dry-run sync --mode full
```

### Targeted reprocess

```bash
uv run raindrop-enhancer reprocess --id 123456789 --reason "content fixed"
```

### Status dashboard

```bash
uv run raindrop-enhancer status --json --limit 5
```

Each command honours `--json`, `--verbose`, `--quiet`, and `--data-dir`. JSON responses include processed counts, export paths, and rate-limit telemetry for automation.

## 4. Observe Rate-Limit Telemetry

- `rate_limit_remaining`, `rate_limit_limit`, and `rate_limit_reset` are captured for every call and surfaced in the sync summary plus the `status` table.
- Metrics are also recorded internally (`retry.attempts`, `retry.delay_seconds`, `raindrop.rate_limit.*`) for downstream monitoring.
- When `rate_limit_remaining` reaches zero, the CLI backs off using jittered exponential retry. Wait until the displayed reset timestamp before rerunning.

## 5. Test & Validate

```bash
uv run pytest --cov
```

The suite covers contract, unit, and integration flows and currently reports ~93% statement coverage.

## 6. Maintenance and Cleanup

- To rotate credentials, rerun `configure` with new values.
- Remove `$RAINDROP_ENHANCER_DATA/config.toml` or the SQLite/`exports/` artefacts to reset state; the CLI will recreate them on the next run.
- For performance smoke tests, execute: `uv run python scripts/perf/benchmark_sync.py --fixtures fixtures/links_1k.json` (target: ≤60 seconds for 1k links).

## Troubleshooting

- **Missing token / LLM creds:** the CLI exits with guidance. Re-run `configure` with the missing values.
- **Rate-limited (HTTP 429):** inspect `rate_limit_reset` in the JSON summary or `status` output and rerun once the window resets. Retries back off automatically up to 60 seconds.
- **Content extraction failures:** affected links are flagged for manual review and listed in the sync summary. Use `reprocess --id ...` after addressing the underlying issue.
- **Unexpected retries:** structured retry logs are emitted as JSON (`logger=raindrop_enhancer.retry`). Enable `--verbose` to review them, or inspect the metrics block in the JSON response.
