# raindrop-enhancer Development Guidelines

Auto-generated from all feature plans. Last updated: 2025-10-01

## Active Technologies
- Python 3.13 (uv-managed) + click, rich, requests, trafilatura, sqlite3/SQLModel (or SQLAlchemy Core), pathlib, tenacity-style retry helper (in-house) (001-build-an-application)

## Project Structure
```
src/
tests/
```

## Commands
uv run pytest - run tests
uv run raindrop-enhancer - run the application
uv add <package> - add python package to the application dependencies
uv add --dev <package> - add python package as development dependency
uv format - run code linter, formatter and checker, run it after every major code change

## Code Style
Python 3.13 (uv-managed): Follow standard conventions

## Recent Changes
- 001-build-an-application: Added Python 3.13 (uv-managed) + click, rich, requests, trafilatura, sqlite3/SQLModel (or SQLAlchemy Core), pathlib, tenacity-style retry helper (in-house)

<!-- MANUAL ADDITIONS START -->
<!-- MANUAL ADDITIONS END -->