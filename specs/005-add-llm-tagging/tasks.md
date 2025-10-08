# Tasks: LLM-Assisted Link Tagging

**Input**: Design documents from `/specs/005-add-llm-tagging/`
**Prerequisites**: `plan.md`, `research.md`, `data-model.md`, `contracts/`, `quickstart.md`

## Phase 3.1: Setup
- [X] T001 Add DSPy dependency via `uv add dspy` updating `pyproject.toml` and `uv.lock`.
- [X] T002 Re-lock dependencies (`uv lock && uv sync`) to ensure the workspace is aligned with the new DSPy requirement.

## Phase 3.2: Tests First (TDD) ⚠️ write tests before implementing
- [X] T003 Extend `tests/unit/test_sqlite_store.py` with a failing test that asserts `_ensure_tagging_columns` creates `auto_tags_json` and `auto_tags_meta_json` as `NULL` defaults.
- [X] T004 [P] Create fail-first normalization tests in `tests/unit/test_tag_generator.py` covering Title Case conversion, ≤10 tag limit, and metadata assembly for generated tags.
- [X] T005 [P] Add DSPy settings tests in `tests/unit/test_dspy_settings.py` verifying `RAINDROP_DSPY_MODEL` handling, missing credentials errors, and caching behavior.
 - [X] T006 [P] Implement CLI contract test `tests/contract/test_cli_tags_generate.py` asserting option parsing, JSON summary structure, and exit codes with a stubbed predictor.
 - [X] T007 [P] Add integration test `tests/integration/test_cli_tags_generate_integration.py` simulating dry-run, persistence, and idempotent rerun flows using an in-memory SQLite copy and fake DSPy predictor.

 - [X] T008 Implement `_ensure_tagging_columns` and related migration logic in `src/raindrop_enhancer/storage/sqlite_store.py` to satisfy the new schema tests.
 - [X] T009 [P] Create `src/raindrop_enhancer/models/tagging.py` housing `TagGenerationMetadata` and `GeneratedTag` dataclasses, and update `src/raindrop_enhancer/models.py` to expose the new auto-tag fields with full type hints.
 - [X] T010 Implement `src/raindrop_enhancer/content/dspy_settings.py` to configure DSPy from environment variables with descriptive error messages and memoization.
 - [X] T011 Implement `src/raindrop_enhancer/content/tag_generator.py` defining the DSPy `Signature`, predictor wrapper, normalization pipeline, and metadata packaging that returns `GeneratedTag` instances.
 - [X] T012 Add store helpers in `src/raindrop_enhancer/storage/sqlite_store.py` for fetching untagged links and writing auto tags plus metadata in a single transaction.
 - [X] T013 Create a tagging orchestrator (e.g., `TagGenerationRunner`) in `src/raindrop_enhancer/content/tag_generator.py` that batches links, invokes the predictor, and emits structured result events for the CLI.

## Phase 3.4: Integration
- [X] T014 Wire the `tags generate` Click command into `src/raindrop_enhancer/cli.py`, respecting existing option patterns and delegating to the new runner.
- [X] T015 Layer Rich progress reporting and summary formatting into the CLI command, including `--quiet`, `--json`, `--verbose`, and `--limit` behaviors.
- [X] T016 Implement CLI exit code mapping and error handling paths in `src/raindrop_enhancer/cli.py`, covering migration failures, DSPy misconfiguration, and unexpected exceptions.

## Phase 3.5: Polish & Validation
- [ ] T017 Add performance smoke test `tests/perf/test_cli_tags_generate.py` ensuring a 50-link dry run completes within the documented latency and memory envelopes.
- [X] T018 Update `README.md` with usage docs, environment variable guidance, and sample output for `uv run raindrop-enhancer tags generate`.
- [X] T019 Update `docs/manual-testing.md` with manual validation steps aligned to the quickstart scenarios.
- [X] T020 Run `uv run pytest` and capture results in the feature branch notes.
- [ ] T021 Execute the quickstart commands end-to-end (dry-run then persistence) and record outputs or issues in `docs/manual-testing.md`.

## Dependencies
- T002 depends on T001 (requires DSPy added before re-locking).
- T003 depends on T002 completing (tests rely on updated environment).
- T004–T007 depend on T003 (schema test establishes baseline fixtures) but can start in parallel once T003 is red.
- T008 depends on all Phase 3.2 tests being red.
- T009 depends on T008 (models rely on updated store contract).
- T010 depends on T005 (tests define required behavior).
- T011 depends on T004, T005, T009, and T010.
- T012 depends on T008.
- T013 depends on T011 and T012.
- T014 depends on T013.
- T015 depends on T014.
- T016 depends on T015.
- T017 depends on T016.
- T018 and T019 depend on T016 (docs should match final behavior).
- T020 depends on T017–T019.
- T021 depends on T020 (run quickstart after tests pass).

## Parallel execution example
```
# After completing T003, launch the independent fail-first tests together:
task run --id T004
task run --id T005
task run --id T006
task run --id T007
```