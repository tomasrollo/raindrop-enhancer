# Phase 0 Research — Raindrop Link Enhancer CLI

_Date: 2025-10-01_

## Token & Configuration Storage
- **Decision**: Persist the Raindrop token and CLI configuration in a plaintext `config.toml` file inside the user-selected data directory with `0600` permissions.
- **Rationale**: Aligns with FR-012a clarification, keeps secrets local, avoids external keychain dependencies, and works cross-platform while meeting security expectations when permissions are locked down; mirrors Raindrop documentation guidance on using application console "Test token" values for personal integrations.
- **Alternatives Considered**:
  - macOS Keychain / credential manager — rejected to avoid platform-specific implementations and because spec explicitly chose plaintext config.
  - Environment variables per run — rejected because the CLI must reuse the token across runs without repeated prompts.

## LLM Tagging API Strategy
- **Decision**: Integrate with a configurable external LLM tagging REST API that accepts batched URL content payloads and returns tag/confidence pairs; provide adapter interface for swapping providers.
- **Rationale**: Meets FR-005 clarification while keeping the CLI provider-agnostic; batching lowers latency/cost; abstraction enables mocking for tests.
- **Alternatives Considered**:
  - Local NLP models — rejected due to higher maintenance and performance costs.
  - Keyword frequency heuristics — rejected by clarification in favor of LLM quality.

## SQLite Schema & Performance
- **Decision**: Use SQLite with WAL mode, tables for `links`, `collections`, `link_collections`, `tag_suggestions`, and `sync_runs`, plus indices on `raindrop_id`, `updated_at`, and `processed_at`.
- **Rationale**: Supports deduplication, incremental lookup by collection timestamp, and audit trail storage while staying lightweight.
- **Alternatives Considered**:
  - Plain JSON storage — rejected for inefficient incremental queries and concurrency issues.
  - Embedded key-value store (e.g., TinyDB) — rejected due to weaker query capabilities and type safety.

## Retry & Backoff Handling
- **Decision**: Implement a reusable exponential backoff helper (1s base, doubling to 60s max with full jitter) applied to all Raindrop API calls and LLM tagging requests, honoring `Retry-After` when present.
- **Rationale**: Complies with FR-010 clarification, keeps retries consistent, and isolates retry policy for testing.
- **Alternatives Considered**:
  - Fixed-delay retry — rejected for slower recovery and higher rate-limit risk.
  - No retry — rejected due to reliability requirements.

## Rate Limit Monitoring
- **Decision**: Track `X-RateLimit-Limit`, `X-RateLimit-Remaining`, and `X-RateLimit-Reset` response headers to dynamically throttle and log approaching limits; hard cap concurrent requests to stay within 120 req/min.
- **Rationale**: Matches official Raindrop API guidance; prevents accidental lockouts and feeds metrics into sync summaries.
- **Alternatives Considered**:
  - Blind exponential backoff only — rejected because proactive monitoring avoids unnecessary retries and surfaces better diagnostics.

## CLI UX with click & rich
- **Decision**: Build a `click` command group `raindrop-enhancer` with subcommands `sync` (full/incremental), `reprocess`, and `status`; use `rich` for progress bars/log summaries, but disable rich rendering when `--json` or `--quiet` is active.
- **Rationale**: Satisfies UX consistency principles, provides clear structure, and supports future extensibility.
- **Alternatives Considered**:
  - Single monolithic command with option overload — rejected for poorer discoverability.
  - Alternative CLI frameworks — rejected to follow requirement for `click`.
