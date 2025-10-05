# Tasks: Full-Text Capture Command for Saved Links

**Input**: Design documents from `/specs/003-add-trafilatura-add/`
**Prerequisites**: plan.md (required), research.md, data-model.md, contracts/, quickstart.md

## Execution Flow (main)
```
1. Load plan.md from feature directory
   → If not found: ERROR "No implementation plan found"
   → Extract: tech stack, libraries, structure
2. Load optional design documents:
   → data-model.md: Extract entities → model tasks
   → contracts/: Each file → contract test task
   → research.md: Extract decisions → setup tasks
   → quickstart.md: Extract scenarios → integration/validation tasks
3. Generate tasks by category:
   → Setup: project init, dependencies, linting
   → Tests: contract tests, integration tests
   → Core: models, services, CLI commands
   → Integration: DB, middleware, logging
   → Polish: unit tests, performance, docs
4. Apply task rules:
   → Different files = mark [P] for parallel
   → Same file = sequential (no [P])
   → Tests before implementation (TDD)
5. Number tasks sequentially (T001, T002...)
6. Generate dependency graph
7. Create parallel execution examples
8. Validate task completeness:
   → All contracts have tests?
   → All entities have model tasks?
   → All endpoints implemented?
9. Return: SUCCESS (tasks ready for execution)
```

## Tasks
- [X] T001 Update dependencies: add Trafilatura (and optional accelerator `cchardet`) in `pyproject.toml`, run `uv add`, `uv lock`, and `uv sync` to refresh the environment.
- [X] T002 Create synthetic capture fixtures in `tests/fixtures/content_links.json` (or similar) to provide predictable HTML/Markdown inputs for tests.
- [X] T003 [P] Author failing contract tests in `tests/contract/test_cli_content_capture.py` covering CLI options, JSON schema, exit codes, and `--timeout` handling.
- [X] T004 [P] Author failing integration tests in `tests/integration/test_cli_content_capture.py` for fresh capture, refresh flag, partial failure exit status, and dry-run behavior using a temporary sqlite DB.
- [X] T005 [P] Author failing unit tests in `tests/unit/test_content_fetcher.py` validating Trafilatura interactions (timeouts, metadata flags, retry classification) with patched `trafilatura.fetch_url`/`extract`.
- [X] T006 [P] Author failing unit tests in `tests/unit/test_sqlite_store_content.py` validating schema migration, new columns, selection of uncaptured links, and persistence of Markdown blobs.
- [X] T007 Extend `src/raindrop_enhancer/storage/sqlite_store.py` to add content columns, upgrade logic (user_version bump), selection helpers, and write/update methods for Markdown plus timestamps.
- [X] T008 Update data models in `src/raindrop_enhancer/models.py` to include content fields on `RaindropLink` (or companion dataclass) and introduce `LinkCaptureAttempt`/`ContentCaptureSession` helpers.
- [X] T009 Implement Trafilatura fetcher service in `src/raindrop_enhancer/content/fetcher.py` providing a reusable class/function that manages shared session, markdown extraction, timeouts, and retry classification.
- [X] T010 Implement capture runner/coordinator in `src/raindrop_enhancer/content/capture_runner.py` orchestrating selection of pending links, invoking the fetcher, applying refresh semantics, and building session/attempt summaries.
- [X] T011 Integrate new runner with the CLI by adding a `capture-content` command in `src/raindrop_enhancer/cli.py` (ensure Click group/entrypoint updates, JSON/human output parity, Rich formatting, logging, and CLI flags per contract).
- [ ] T012 [P] Add performance baseline tests in `tests/perf/test_content_capture.py` to validate p95/p99 timing goals across ~100 link fixtures (using fakes/mocks where appropriate).
- [X] T013 [P] Update documentation (`README.md`, `docs/manual-testing.md`, `specs/003-add-trafilatura-add/quickstart.md`) with usage instructions, CLI help snippet, and troubleshooting for the new command.
- [X] T014 Run formatting and lint gates (`uv run ruff check .`, `uv run ruff format`, `uv run mypy src`) ensuring no regressions.
- [X] T015 Run automated tests (`uv run pytest` across contract, unit, integration, perf suites) and capture results for the changelog/PR summary.
- [ ] T016 Perform smoke tests: execute `uv run raindrop-enhancer capture-content` in dry-run and live modes against sample DB, verify Markdown persisted, and document observations.

## Dependencies
- T001 → T002-T016
- T002 → T003, T004 (fixtures required for tests)
- T003-T006 → T007-T011 (tests must fail before implementation)
- T007 → T008 (models rely on updated schema contract)
- T007-T010 → T011 (CLI wiring depends on data + services)
- T011 → T012, T016 (perf/smoke depend on complete command)
- T007-T011 → T014-T015 (quality gates run after implementation)
- T015 → T016 (smoke tests run after green suite)

## Parallel Execution Example
```
# Launch parallel test authoring once fixtures are ready (after T002):
Task: "T003 Author failing contract tests in tests/contract/test_cli_content_capture.py"
Task: "T004 Author failing integration tests in tests/integration/test_cli_content_capture.py"
Task: "T005 Author failing unit tests in tests/unit/test_content_fetcher.py"
Task: "T006 Author failing unit tests in tests/unit/test_sqlite_store_content.py"
```

## Notes
- Maintain TDD: ensure T003-T006 fail before moving to T007.
- Use `uv run` for all commands per constitution.
- Rich/Click output must remain deterministic for JSON mode.
- Performance targets: p95 < 5s/link, p99 < 500ms overhead, RSS < 150MB.
- Ensure new CLI command registers in entry points so `uv run raindrop-enhancer capture-content --help` works.
- Document migration/backfill steps clearly in README/manual testing.
