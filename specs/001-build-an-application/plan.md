# Implementation Plan: Raindrop Link Enhancer CLI

**Branch**: `001-build-an-application` | **Date**: 2025-10-01 | **Spec**: [/Users/tomas/Documents/projects/raindrop-enhancer/specs/001-build-an-application/spec.md](spec.md)
**Input**: Feature specification from `/specs/001-build-an-application/spec.md`

## Execution Flow (/plan command scope)
```
1. Load feature spec from Input path
   → If not found: ERROR "No feature spec at {path}"
2. Fill Technical Context (scan for NEEDS CLARIFICATION)
   → Detect Project Type from file system structure or context (web=frontend+backend, mobile=app+api)
   → Set Structure Decision based on project type
3. Fill the Constitution Check section based on `.specify/memory/constitution.md`.
4. Evaluate Constitution Check section below
   → If violations exist: Document in Complexity Tracking
   → If no justification possible: ERROR "Simplify approach first"
   → Update Progress Tracking: Initial Constitution Check
5. Execute Phase 0 → research.md
   → If NEEDS CLARIFICATION remain: ERROR "Resolve unknowns"
6. Execute Phase 1 → contracts, data-model.md, quickstart.md, agent-specific template file (e.g., `CLAUDE.md` for Claude Code, `.github/copilot-instructions.md` for GitHub Copilot, `GEMINI.md` for Gemini CLI, `QWEN.md` for Qwen Code or `AGENTS.md` for opencode).
7. Re-evaluate Constitution Check section
   → If new violations: Refactor design, return to Phase 1
   → Update Progress Tracking: Post-Design Constitution Check
8. Plan Phase 2 → Describe task generation approach (DO NOT create tasks.md)
9. STOP - Ready for /tasks command
```

**IMPORTANT**: The /plan command STOPS at step 7. Phases 2-4 are executed by other commands:
- Phase 2: /tasks command creates tasks.md
- Phase 3-4: Implementation execution (manual or via tools)

## Summary
Deliver a Python CLI that authenticates with the Raindrop API (using test tokens or OAuth access tokens), performs full and incremental synchronisation of all collections, respects the documented 120-requests-per-minute rate limit, enriches each link via an external LLM tagging API, and exports a deduplicated JSON dataset backed by SQLite for incremental tracking. The tool will use `click` for CLI orchestration, `rich` for progress and summaries, `requests` for API calls, `trafilatura` for content extraction, and maintain configuration (including the Raindrop token) in a permissions-restricted plaintext config file within the user-selected data directory.

## Technical Context
**Language/Version**: Python 3.13 (uv-managed)  
**Primary Dependencies**: click, rich, requests, trafilatura, sqlite3/SQLModel (or SQLAlchemy Core), pathlib, tenacity-style retry helper (in-house)  
**Storage**: SQLite database in the chosen data directory plus JSON export and plaintext config file in same location  
**Testing**: pytest with coverage enforcement, Click CliRunner contract tests, Raindrop/LLM client fakes, MyPy in strict mode  
**Target Platform**: Cross-platform CLI (macOS & Linux focus)  
**Project Type**: Single Python CLI project (`src/raindrop_enhancer`)  
**Performance Goals**: p95 link processing <200ms, p99 <500ms; 10k-link full sync ≤60s; incremental sync <10s for ≤200 links; RSS ≤150MB  
**Constraints**: Must respect Raindrop rate limit of 120 requests/minute by monitoring `X-RateLimit-*` headers and applying exponential backoff (1s→60s jitter); CLI requires `--json`, `--verbose`, `--quiet`, `--dry-run`; offline-safe replays for cached data; store Raindrop token only in config file with user-only permissions  
**Scale/Scope**: Up to 10k links across 50 collections; incremental runs typically <200 links; future cron automation compatible

## Constitution Check
*Initial Gate — PASS (2025-10-01)*

