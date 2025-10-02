# Raindrop Enhancer

Raindrop Enhancer is a Python CLI that synchronises collections from the Raindrop API, enriches each link with LLM-generated tags, and maintains both SQLite persistence and versioned JSON exports. It is designed for repeatable full and incremental syncs, resilient rate-limit handling, and rich operational telemetry.

## Installation

The project is managed with [uv](https://github.com/astral-sh/uv). Clone the repository and install dependencies:

```bash
uv sync
```

Verify the environment:

```bash
uv run python --version
uv run raindrop-enhancer --help
```

## Configuration

All runtime settings live in `config.toml` inside the configured data directory. Create or update it through the bundled `configure` command:

```bash
uv run raindrop-enhancer configure \
	--token "$RAINDROP_TOKEN" \
	--data-dir "$HOME/.raindrop-enhancer" \
	--llm-api-base "https://llm.example.com/tag" \
	--llm-api-key "$LLM_API_KEY" \
	--tag-threshold 0.65 \
	--max-tags 8
```

The CLI enforces `0600` permissions on `config.toml` to protect API credentials. Settings can also be bootstrapped by exporting `RAINDROP_ENHANCER_DATA` before running the CLI.

## Core Commands

- **Full sync** – pull every collection and write `exports/latest.json`:
	```bash
	uv run raindrop-enhancer sync --mode full --batch-size 50
	```
- **Incremental sync** – only process entries updated since the last run:
	```bash
	uv run raindrop-enhancer sync --mode incremental --since last
	```
- **Dry-run / JSON output** – inspect behaviour without touching disk:
	```bash
	uv run raindrop-enhancer --json --dry-run sync --mode full
	```
- **Targeted reprocess** – re-enrich a single bookmark:
	```bash
	uv run raindrop-enhancer reprocess --id 123456789 --reason "content fixed"
	```
- **Run status** – review recent executions and rate-limit telemetry:
	```bash
	uv run raindrop-enhancer status --json --limit 5
	```

All commands honour `--json`, `--verbose`, `--quiet`, `--dry-run`, and `--data-dir`. JSON output includes the sync summary, export path, and rate-limit counters so it can be scripted easily.

## Rate-Limit Telemetry

Every sync captures Raindrop `X-RateLimit-*` headers. These values are persisted on the associated `SyncRun`, surfaced in CLI summaries, and emitted as metrics:

- `rate_limit_remaining` – requests left in the current window.
- `rate_limit_limit` – documented 120 requests per minute.
- `rate_limit_reset` – UNIX epoch when the window resets (rendered in UTC).
- Metrics streamline into `retry.*` counters and gauges exposed via JSON output.

When the remaining budget drops toward zero, the CLI automatically backs off using jittered exponential retry logic, and the status command will highlight the reset timestamp.

## Troubleshooting

- **Missing token** – `sync` and `reprocess` exit with a helpful message if the Raindrop token is absent. Re-run `configure --token ...`.
- **Missing LLM credentials** – ensure both `--llm-api-base` and `--llm-api-key` are configured; they are required even for dry runs so tagging can proceed.
- **HTTP 429 / rate-limit exhaustion** – wait until the reported `rate_limit_reset` timestamp, or use `status` to confirm the next window, then rerun.
- **Content extraction failures** – entries with failed fetches are pushed to the manual review list; check the JSON export’s `failures` block or rerun `reprocess` after resolving the source.
- **Resetting state** – delete `config.toml`, the SQLite database, or the `exports/` directory inside the data directory to reset; the CLI will recreate them on the next run.

## Development

Key scripts are available via `uv run`:

```bash
uv run pytest --cov        # run tests with coverage (≥90%)
uv run raindrop-enhancer --help
```

The codebase follows the repository constitution (`.specify/memory/constitution.md`) for style, testing, and governance. Use `uv lock`/`uv sync` to manage dependencies and keep the lockfile up to date.
