# Raindrop Enhancer

See the project Constitution at `.specify/memory/constitution.md` for core principles, quality gates, and governance. All plans and tasks must comply with these standards.

## Tooling

This project uses `uv` for Python package, dependency, and build management. Use `uv run` for commands and keep lockfiles current via `uv lock`/`uv sync`.

## Quickstart (summary)

CLI: `raindrop-export`

- Default behavior: outputs a JSON array of active raindrops to stdout.
- Common flags:
	- `--output <path>`: write JSON to a file instead of stdout.
	- `--quiet`: suppress progress/status messages.
	- `--verbose`: enable structured logging and detailed progress.
	- `--dry-run`: validate token and list collection counts without exporting raindrops.
	- `--pretty`: show a human-friendly summary table (instead of JSON).

Run example:

```bash
uv run raindrop-export --verbose --output my_raindrops.json
```

## Database-backed sync

The project includes a `raindrop-sync` command which persists raindrops into a local
SQLite database and supports incremental runs via a recorded cursor.

Default DB locations:

- macOS: `~/Library/Application Support/raindrop_enhancer/raindrops.db`
- Linux: `~/.local/share/raindrop_enhancer/raindrops.db`
- Windows: `%APPDATA%\\raindrop_enhancer\\raindrops.db`

Run a baseline sync:

```bash
uv run raindrop-sync --json
```

Use `--db-path` to override the DB file location for testing:

```bash
uv run raindrop-sync --db-path ./tmp/test.db --json
```

## Capture content

The project also includes a `capture-content` command to capture full-text Markdown for saved links and persist it into the SQLite database.

Basic usage:

```bash
uv run capture-content --dry-run --limit 10 --verbose
uv run capture-content --limit 100
uv run capture-content --refresh --limit 50
```

## YouTube links

The capture pipeline now includes special handling for YouTube video links. When a saved link is identified as a YouTube video the system will use `yt-dlp` to fetch the video's title and description (without downloading the full video) and save it into the `content_markdown` column as Markdown:

```
# {title}

{description}
```

Behavior and notes:
- Dependency: `yt-dlp` is added to the project's dependencies. Ensure your environment can install native wheels if required.
- Timeout: the YouTube metadata fetch uses a 30-second timeout to avoid long hangs.
- Failure modes:
	- If the link is not a YouTube URL, capture falls back to Trafilatura as before.
	- If the video is unavailable, the extractor records a short error code and the capture attempt is marked as failed; you can inspect the CLI output for details.
	- If fetching metadata fails, the capture flow will not write partial/invalid content. Placeholder codes used in the data model include:
		- `[YOUTUBE VIDEO NOT AVAILABLE]` when the video is known to be missing (integration-dependent)
		- `[YOUTUBE METADATA FETCH FAILED]` when the extractor fails for other reasons

CLI examples (YouTube capture)

```bash
# Dry-run: show what would be processed (no DB writes)
uv run capture-content --db-path ./tmp/test.db --dry-run --limit 10

# Process links and persist fetched YouTube metadata when present
uv run capture-content --db-path ./tmp/raindrops.db --limit 200
```

### Migration note

You can add the `content_markdown` and `content_fetched_at` columns to your existing DB either via a one-off Python helper or via the new `migrate` CLI command that performs a safe backup and applies the schema change.

Run the migrate command (recommended):

```bash
uv run raindrop-migrate --db-path ~/.local/share/raindrop_enhancer/raindrops.db --target content-markdown --yes
```

This will create a timestamped backup of the DB and then ensure the `content_markdown`, `content_fetched_at`, and `content_source` columns exist. Omit `--yes` to be prompted for confirmation.

Alternative (Python one-off):

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

## Troubleshooting

- Missing token: create a `.env` file at the repository root with `RAINDROP_TOKEN=your_token_here`.
- Rate limit errors (HTTP 429): the CLI retries with exponential backoff; repeated failures indicate an exhausted rate budget—try again later or reduce parallelism.
- Empty output: run with `--dry-run --verbose` to inspect available collections and counts.

## Performance tests

Small performance smoke tests live under `tests/perf/`. They are skipped by default and must be enabled via environment variables. Example invocations:

```bash
# Run baseline perf test (small dataset)
ENABLE_PERF=1 PERF_COUNT=50 PERF_MAX_SECONDS=5 uv run pytest tests/perf/test_sync_baseline.py

# Run incremental perf test (baseline + incremental)
ENABLE_PERF=1 PERF_BASELINE_COUNT=50 PERF_INCREMENTAL_COUNT=10 PERF_INCREMENTAL_MAX_SECONDS=2 uv run pytest tests/perf/test_sync_incremental.py
```

## Auto-tagging (LLM-assisted)

You can generate auto-tags for links stored in the local SQLite DB using the DSPy-powered tag generator.

Basic dry-run (no DB writes):

```bash
uv run raindrop-enhancer tags generate --db-path ./tmp/raindrops.db --dry-run --verbose
```

Persist generated tags (writes to DB):

```bash
uv run raindrop-enhancer tags generate --db-path ./tmp/raindrops.db
```

Important flags:
- `--require-dspy`: fail immediately if DSPy is not configured (useful for CI/production to avoid fallback fake predictor)
- `--fail-on-error`: return non-zero exit code (4) if any individual link generation failed
- `--json`: print a JSON summary (suitable for CI parsing)

Exit codes:
- `0` — success
- `2` — DSPy required but not configured (when `--require-dspy` is used)
- `3` — persistence/write failure when saving generated tags
- `4` — per-link generation failures when `--fail-on-error` is used


Supported environment variables:
- ENABLE_PERF: set to `1` to run perf tests (default: tests are skipped)
- PERF_COUNT: number of synthetic items for baseline test (default: 1000)
- PERF_MAX_SECONDS: allowed seconds for baseline insert (default: 2.0)
- PERF_BASELINE_COUNT: baseline count for incremental test (default: 500)
- PERF_INCREMENTAL_COUNT: incremental items to insert (default: 50)
- PERF_INCREMENTAL_MAX_SECONDS: allowed seconds for incremental insert (default: 0.5)

These are small smoke-tests intended for quick local validation. For CI or larger benchmarks, increase counts and record results separately.
