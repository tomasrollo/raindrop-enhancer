# Feature Specification: Full-Text Capture Command for Saved Links

**Feature Branch**: `003-add-trafilatura-add`  
**Created**: 2025-10-05  
**Status**: Draft  
**Input**: User description: "Add trafilatura. Add support to fetch the link content using the trafilatura python library and store it in the database alongside the link details. Should be a separate CLI command."

## Execution Flow (main)
```
1. User invokes the new content-capture CLI command
2. System gathers saved links that do not yet have stored full-text content
3. For each link:
   → Request readable article content from the designated extraction service
   → Persist the retrieved text with the link record
   → Record success or the encountered error
4. System summarizes results for the user (counts of successes, skips, failures)
5. Command exits with status reflecting whether any blocking errors occurred
```

---

## ⚡ Quick Guidelines
- Prioritize delivering readable offline access to saved links without changing existing export/sync flows
- Keep the command safe to rerun; already-populated links should not be overwritten unintentionally
- Provide clear feedback so users understand which links gained content and which still need attention

---

## User Scenarios & Testing *(mandatory)*

### Primary User Story
As a knowledge worker who reviews saved bookmarks offline, I want to trigger a command that captures the full article text for my saved links so I can read and search them later without leaving the application.

### Acceptance Scenarios
1. **Given** a stored link without full-text content, **When** the user runs the content-capture command, **Then** the system retrieves the article text, saves it with the link, and confirms completion in the command output.
2. **Given** a stored link whose source page cannot be fetched, **When** the user runs the content-capture command, **Then** the system records the failure for that link, continues processing the remaining links, and reports the issue at the end.

### Edge Cases
- What happens when the command encounters a link that already has stored content? → The system should skip it by default and note the skip count.
- How does the system handle repeated transient extraction failures? → The command should surface a failure summary while leaving the link flagged for future retries.
- What if the database contains no links without content? → The command should exit successfully and inform the user that nothing required processing.
- What happens when a fetch attempt fails once due to a transient issue? → The command should retry the link exactly one additional time before marking it failed for the session.
- How should the command report partial success when some links fail? → The command should exit with success if at least one link succeeded and exit with failure only when every link failed.

## Requirements *(mandatory)*

### Functional Requirements
- **FR-001**: The system MUST provide a dedicated CLI command that initiates full-text capture for saved links.
- **FR-002**: The system MUST identify saved links that lack stored full-text content each time the command runs.
- **FR-003**: The system MUST request readable article content for each identified link via the selected extraction service (Trafilatura).
- **FR-004**: The system MUST persist the extracted content as Markdown alongside the existing link details without removing previously stored metadata.
- **FR-005**: The system MUST present a user-facing summary showing counts of processed, skipped, and failed links after the command completes.
- **FR-006**: The system MUST log or surface detailed error information for any link whose content could not be captured while allowing the overall command to continue processing other links.
- **FR-007**: The system MUST ensure rerunning the command does not overwrite existing full-text content unless the user opts in via a refresh option during command invocation.
- **FR-008**: The system MUST attempt exactly one automatic retry for transient content-fetch failures before recording the link as failed.
- **FR-009**: The system MUST exit with a non-zero status only when every processed link fails to capture content; mixed outcomes must still return success.
- **FR-010**: The system MUST automatically reuse the existing CLI authentication and configuration context without requiring users to supply credentials again for this command.

### Key Entities *(include if feature involves data)*
- **Saved Link**: Represents a bookmark stored in the application, including URL, title, metadata, and references to stored content.
- **Link Content Snapshot**: Captures the extracted Markdown text for a saved link, including capture timestamp and the source used for extraction.
- **Content Capture Session**: Represents a single run of the CLI command, tracking counts of processed links and any errors to display to the user.
- **CLI Context**: Represents the stored authentication tokens and configuration already used by other commands, automatically applied to the content-capture command.

## Clarifications

### Session 2025-10-05
- Q: What format should we persist the extracted article content in? → A: Markdown generated by Trafilatura
- Q: Should the new CLI command include an option to refresh Markdown content for links that already have stored text? → A: Provide an opt-in refresh flag
- Q: How many retry attempts should the command make when Trafilatura fails to fetch content for a link in a transient way? → A: One retry before skipping
- Q: What exit status should the CLI command use when some links fail to capture content? → A: Exit failure only if all links fail
- Q: Should the command automatically load environment variables (e.g., API tokens, configuration) from the existing CLI context, or require explicit inputs when running? → A: Reuse existing CLI authentication/config automatically

---

## Review & Acceptance Checklist
*GATE: Automated checks run during main() execution*

### Content Quality
- [x] No implementation details (languages, frameworks, APIs)
- [x] Focused on user value and business needs
- [x] Written for non-technical stakeholders
- [x] All mandatory sections completed

### Requirement Completeness
- [x] No [NEEDS CLARIFICATION] markers remain
- [x] Requirements are testable and unambiguous  
- [x] Success criteria are measurable
- [x] Scope is clearly bounded
- [x] Dependencies and assumptions identified

---

## Execution Status
*Updated by main() during processing*

- [x] User description parsed
- [x] Key concepts extracted
- [x] Ambiguities marked
- [x] User scenarios defined
- [x] Requirements generated
- [x] Entities identified
- [x] Review checklist passed

---
