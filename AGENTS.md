# raindrop-enhancer Development Guidelines

Auto-generated from all feature plans. Last updated: 2025-10-03

## Active Technologies
- Python 3.13 (per `pyproject.toml` / uv defaults) + Gracy (HTTP client), httpx (indirect via Gracy), Click (CLI), Rich (console rendering), python-dotenv or uv-managed dotenv support (verify) (001-build-a-small)
- Python 3.13 (uv-managed per `pyproject.toml`) + Gracy/httpx (Raindrop API), Click (CLI), Rich (console UX), sqlite3 stdlib (embedded DB), python-dotenv (env loading) (002-storage-and-sync)
- SQLite `.db` file stored under user config directory (`~/.local/share/raindrop_enhancer/raindrops.db` on POSIX, platform-specific equivalent elsewhere) (002-storage-and-sync)
- Python 3.13 + Click, Rich, Gracy/httpx, Trafilatura, sqlite3, python-dotenv (003-add-trafilatura-add)
- SQLite database at platform config directory (`raindrops.db`) (003-add-trafilatura-add)
- Python 3.13 (uv-managed) + Click, Rich, Gracy/httpx, SQLite stdlib, Trafilatura, DSPy (new), python-dotenv, pytes (005-add-llm-tagging)
- SQLite database at user config path (`raindrop_links` table) (005-add-llm-tagging)

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
- 005-add-llm-tagging: Added Python 3.13 (uv-managed) + Click, Rich, Gracy/httpx, SQLite stdlib, Trafilatura, DSPy (new), python-dotenv, pytes
- 004-handle-youtube-videos: Added [if applicable, e.g., PostgreSQL, CoreData, files or N/A]
- 003-add-trafilatura-add: Added Python 3.13 + Click, Rich, Gracy/httpx, Trafilatura, sqlite3, python-dotenv

<!-- MANUAL ADDITIONS START -->
<!-- MANUAL ADDITIONS END -->
