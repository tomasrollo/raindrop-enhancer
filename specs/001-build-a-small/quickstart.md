# Quickstart: Unified Raindrop Export CLI

## Prerequisites
- Python toolchain managed via `uv` (install per project README).
- Raindrop API test token with read access.
- `.env` file at repository root containing `RAINDROP_TOKEN=your_token_here`.

## Environment Setup
1. Sync dependencies (ensures Click, Rich, Gracy, python-dotenv available):
   ```bash
   uv sync
   ```
2. Confirm virtual environment activation for subsequent commands (uv handles automatically when using `uv run`).

## Run the CLI (happy path)
```bash
uv run raindrop-export --verbose
```
- Loads `.env`, validates token, shows Rich progress for collections & raindrops.
- Outputs JSON array of raindrops to stdout upon completion.

### Optional flags
- `--output path.json`: write JSON to file instead of stdout.
- `--quiet`: suppress progress/status messages.
- `--dry-run`: validate credentials and list collection counts without exporting raindrops.
- `--pretty`: render summary table (Rich) instead of JSON (primarily for manual inspection).

## Dry Run & Diagnostics
```bash
uv run raindrop-export --dry-run --verbose
```
- Verifies token and API connectivity.
- Prints collection inventory without fetching raindrops.

## Test Suite
1. Run unit & contract tests:
   ```bash
   uv run pytest tests/unit tests/contract
   ```
2. Run integration tests (CLI level):
   ```bash
   uv run pytest tests/integration
   ```
3. Generate coverage report (expect ≥90% on touched code):
   ```bash
   uv run pytest --cov=raindrop_enhancer --cov-report=term-missing
   ```

## Performance Smoke Test
After implementation, execute:
```bash
uv run raindrop-export --verbose --limit-mock 10000
```
- Uses mock fixture (to be added) to simulate 10k raindrops and ensures export completes within 60s.

## Performance & Troubleshooting Notes

- Performance expectation: exporting up to 10k active raindrops should complete within 60s on a typical developer machine when the mock fixture/run is used and network latency is reasonable. Real-world performance depends on network conditions and Raindrop API rate limiting (120 req/min), which the CLI respects via throttling and exponential backoff.
- If you see slower runs, enable `--verbose` to surface retry/backoff logs and consider running during off-peak hours or reducing per-request concurrency in a future configuration flag.

## Troubleshooting
- Missing token: ensure `.env` is in repo root and not ignored; rerun `uv run raindrop-export --help` to confirm CLI installed.
- Rate-limit errors: CLI automatically retries for up to 60s; repeated failures logged. Increase delay via future config flag if necessary.
- JSON output empty: verify user has collections or use `--dry-run` to inspect counts.
