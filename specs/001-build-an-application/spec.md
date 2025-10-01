# Feature Specification: Raindrop Link Enhancer CLI

**Feature Branch**: `001-build-an-application`  
**Created**: 2025-10-01  
**Status**: Draft  
**Input**: User description: "build an application that connects to the Raindrop service over API, downloads all links in all collections, stores them locally, then fetches each of the links using the `trafilatura` python library and generates a set of suggested tags for each of the links. Make the links and the tags available in a local JSON file. Include support for incrementally processing newly added links later one. The application should be a cli application."

## User Scenarios & Testing *(mandatory)*

### Primary User Story
A knowledge worker who saves research links in Raindrop wants to export structured insights. They run the CLI, authenticate with their Raindrop account, download all saved links, enrich each link with suggested tags, and receive an up-to-date JSON file they can open in spreadsheets or share with collaborators.

### Acceptance Scenarios
1. **Given** the user has provided valid Raindrop API credentials and a writable local data directory, **When** they execute the CLI for a full sync, **Then** the tool downloads every link from all Raindrop collections, stores metadata locally, enriches each link with suggested tags, and writes a JSON file containing link metadata and tags.
2. **Given** a prior full sync completed and new links have since been added to Raindrop, **When** the user runs the CLI in incremental mode, **Then** only the newly added or updated links are fetched, enriched, and appended to the local store and JSON without duplicating previously processed entries.

### Edge Cases
- Raindrop API rate limiting or service outages MUST trigger exponential backoff with resumable syncing; unresolved outages are reported in the run summary (see **FR-010**).
- If `trafilatura` cannot extract content, the link MUST be marked as "needs manual review", logged with the failure reason, and progress MUST continue for other links (see **FR-012** / **FR-017**).
- Links encountered multiple times (e.g., across collections or re-saved) MUST be deduplicated by Raindrop ID while retaining all collection memberships and metadata updates (see **FR-016**).
- Invalid or expired Raindrop Test tokens MUST prompt the user to re-enter a token and abort the sync with a clear message if authentication cannot be restored (see **FR-001**).

## Requirements *(mandatory)*

### Functional Requirements
- **FR-001**: The CLI MUST prompt for or accept the Raindrop Test token issued via the Raindrop management console, verify it is valid before syncing, and prompt the user to re-enter a token if authentication fails.
- **FR-002**: The system MUST retrieve all collections and associated links from the Raindrop API during an initial full sync.
- **FR-003**: The system MUST persist downloaded link metadata (identifier, collection membership, URL, title, description, timestamps) in a local storage layer to support incremental processing.
- **FR-003**: The system MUST persist downloaded link metadata (identifier, collection membership, URL, title, description, timestamps) in a SQLite database file stored in the user-selected data directory to support incremental processing and synchronization tracking.
- **FR-004**: The system MUST fetch each link’s content using the `trafilatura` library (or equivalent content extraction) for links that have not yet been processed.
- **FR-005**: The system MUST generate a set of suggested tags for each processed link based on extracted content and existing metadata.
- **FR-005**: The system MUST generate a set of suggested tags for each processed link by calling an external LLM tagging API (paid) that analyzes the extracted content and existing metadata. The CLI MUST handle API errors gracefully and allow configuration of API credentials via the same local config file that stores the Raindrop token.
- **FR-006**: The CLI MUST produce a JSON export containing link metadata, suggested tags, processing timestamp, and collection references, and update it after each sync.
- **FR-007**: The system MUST support incremental sync operations that identify and process only links that are new or changed since the previous run.
- **FR-007**: The system MUST support incremental sync operations that identify and process only links that are new or changed since the previous run by tracking the last sync timestamp per collection and fetching links whose Raindrop `lastUpdate` falls after that timestamp.
- **FR-008**: Users MUST be able to specify the destination directory for local storage and JSON output.
- **FR-009**: The CLI MUST provide clear progress output and summary reporting, including counts of processed links, skipped links, and encountered failures.
- **FR-010**: The system MUST handle Raindrop API rate limits or errors gracefully by retrying with backoff and surfacing unresolved issues without aborting successful work.
- **FR-010**: The system MUST handle Raindrop API rate limits or errors gracefully by retrying with exponential backoff starting at 1 second, doubling up to a maximum delay of 60 seconds, and applying jitter. After exhausting retries, unresolved issues must be surfaced without aborting successful work.
- **FR-011**: The CLI MUST expose a way to reprocess a specific link or collection on demand without requiring a full resync.
- **FR-012**: The system MUST log failures (e.g., content extraction errors) with enough detail for troubleshooting while keeping sensitive data secure.
- **FR-012a**: The CLI MUST store the provided Raindrop Test token in a local plaintext config file alongside other settings within the user-selected data directory and reuse it for subsequent runs unless the user supplies a new token. The config file MUST be created with file permissions that restrict access to the current user and include a warning in the documentation about rotating or deleting the token file when necessary.
- **FR-013**: The solution MUST allow users to configure the minimum confidence threshold or number of suggested tags generated per link.
- **FR-014**: The system MUST maintain an audit trail of sync runs (timestamps, counts, duration) accessible via the CLI.
- **FR-015**: The CLI MUST exit with a non-zero status code if critical failures prevent producing an updated JSON.
- **FR-016**: The system MUST deduplicate links by Raindrop ID, merging collection memberships, tags, and updated metadata into a single canonical record.
- **FR-017**: When content extraction fails for a link, the system MUST flag the link as requiring manual review, log the reason, and ensure the link remains in the JSON with a status indicator.

### Key Entities *(include if feature involves data)*
- **Link Record**: Represents a Raindrop item with fields for Raindrop ID, URL, title, description, collection IDs, original tags, processed timestamp, and enrichment status.
- **Tag Suggestion**: Captures suggested tags per link, including tag text, confidence score, and the source (content analysis, metadata, existing tags).
- **Sync Run**: Tracks an execution of the CLI with attributes such as run identifier, start/end time, mode (full vs incremental), number of processed/skipped links, failures, and output file path.

---

## Clarifications
### Session 2025-10-01
- Q: How should we persist the Raindrop Test token securely between runs? → A: Option C — store in a local plaintext config file alongside other settings.
- Q: What strategy should the CLI use to generate suggested tags once link content is available? → A: Option C — call an external LLM tagging API (paid).
- Q: How should incremental sync decide which links need reprocessing? → A: Option A — track last sync timestamp per collection and fetch links updated since then.
- Q: What storage mechanism should the CLI use for local metadata and sync tracking? → A: Option A — SQLite database file in the data directory.
- Q: Which retry/backoff strategy should the CLI follow when Raindrop API calls hit rate limits or transient errors? → A: Option A — exponential backoff starting at 1s, doubling up to 60s, with jitter.

---

## Review & Acceptance Checklist
*GATE: Automated checks run during main() execution*

### Content Quality
- [ ] No implementation details (languages, frameworks, APIs)
- [ ] Focused on user value and business needs
- [ ] Written for non-technical stakeholders
- [ ] All mandatory sections completed

### Requirement Completeness
- [ ] No [NEEDS CLARIFICATION] markers remain
- [ ] Requirements are testable and unambiguous  
- [ ] Success criteria are measurable
- [ ] Scope is clearly bounded
- [ ] Dependencies and assumptions identified

---

## Execution Status
*Updated by main() during processing*

- [ ] User description parsed
- [ ] Key concepts extracted
- [ ] Ambiguities marked
- [ ] User scenarios defined
- [ ] Requirements generated
- [ ] Entities identified
- [ ] Review checklist passed

---