- **Code Quality**: Enforce Black/Ruff/MyPy via uv scripts; modules organised by domain/service/CLI to keep complexity manageable (<10); public APIs documented; dataclasses/TypedDicts for schemas; forbid dead code via Ruff checks.
- **Testing Standards & TDD**: Contract tests (CLI JSON schema, Raindrop API requests), unit tests (storage, tagging, retry), integration tests (full and incremental sync) all scaffolded before implementation; coverage target 90/80 enforced; fixtures stub network to keep runs deterministic.
- **UX Consistency**: CLI interface ensures `--help`, `--json`, `--verbose`, `--quiet`, `--dry-run`; output defaults human-readable with `rich`; errors go to stderr with exit codes; JSON export versioned for compatibility.
- **Performance & Efficiency**: Adopt default performance goals plus 10k-link ≤60s objective; plan includes batching (pagination + LLM tag pooling) and asynchronous executor capped to avoid throttling; perf benchmark script scheduled.
- **Tooling & Dependency Management**: All dependency operations via `uv add/remove/lock`; execution documented with `uv run`; quickstart instructs `uv sync`; lockfile to be checked in.

No deviations requiring Complexity Tracking at this stage.

## Project Structure

### Documentation (this feature)
```
specs/001-build-an-application/
├── plan.md              # This file (/plan command output)
├── research.md          # Phase 0 output (/plan command)
├── data-model.md        # Phase 1 output (/plan command)
├── quickstart.md        # Phase 1 output (/plan command)
├── contracts/           # Phase 1 output (/plan command)
└── tasks.md             # Phase 2 output (/tasks command - NOT created by /plan)
```

### Source Code (repository root)
ios/ or android/
<!--
   ACTION REQUIRED: Replace the placeholder tree below with the concrete layout
   for this feature. Delete unused options and expand the chosen structure with
   real paths (e.g., apps/admin, packages/something). The delivered plan must
   not include Option labels.
-->
```
src/
├── raindrop_enhancer/
│   ├── __init__.py
│   ├── cli/
│   │   └── main.py
│   ├── api/
│   │   ├── client.py
│   │   └── models.py
│   ├── services/
│   │   ├── sync.py
│   │   ├── tagging.py
│   │   └── storage.py
│   ├── domain/
│   │   ├── entities.py
│   │   └── repositories.py
│   └── util/
│       ├── config.py
│       ├── logging.py
│       └── retry.py

tests/
├── unit/
│   ├── test_storage.py
│   ├── test_tagging.py
│   └── test_retry.py
├── integration/
│   ├── test_full_sync.py
│   └── test_incremental_sync.py
└── contract/
   ├── test_cli_contract.py
   └── test_raindrop_api_contracts.py

scripts/
└── perf/
   └── benchmark_sync.py
```

**Structure Decision**: Single Python CLI project housed in `src/raindrop_enhancer` with layered modules (domain → services → CLI). Tests mirror production packages, and a dedicated `scripts/perf` directory hosts benchmark harnesses mandated by the constitution.

## Phase 0: Outline & Research
Completed in `research.md` (2025-10-01). Key investigations and resulting decisions:

1. **Raindrop token storage** — validated plaintext config with restrictive permissions; documented rotation and cleanup operations and linked to Raindrop authentication docs for retrieving test tokens or OAuth credentials.
2. **External LLM tagging API** — compared providers; selected HTTP JSON API with batch endpoint, cost guardrails, and mockable contract.
3. **SQLite schema & performance** — designed tables/indexes for Raindrop IDs, collections, tag suggestions, sync runs; confirmed WAL mode and chunked transactions to meet 10k-link SLA.
4. **Retry/backoff implementation** — specified jittered exponential helper aligning with FR-010; mapped to requests session adapter.
5. **Rate limit compliance** — interpreted Raindrop docs: monitor `X-RateLimit-*` headers (limit 120/min), feed telemetry into sync summaries, and gate concurrent requests accordingly.
6. **CLI UX using click + rich** — established patterns for mutually exclusive verbosity flags, JSON output mode bypassing rich progress, and summary reporting.

Each research item follows Decision/Rationale/Alternatives template, eliminating remaining ambiguities.

## Phase 1: Design & Contracts
*Prerequisites: research.md complete*

Artifacts created:

1. **`data-model.md`** — documents entities (`LinkRecord`, `Collection`, `TagSuggestion`, `SyncRun`, `ConfigSettings`) with fields, types, normalization, indices, and lifecycle states (pending → processed → manual-review). Includes ER diagram outline and audit trail requirements.
2. **Contracts** — `contracts/raindrop_api.yaml` (OpenAPI snippet for Raindrop endpoints + incremental filters) and `contracts/cli_commands.md` (CLI command/flag schema, exit codes, JSON output contract). Both paired with failing pytest stubs: `tests/contract/test_raindrop_api_contracts.py` & `test_cli_contract.py` (referenced in plan for Phase 2 tasks).
3. **`quickstart.md`** — uv-based setup, running unit/contract/integration tests, executing full vs incremental sync, verifying JSON export schema, observing `rate_limit_remaining/reset` telemetry against the documented 120 req/min window, cleaning up config/token, and performing 1k-link performance smoke.
4. **Agent context** — updated via `.specify/scripts/bash/update-agent-context.sh codex` to capture new dependencies and plan focus (SQLite, LLM tagging API, retry helper).

