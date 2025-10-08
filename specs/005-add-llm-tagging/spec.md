# Feature Specification: LLM-Assisted Link Tagging

**Feature Branch**: `005-add-llm-tagging`  
**Created**: 2025-10-08  
**Status**: Draft  
**Input**: User description: "add llm tagging - add a command that generates tags for links based on the downloaded link content (DB column content_markdown) and stores them in the DB. Use the DSPy library to manage calling the LLM."

## Clarifications

### Session 2025-10-08
- Q: Should the new tagging command operate on a single link specified by the user, the entire stored library, or only links missing tags? → A: Process only links lacking tags.
- Q: When tags already exist for a link, should the command append to, overwrite, or leave existing tags unchanged? → A: Skip links that already have tags.
- Q: Is there a desired limit or formatting convention for generated tags (e.g., maximum count, character length, case style)? → A: Generate up to 10 Title Case tags per link, each ≤20 characters.
- Q: Should tags be generated in the user's language, detected language, or always in English? → A: Always generate tags in English.
- Q: Are there privacy or compliance constraints on sending link content to an external LLM provider that need to be documented for users? → A: No new constraints beyond existing usage.
- Q: Existing database schema details (e.g., where tags are stored) must be reviewed to confirm compatibility with auto-generated tags; migrations may be required if no appropriate storage exists. → A: Store auto-generated tags in a dedicated column on the links table, separate from manual tags.
- Q: What runtime expectation should the tagging command meet? → A: No strict SLA—just provide clear progress feedback.
- Q: How should transient LLM or network failures be handled? → A: Do not retry automatically; report failures immediately.

## Execution Flow (main)
```
1. Parse user description from Input
   → If empty: ERROR "No feature description provided"
2. Extract key concepts from description
   → Identify: actors, actions, data, constraints
3. For each unclear aspect:
   → Mark with [NEEDS CLARIFICATION: specific question]
4. Fill User Scenarios & Testing section
   → If no clear user flow: ERROR "Cannot determine user scenarios"
5. Generate Functional Requirements
   → Each requirement must be testable
   → Mark ambiguous requirements
6. Identify Key Entities (if data involved)
7. Run Review Checklist
   → If any [NEEDS CLARIFICATION]: WARN "Spec has uncertainties"
   → If implementation details found: ERROR "Remove tech details"
8. Return: SUCCESS (spec ready for planning)
```

---

## User Scenarios & Testing *(mandatory)*

### Primary User Story
As a knowledge worker who curates links in Raindrop Enhancer, I want to run a command that automatically creates meaningful tags for stored links so that I can later filter and organize my collection without manually reviewing each item.

### Acceptance Scenarios
1. **Given** stored links that already have `content_markdown` captured, **When** the user runs the tagging command, **Then** the system generates relevant tags for each processed link and saves them in the database.
2. **Given** a link whose content cannot yield any meaningful tags, **When** the tagging command processes the link, **Then** the system records that no tags were produced and communicates this outcome to the user without failing the overall run.
3. **Given** a link that already has tags on record, **When** the tagging command is executed, **Then** the system skips that link and leaves the existing tags unchanged while noting the skip in command output.

### Edge Cases
- How should the system behave if `content_markdown` is empty, missing, or too short to produce meaningful tags?
- What feedback should users receive when the LLM returns an error or times out during tagging?
- How should duplicate tags or tags consisting solely of stopwords be handled to avoid clutter?
- How should the system respond if the LLM returns more than 10 tags or tags that exceed 30 characters?
- How should the system respond if the LLM suggests tags in a language other than English?

## Requirements *(mandatory)*

### Functional Requirements
- **FR-001**: The system MUST provide a CLI-accessible command that initiates automated tag generation for stored links with available `content_markdown`.
- **FR-002**: The system MUST send link context derived from `content_markdown` to an LLM-driven tagging workflow and receive a collection of proposed tags.
- **FR-003**: The system MUST persist the generated tags in the existing database schema so they are accessible to downstream features.
- **FR-004**: The system MUST surface a per-link summary of tagging outcomes (e.g., number of tags added or reason for skipping) in the command output.
- **FR-005**: The system MUST skip processing for links that already contain tags, preserving their existing tag set unchanged.
- **FR-006**: The system MUST log or report any tagging failures, including LLM errors, so users can retry or inspect affected links.
- **FR-007**: The system MUST automatically scope each run to only links that currently lack tags, skipping links that already have tags recorded.
- **FR-008**: The system MUST ensure that links lacking usable `content_markdown` are skipped gracefully without stopping the batch command.
- **FR-009**: The system MUST constrain generated tags to a maximum of 10 per link, each formatted in Title Case and limited to 30 characters.
- **FR-010**: The system MUST normalize all generated tags to English, regardless of the original content language.
- **FR-011**: The system MUST store auto-generated tags in a dedicated column on the links table, separate from manually curated tags.

### Non-Functional Requirements
- **NFR-001**: The tagging command MUST provide continuous progress feedback during execution; no fixed completion SLA is required.
- **NFR-002**: The system MUST provide transparency to users about data sent to LLM services, including any opt-in prompts or audit logs, consistent with existing privacy policy.
- **NFR-003**: The tagging workflow MUST report LLM or network failures immediately without automatic retries, enabling users to address issues manually.
- **NFR-004**: Stored tags MUST maintain consistency in formatting (e.g., casing, delimiter use) to support reliable filtering.

### Key Entities *(include if feature involves data)*
- **Link**: Represents a saved web resource with attributes including URL, title, existing tags, `content_markdown`, and a dedicated column for auto-generated tags used for automated filtering features.
- **Tag Assignment**: Represents the association possibilities between a link and tags, distinguishing manually curated tags from auto-generated tags stored separately.

## Out of Scope
- Introducing user-facing UI components beyond the new tagging command.
- Building advanced taxonomy management (e.g., hierarchical tags, manual review queues) beyond storing flat tags.
- Guaranteeing semantic accuracy of tags beyond what the LLM produces; human review remains optional.

## Technical Notes
- The user has specified that LLM orchestration should leverage the DSPy library for prompt management and model interactions; implementation should document how DSPy is configured without exposing provider secrets.
- The database schema must add or reuse a dedicated column on the links table to store auto-generated tags separately from manual tags.

---

## Review & Acceptance Checklist
*GATE: Automated checks run during main() execution*

### Content Quality
- [ ] No implementation details (languages, frameworks, APIs)
- [ ] Focused on user value and business needs
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
