Raindrop Enhancer


See the project Constitution at `.specify/memory/constitution.md` for core principles, quality gates, and governance. All plans and tasks must comply with these standards.

## Tooling

This project uses `uv` for Python package, dependency, and build management. Use `uv run` for all commands and keep lockfiles current via `uv lock`/`uv sync`.

---

## CLI Usage

All commands should be run with `uv run` for environment consistency. For a full workflow and advanced usage, see [Quickstart](specs/001-build-an-application/quickstart.md).

### Configure
```bash
uv run raindrop-enhancer configure --config ~/.config/raindrop-enhancer/config.toml
```
Interactively sets up your config file (token, DB path, etc). File permissions are set to 0600. You can also pass flags for non-interactive setup:
```bash
uv run raindrop-enhancer configure \
	--token "$RAINDROP_TOKEN" \
	--data-dir "$RAINDROP_ENHANCER_DATA" \
	--llm-api-base "https://api.example.com/tag" \
	--llm-api-key "$LLM_API_KEY" \
	--tag-threshold 0.6 \
	--max-tags 10
```

### Full Sync
```bash
uv run raindrop-enhancer --config ~/.config/raindrop-enhancer/config.toml sync --mode full --json-output
```
Performs a full sync, exporting all links and tags to JSON. Use `--dry-run` to test API fetches without writing outputs.

### Incremental Sync
```bash
uv run raindrop-enhancer --config ~/.config/raindrop-enhancer/config.toml sync --mode incremental --since 2d
```
Syncs only links updated in the last 2 days. `--since` accepts values like `last`, `2d`, or an ISO timestamp.

### Status
```bash
uv run raindrop-enhancer --config ~/.config/raindrop-enhancer/config.toml status --json
```
Shows last sync run, rate-limit status, and export path. Use `--json` for machine-readable output.

### Reprocess
```bash
uv run raindrop-enhancer --config ~/.config/raindrop-enhancer/config.toml reprocess --id 123456789 --reason "content fixed"
```
Reprocesses a specific link after manual review.

---

## Rate Limit Guidance

- The Raindrop API enforces a 120-requests-per-minute limit. The CLI captures and displays `X-RateLimit-*` headers (`rate_limit_limit`, `rate_limit_remaining`, `rate_limit_reset`) after each sync.
- If you hit the limit, the CLI will retry with exponential backoff up to 60s, then exit with a warning if still rate-limited.
- Wait until the reported `rate_limit_reset` time before retrying a sync.
- Use `status` to check your current rate-limit state.

---

## Troubleshooting

- **Rate limit exceeded**: Wait for `rate_limit_reset` before retrying. Use `--dry-run` to test without writing outputs.
- **Content extraction failures**: Check `$DATA/manual_review.log` for details. Use `reprocess` after manual review.
- **Config file not found/permissions**: Ensure the config path is correct and file permissions are 0600. Use `configure` to regenerate.
- **Token expired**: Delete or edit your config file and rerun `configure`.
- **Dry run**: Use `--dry-run` to exercise API fetches without writing JSON export.

### Common Issues

- **Database errors**: Ensure your DB path is writable and not locked by another process.
- **API errors**: Check your token validity and network connectivity. Inspect CLI output for error messages.
- **Export not found**: Confirm the export path in your config and check for errors in the sync output.
- **Manual review required**: See `$DATA/manual_review.log` for links needing attention.

---

For a full workflow, advanced usage, and troubleshooting, see [`specs/001-build-an-application/quickstart.md`](specs/001-build-an-application/quickstart.md).
