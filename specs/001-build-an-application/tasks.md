# Tasks: Raindrop Link Enhancer CLI

**Input**: Design documents from `/specs/001-build-an-application/`
**Prerequisites**: plan.md (required), research.md, data-model.md, contracts/, quickstart.md

## Phase 3.1: Setup
- [X] T001 Establish package layout under `src/raindrop_enhancer/` (create `__init__.py`, `cli/`, `api/`, `services/`, `domain/`, `util/`, and `scripts/perf/benchmark_sync.py` scaffolds) and add matching `tests/` package placeholders.  
  _Depends on_: —
- [ ] T002 Update `pyproject.toml` using `uv add` to include runtime dependencies (`click`, `rich`, `requests`, `trafilatura`, `sqlmodel`, `tenacity`-style helper or equivalent) and register the CLI entry point `raindrop-enhancer=raindrop_enhancer.cli.main:app`.  
  _Depends on_: T001
- [ ] T003 Configure linting/typing in `pyproject.toml` (Black, Ruff, MyPy strict settings, pytest coverage), add any supporting config files, and ensure `uv lock && uv sync` succeeds.  
  _Depends on_: T002

## Phase 3.2: Tests First (must fail before implementation)
- [ ] T004 [P] Flesh out `tests/contract/test_raindrop_api_contracts.py` to validate OpenAPI schema compliance and `X-RateLimit-*` headers against `contracts/raindrop_api.yaml` (use `uv run pytest -k raindrop_api`).  
  _Depends on_: T001
- [ ] T005 [P] Flesh out `tests/contract/test_cli_contract.py` to assert CLI flags, JSON schema, and rate-limit telemetry fields defined in `contracts/cli_commands.md`.  
  _Depends on_: T001
- [ ] T006 [P] Author failing integration test `tests/integration/test_full_sync.py` covering full sync happy-path (JSON export, SQLite persistence, tagging flow) using Raindrop/LLM fakes.  
  _Depends on_: T001
- [ ] T007 [P] Author failing integration test `tests/integration/test_incremental_sync.py` ensuring incremental mode only processes updated links and records rate-limit telemetry.  
  _Depends on_: T001
- [ ] T008 [P] Author failing integration test `tests/integration/test_reprocess_status.py` validating targeted reprocess and status summary outputs.  
  _Depends on_: T001
- [ ] T009 [P] Author failing unit tests in `tests/unit/test_storage.py` for SQLite repository CRUD, deduping, and audit trail.  
  _Depends on_: T001
- [ ] T010 [P] Author failing unit tests in `tests/unit/test_tagging.py` for LLM tagging adapter (batching, confidence filtering, error handling).  
  _Depends on_: T001
- [ ] T011 [P] Author failing unit tests in `tests/unit/test_retry.py` covering exponential backoff, jitter, and `Retry-After` handling.  
  _Depends on_: T001

## Phase 3.3: Core Implementation (make tests pass in order)
- [ ] T012 Implement SQLModel definitions for `LinkRecord` and link-collection association in `src/raindrop_enhancer/domain/entities.py`.  
  _Depends on_: T004–T011
- [ ] T013 Implement SQLModel definitions for `Collection` and `ConfigSettings` in `src/raindrop_enhancer/domain/entities.py`.  
  _Depends on_: T012
- [ ] T014 Implement SQLModel definitions for `TagSuggestion` and `SyncRun` (with rate-limit fields) in `src/raindrop_enhancer/domain/entities.py`.  
  _Depends on_: T013
- [ ] T015 Build SQLite repository layer in `src/raindrop_enhancer/domain/repositories.py` (WAL setup, migrations, CRUD, incremental queries, audit logging).  
  _Depends on_: T012–T014, T009
- [ ] T016 Implement configuration manager in `src/raindrop_enhancer/util/config.py` (read/write `config.toml`, enforce `0600` permissions, expose thresholds).  
  _Depends on_: T013, T005, T009
- [ ] T017 Implement retry/backoff helper in `src/raindrop_enhancer/util/retry.py` honoring Raindrop rate-limit headers and emitting telemetry hooks.  
  _Depends on_: T011
- [ ] T018 Implement Raindrop API client in `src/raindrop_enhancer/api/client.py` (collections & raindrops endpoints, pagination, header capture, auth).  
  _Depends on_: T015, T017, T004
- [ ] T019 Implement tagging adapter in `src/raindrop_enhancer/services/tagging.py` (LLM batch requests, retries, confidence threshold, error tagging).  
  _Depends on_: T010, T017
- [ ] T020 Implement content extraction + enrichment helpers in `src/raindrop_enhancer/services/sync.py` (trafilatura fetch, metadata merge, manual-review flagging).  
  _Depends on_: T015, T018, T019, T006
- [ ] T021 Wire incremental/full/reprocess orchestration in `src/raindrop_enhancer/services/sync.py` (detect new links, dedupe, update SyncRun, write JSON export).  
  _Depends on_: T020, T007, T008
- [ ] T022 Implement CLI commands in `src/raindrop_enhancer/cli/main.py` (configure, sync, reprocess, status, global options, rich output) and register `app` entry.  
  _Depends on_: T016, T021, T005

## Phase 3.4: Integration & Performance
- [ ] T023 Integrate structured logging & metrics in `src/raindrop_enhancer/util/logging.py` and surface rate-limit telemetry in CLI summaries.  
  _Depends on_: T022
- [ ] T024 Complete JSON export writer and schema versioning in `src/raindrop_enhancer/services/storage.py` (ensure idempotent updates).  
  _Depends on_: T021
- [ ] T025 Implement performance benchmark in `scripts/perf/benchmark_sync.py` targeting 1k-link fixture and report against 60s SLA.  
  _Depends on_: T021, T024

## Phase 3.5: Polish & Validation
- [ ] T026 [P] Add supplemental unit tests (config manager, logging) and ensure overall coverage ≥90% via `uv run pytest --cov`.  
  _Depends on_: T016, T023
- [ ] T027 Update `README.md` and `specs/001-build-an-application/quickstart.md` with final CLI usage, rate-limit guidance, and troubleshooting.  
  _Depends on_: T022–T024
- [ ] T028 Execute final validation (`uv run pytest`, `uv run raindrop-enhancer sync --mode full --dry-run --json`) and document results in `specs/001-build-an-application/plan.md` Progress Tracking notes.  
  _Depends on_: T026, T027

## Dependencies Summary
- T002 → T001
- T003 → T002
- T004–T011 → T001 (parallel allowed)
- T012 → T004–T011
- T013 → T012; T014 → T013
- T015 → T012–T014 & T009
- T016 → T013, T005, T009
- T017 → T011
- T018 → T015, T017, T004
- T019 → T010, T017
- T020 → T015, T018, T019, T006
- T021 → T020, T007, T008
- T022 → T016, T021, T005
- T023 → T022
- T024 → T021
- T025 → T021, T024
- T026 → T016, T023
- T027 → T022–T024
- T028 → T026, T027

## Parallel Execution Example
```bash
# Kick off contract and integration test authoring together after T001
TaskAgent run --id T004 &
TaskAgent run --id T005 &
TaskAgent run --id T006 &
TaskAgent run --id T007 &
TaskAgent run --id T008 &
TaskAgent run --id T009 &
TaskAgent run --id T010 &
TaskAgent run --id T011
wait
```

## Notes
- Maintain TDD: ensure tasks in Phase 3.2 fail before progressing to implementations.
- All commands should use `uv run` / `uv add` to comply with tooling policy.
- Avoid editing shared files concurrently when tasks lack `[P]`.
