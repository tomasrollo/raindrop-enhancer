# Tasks: Unified Raindrop Export CLI

**Input**: Design documents from `/specs/001-build-a-small/`
**Prerequisites**: plan.md (required), research.md, data-model.md, contracts/, quickstart.md

## Phase 3.1: Setup
- [X] T001 Create package skeleton (`src/raindrop_enhancer/__init__.py`, `api/__init__.py`, `exporters/__init__.py`, `models.py`) matching plan structure.
- [X] T002 Ensure runtime dependencies in `pyproject.toml` (`gracy`, `click`, `rich`, `python-dotenv`, `httpx`) are present via `uv add` if missing; sync lockfile.
- [X] T003 Add/verify test support dependencies in `pyproject.toml` (`pytest-httpx`, `pytest-asyncio`, `click`) and configure `tool.pytest.ini_options` if needed for async tests.

## Phase 3.2: Tests First (TDD)
- [X] T004 [P] Add failing contract test for `GET /rest/v1/collections` in `tests/contract/test_raindrop_endpoints.py::test_list_collections_contract` using mocked HTTP responses.
- [X] T005 [P] Add failing contract test for `GET /rest/v1/raindrops/{collection_id}` in `tests/contract/test_raindrop_endpoints.py::test_list_raindrops_contract` covering pagination and filters.
- [X] T006 [P] Add failing unit tests for collection and raindrop dataclass helpers in `tests/unit/test_models.py` (validation rules, mapping from API payload).
- [X] T007 [P] Add failing unit tests for pagination, retry/backoff behavior in `tests/unit/test_raindrop_client.py` using `pytest-httpx` fixtures.
- [X] T008 [P] Add failing unit tests for JSON exporter formatting in `tests/unit/test_json_exporter.py` (ensures JSON array structure and field names).
- [X] T009 Add failing integration test for successful CLI export (`raindrop-export`) in `tests/integration/test_cli_export.py::test_export_success_writes_json` asserting stdout JSON and progress output handling.
- [X] T010 Add failing integration test for missing token handling in `tests/integration/test_cli_export.py::test_export_missing_token_exits_with_error` validating exit code and stderr messaging.

## Phase 3.3: Core Implementation (after tests are failing)
- [X] T011 Implement data models in `src/raindrop_enhancer/models.py` (dataclasses/TypedDicts with validation helpers to filter inactive items).
- [X] T012 Implement Gracy-based Raindrop client in `src/raindrop_enhancer/api/raindrop_client.py` (auth header from env, pagination, retry/backoff, filtering of inactive raindrops).
- [X] T013 Implement JSON exporter in `src/raindrop_enhancer/exporters/json_exporter.py` producing ordered JSON array and optional pretty formatting hooks.
- [X] T014 Implement CLI command in `src/raindrop_enhancer/cli.py` (Click command with `--output`, `--quiet`, `--verbose`, `--dry-run`, `--pretty`, loads `.env`, wires Rich progress, invokes client + exporter).
- [X] T015 Register CLI entrypoint in `src/raindrop_enhancer/__init__.py` and `pyproject.toml` `[project.scripts]` so `uv run raindrop-export` is available; ensure package exports necessary symbols.

## Phase 3.4: Integration & Resilience
- [ ] T016 Enhance client logging and telemetry in `src/raindrop_enhancer/api/raindrop_client.py` (structured logs, Rich console integration for verbose mode).
- [ ] T017 Implement retry/throttle configuration using Gracy settings to honor 120 req/min and exponential backoff limits; expose observability hooks for retries.
- [ ] T018 Wire CLI progress indicators and summary metrics in `src/raindrop_enhancer/cli.py` (collection/raindrop counters, elapsed time reporting, proper exit codes).

## Phase 3.5: Polish & Validation
- [ ] T019 [P] Add performance smoke test in `tests/perf/test_export_performance.py` simulating 10k raindrops to verify completion within 60s and document results.
- [ ] T020 [P] Update `quickstart.md` and `README.md` with final CLI usage, flags, performance expectations, and troubleshooting notes.
- [ ] T021 Run full quality gate: `uv run ruff check`, `uv run pytest --cov=raindrop_enhancer --cov-report=term-missing`, `uv run mypy src`; capture outcomes in PR notes.
- [ ] T022 Document manual validation steps and results in `docs/manual-testing.md` (dry run, successful export, rate-limit retry scenario); attach CLI logs.

## Dependencies
- T002 → T003 (same file adjustments)
- Tests (T004-T010) must be completed and failing before implementing T011-T018
- T011 → T012 → T013 → T014 (core layering)
- T015 depends on T014 completion
- T017 depends on T012 implementation
- T018 depends on T014 & T017
- Polish tasks (T019-T022) depend on all core tasks (T011-T018)

## Parallel Execution Example
```
# Once setup tasks complete and before implementation:
Run in parallel:
  - T004 Add failing contract test for collections
  - T005 Add failing contract test for raindrops
  - T006 Add failing unit tests for models
  - T007 Add failing unit tests for pagination/retry logic
  - T008 Add failing unit tests for JSON exporter

# During polish phase:
Run in parallel:
  - T019 Add performance smoke test (tests/perf)
  - T020 Update quickstart/README docs
```
