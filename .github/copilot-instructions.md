# raindrop-enhancer Development Guidelines

Auto-generated from all feature plans. Last updated: 2025-10-03

## Active Technologies
- Python 3.13 (per `pyproject.toml` / uv defaults) + Gracy (HTTP client), httpx (indirect via Gracy), Click (CLI), Rich (console rendering), python-dotenv or uv-managed dotenv support (verify) (001-build-a-small)
- N/A (remote Raindrop API only) (001-build-a-small)
- Python 3.13 (uv-managed per `pyproject.toml`) + Gracy/httpx (Raindrop API), Click (CLI), Rich (console UX), sqlite3 stdlib (embedded DB), python-dotenv (env loading) (002-storage-and-sync)
- SQLite `.db` file stored under user config directory (`~/.local/share/raindrop_enhancer/raindrops.db` on POSIX, platform-specific equivalent elsewhere) (002-storage-and-sync)

## Project Structure
```
src/
tests/
```

## Commands
cd src [ONLY COMMANDS FOR ACTIVE TECHNOLOGIES][ONLY COMMANDS FOR ACTIVE TECHNOLOGIES] pytest [ONLY COMMANDS FOR ACTIVE TECHNOLOGIES][ONLY COMMANDS FOR ACTIVE TECHNOLOGIES] ruff check .

## Code Style
Python 3.13 (per `pyproject.toml` / uv defaults): Follow standard conventions

## Recent Changes
- 002-storage-and-sync: Added Python 3.13 (uv-managed per `pyproject.toml`) + Gracy/httpx (Raindrop API), Click (CLI), Rich (console UX), sqlite3 stdlib (embedded DB), python-dotenv (env loading)
- 001-build-a-small: Added Python 3.13 (per `pyproject.toml` / uv defaults) + Gracy (HTTP client), httpx (indirect via Gracy), Click (CLI), Rich (console rendering), python-dotenv or uv-managed dotenv support (verify)
- 001-build-a-small: Added Python 3.13 (per `pyproject.toml` / uv defaults) + Gracy (HTTP client), httpx (indirect via Gracy), Click (CLI), Rich (console rendering), python-dotenv or uv-managed dotenv support (verify)

<!-- MANUAL ADDITIONS START -->
<!-- MANUAL ADDITIONS END -->
