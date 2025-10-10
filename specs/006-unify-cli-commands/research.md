````markdown
# Research: Unify CLI commands into single entrypoint

## Decision Summary
- Migration strategy for old console scripts: Remove old scripts immediately (breaking change). Rationale: simplifies maintenance and avoids long-term duplication; project owner accepted breaking change and will provide clear migration instructions in release notes.
- Optional-dependency behavior: Subcommands remain listed; invoking a subcommand with missing optional dependency prints a clear, actionable error with the exact install command and exits non-zero. Rationale: visible UX reduces surprise and makes discoverability consistent; errors guide users to fix missing capabilities.

## Technical Context
- Language/Version: Python >=3.13 (as per pyproject.toml)
- Primary Dependencies: click, gracy, rich, httpx, trafilatura, yt-dlp, dspy (optional)
- Testing: pytest (dev dependencies in pyproject.toml)
- Tooling: uv-managed workflow (uv run, uv add, uv lock)
- Project type: Single Python CLI package (src/raindrop_enhancer)

## Unknowns (resolved)
- Migration approach: resolved (see Decision Summary)
- Optional dependency handling: resolved (see Decision Summary)

## Alternatives considered
- Keep old scripts for N releases: considered but rejected to avoid long-term maintenance and enforcement complexity.
- Hide subcommands when deps missing: considered but rejected in favor of explicit error guidance for discoverability.

## Impact & Risks
- Breaking change: removing old console scripts is a breaking change; must be communicated with MAJOR release and migration docs per Constitution.
- CI and tests: update tests to target new `raindrop-enhancer` entrypoint; ensure coverage gates remain satisfied.

## Actionable Outcomes
- Update `pyproject.toml` to add `raindrop-enhancer` script, remove old scripts (FR-005).
- Update `src/raindrop_enhancer/cli.py` to expose subcommands and implement optional-dep error messages (FR-006).
- Update tests to use new CLI entrypoint and adjust any console-script related assertions.
- Prepare release notes & migration guide snippets in `quickstart.md`.

````
