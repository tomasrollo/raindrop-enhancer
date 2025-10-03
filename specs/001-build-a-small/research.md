# Research Log: Unified Raindrop Export CLI

## Decision 1: Raindrop endpoints & pagination
- **Decision**: Use `GET /collections` to list accessible collections (including `collections?perpage=200` to reduce calls) and `GET /raindrops/{collection_id}` with `page` + `perpage` query parameters to fetch active items, filtering with `search=type:link -is:archived -is:duplicate` when available; treat `collection_id=0` for unfiled items. Continue paging until `items` array is empty or `page * perpage >= count`.
- **Rationale**: These documented endpoints expose all user collections and raindrops, supporting pagination via `page` and `perpage` with counts in response metadata. Filtering by status ensures only active raindrops per clarification, and using highest allowed `perpage` (200) limits total requests while respecting rate limits.
- **Alternatives Considered**:
  - `GET /raindrops/0` with `search` only: rejected because it omits collection metadata and requires extra mapping.
  - Export backups endpoint: rejected; asynchronous generation with email delivery violates requirement for immediate CLI output.

## Decision 2: Authentication & environment loading
- **Decision**: Load `.env` via `python-dotenv` at CLI startup, retrieve `RAINDROP_TOKEN`, and inject it as `Authorization: Bearer {token}` header in all Gracy requests.
- **Rationale**: Specification mandates `.env` source and fixed variable name. `python-dotenv` integrates cleanly with uv projects and Click CLIs without global side effects. Bearer header is the documented method for test tokens.
- **Alternatives Considered**:
  - Passing token via CLI flag: rejected as it contradicts spec and risks exposing secrets in shell history.
  - Relying on OS env variables only: rejected; `.env` explicit requirement.

## Decision 3: Gracy configuration for rate limits & retries
- **Decision**: Configure Gracy with `GracefulRetry` using exponential backoff starting at 1 second, doubling up to 8 seconds, capping total wait at 60 seconds, retrying on HTTP 429/503. Combine with `GracefulThrottle` rule limiting to 2 requests per second globally to stay under 120/min and reuse a single httpx AsyncClient session.
- **Rationale**: Aligns with FR-007a and Raindrop 120 req/min policy. Exponential backoff mitigates rate bursts; throttle prevents hitting limit. Gracy supports both via built-in configs, simplifying implementation.
- **Alternatives Considered**:
  - Manual retry loops: rejected; more error-prone and bypasses Gracy features.
  - Higher throttle burst (e.g., 5 req/sec): rejected due to risk of hitting limit on large libraries.

## Decision 4: CLI output & user experience
- **Decision**: Implement Click command `raindrop-export` with optional `--output` path (default stdout), `--quiet`, `--verbose`, `--dry-run`, and `--pretty` (for human-readable table). Default output is JSON array written to stdout; Rich used for progress/status when not quiet and not in `--json` only mode.
- **Rationale**: Satisfies constitution's UX expectations while keeping JSON-first contract. Rich progress bars aid feedback during longer exports; options align with existing CLI conventions.
- **Alternatives Considered**:
  - Streaming JSON Lines output: rejected by clarification requiring JSON array.
  - Omit progress indicators: rejected; long exports would appear frozen, harming UX.

## Decision 5: Testing approach
- **Decision**: Use pytest with `pytest-httpx` to simulate Raindrop API responses in unit/contract tests, and `click.testing.CliRunner` for CLI integration tests. Snapshot JSON output using approval fixtures to ensure stable schema.
- **Rationale**: `pytest-httpx` integrates with httpx (used under Gracy), enabling deterministic offline tests. CliRunner is standard for Click-based commands.
- **Alternatives Considered**:
  - Respx: richer mocking but heavier; pytest-httpx simpler and async-friendly.
  - Live API testing: rejected due to credentials & determinism concerns.
