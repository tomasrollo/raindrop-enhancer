# raindrop-enhancer Development Guidelines

Auto-generated from all feature plans. Last updated: 2025-10-03

## Active Technologies
- Python 3.13 (per `pyproject.toml` / uv defaults) + Gracy (HTTP client), httpx (indirect via Gracy), Click (CLI), Rich (console rendering), python-dotenv or uv-managed dotenv support (verify) (001-build-a-small)

## Project Structure
```
src/
tests/
```

## Commands
- `uv run pytest` - run tests
- `uv run raindrop-enhancer` - run the application
- `uv add <package>` - add python package to the application dependencies
- `uv add --dev <package>` - add python package as development dependency
- `uv format` - run code linter, formatter and checker, run it after every major code change

## Code Style
Python 3.13 (per `pyproject.toml` / uv defaults): Follow standard conventions

## Recent Changes
- 001-build-a-small: Added Python 3.13 (per `pyproject.toml` / uv defaults) + Gracy (HTTP client), httpx (indirect via Gracy), Click (CLI), Rich (console rendering), python-dotenv or uv-managed dotenv support (verify)

<!-- MANUAL ADDITIONS START -->
<!-- MANUAL ADDITIONS END -->