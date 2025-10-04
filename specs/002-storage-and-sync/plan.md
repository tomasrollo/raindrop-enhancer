
# Implementation Plan: Persistent Storage and Incremental Sync for Raindrop Links

**Branch**: `002-storage-and-sync` | **Date**: 2025-10-03 | **Spec**: `/specs/002-storage-and-sync/spec.md`
**Input**: Feature specification from `/specs/002-storage-and-sync/spec.md`

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
Provide a repeatable CLI sync flow that writes exported Raindrop link metadata into a persistent local SQLite database, establishes a baseline archive when none exists, and supports incremental runs that append only newly created links while leaving prior records untouched.

## Technical Context
**Language/Version**: Python 3.13 (uv-managed per `pyproject.toml`)  
**Primary Dependencies**: Gracy/httpx (Raindrop API), Click (CLI), Rich (console UX), sqlite3 stdlib (embedded DB), python-dotenv (env loading)  
**Storage**: SQLite `.db` file stored under user config directory (`~/.local/share/raindrop_enhancer/raindrops.db` on POSIX, platform-specific equivalent elsewhere)  
**Testing**: pytest, pytest-httpx for HTTP mocking, temporary SQLite fixtures via `tmp_path`, Click `CliRunner` for CLI integration  
**Target Platform**: Cross-platform terminal environments (macOS/Linux/Windows)  
**Project Type**: Single Python package (`src/raindrop_enhancer`) with layered modules  
**Performance Goals**: Baseline export of 10k links ≤60s (constitution default); incremental sync of ≤500 new links completes ≤5s; p95 DB insert batch latency <50ms  
**Constraints**: Single-device sync assumption, append-only archive (ignore upstream updates/deletes), CLI must expose `--full-refresh` flag, RAINDROP_TOKEN from env, memory footprint ≤150MB  
**Scale/Scope**: Expect tens of thousands of links per user with daily incremental runs capturing up to hundreds of additions

## Constitution Check
*GATE: Must pass before Phase 0 research. Re-check after Phase 1 design.*

The plan MUST explicitly address the following gates per the Constitution:
- **Code Quality**: Introduce `storage/sqlite_store.py` with fully typed functions, docstrings, and centralized SQL; limit function complexity (<10) by decomposing schema creation, insert batching, and cursor management. Extend `sync/orchestrator.py` with dataclass-based logic and thorough docstrings. Enforce Black/Ruff/MyPy via uv before merge.
- **Testing Standards & TDD**: Draft failing unit tests for SQLite store operations (schema setup, append-only constraint, corruption guard), orchestration logic (baseline vs incremental vs full refresh), and CLI flows (output summaries, exit codes). Maintain contract tests to confirm Raindrop requests filter by creation timestamp and honor rate-limit handling. All tests deterministic using temporary DB paths and patched timestamps; coverage ≥90% on new modules.
- **UX Consistency**: Extend CLI with `sync` command (or equivalent option) honoring existing `--quiet/--verbose/--dry-run` semantics, add `--full-refresh` flag, optional `--db-path` override, and consistent messaging to stdout/stderr. Preserve backward compatibility with existing export behavior and ensure `--help` reflects new options; provide optional JSON summary flag.
- **Performance & Efficiency**: Use batched `executemany` inserts inside transactions, employ WAL mode for durability without impacting single-writer performance, and reuse HTTP + DB connections. Document benchmarks ensuring baseline sync ≤60s for 10k links and incremental run ≤5s for 500 links; profile if thresholds breached.
- **Tooling & Dependency Management**: Stay within existing dependencies (use stdlib sqlite3); run commands via `uv run` and capture in quickstart. Update AGENTS.md via provided script to register SQLite storage context; ensure lockfile unchanged unless new dependency introduced (not expected).

**Initial Constitution Check Status**: PASS — design remains within constitutional guardrails with no outstanding exceptions.

## Project Structure

### Documentation (this feature)
```
specs/[###-feature]/
├── plan.md              # This file (/plan command output)
├── research.md          # Phase 0 output (/plan command)
├── data-model.md        # Phase 1 output (/plan command)
├── quickstart.md        # Phase 1 output (/plan command)
├── contracts/           # Phase 1 output (/plan command)
└── tasks.md             # Phase 2 output (/tasks command - NOT created by /plan)
```

### Source Code (repository root)
```
src/
└── raindrop_enhancer/
   ├── __init__.py
   ├── cli.py                    # Click entrypoint extended with sync flag/command
   ├── api/
   │   ├── __init__.py
   │   └── raindrop_client.py    # Gracy client reused for incremental fetch
   ├── models.py                 # Domain models extended with persistence helpers
   ├── storage/
   │   ├── __init__.py
   │   └── sqlite_store.py       # NEW: SQLite schema management & CRUD
   └── sync/
      ├── __init__.py
      └── orchestrator.py     # NEW: Sync orchestration (baseline/incremental/full refresh)

tests/
├── contract/
│   ├── __init__.py
│   └── test_raindrop_incremental_contract.py  # NEW: validates API usage for incremental filter
├── integration/
│   ├── __init__.py
│   └── test_cli_sync.py                       # NEW: CLI sync baseline/incremental/full refresh flows
└── unit/
   ├── __init__.py
   ├── test_sqlite_store.py                # NEW: schema, inserts, corruption recovery
   ├── test_sync_orchestrator.py           # NEW: incremental logic, cursor updates
   └── test_retry_backoff.py               # Existing (no changes)
```

