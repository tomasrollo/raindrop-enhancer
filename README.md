Raindrop Enhancer

Small CLI to sync Raindrop links, enrich content, generate tag suggestions and write audited JSON exports.

Quickstart

- Install dependencies and create virtualenv with `uv sync`.
- Configure the CLI with `uv run raindrop-enhancer configure --token "$RAINDROP_TOKEN" --data-dir "$HOME/.raindrop_enhancer"`.
- Run a dry-run sync: `uv run raindrop-enhancer sync --mode full --dry-run --json`.

Tooling

This project uses `uv` for Python package, dependency, and build management. Use `uv run` for commands and keep lockfiles current via `uv lock`/`uv sync`.
