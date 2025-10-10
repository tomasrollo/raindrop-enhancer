
# Implementation Plan: LLM-Assisted Link Tagging

**Branch**: `005-add-llm-tagging` | **Date**: 2025-10-08 | **Spec**: [link](./spec.md)
**Input**: Feature specification from `/specs/005-add-llm-tagging/spec.md`

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
Add a new CLI command that scans stored links lacking tags, generates up to 10 English Title Case tags (≤20 characters) per link using a DSPy-driven LLM workflow, and saves the results in a dedicated `auto_tags` column in the SQLite store while leaving manually curated tags untouched. The run must provide continuous progress reporting, skip links that already have tags, and surface per-link outcomes and failures without retrying automatically.

## Technical Context
**Language/Version**: Python 3.13 (uv-managed)
**Primary Dependencies**: Click, Rich, Gracy/httpx, SQLite stdlib, Trafilatura, DSPy (new), python-dotenv, pytest
**Storage**: SQLite database at user config path (`raindrop_links` table)
**Testing**: pytest with existing contract/integration/unit suites (execute via `uv run pytest`)
**Target Platform**: Cross-platform CLI (macOS/Linux/Windows shells)
**Project Type**: Single back-end/CLI project (src + tests)
**Performance Goals**: Provide progress feedback each 5 links processed; per-link LLM latency budget ≤ 25s (95th percentile) with batch memory ≤ 150 MB; command should finish 200-link batches in ≤ 15 minutes given external LLM latency.
**Constraints**: Tags limited to 10 Title Case entries (≤20 chars), English only, no automatic retries, respect existing CLI flag conventions, must run fully offline after content is downloaded except for LLM calls.
**Scale/Scope**: Designed for collections up to 10k stored links with typical tagging runs on 0.5–2k untagged items.

## Constitution Check
*GATE: Must pass before Phase 0 research. Re-check after Phase 1 design.*

The plan MUST explicitly address the following gates per the Constitution:
- **Code Quality**: All new modules will include full type hints and docstrings. We will extend MyPy coverage, enforce Black/Ruff via pre-commit, and isolate pure functions for DSPy prompt construction to keep cyclomatic complexity < 8 per function.
- **Testing Standards & TDD**: Add fail-first unit tests for DSPy prompt builder and tag post-processing, integration tests to validate CLI command flow with faked DSPy predictor, and contract-style tests for CLI output (text and `--json`). Maintain ≥90% line / 80% branch coverage on new code with deterministic fakes for LLM responses.
- **UX Consistency**: Introduce `tags generate` CLI subcommand supporting `--limit`, `--dry-run`, `--json`, `--verbose`, and `--quiet`. Tool will emit progress to stdout, errors to stderr, and maintain existing exit-code semantics (0 success, >0 failure). Help text updated accordingly.
- **Performance & Efficiency**: Track per-link timing via Rich progress display and log summary metrics; fall back to chunked processing (size 5) to avoid memory spikes. Define follow-up profiling if p95 latency exceeds 25s or memory >150 MB.
- **Tooling & Dependency Management**: Add DSPy via `uv add dspy`, lock dependencies with `uv lock`, and ensure execution paths use `uv run`. Any environment variables (model keys) documented in quickstart; no ad-hoc virtualenv creation.

ios/ or android/
## Project Structure

### Documentation (this feature)
```
specs/005-add-llm-tagging/
├── plan.md              # This file (/plan command output)
├── research.md          # Phase 0 output (/plan command)
├── data-model.md        # Phase 1 output (/plan command)
├── quickstart.md        # Phase 1 output (/plan command)
├── contracts/           # Phase 1 output (/plan command)
│   └── README.md
└── tasks.md             # Phase 2 output (/tasks command - NOT created by /plan)
```

### Source Code (repository root)
```
src/
└── raindrop_enhancer/
   ├── cli.py
   ├── models.py
   ├── api/
   │   └── raindrop_client.py
   ├── content/
   │   ├── capture_runner.py
   │   ├── fetcher.py
   │   ├── youtube_extractor.py
   │   └── __init__.py
   ├── exporters/
   │   └── json_exporter.py
   ├── storage/
   │   ├── __init__.py
   │   └── sqlite_store.py
   └── sync/
      └── __init__.py

tests/
├── contract/
├── integration/
│   ├── test_cli_content_capture_integration.py
│   ├── test_cli_export.py
│   └── test_cli_sync.py
└── unit/
   ├── test_content_fetcher.py
   ├── test_sqlite_store.py
   ├── test_sqlite_store_content.py
   └── test_youtube_extractor.py
```

**Structure Decision**: Single uv-managed CLI/backend project. New tagging logic will live in `src/raindrop_enhancer/content/tag_generator.py` (or similar) with DSPy pipeline helpers, while CLI wiring occurs in `cli.py` and persistence updates in `storage/sqlite_store.py`. Tests will extend existing `tests/unit` and `tests/integration` suites.
## Phase 0: Outline & Research
- Reviewed DSPy tutorials via context7 to confirm best practices for defining `dspy.Signature` classes and instantiating `dspy.Predictor` modules with global settings. Documented the chosen approach plus alternatives in `research.md`.
- Established environment strategy: expose `RAINDROP_DSPY_MODEL` and rely on provider-specific API keys (OpenAI example), keeping uv-driven execution documented in quickstart.
- Analyzed SQLite schema to confirm compatibility and planned new `auto_tags_json` + metadata columns for idempotent runs.
- Selected Rich progress integration and failure-reporting pattern to satisfy UX and non-retry constraints while aligning with constitution defaults.

**Output**: `research.md` capturing decisions, rationales, and rejected alternatives.

## Phase 1: Design & Contracts
- Updated data model (`data-model.md`) to add `auto_tags_json` and `auto_tags_meta_json` columns on `raindrop_links`, plus an internal `GeneratedTag` dataclass with validation rules.
- Authored CLI contract (`contracts/cli_tags_generate.md`) detailing flags, IO guarantees, exit codes, and JSON schema expectations; updated contracts README accordingly.
- Drafted quickstart guide showing dry-run usage, credential configuration, and verification steps, ensuring TDD focus on CLI and storage flows.
- Planned DSPy module structure (`content/tag_generator.py`) including signature definitions, normalization pipeline, and metadata capture, with emphasis on testability using deterministic fakes.
- Ran `.specify/scripts/bash/update-agent-context.sh codex` to record DSPy as an active technology and keep recent changes current.

**Output**: `data-model.md`, `contracts/`, `quickstart.md`, refreshed agent context, and design notes for fail-first tests.

## Phase 2: Task Planning Approach
*This section describes what the /tasks command will do - DO NOT execute during /plan*

**Task Generation Strategy**:
- Use `.specify/templates/tasks-template.md` as the scaffold.
- Derive tasks from research, data model, quickstart, and contracts: schema migration tasks, DSPy pipeline module creation, CLI wiring, persistence updates, and multi-layer tests (unit, integration, contract/CLI output, perf smoke).
- Include dedicated tasks for uv dependency update (`uv add dspy`), DSPy settings configuration, and documenting environment variables.
- Parallelize independent test authoring tasks (mark with [P]) once shared fixtures exist.

**Ordering Strategy**:
1. Begin with database migration and data model tests to ensure storage ready for implementation.
2. Add fail-first unit tests for DSPy signature + tag normalization, followed by implementation tasks.
3. Wire CLI command and integration tests, then contract tests for CLI output and quickstart script validation.
4. Close with documentation and performance validation tasks.

**Estimated Output**: 20–28 ordered tasks in `tasks.md`, with ~6 tasks flagged [P] for parallel execution.

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
