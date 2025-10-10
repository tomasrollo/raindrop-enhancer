````markdown
# CLI Contract: `raindrop-enhancer`

This document defines the contract for the `raindrop-enhancer` CLI and its subcommands. Contract tests must assert the CLI's I/O shape, flags, exit codes, and help output.

## Global behavior
- `--help` or `-h`: prints help to stdout (exit code 0)
- `--version`: prints version to stdout (exit code 0)
- `--json`: when supported by a subcommand, produce machine-readable JSON to stdout
- `--quiet` / `--verbose` flags: control logging levels; quiet suppresses non-error output, verbose enables debug output
- Errors MUST be printed to stderr and exit with a non-zero code

## Mapping note
The following contract maps each existing command implementation in `src/raindrop_enhancer/cli.py` to the new top-level `raindrop-enhancer <subcommand>` shape. Tests should validate that each subcommand preserves the same flags and runtime behavior as the original commands.

## Subcommands and options (detailed)

1) export (originally the module-level `main` command)
- Command name: `raindrop-enhancer export`
- Options:
	- `--output PATH` (default `-`) — output file path; `-` means stdout
	- `--quiet` — suppress non-error output
	- `--verbose` — verbose output (debug logging)
	- `--dry-run` — validate without writing output
	- `--pretty` — pretty-print JSON output when applicable
	- `--enforce-rate-limit/--no-enforce-rate-limit` (default: `--no-enforce-rate-limit`) — enforce request pacing
	- `--rate-limit N` (default: 120) — requests per minute when enforcing rate limit
- Behavior:
	- Requires environment variable `RAINDROP_TOKEN`; if missing, prints error to stderr and exits with code `2`.
	- On success prints informative summary to stdout (unless `--quiet`) and exits `0`.
	- On predictable failure modes (export-specific failure) tests should assert a distinct non-zero exit code (contract tests may assert exit codes for simulated failures where possible).

2) sync
- Command name: `raindrop-enhancer sync`
- Options:
	- `--db-path PATH` — path to SQLite DB (optional)
	- `--full-refresh` — perform full refresh (backup & rebuild)
	- `--dry-run` — run without writing to DB
	- `--json` — emit JSON summary to stdout
	- `--quiet` — suppress non-error output
	- `--verbose` — verbose output
	- `--enforce-rate-limit/--no-enforce-rate-limit` (default: `--enforce-rate-limit`) — enforce pacing
	- `--rate-limit N` (default: 120)
- Behavior:
	- Requires `RAINDROP_TOKEN`; if missing, prints error to stderr and exits `2`.
	- On non-recoverable sync failure, the implementation raises or exits with a non-zero code (contract tests should assert for expected error handling; a representative failure in code uses exit `1` for orchestrator exceptions).
	- When `--json` is used the command prints a JSON object with run timestamps, counts, and db_path.

3) capture (maps to `capture-content`)
- Command name: `raindrop-enhancer capture` (maps from `capture-content` implementation)
- Options:
	- `--db-path PATH` — path to SQLite DB (optional)
	- `--limit N` — maximum links to process
	- `--dry-run` — do not mutate DB
	- `--refresh` — refresh existing captured content
	- `--json` — emit JSON summary
	- `--timeout FLOAT` (default 10.0) — per-link fetch timeout (seconds)
	- `--quiet` / `--verbose`
- Behavior:
	- Runs capture flow using Trafilatura; returns `0` on success.
	- If processed > 0 and every capture attempt failed, the code exits with `1` (per current implementation). Contract tests should assert this mapping.

4) migrate
- Command name: `raindrop-enhancer migrate`
- Options:
	- `--db-path PATH` — path to SQLite DB (optional)
	- `--target IDENT` (default `content-markdown`) — migration target
	- `--yes` — apply migration without prompting
	- `--quiet`
- Behavior:
	- Prints migration summary to stdout; on unknown target prints to stderr and exits `2`.
	- Backup or migration failures should exit non-zero (current implementation uses exit `1` for backup/migration errors).

5) tag (maps to `tags generate` group)
- Command name: `raindrop-enhancer tag` (or `raindrop-enhancer tags generate` if preserving original group name; tests should assert whichever naming decision is implemented)
- Options (from `tags_generate`):
	- `--db-path PATH`
	- `--limit N`
	- `--dry-run`
	- `--json` — emit JSON summary
	- `--quiet` / `--verbose`
	- `--fail-on-error` — exit non-zero if any individual link generation failed
- Behavior:
	- Attempts to configure DSPy via `configure_dspy()`; if DSPy is not configured or missing, the command prints an error to stderr explaining how to install/configure DSPy (example: `pip install dspy` or `uv run pip install dspy`) and exits with code `2`.
	- Persists generated tags when not `--dry-run`; on DB persist failure exits with code `3`.
	- If `--fail-on-error` and any individual generation failed, exits with code `4`.

## Contract test expectations
- Verify top-level help text lists subcommands and shows per-subcommand help with the exact flags above.
- For each subcommand, snapshot the help output and assert stability across changes.
- Simulate missing prerequisites (e.g., missing `RAINDROP_TOKEN`, missing `dspy`) and assert the command prints a clear error to stderr and exits with the specified non-zero code.
- For subcommands that support `--json`, validate JSON schema of the output in a contract test.
- Assert that `--quiet` suppresses non-error stdout, and `--verbose` enables debug-level logging messages to stderr.

````