Post-design constitution check re-confirmed PASS; no additional violations surfaced.

## Phase 2: Task Planning Approach
*This section describes what the /tasks command will do - DO NOT execute during /plan*

**Task Generation Strategy**:
- Load `.specify/templates/tasks-template.md` as base
- Generate tasks from Phase 1 design docs (contracts, data model, quickstart)
- Each contract → contract test task [P]
- Each entity → model creation task [P] 
- Each user story → integration test task
- Add telemetry task to capture and persist `X-RateLimit-*` headers within `SyncRun` records and surface in CLI output.
- Implementation tasks to make tests pass

**Ordering Strategy**:
- TDD order: Tests before implementation 
- Dependency order: Models before services before UI
- Mark [P] for parallel execution (independent files)

**Estimated Output**: 25-30 numbered, ordered tasks in tasks.md

**IMPORTANT**: This phase is executed by the /tasks command, NOT by /plan

## Phase 3+: Future Implementation
*These phases are beyond the scope of the /plan command*

**Phase 3**: Task execution (/tasks command creates tasks.md)  
**Phase 4**: Implementation (execute tasks.md following constitutional principles)  
**Phase 5**: Validation (run tests, execute quickstart.md, performance validation)

## Complexity Tracking
*Fill ONLY if Constitution Check has violations that must be justified*

| Violation | Why Needed | Simpler Alternative Rejected Because |
|-----------|------------|-------------------------------------|
| [e.g., 4th project] | [current need] | [why 3 projects insufficient] |
| [e.g., Repository pattern] | [specific problem] | [why direct DB access insufficient] |


## Progress Tracking
*This checklist is updated during execution flow*

- **Phase Status**:
- [x] Phase 0: Research complete (/plan command)
- [x] Phase 1: Design complete (/plan command)
- [x] Phase 2: Task planning complete (/plan command - describe approach only)
- [ ] Phase 3: Tasks generated (/tasks command)
- [ ] Phase 4: Implementation complete
- [ ] Phase 5: Validation passed

**Gate Status**:
- [x] Initial Constitution Check: PASS
- [x] Post-Design Constitution Check: PASS
- [x] All NEEDS CLARIFICATION resolved
- [ ] Complexity deviations documented

---
*Based on Constitution v1.1.0 - See `.specify/memory/constitution.md`*

# Final validation (T028) — 2025-10-01

Validation steps executed:

- Full test suite: `uv run pytest -q` — ALL TESTS PASSED (unit, integration, contract).
- Coverage: `uv run pytest --cov -q` — TOTAL COVERAGE 90% (meets T026 requirement).
- CLI dry-run sync: `uv run raindrop-enhancer sync --mode full --dry-run --json --data-dir ./.tmp_test_data`

Observed CLI sync structured log (example):

{"message": "sync.complete", "run_id": "1205edda-cc61-44b4-a777-31c1f456fa59", "processed": 0, "export_count": 0, "duration_seconds": 2.119412, "rate_limit": {"limit": null, "remaining": null, "reset": null}}

CLI-returned summary (example):

{"run_id": "1205edda-cc61-44b4-a777-31c1f456fa59", "started_at": "2025-10-01T11:24:39.213535+00:00", "completed_at": "2025-10-01T11:24:41.332947+00:00", "duration_seconds": 2.119412, "processed": 0, "export_count": 0, "rate_limit": {"limit": null, "remaining": null, "reset": null}}

Notes:

- Coverage run emitted ResourceWarning messages about unclosed SQLite connections during tests. They don't fail CI but indicate some sessions/connections may not be closed cleanly in tests.
- The dry-run completed successfully and the repo persisted a `SyncRun` record where available.

Validation status: PASS — tests and coverage target satisfied.

Next recommended steps:

- Add a small test or cleanup step to ensure SQLModel sessions are closed to silence ResourceWarnings.
- Run the performance benchmark with a 1k-link fixture and assert the 60s SLA; I can parameterize the benchmark script to accept the fixture/size if you'd like.
