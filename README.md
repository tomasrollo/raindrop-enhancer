Raindrop Enhancer

See the project Constitution at `.specify/memory/constitution.md` for core principles, quality gates, and governance. All plans and tasks must comply with these standards.


Tooling

This project uses `uv` for Python package, dependency, and build management. Use `uv run` for commands and keep lockfiles current via `uv lock`/`uv sync`.

## Usage

All commands should be run with `uv run` for environment consistency.

### Configure
```bash
uv run raindrop-enhancer configure --config ~/.config/raindrop-enhancer/config.toml
```
Interactively sets up your config file (token, DB path, etc). File permissions are set to 0600.

### Full Sync
```bash
uv run raindrop-enhancer --config ~/.config/raindrop-enhancer/config.toml sync --mode full --json-output
```
Performs a full sync, exporting all links and tags to JSON. Use `--dry-run` to avoid writing outputs.

### Incremental Sync
```bash
uv run raindrop-enhancer --config ~/.config/raindrop-enhancer/config.toml sync --mode incremental --since 2d
```
Syncs only links updated in the last 2 days.

### Status
```bash
uv run raindrop-enhancer --config ~/.config/raindrop-enhancer/config.toml status
```
Shows last sync run, rate-limit status, and export path.

### Reprocess
```bash
uv run raindrop-enhancer --config ~/.config/raindrop-enhancer/config.toml reprocess --id 123456789 --reason "content fixed"
```
Reprocesses a specific link (stub).

## Rate Limit Guidance

- The Raindrop API enforces a 120-requests-per-minute limit. The CLI captures and displays `X-RateLimit-*` headers after each sync.
- If you hit the limit, the CLI will retry with exponential backoff up to 60s, then exit with a warning if still rate-limited.
- Wait until the reported `rate_limit_reset` time before retrying a sync.

## Troubleshooting

- **Rate limit exceeded**: Wait for `rate_limit_reset` before retrying. Use `--dry-run` to test without writing outputs.
- **Content extraction failures**: Check `$DATA/manual_review.log` for details. Use `reprocess` after manual review.
- **Config file not found/permissions**: Ensure the config path is correct and file permissions are 0600. Use `configure` to regenerate.
- **Token expired**: Delete or edit your config file and rerun `configure`.

See `specs/001-build-an-application/quickstart.md` for a full workflow and advanced usage.
