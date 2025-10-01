<!--
Sync Impact Report
Version change: 1.0.0 → 1.1.0
Modified principles: (no title changes)
Added sections:
 - Tooling & Dependency Management (uv standardization)
 - Documentation & Release Standards (expanded with tooling note)
Removed sections:
 - None
Templates requiring updates:
 - .specify/templates/plan-template.md ✅ updated (Constitution Check includes uv usage)
 - .specify/templates/tasks-template.md ✅ updated (Setup and validation reference uv)
 - .specify/templates/spec-template.md ✅ reviewed (no change needed)
 - README.md ✅ updated (constitution link + uv note)
Follow-up TODOs:
 - None
-->

# Raindrop Enhancer Constitution

## Core Principles

### I. Code Quality Discipline
Non-negotiable rules:
- Code MUST pass formatting and linting in CI using Black (format), Ruff (lint), and conventional import/order rules.
- Static typing with MyPy is REQUIRED for all modules; disallow implicit Any. Exemptions MUST be local with a comment and an issue link.
- Complexity limits: per-function cyclomatic complexity ≤ 10; files ≥ 500 lines REQUIRE justification in the PR description.
- No dead code or unused dependencies; public APIs MUST include docstrings with usage examples.

Rationale: Consistent style, static guarantees, and bounded complexity keep the codebase maintainable and reviewable over time.

### II. Testing Standards & TDD
Non-negotiable rules:
- Tests MUST be written before implementation for new behavior (Red → Green → Refactor cycle enforced).
- Test layers: unit tests for logic, integration tests for IO/boundaries, and contract tests when external APIs or CLIs are exposed.
- Coverage thresholds: lines ≥ 90% and branches ≥ 80% on changed code; overall coverage MUST not decrease.
- Tests MUST be deterministic and fast: unit tests run without network or real external services; use fakes/mocks; each test completes in < 2s.
- CI is a hard gate: failing tests or insufficient coverage block merges.

Rationale: TDD and strong coverage produce reliable, evolvable features and prevent regressions.

### III. User Experience Consistency
Non-negotiable rules:
- CLI commands MUST provide --help, consistent flag names (kebab-case), and support --verbose, --quiet, and --dry-run where applicable.
- IO contract: human-readable text to stdout by default; machine-readable JSON via --json; errors to stderr with stable exit codes.
- Defaults favor safety and idempotency; messages and prompts follow a consistent tone and structure.
- Backward compatibility is REQUIRED for user-facing flags and output fields; breaking changes require a MAJOR release and a deprecation window.

Rationale: Predictable interfaces reduce user friction and support scripting/automation.

### IV. Performance & Efficiency
Non-negotiable rules:
- Each feature plan MUST declare explicit performance goals. If unspecified, apply defaults: p95 latency < 200ms per core operation, p99 < 500ms; peak RSS ≤ 150MB for typical workloads.
- Core flows MUST include a performance test or benchmark; regressions > 10% require explicit approval and a follow-up optimization task.
- Batch operations MUST handle at least 10k items in ≤ 60s by default, or document domain-specific targets.
- Substantive changes implicated in > 5% CPU or memory use MUST be profiled and have findings documented in the PR.

Rationale: Guardrails ensure responsiveness and prevent performance drift as features evolve.

## Quality Gates & Workflow

- Pre-merge gates in CI: format (Black), lint (Ruff), types (MyPy), tests (pytest), coverage enforcement, and performance checks for impacted paths.
- Definition of Done includes: updated docs (--help output snapshots and README sections), changelog entry, and constitution compliance checklist.
- PRs MUST document any deviations from principles with a justification and link to follow-up tasks.

## Documentation & Release Standards

- User-facing documentation MUST be updated alongside code changes that alter behavior or flags.
- Semantic Versioning (SemVer) governs releases; breaking changes require MAJOR bump and a migration note.
- Release notes MUST summarize behavior changes, performance impacts, and any deprecations.

## Tooling & Dependency Management

- The project MUST use uv for package, dependency, and build management.
	- Dependency add/update: `uv add/remove`, lock with `uv lock`, sync with `uv sync`.
	- Execution: `uv run <cmd>` is the canonical way to run tools and project entry points.
	- Python version and project metadata live in `pyproject.toml`; uv-managed virtualenvs MUST be used.
	- CLI entry points SHOULD be defined in `[project.scripts]` and runnable via `uv run`.
- Lockfiles MUST be kept up to date and committed as required by repository policy (use `uv lock`/`uv export` per workflow).
- CI pipelines MUST install and use uv to reproduce environments and run checks.

## Governance

- This Constitution supersedes other practices when conflicts arise.
- Amendments: open a PR labeled governance with a summary of changes, rationale, version bump type (MAJOR/MINOR/PATCH), and migration guidance if applicable.
- Versioning policy for this document follows SemVer:
	- MAJOR: backward-incompatible governance or principle redefinitions/removals.
	- MINOR: new principles/sections or materially expanded guidance.
	- PATCH: clarifications and non-semantic edits.
- Ratification: at least one maintainer approval required; merge records the new version and updates dates.
- Compliance: code reviews MUST verify principle adherence; CI enforces gates. Non-compliance requires either remediation before merge or an approved, time-bound exception with tracking.

**Version**: 1.1.0 | **Ratified**: 2025-10-01 | **Last Amended**: 2025-10-01