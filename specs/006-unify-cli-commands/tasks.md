````markdown
# Tasks: Unify CLI commands into `raindrop-enhancer`

Feature: Unify existing console scripts into a single CLI entrypoint `raindrop-enhancer` with subcommands `export`, `sync`, `capture`, `migrate`, `tag` (breaking change — old scripts removed).

Order: TDD-first, setup -> contract tests -> unit/integration tests -> implementation -> polish

Parallelizable tasks are marked [P]. Tasks that must run sequentially are unmarked.

T001 - Setup: Ensure development tooling and CI gates (SEQUENTIAL)
- Status: completed
- Purpose: Ensure consistent dev environment and CI gate compliance per Constitution.
- Edits / Commands:
  - Verify `pyproject.toml` contains dev dependency group for `pytest`, `pytest-httpx`, `pytest-asyncio`
  - Files: `/Users/tomas/Documents/projects/raindrop-enhancer/pyproject.toml`

T002 - Contract tests: Top-level help and per-subcommand help snapshots [P]
- Status: completed
- Purpose: Capture and lock top-level and subcommand help outputs.
- Test to add: `tests/contract/test_cli_help.py`
- Test actions:
  - Use Click's `CliRunner` to invoke `raindrop-enhancer --help` and assert exit code 0 and stable snapshot.
  - For each subcommand (`export`, `sync`, `capture`, `migrate`, `tag generate`), run `<command> --help` and snapshot output.
- Files to create: `tests/contract/test_cli_help.py`
- Dependencies: uses current `src/raindrop_enhancer/cli.py` imports; ensure entrypoint callable via Click group when implemented.

T003 - Contract tests: Missing prerequisites behavior (RAINDROP_TOKEN, dspy) [P]
- Status: completed
- Purpose: Validate clear error messages and exit codes for missing prerequisites.
- Tests to add: `tests/contract/test_cli_missing_prereqs.py`
- Test cases:
  - Invoke `export`/`sync`/`capture` without `RAINDROP_TOKEN` set; assert exit code `2` and stderr contains `Missing RAINDROP_TOKEN`.
  - Invoke `tag generate` while simulating `configure_dspy()` raising `DSPyConfigError`; assert exit code `2` and stderr contains `DSPy configuration required` and install suggestion `pip install dspy`.
- Files to create: `tests/contract/test_cli_missing_prereqs.py`

T004 - Contract tests: JSON output schema validation [P]
- Status: completed
- Purpose: Ensure `--json` outputs valid JSON with expected keys.
- Tests to add: `tests/contract/test_cli_json_outputs.py`
- Test cases:
  - For `sync --json` assert JSON contains keys: `run_started_at`, `run_finished_at`, `new_links`, `total_links`, `db_path`, `requests_made`, `retries`.
  - For `capture --json` assert JSON contains `session` and `attempts` keys.
  - For `tag --json` assert JSON summary contains `processed`, `generated`, `failed`, `db`, `model`.
- Files to create: `tests/contract/test_cli_json_outputs.py`

T005 - Integration tests: Quickstart scenarios [P]
- Status: completed
- Purpose: Implement integration tests that mirror `quickstart.md` happy paths.
- Tests to add: `tests/integration/test_quickstart_export_sync_capture.py`
- Scenarios:
  - Run `raindrop-enhancer export --output -` with a mocked Raindrop API (use pytest-httpx or monkeypatch RaindropClient) and assert expected stdout counts and exit code 0.
  - Run `raindrop-enhancer sync --dry-run` with orchestrator stub to assert dry-run summary.
  - Run `raindrop-enhancer capture --dry-run` with Trafilatura fetcher stub to assert processed output.
- Files to create: `tests/integration/test_quickstart_export_sync_capture.py`

T006 - Unit tests: CLI flag handling and logging behavior [P]
- Status: completed
- Purpose: Ensure `--quiet`/`--verbose`/`--dry-run` flags alter behavior as expected.
- Tests to add: `tests/unit/test_cli_flags.py`
- Cases:
  - `--quiet` suppresses non-error output (assert stdout empty for summary), `--verbose` logs debug to stderr.
  - `--dry-run` causes early exit with dry-run summary message.
- Files to create: `tests/unit/test_cli_flags.py`

