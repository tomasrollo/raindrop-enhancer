# Raindrop Enhancer

See the project Constitution at `.specify/memory/constitution.md` for core principles, quality gates, and governance. All plans and tasks must comply with these standards.

## Tooling

This project uses `uv` for Python package, dependency, and build management. Use `uv run` for commands and keep lockfiles current via `uv lock`/`uv sync`.

## Quickstart (summary)

CLI: `raindrop-enhancer <subcommand>`

- Default behavior: outputs a JSON array of active raindrops to stdout.
- Common flags:
	- `--output <path>`: write JSON to a file instead of stdout.
	- `--quiet`: suppress progress/status messages.
	- `--verbose`: enable structured logging and detailed progress.
	- `--dry-run`: validate token and list collection counts without exporting raindrops.
	- `--pretty`: show a human-friendly summary table (instead of JSON).

Run example:

```bash
uv run raindrop-enhancer export --verbose --output my_raindrops.json
```

## Database-backed sync

The project includes a `raindrop-enhancer sync` command which persists raindrops into a local
SQLite database and supports incremental runs via a recorded cursor.

Default DB locations:

- macOS: `~/Library/Application Support/raindrop_enhancer/raindrops.db`
- Linux: `~/.local/share/raindrop_enhancer/raindrops.db`
- Windows: `%APPDATA%\\raindrop_enhancer\\raindrops.db`

Run a baseline sync:

```bash
uv run raindrop-enhancer sync --json
```

Use `--db-path` to override the DB file location for testing:

```bash
uv run raindrop-enhancer sync --db-path ./tmp/test.db --json
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
uv run raindrop-enhancer capture --db-path ./tmp/test.db --dry-run --limit 10

# Process links and persist fetched YouTube metadata when present
uv run raindrop-enhancer capture --db-path ./tmp/raindrops.db --limit 200
```

### Content columns

The SQLite store ensures the content-related columns (`content_markdown`, `content_fetched_at`, `content_source`) exist whenever the database is opened. Older databases are upgraded automatically the next time you run `raindrop-enhancer capture` or interact with the store via Python.

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
uv run raindrop-enhancer tag --db-path ./tmp/raindrops.db --dry-run --verbose
```

Persist generated tags (writes to DB):

```bash
uv run raindrop-enhancer tag --db-path ./tmp/raindrops.db
```

Important flags:
- `--fail-on-error`: return non-zero exit code (4) if any individual link generation failed
- `--json`: print a JSON summary (suitable for CI parsing)

Exit codes:
- `0` — success
- `2` — DSPy required but not configured
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

### LLM / DSPy environment variables

When using the auto-tagging feature the CLI configures DSPy (the DSPy library) and an underlying language model (LM). The following environment variables control that behavior; they are looked up by `src/raindrop_enhancer/content/dspy_settings.py`.

- `RAINDROP_DSPY_MODEL` — Optional. DSPy model identifier in the form `<provider>/<model>` (example: `openai/gpt-4o-mini`). Default: `openai/gpt-4o-mini` when not set.
- `RAINDROP_DSPY_TRACK_USAGE` — Optional. If set to `1` enables DSPy LM usage tracking so token counts may be recorded in generated metadata. Default: `0` (disabled).
- `RAINDROP_DSPY_{PROVIDER}_API_KEY` — Optional. Provider-specific API key (e.g. `RAINDROP_DSPY_OPENAI_API_KEY`) — highest priority when present.
- `{PROVIDER}_API_KEY` — Optional fallback for common provider env names (e.g. `OPENAI_API_KEY`, `ANTHROPIC_API_KEY`).
- `RAINDROP_DSPY_API_KEY` — Optional fallback generic API key used if provider-specific keys are not present.
- `RAINDROP_DSPY_API_BASE` — Optional. Custom API base URL for OpenAI-compatible or provider endpoints (e.g. for self-hosted or proxied endpoints). Falls back to `{PROVIDER}_API_BASE` if present.

Examples:

```bash
# Preferred (provider-specific):
export RAINDROP_DSPY_OPENAI_API_KEY="sk-..."

# Or use the common name OpenAI expects:
export OPENAI_API_KEY="sk-..."

# Enable usage tracking to capture tokens used in metadata
export RAINDROP_DSPY_TRACK_USAGE=1

# Override model (optional; defaults to openai/gpt-4o-mini):
export RAINDROP_DSPY_MODEL=openai/gpt-4o-mini
```

Notes:

- The `tags generate` command requires DSPy to be configured. If DSPy cannot be configured with the specified model and credentials, the command will exit with code `2`.

- For CI or production runs, set the `RAINDROP_DSPY_*` environment variables to ensure the predictor is available.
