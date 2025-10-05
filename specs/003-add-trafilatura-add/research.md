# Research Findings: Full-Text Capture Command

## Trafilatura Markdown Extraction Strategy
- **Decision**: Use Trafilatura's `extract()` with `output_format="markdown"`, a shared HTTP session, and 10-second timeout per link, classifying `HTTPError` and `DownloadError` as retryable once.
- **Rationale**: Markdown output aligns with specification, shared session reduces connection overhead, and explicit timeout prevents the command from hanging on slow domains while still allowing one retry for transient network issues.
- **Alternatives Considered**:
  - HTML output + post-processing → rejected because downstream storage/search focuses on readable text and HTML adds sanitization overhead.
  - Relying on Trafilatura CLI subprocess → rejected to avoid external process management and ensure tighter retry/control flow.

## SQLite Storage Update
- **Decision**: Add nullable `content_markdown` (TEXT) and `content_fetched_at` (TIMESTAMP) columns to the existing `saved_links` table via migration, with indices for filtering `NULL` content.
- **Rationale**: Keeping content on the same record simplifies lookups, keeps schema backward compatible (NULL default), and index allows fast selection of uncaptured links for future runs.
- **Alternatives Considered**:
  - Separate `link_contents` table → rejected for additional joins without immediate multi-version needs.
  - Storing compressed blobs → rejected initially; gzipping can be evaluated later if size becomes an issue.

## CLI UX Consistency
- **Decision**: Name the command `capture-content`, support `--refresh`, `--dry-run`, `--limit`, `--json`, `--verbose`, `--quiet`, and print summary plus optional JSON payload consistent with existing CLI output patterns.
- **Rationale**: Mirrors existing sync/export commands, provides safe defaults, and exposes flags users expect (refresh opt-in, dry-run for audit, limit for testing) while maintaining constitution-required options.
- **Alternatives Considered**:
  - Embedding functionality into existing `sync` command → rejected to keep responsibilities separated and avoid unexpected side effects for current workflows.
  - Using subcommands under `sync` → rejected to avoid deeper nesting and preserve discoverability via top-level help.

## Storage & Performance Considerations
- **Decision**: Process links sequentially by default with optional configurable concurrency later, logging attempt outcomes to a transient in-memory list, and stream summaries to stdout with minimal Rich formatting to avoid slowdowns; add perf test covering 100-link dataset.
- **Rationale**: Sequential processing ensures deterministic behavior, reduces risk of Trafilatura rate limits, and keeps memory usage predictable; performance test enforces constitution defaults.
- **Alternatives Considered**:
  - Immediate concurrency (async or thread pool) → deferred until baseline performance validated; adds complexity with diminishing initial benefit.
  - Persistent attempt log table → rejected for now; existing logging plus CLI summary suffice for MVP.
