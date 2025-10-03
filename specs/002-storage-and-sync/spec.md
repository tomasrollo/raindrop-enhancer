# Feature Specification: Persistent Storage and Incremental Sync for Raindrop Links

**Feature Branch**: `002-storage-and-sync`  
**Created**: 2025-10-03  
**Status**: Draft  
**Input**: User description: "Storage and sync - add SQLite DB to store the retrieve links and incremental sync that only fetches newly added links"

## User Scenarios & Testing *(mandatory)*

### Primary User Story
A Raindrop power user wants their exported links preserved locally so they can search or analyze them later without re-running a full export. They run the CLI regularly, expecting it to remember earlier results, capture only newly added links from Raindrop, and keep the local archive current.

### Acceptance Scenarios
1. **Given** the user has previously completed an export and a local archive exists, **When** they run the sync command again, **Then** the system records the last successful sync point, fetches only raindrops created since that point, and appends the new links to the archive while informing the user how many items were added.
2. **Given** the user launches the sync command with no existing archive on disk, **When** the process runs, **Then** the system performs a complete fetch of all accessible raindrops, saves them locally, establishes a baseline sync marker, and confirms the archive is ready for future incremental runs.

### Edge Cases
- What happens when the local archive is missing, corrupted, or unreadable? → The system should recreate it safely or prompt the user before overwriting. 
- How does the system handle Raindrop API rate limits or outages encountered mid-sync? → It should retry gracefully and avoid marking the sync as complete until successful.
- What if a raindrop is updated or deleted in Raindrop after being stored locally? → The system ignores upstream edits or deletions and retains the original record, only adding brand-new links.
- How should the system behave when multiple devices or users share the same token and run sync concurrently? → The feature assumes single-device usage; simultaneous runs are unsupported and may lead to conflicts.

## Requirements *(mandatory)*

### Functional Requirements
- **FR-001**: The system MUST maintain a persistent local archive of retrieved raindrop metadata so that the user can review prior exports without re-fetching from Raindrop.
- **FR-002**: When no archive exists, the system MUST perform a complete export of all accessible raindrops and initialize baseline sync metadata for future runs.
- **FR-003**: After a baseline exists, the system MUST request only raindrops created after the last successful sync point and append them to the archive without altering or removing existing records.
- **FR-004**: The system MUST record and update a reliable sync cursor (e.g., timestamp or identifier) after each successful run to support future incremental fetches.
- **FR-005**: The system MUST verify the integrity of the local archive at the start of each run and prevent corruption by rolling back or alerting the user if the archive cannot be updated safely.
- **FR-006**: The system MUST provide a user-facing summary at the end of each run that states whether the sync succeeded and how many new links were stored.
- **FR-007**: The system MUST handle Raindrop API pagination, rate limits, and transient errors during sync without duplicating entries or marking the run as successful prematurely.
- **FR-008**: The system MUST allow the user to trigger a full re-sync when needed without manually deleting files by offering a dedicated CLI flag (e.g., `--full-refresh`).

### Key Entities
- **Stored Link Record**: Represents a locally archived raindrop, including identifiers, URL, title, tags, collection reference, created timestamp, and the sync run that captured it.
- **Sync Metadata**: Represents the state needed for incremental sync, including the last successful sync cursor, archive integrity status, and statistics from previous runs.

## Dependencies & Assumptions
- Raindrop API responses include a reliable attribute (e.g., creation timestamp or incremental cursor) that can distinguish newly added links from previously captured ones.
- Users are comfortable storing their Raindrop data locally on the same machine that runs the CLI and accept the associated privacy responsibilities.
- Stakeholders require a lightweight embedded database for storage and explicitly mandate SQLite as the local store, persisted in a single `.db` file per user environment.
- Sync operations are expected to run from a single device at a time; concurrent executions against the same account are out of scope.

## Clarifications

### Session 2025-10-03
- Q: Should the local archive reflect updates or deletions made in Raindrop after initial capture? → A: Ignore upstream changes after capture; only add new links.
- Q: Do we need to support multiple machines syncing against the same Raindrop account without conflicts? → A: Assume single-device usage; concurrent runs are unsupported.
- Q: How should users trigger a complete rebuild of the archive when they suspect data drift? → A: Provide a dedicated CLI flag (e.g., `--full-refresh`).
- Q: Is SQLite a hard requirement, or may we choose any local storage solution meeting the business goals? → A: SQLite is mandatory; use a single local `.db` file.

## Review & Acceptance Checklist

### Content Quality
- [x] No implementation details (languages, frameworks, APIs)
- [x] Focused on user value and business needs
- [x] Written for non-technical stakeholders
- [x] All mandatory sections completed

### Requirement Completeness
- [ ] No [NEEDS CLARIFICATION] markers remain
- [x] Requirements are testable and unambiguous  
- [x] Success criteria are measurable
- [x] Scope is clearly bounded
- [x] Dependencies and assumptions identified

## Execution Status

- [x] User description parsed
- [x] Key concepts extracted
- [x] Ambiguities marked
- [x] User scenarios defined
- [x] Requirements generated
- [x] Entities identified
- [ ] Review checklist passed

