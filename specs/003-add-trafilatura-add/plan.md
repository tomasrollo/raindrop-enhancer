
# Implementation Plan: Full-Text Capture Command for Saved Links

**Branch**: `003-add-trafilatura-add` | **Date**: 2025-10-05 | **Spec**: [/specs/003-add-trafilatura-add/spec.md](/specs/003-add-trafilatura-add/spec.md)
**Input**: Feature specification from `/specs/003-add-trafilatura-add/spec.md`

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
Introduce a resilient CLI command that uses Trafilatura’s documented `fetch_url` + `extract(..., output_format="markdown")` pipeline to capture and store Markdown-formatted article content for saved links, skipping previously captured items by default while offering an opt-in refresh flag, performing a single retry on transient failures, reusing existing CLI authentication context, and exiting with failure only when every link fails.

## Technical Context
**Language/Version**: Python 3.13  
**Primary Dependencies**: Click, Rich, Gracy/httpx, Trafilatura, sqlite3, python-dotenv  
**Storage**: SQLite database at platform config directory (`raindrops.db`)  
**Testing**: pytest (unit, integration, contract, perf suites)  
**Target Platform**: Cross-platform CLI (macOS/Linux/Windows) executed via `uv run`  
**Project Type**: Single-project CLI with supporting packages  
**Performance Goals**: Default CLI run processes ≥100 links with p95 end-to-end capture latency < 5s/link and overall wall-clock < 60s; memory footprint < 150MB RSS  
**Constraints**: Must operate offline-friendly (graceful failures), idempotent by default, and comply with uv tooling (dependency add via `uv add`)  
**Scale/Scope**: Support libraries with up to 10k saved links and repeated nightly capture runs

## Constitution Check
*GATE: Must pass before Phase 0 research. Re-check after Phase 1 design.*

- **Code Quality Discipline**: Implementation will follow Black/Ruff/MyPy gates; new modules receive docstrings, typed signatures, and stay under complexity limits by isolating Trafilatura integration in a dedicated service with <=10 cyclomatic complexity.
- **Testing Standards & TDD**: Plan adds failing contract, unit, and integration tests before implementation, covering retry logic, refresh flag paths, and CLI exit codes; fast deterministic tests use fixtures/mocks for Trafilatura and sqlite.
- **UX Consistency**: CLI command exposes `--refresh`, `--dry-run`, `--json`, `--verbose`, `--quiet` aligned with existing conventions; outputs human-readable summaries to stdout, JSON with `--json`, errors to stderr; exit codes: 0 success or partial, 1 when all fail.
- **Performance & Efficiency**: Adopt stated goals (≤5s p95 per link, ≤60s per 100 links); batching with configurable concurrency guard, reuse HTTP session; perf regression test added under `tests/perf` with fixture dataset.
- **Tooling & Dependency Management**: Add Trafilatura via `uv add trafilatura`; sync lockfile; all commands run via `uv run` (tests, CLI); document dependency in plan & quickstart.

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
<!--
  ACTION REQUIRED: Replace the placeholder tree below with the concrete layout
  for this feature. Delete unused options and expand the chosen structure with
  real paths (e.g., apps/admin, packages/something). The delivered plan must
  not include Option labels.
-->
```
src/
└── raindrop_enhancer/
   ├── __init__.py
   ├── cli.py
   ├── api/
   │   └── raindrop_client.py
   ├── storage/
   │   └── sqlite_store.py
   ├── sync/
   │   └── orchestrator.py
   ├── exporters/
   │   └── json_exporter.py
   └── content/              # planned module for Markdown capture helpers
      └── __init__.py (new) + fetcher service

tests/
├── contract/
├── integration/
├── unit/
└── perf/
```

**Structure Decision**: Single-project Python CLI; extend `src/raindrop_enhancer/` with a new `content` subpackage for capture services and add matching tests under existing `tests/` hierarchy.

## Phase 0: Outline & Research
1. Confirm Trafilatura capabilities for Markdown extraction, rate-limiting, timeout management, and error signals to map retryable vs fatal failures.
2. Validate Trafilatura usage patterns from documentation: `fetch_url` for downloading pages, `extract(..., output_format="markdown", with_metadata=True)` for content, `no_fallback=True`/`include_comments=False` trade-offs, and optional modules (e.g., `cchardet`) for performance.
3. Review existing sqlite schema and determine schema changes required to add Markdown content column(s) while keeping backward compatibility.
4. Audit existing CLI patterns in `cli.py` for flag conventions, JSON output structure, and environment handling to maintain UX consistency.
5. Investigate best practices for storing lengthy Markdown blobs in sqlite (compression, indexing) and ensure searchability requirements.
6. Document findings in `research.md` as Decision/Rationale/Alternatives for each topic; unresolved items must be closed before moving to Phase 1.

**Output**: `research.md` containing finalized decisions for Trafilatura integration, schema updates, CLI UX patterns, and storage considerations.

## Phase 1: Design & Contracts
*Prerequisites: research.md complete*

1. Capture entities and relationships in `data-model.md`, including `SavedLink` (existing fields + `content_markdown`, `content_fetched_at`), `ContentCaptureSession`, and `LinkCaptureAttempt` for logging retries/status.
2. Define a CLI contract `contracts/cli_content_capture_contract.md` covering command name (`capture-content`), flags (`--refresh`, `--dry-run`, `--json`, `--limit`, `--verbose`, `--quiet`, `--timeout`), inputs, outputs, and exit codes; include JSON schema for `--json` output influenced by Trafilatura status fields (`status`, `retry_count`, `error_type`).
3. Draft failing contract tests (e.g., `tests/contract/test_cli_content_capture.py`) that assert CLI behavior from the contract, verify the JSON schema, and ensure Markdown extraction toggles (`with_metadata`, `include_comments`) are invoked as designed before implementation.
4. Translate user stories and edge cases into integration test scenarios in `tests/integration/test_cli_content_capture.py`, focusing on fresh capture, refresh flag, retry failure, option-driven skips, and partial-success exit code while simulating Trafilatura responses (`fetch_url`, `extract`).
5. Write `quickstart.md` steps detailing environment setup (`uv add trafilatura` plus optional accelerators like `uv add cchardet`), database migration, command invocation in dry-run and live modes, and verification steps (checking sqlite content, JSON mode).
6. Execute `.specify/scripts/bash/update-agent-context.sh codex` to append Trafilatura and content capture context to agent guidelines.

**Output**: `data-model.md`, `/contracts/cli_content_capture_contract.md`, placeholder failing tests (documented in plan), `quickstart.md`, and updated `AGENTS.md`.

## Phase 2: Task Planning Approach
*This section describes what the /tasks command will do - DO NOT execute during /plan*

**Task Generation Strategy**:
- Load `.specify/templates/tasks-template.md` as base
- Generate tasks from Phase 1 design docs (contracts, data model, quickstart)
- Each contract → contract test task [P]
- Each entity → model creation task [P] 
- Each user story → integration test task
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
