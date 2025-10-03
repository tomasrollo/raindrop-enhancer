# Tasks: Persistent Storage and Incremental Sync for Raindrop Links

**Input**: Design documents from `/specs/002-storage-and-sync/`
**Prerequisites**: plan.md (required), research.md, data-model.md, contracts/, quickstart.md

## Phase 3.1: Setup & Environment
- [ ] T001 Ensure uv environment is current by running `uv sync` and verifying `pyproject.toml` still pins required deps (no new packages expected).
- [ ] T002 [P] Create platform-specific data directory helpers preview (doc-only): note default DB paths in README draft (no code changes yet) to guide later implementation.

## Phase 3.2: Tests First (TDD) — must fail before implementation
- [X] T003 Create contract test for incremental Raindrop fetch in `tests/contract/test_raindrop_incremental_contract.py` covering `sort=created` query and cursor filter.
- [X] T004 [P] Add unit test skeletons in `tests/unit/test_sqlite_store.py` validating schema creation, insert batching, append-only constraint, and corruption detection via `PRAGMA quick_check`.
- [X] T005 [P] Add unit test skeletons in `tests/unit/test_sync_orchestrator.py` covering baseline sync, incremental sync, and full-refresh flag behavior.
- [X] T006 [P] Add integration test skeleton in `tests/integration/test_cli_sync.py` exercising CLI baseline run, incremental run (no new data), dry-run, and `--full-refresh` path with temp DB.
- [X] T007 [P] Define performance smoke test placeholders in `tests/perf/test_sync_baseline.py` and `tests/perf/test_sync_incremental.py` asserting target runtimes (skip markers allowed until implementation).

## Phase 3.3: Core Implementation (only after tests exist & fail)
- [X] T008 Implement SQLite storage module in `src/raindrop_enhancer/storage/sqlite_store.py` (schema creation, WAL mode, insert batching, sync_state management, corruption checks).
- [X] T009 Update `src/raindrop_enhancer/models.py` with persistence-friendly dataclasses/TypedDicts (`RaindropLink`, `SyncState`, `SyncOutcome`) mirroring `data-model.md`.
- [X] T010 Implement sync orchestration in `src/raindrop_enhancer/sync/orchestrator.py` (baseline vs incremental flows, cursor tracking, dry-run handling, full-refresh path).
- [X] T011 Extend CLI in `src/raindrop_enhancer/cli.py` with `raindrop-sync` command/flags, wiring orchestrator, summary reporting, JSON output, and exit codes per contract.
- [X] T012 Ensure Gracy client (`src/raindrop_enhancer/api/raindrop_client.py`) supports created-timestamp filtering and exposes hook for incremental queries.

## Phase 3.4: Integration & Observability
- [X] T013 Add logging/metrics hooks in orchestrator (requests count, retries, new link count) and surface through CLI summaries.
- [X] T014 Implement backup-on-full-refresh and DB path resolution utilities, including cross-platform defaults, under `src/raindrop_enhancer/storage`.
- [X] T015 Wire performance benchmark fixtures used by `tests/perf/` (synthetic dataset builders, timers) in a new helper `tests/perf/utils.py`.

## Phase 3.5: Polish & Documentation
- [X] T016 [P] Flesh out unit tests in `tests/unit/test_sqlite_store.py` to cover edge cases (duplicate insert, invalid URL rejection, corruption recovery) and ensure green after implementation.
- [X] T017 [P] Flesh out unit tests in `tests/unit/test_sync_orchestrator.py` (baseline/incremental logic, cursor updates, dry-run).
- [X] T018 [P] Flesh out integration test `tests/integration/test_cli_sync.py` verifying CLI output (text & JSON), exit codes, and temp DB behavior.
- [X] T019 [P] Finalize contract test assertions in `tests/contract/test_raindrop_incremental_contract.py` ensuring request headers, query params, and pagination stop conditions.
- [X] T020 [P] Fill in performance tests in `tests/perf/test_sync_baseline.py` and `tests/perf/test_sync_incremental.py`, ensuring runtime thresholds documented in constitution are enforced.
- [X] T021 Update `docs/manual-testing.md` (or create section) with manual verification steps for baseline, incremental, and full-refresh sync flows.
- [X] T022 Update `README.md` (or CLI docs) with new `raindrop-sync` command usage, flags, and default DB locations.
- [X] T023 Run `uv run pytest --cov=raindrop_enhancer --cov-report=term-missing` and ensure coverage ≥90% on new modules; address gaps.
- [skipped] T024 Run performance smoke tests via `uv run pytest tests/perf` and document results in plan/README if targets met.
- [ ] T025 Conduct manual quickstart validation following `specs/002-storage-and-sync/quickstart.md`; record findings (log or docs update).

## Dependencies & Execution Notes
- T003–T007 must be completed (and failing) before starting T008 onwards.
- T008 feeds T010–T012; orchestrator relies on storage and models.
- CLI wiring (T011) depends on orchestrator (T010) and storage (T008).
- Logging/backups (T013–T014) depend on core modules.
- Performance fixtures (T015) required before finalizing perf tests (T020, T024).
- Parallelizable `[P]` tasks operate on distinct files—safe to run concurrently once dependencies satisfied.

## Parallel Execution Examples
```
# After setup, author initial failing tests in parallel:
Task "T004 Add unit test skeletons in tests/unit/test_sqlite_store.py"
Task "T005 Add unit test skeletons in tests/unit/test_sync_orchestrator.py"
Task "T006 Add integration test skeleton in tests/integration/test_cli_sync.py"
Task "T007 Define performance smoke test placeholders in tests/perf/…"

# During polish phase, run test finalization together post-implementation:
Task "T016 Flesh out unit tests in tests/unit/test_sqlite_store.py"
Task "T017 Flesh out unit tests in tests/unit/test_sync_orchestrator.py"
Task "T018 Flesh out integration test tests/integration/test_cli_sync.py"
Task "T019 Finalize contract test assertions"
Task "T020 Fill in performance tests"
```
