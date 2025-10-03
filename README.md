Raindrop Enhancer

See the project Constitution at `.specify/memory/constitution.md` for core principles, quality gates, and governance. All plans and tasks must comply with these standards.

Tooling

This project uses `uv` for Python package, dependency, and build management. Use `uv run` for commands and keep lockfiles current via `uv lock`/`uv sync`.

Quickstart (summary)

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

Database-backed sync (new)

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

Troubleshooting

- Missing token: create a `.env` file at the repository root with `RAINDROP_TOKEN=your_token_here`.
- Rate limit errors (HTTP 429): the CLI retries with exponential backoff; repeated failures indicate an exhausted rate budget—try again later or reduce parallelism.
- Empty output: run with `--dry-run --verbose` to inspect available collections and counts.
