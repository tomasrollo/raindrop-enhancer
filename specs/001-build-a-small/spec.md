# Feature Specification: Unified Raindrop Export CLI

**Feature Branch**: `001-build-a-small`  
**Created**: 2025-10-03  
**Status**: Draft  
**Input**: User description: "Build a small CLI script that connects to Raindrop API, authenticates using a token from .env file and downloads and outputs all links (Raindrops) from all collections"

## User Scenarios & Testing *(mandatory)*

### Primary User Story
A productivity-focused user who manages bookmarks in Raindrop wants a quick way to review or export every saved link without leaving the terminal. They run a command-line tool that authenticates with their Raindrop account and presents the complete set of saved raindrops in a single view so they can process them further.

### Acceptance Scenarios
1. **Given** a valid Raindrop API token stored in the user's environment configuration, **When** the user executes the CLI without additional setup, **Then** the tool confirms the token, retrieves every accessible collection, gathers all raindrops within each collection, and prints the aggregated list as a JSON array for the user to consume.
2. **Given** the user has not provided a valid token in the expected configuration, **When** they attempt to run the CLI, **Then** the tool halts gracefully with a clear message explaining the missing or invalid credential so the user can correct it.

### Edge Cases
- What happens when a collection contains more raindrops than can be returned in a single API response (pagination or limits)?
- How does the system handle API throttling, network failures, or partial responses during the fetch process?
- What should the user see if they have zero collections or if individual collections contain zero raindrops?
- How are archived, duplicated, or restricted items represented in the output, if at all? → They are excluded; only active items appear.
- What happens when the API enforces rate limits during export? → CLI retries with exponential backoff up to a defined limit before failing.

## Requirements *(mandatory)*

### Functional Requirements
- **FR-001**: The CLI MUST allow users to initiate a full raindrop export through a single command with no interactive prompts required for authentication.
- **FR-002**: The system MUST read the Raindrop access token from a designated environment configuration so that sensitive credentials are not passed directly on the command line.
- **FR-002a**: The CLI MUST load the token from a `.env` file using the environment variable name `RAINDROP_TOKEN` with no alternate fallbacks.
- **FR-003**: The system MUST validate the presence and basic format of the token and inform the user immediately if it is missing or malformed.
- **FR-004**: Upon successful authentication, the system MUST retrieve the complete list of collections available to the token holder and iterate through each to gather their raindrops.
- **FR-005**: The system MUST ensure its fetch strategy covers every raindrop irrespective of API pagination or collection size constraints.
- **FR-006**: The output MUST present every active raindrop with essential identifying details (collection identifier, collection name, item title, URL, saved timestamp, and tags) in a JSON array of objects suitable for downstream processing.
- **FR-007**: The system MUST communicate recoverable errors (such as temporary API issues) with actionable guidance and stop execution only when continuation would risk inaccurate results.
- **FR-007a**: When the Raindrop API responds with HTTP 429, the system MUST retry requests using exponential backoff for a fixed duration (e.g., up to 60 seconds total wait) before surfacing a rate-limit failure to the user.
- **FR-008**: The system MUST exit with a success indicator only when all collections have been processed and reported without omission.

### Key Entities
- **Raindrop Collection**: Represents a grouping of raindrops the user has access to; key attributes include collection identifier, display name, and any metadata needed to iterate over contents.
- **Raindrop Item**: Represents an individual active saved link included in the export; key attributes include item identifier, URL, title, timestamps, collection reference, and optional status flags (tags) relevant to active items while archived or restricted items remain out of scope.
- **Authentication Context**: Represents the credential and session state derived from the stored token, including any scope limitations that influence which collections or raindrops are included.

### Dependencies & Assumptions
- Access to the Raindrop API must remain available and stable during the export run, including endpoints for listing collections and items.
- Users possess a personal Raindrop API token with sufficient permissions to read all desired collections, stored in the `.env` file under the key `RAINDROP_TOKEN` prior to execution.
- The environment running the CLI has outbound internet access and can read environment configuration files (e.g., `.env`).
- Downstream consumers of the export will handle any additional formatting they require once the CLI outputs the dataset.

## Clarifications

### Session 2025-10-03
- Q: Which raindrop types should the CLI include in its export output? → A: Only active (non-archived, non-duplicate) raindrops.
- Q: What format should the CLI use when printing the combined raindrops? → A: JSON array of objects.
- Q: How should the CLI determine the environment variable name that holds the Raindrop API token? → A: Always read `RAINDROP_TOKEN` from `.env`.
- Q: How should the CLI behave if the Raindrop API returns a rate-limit response (HTTP 429)? → A: Retry with exponential backoff up to time limit.

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