T007 - Implementation: Add `raindrop-enhancer` console script in `pyproject.toml` (SEQUENTIAL)
- Status: completed
- Purpose: Add new entrypoint and remove legacy console scripts per FR-005.
- Edits:
  - Update `pyproject.toml` [project.scripts]: remove `raindrop-export`, `raindrop-sync`, `capture-content`, `raindrop-migrate`, `raindrop-tags` keys and add `raindrop-enhancer = "raindrop_enhancer.cli:cli"` (or the Click group function path). Ensure naming matches module's Click group (create group function if needed).
  - Files: `/Users/tomas/Documents/projects/raindrop-enhancer/pyproject.toml`
  - Note: This is a breaking change — ensure tests updated to call the new entrypoint.

T008 - Implementation: Convert existing command functions into Click subcommands under a Click group (SEQUENTIAL)
- Status: completed
- Purpose: Wire current `main`, `sync`, `capture_content`, `migrate`, and tags commands into a single Click group function.
- Edits:
  - Modify `/Users/tomas/Documents/projects/raindrop-enhancer/src/raindrop_enhancer/cli.py`:
    * Define a `@click.group()` function named `cli` or `raindrop_enhancer_cli` at module top.
    * Register existing commands as `@cli.command(name="export")` (for `main`), `@cli.command(name="sync")`, `@cli.command(name="capture")` (wrap `capture_content`), `@cli.command(name="migrate")`, and a sub-group/command for tagging (`@cli.group(name="tag")` with `generate` subcommand) preserving their existing function signatures and behaviors.
    * Keep existing environment checks and exit codes.
  - Files: `/Users/tomas/Documents/projects/raindrop-enhancer/src/raindrop_enhancer/cli.py`

T009 - Implementation: Update tagging flow to implement FR-006 behavior (SEQUENTIAL)
- Status: completed
- Purpose: Ensure `tag generate` prints actionable error when DSPy missing and exit `2`.
- Edits:
  - In `tags_generate`, catch `DSPyConfigError` and ensure stderr message contains `pip install dspy` and exit code `2` (currently raises SystemExit(2) but ensure message includes install guidance).
  - Files: `/Users/tomas/Documents/projects/raindrop-enhancer/src/raindrop_enhancer/cli.py` and `/Users/tomas/Documents/projects/raindrop-enhancer/src/raindrop_enhancer/content/dspy_settings.py`

T010 - Tests: Update existing tests referencing old console scripts (SEQUENTIAL)
- Status: completed
- Purpose: Migrate tests to invoke `raindrop-enhancer` entrypoint instead of legacy script names.
- Edits:
  - Search in `tests/` for usages of `raindrop-export`, `raindrop-sync`, `capture-content`, `raindrop-migrate`, `raindrop-tags` and replace with `raindrop-enhancer <subcommand>` or adjust to call Click commands via `CliRunner`.
  - Files: multiple under `/Users/tomas/Documents/projects/raindrop-enhancer/tests/` (update in-place).

T011 - Implementation: Update README, quickstart, and CHANGELOG (SEQUENTIAL)
  - Purpose: Document new invocation and migration steps.
  - Edits:
    - Update `README.md` usage examples to use `raindrop-enhancer`.
    - Add change note describing removal of legacy scripts and example sed snippet from `quickstart.md`.
    - Files: `/Users/tomas/Documents/projects/raindrop-enhancer/README.md`, `/Users/tomas/Documents/projects/raindrop-enhancer/specs/006-unify-cli-commands/quickstart.md`
  - Status: completed

T012 - Polish: Lint, types, and CI (P)
- Purpose: Run formatting, linting, typing, and full tests.
- Actions:
  - Run `uv run ruff check .`, `uv run mypy .`, `uv run pytest -q` and fix reported issues.
  - Ensure new/changed files have docstrings and comments where appropriate.

T013 - Polish: Release notes and MAJOR bump (SEQUENTIAL)
- Purpose: Prepare release notes and bump version for breaking change.
- Edits:
  - Update `CHANGELOG.md` or `pyproject.toml` version and add migration instructions in `docs/` or `specs/.../quickstart.md`.

Parallel groups examples
- Group A [P]: Contract tests (T002, T003, T004) can run in parallel
- Group B [P]: Unit/integration tests (T005, T006) can run in parallel after Group A passes

Notes about monotonic ordering
- Tests must be created and committed before implementing corresponding code changes to follow TDD.
- Keep commits small and focused: tests -> minimal implementation -> tests pass -> refactor.

````