**Structure Decision**: Single-package CLI with new `storage` and `sync` submodules inside `src/raindrop_enhancer`, mirrored tests under existing `tests/` hierarchy for contract/unit/integration coverage.

## Phase 0: Outline & Research
1. **Research focus areas**
   - Confirm Raindrop API exposes a reliable `created` timestamp or sort filter to fetch only new items and document the exact query parameters/pagination rules.
   - Evaluate SQLite append-only schema patterns (primary key strategy, indices, WAL mode usage) suitable for bookmark archives and single-writer access.
   - Determine cross-platform path for storing the `.db` without new dependencies (fallback to home directory if platform-specific path unsupported).
   - Define corruption detection/remediation signals and messaging that align with spec requirement to recreate archive safely.

2. **Research tasks dispatched**
   - Task: "Research Raindrop API incremental sync using created/lastUpdate fields"
   - Task: "Survey SQLite best practices for append-only link archives (PK/indices/WAL)"
   - Task: "Identify cross-platform config directory strategy without platformdirs dependency"
   - Task: "Outline corruption detection & recovery messaging for CLI sync"

3. **Consolidation plan**
   - Document findings (Decision/Rationale/Alternatives) in `research.md` for each topic.
   - Record API parameter set, rate-limit expectations, and incremental cursor calculations.
   - Capture final DB path strategy and integrity checks feeding Phase 1 design.

**Output**: `research.md` summarizing incremental strategy, SQLite schema, storage path, and recovery guidance.

## Phase 1: Design & Contracts
*Prerequisites: research.md complete*

1. **Data modelling**
   - Document `raindrop_links` table (columns: `raindrop_id` PK, `collection_id`, `collection_title`, `title`, `url`, `created_at`, `synced_at`, `tags_json`, `raw_payload`).
   - Document `sync_state` table (singleton row storing `id=1`, `last_cursor_iso`, `last_run_at`, `db_version`, `last_full_refresh`).
   - Outline invariants: append-only, unique `raindrop_id`, ignore upstream edits/deletes, track schema version for migrations.

2. **Contracts generation**
   - Create `/specs/002-storage-and-sync/contracts/cli_sync_contract.md` describing CLI command/flags, exit codes, stdout/stderr expectations, summary JSON schema, and DB side-effects.
   - Include Raindrop API request contract snippet referencing created timestamp filters and pagination expectations.

3. **Test scaffolding plan**
   - Failing contract test `tests/contract/test_raindrop_incremental_contract.py` verifying API usage.
   - Unit test skeletons for store/orchestrator capturing baseline, incremental, corruption handling.
   - Integration test skeleton for CLI verifying DB file creation, incremental counts, `--full-refresh` behavior, and dry-run summary.

4. **Quickstart**
   - Document prerequisites (SQLite bundled with Python, RAINDROP_TOKEN set), DB path configuration, commands for baseline sync, incremental run, full refresh, running tests, and verifying performance metrics.

5. **Agent update**
   - After drafting docs, run `.specify/scripts/bash/update-agent-context.sh codex` to record new storage workflow and SQLite usage.

**Output**: `data-model.md`, `/contracts/cli_sync_contract.md`, `quickstart.md`, failing test skeleton plan, updated agent context file.

**Post-Design Constitution Check**: PASS — documentation confirms append-only storage invariants, comprehensive test coverage strategy, CLI UX alignment, and performance benchmarks.

## Phase 2: Task Planning Approach
*This section describes what the /tasks command will do - DO NOT execute during /plan*

**Task Generation Strategy**:
- Use `.specify/templates/tasks-template.md` as base.
- Derive tasks from data model, contracts, and quickstart scenarios.
- For each contract/API interaction create contract test + implementation tasks ([P] where independent).
- For each table/entity generate schema migration + persistence logic tasks preceding orchestrator tasks.
- Map user story scenarios to integration tests prior to implementation; include dry-run/full-refresh coverage.
- Add documentation/update tasks (quickstart validation, README/AGENTS updates) and performance validation tasks.

**Ordering Strategy**:
- Enforce TDD: write/store tests → orchestrator tests → CLI integration tests before writing production code.
- Sequence: storage schema → sync orchestration → CLI wiring → observability/performance instrumentation.
- Mark independent tasks (e.g., storage tests vs CLI tests) as [P] for possible parallel execution.

**Estimated Output**: 22-26 ordered tasks in `tasks.md` (lean feature scope).

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

**Phase Status**:
- [x] Phase 0: Research complete (/plan command)
- [x] Phase 1: Design complete (/plan command)
- [ ] Phase 2: Task planning complete (/plan command - describe approach only)
- [ ] Phase 3: Tasks generated (/tasks command)
- [ ] Phase 4: Implementation complete
- [ ] Phase 5: Validation passed

**Gate Status**:
- [x] Initial Constitution Check: PASS
- [x] Post-Design Constitution Check: PASS
- [x] All NEEDS CLARIFICATION resolved
- [ ] Complexity deviations documented

---
*Based on Constitution v1.0.0 - See `.specify/memory/constitution.md`*
