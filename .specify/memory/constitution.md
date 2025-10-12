<!--
Sync Impact Report
- Version change: N/A -> 1.0.0
- Modified principles: [PRINCIPLE_1_NAME] -> Code Quality First; [PRINCIPLE_2_NAME] -> Tests Define Delivery; [PRINCIPLE_3_NAME] -> Consistent CLI Experience
- Added sections: Tooling & Environment Standards; Development Workflow
- Removed sections: Principle slots IV and V placeholders
- Templates requiring updates: .specify/templates/plan-template.md -> updated; .specify/templates/spec-template.md -> updated; .specify/templates/tasks-template.md -> updated
- Follow-up TODOs: none
-->

# raindrop-enhancer Constitution

## Core Principles

### Code Quality First
We build features as maintainable Python 3.13 modules that favor clarity, type safety, and reuse. Every change MUST keep module boundaries tidy, document tricky decisions inline, and rely on the standard library or existing helpers before adding new dependencies.

### Tests Define Delivery
No work is complete until automated tests verify it. Each increment MUST add or update pytest coverage across the right levels (unit, integration, contract, CLI) so the intended behavior fails without the implementation and passes after. Regression gaps require explicit sign-off.

### Consistent CLI Experience
Our Click-powered CLI MUST present stable command shapes, flags, and output formats. Human-readable output uses the existing Rich patterns, and machine output remains valid JSON. Error conditions return actionable stderr messaging with non-zero exit codes.

## Tooling & Environment Standards

- Manage dependencies, formatting, and execution with `uv`; document any command beyond `uv add`, `uv run raindrop-enhancer`, `uv run pytest`, and `uv format`.
- Prefer project-wide linting and formatting defaults; justify deviations in the change description.
- Persist local assets such as SQLite databases in the configured platform path and never hard-code user-specific locations.
- Capture new third-party requirements in `pyproject.toml` with rationale and minimum supported versions, use `uv add` to add new third-party requirements in controlled fashion.

## Development Workflow

- Start with plan and research artifacts that spell out module impacts, test scope, and CLI UX adjustments aligned with these principles.
- Draft or update tests before implementation, ensuring they fail to guard against false positives.
- Implement features using small, reviewable commits, and update Rich or Click output snapshots in docs or tests when behavior changes.
- Manually exercise user-facing commands to confirm ergonomics, documenting notable UX adjustments in quickstarts or docs.

## Governance

- This constitution guides feature planning, specifications, implementation tasks, and reviews; conflicts resolve in favor of the newest version.
- Amendments require maintainer consensus, a template impact audit, and a documented rationale committed with the change.
- Versioning follows semantic rules: MAJOR for breaking governance shifts, MINOR for new enforceable rules, PATCH for clarifications without new obligations.
- Maintainers review compliance during planning, code review, and manual testing. Deviations require explicit tracking in plan or task documents with mitigation steps.

**Version**: 1.0.0 | **Ratified**: 2025-10-12 | **Last Amended**: 2025-10-12
