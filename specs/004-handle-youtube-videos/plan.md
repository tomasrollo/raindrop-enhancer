# Implementation Plan: Handle Youtube Videos

**Branch**: `004-handle-youtube-videos` | **Date**: 2025-10-06 | **Spec**: [link](./spec.md)
**Input**: Feature specification from `/specs/004-handle-youtube-videos/spec.md`

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
This feature will enhance the Raindrop bookmarking tool to automatically fetch and store the title and description for any YouTube video links. It will use the `yt-dlp` library to extract this metadata, format it as Markdown, and save it to the `content_markdown` field in the database. The system will handle cases where videos are unavailable or fetching fails by storing specific placeholder text.

## Technical Context
**Language/Version**: Python 3.11
**Primary Dependencies**: `yt-dlp`, `gracy`, `trafilatura`
**Storage**: SQLite
**Testing**: `pytest`
**Target Platform**: CLI application
**Project Type**: Single project
**Performance Goals**: 30-second timeout for YouTube metadata fetch.
**Constraints**: None
**Scale/Scope**: Handle individual links.

## Constitution Check
*GATE: Must pass before Phase 0 research. Re-check after Phase 1 design.*

The plan MUST explicitly address the following gates per the Constitution:
- Code Quality: All new code will be formatted with Black, linted with Ruff, and type-checked with MyPy. Docstrings will be added for any new public functions.
- Testing Standards & TDD: Unit tests will be created to verify the YouTube link identification and metadata extraction logic. Integration tests will ensure the end-to-end process works correctly. Contract tests are not applicable as no new APIs are being exposed.
- UX Consistency: The feature is an enhancement to an existing command, so no new CLI flags are needed.
- Performance & Efficiency: A 30-second timeout is specified for the YouTube metadata fetch to prevent the application from hanging.
- Tooling & Dependency Management: `uv` will be used to manage dependencies.

## Project Structure

### Documentation (this feature)
```
specs/004-handle-youtube-videos/
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
# Option 1: Single project (DEFAULT)
src/
└── raindrop_enhancer/
    ├── content/
    │   └── youtube_extractor.py # New module for YouTube metadata extraction
    ├── cli.py # Modified to integrate the new feature
    └── storage/
        └── sqlite_store.py # Existing storage layer

tests/
└── unit/
    └── test_youtube_extractor.py # New unit tests
```

**Structure Decision**: The project is a single CLI application. The new logic for handling YouTube videos will be encapsulated in a new module, `youtube_extractor.py`, within the `content` package.

## Phase 0: Outline & Research
1. **Extract unknowns from Technical Context**: All technical context items were clarified.
2. **Generate and dispatch research agents**: The user provided the key technical detail (`yt-dlp` usage), so no further research was needed.
3. **Consolidate findings** in `research.md`.

**Output**: `research.md` with all NEEDS CLARIFICATION resolved.

## Phase 1: Design & Contracts
*Prerequisites: research.md complete*

1. **Extract entities from feature spec** → `data-model.md`: The `content_markdown` field of the existing `Raindrop` entity will be used.
2. **Generate API contracts**: No new APIs are being exposed, so no contracts are needed.
3. **Generate contract tests**: Not applicable.
4. **Extract test scenarios** from user stories → `quickstart.md`.
5. **Update agent file incrementally**: The agent file has been updated.

**Output**: `data-model.md`, `/contracts/README.md`, `quickstart.md`, and the updated agent file.

## Phase 2: Task Planning Approach
*This section describes what the /tasks command will do - DO NOT execute during /plan*

**Task Generation Strategy**:
- Create a new module `src/raindrop_enhancer/content/youtube_extractor.py`.
- Implement a function to identify YouTube links.
- Implement a function to extract title and description using `yt-dlp`.
- Add unit tests for the new functions in `tests/unit/test_youtube_extractor.py`.
- Modify the `cli.py` and/or `sync/orchestrator.py` to use the new YouTube extractor.
- Add integration tests to verify the end-to-end functionality.

**Ordering Strategy**:
1.  Create the `youtube_extractor.py` module and its unit tests.
2.  Implement the YouTube link identification function and its tests.
3.  Implement the metadata extraction function and its tests.
4.  Integrate the new module into the main application.
5.  Create integration tests.

**Estimated Output**: 5-7 numbered, ordered tasks in `tasks.md`.

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
|           |            |                                     |

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