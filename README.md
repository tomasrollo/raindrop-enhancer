# Raindrop Enhancer

See the project Constitution at `.specify/memory/constitution.md` for core principles, quality gates, and governance. All plans and tasks must comply with these standards.

## Tooling

This project uses `uv` for Python package, dependency, and build management. Use `uv run` for commands and keep lockfiles current via `uv lock`/`uv sync`.

## Quickstart

1. Install project dependencies with `uv sync`.
2. Provide a Raindrop API token via `.env` (`RAINDROP_TOKEN=...`) or your shell when you intend to call the Raindrop API (`export` and `sync`).
3. Inspect available commands with:
   ```bash
   uv run raindrop-enhancer --help
   ```

Example export:

```bash
uv run raindrop-enhancer export --verbose --output my_raindrops.json
```

Each subcommand also supports `--help` to list its flags.

## Command reference

All commands run as `uv run raindrop-enhancer <command> [options]`.

### Export (`raindrop-enhancer export`)

Fetch all active raindrops from the API and emit JSON to stdout or a file. **Requires** `RAINDROP_TOKEN`.

Options:
- `--output PATH` (default `-`): write JSON to a file instead of stdout.
- `--dry-run`: validate the token and list counts without writing output.
- `--pretty`: pretty-print JSON output.
- `--quiet` / `--verbose`: adjust logging verbosity.
- `--enforce-rate-limit/--no-enforce-rate-limit` (default `--no-enforce-rate-limit`): throttle requests.
- `--rate-limit N` (default `120`): requests per minute when rate limiting.

Exit codes: `0` success, `2` when `RAINDROP_TOKEN` is missing.

Example:

```bash
uv run raindrop-enhancer export --dry-run --verbose
```

### Sync (`raindrop-enhancer sync`)

Synchronize the Raindrop archive into a local SQLite database (incremental by default). **Requires** `RAINDROP_TOKEN`.

Options:
- `--db-path PATH`: override the database path (defaults to a platform config directory).
- `--full-refresh`: back up the existing DB, recreate schema, and perform a fresh sync.
- `--dry-run`: simulate without touching the DB.
- `--json`: emit a JSON summary instead of human-readable output.
- `--quiet` / `--verbose`: control logging noise.
- `--enforce-rate-limit/--no-enforce-rate-limit` (default `--enforce-rate-limit`): throttle requests.
- `--rate-limit N` (default `120`): requests per minute when rate limiting.

Default DB locations:

- macOS: `~/Library/Application Support/raindrop_enhancer/raindrops.db`
- Linux: `~/.local/share/raindrop_enhancer/raindrops.db`
- Windows: `%APPDATA%\\raindrop_enhancer\\raindrops.db`

Exit codes: `0` success, `1` on orchestrator error, `2` when `RAINDROP_TOKEN` is missing.

Example:

```bash
uv run raindrop-enhancer sync --db-path ./tmp/raindrops.db --json
```

### Capture (`raindrop-enhancer capture`)

Populate the SQLite store with Markdown content for saved links using Trafilatura and YouTube-specific handling.

Options:
- `--db-path PATH`: point at an alternate database (defaults to the sync location).
- `--limit N`: cap how many links to process.
- `--dry-run`: report what would be captured without writing.
- `--refresh`: re-fetch content even when already present.
- `--json`: emit a JSON session summary.
- `--timeout SECONDS` (default `10.0`): per-link fetch timeout.
- `--quiet` / `--verbose`: control logging.

Exit codes: `0` success, `1` when every processed link failed.

Example:

```bash
uv run raindrop-enhancer capture --db-path ./tmp/raindrops.db --limit 50
```

#### YouTube links

When a link is detected as a YouTube URL the capture flow uses `yt-dlp` to fetch the title and description (without downloading the video) and stores them in Markdown:

```
# {title}

{description}
```

Notes:
- Timeout: metadata fetches use a 30-second timeout to avoid long hangs.
- Failure handling: missing or failed videos record short error codes and do not write partial content.
- Fallback: non-YouTube links fall back to Trafilatura automatically.

#### Automatic content columns

The SQLite store adds the content-related columns (`content_markdown`, `content_fetched_at`, `content_source`) on connect, so no manual migration step is required.

### Tag (`raindrop-enhancer tag`)

Generate AI-assisted tags for links stored in the SQLite database using DSPy. Requires a configured DSPy predictor.

Options:
- `--db-path PATH`: override the database path.
- `--limit N`: cap how many links to tag.
- `--dry-run`: preview tags without writing.
- `--json`: emit a JSON summary (`processed`, `generated`, `failed`, `db`, `model`).
- `--quiet` / `--verbose`: adjust logging.
- `--fail-on-error`: exit non-zero if any individual link failed to generate tags.

Exit codes:
- `0` success
- `2` DSPy missing or misconfigured
- `3` database write failure
- `4` at least one link failed and `--fail-on-error` was supplied

Examples:

```bash
# Dry-run without writing tags
uv run raindrop-enhancer tag --db-path ./tmp/raindrops.db --dry-run --verbose

# Persist generated tags and fail if any generation failed
uv run raindrop-enhancer tag --db-path ./tmp/raindrops.db --fail-on-error
```

#### DSPy configuration

When tagging, the CLI loads DSPy configuration from environment variables read by `src/raindrop_enhancer/content/dspy_settings.py`:

- `RAINDROP_DSPY_MODEL` — Optional override for the DSPy model (`provider/model`, default `openai/gpt-4o-mini`).
- `RAINDROP_DSPY_TRACK_USAGE` — Set to `1` to enable token usage tracking (default `0`).
- `RAINDROP_DSPY_{PROVIDER}_API_KEY` — Provider-specific API key (e.g. `RAINDROP_DSPY_OPENAI_API_KEY`).
- `{PROVIDER}_API_KEY` — Common provider fallbacks (`OPENAI_API_KEY`, `ANTHROPIC_API_KEY`, etc.).
- `RAINDROP_DSPY_API_KEY` — Generic fallback API key.
- `RAINDROP_DSPY_API_BASE` — Override API base URL (falls back to `{PROVIDER}_API_BASE` if present).

Examples:

```bash
export RAINDROP_DSPY_OPENAI_API_KEY="sk-..."
export RAINDROP_DSPY_MODEL="openai/gpt-4o-mini"
export RAINDROP_DSPY_TRACK_USAGE=1
```

If DSPy cannot be configured, the command exits with code `2` and prints installation guidance (`uv add dspy` or `pip install dspy`).

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

Supported environment variables:
- ENABLE_PERF: set to `1` to run perf tests (default: tests are skipped)
- PERF_COUNT: number of synthetic items for baseline test (default: 1000)
- PERF_MAX_SECONDS: allowed seconds for baseline insert (default: 2.0)
- PERF_BASELINE_COUNT: baseline count for incremental test (default: 500)
- PERF_INCREMENTAL_COUNT: incremental items to insert (default: 50)
- PERF_INCREMENTAL_MAX_SECONDS: allowed seconds for incremental insert (default: 0.5)

These are small smoke-tests intended for quick local validation. For CI or larger benchmarks, increase counts and record results separately.

### LLM / DSPy environment variables

See the Tag command section (`README.md:117`) for details on configuring DSPy via environment variables.

Notes:

- The `tags generate` command requires DSPy to be configured. If DSPy cannot be configured with the specified model and credentials, the command will exit with code `2`.

- For CI or production runs, set the `RAINDROP_DSPY_*` environment variables to ensure the predictor is available.
