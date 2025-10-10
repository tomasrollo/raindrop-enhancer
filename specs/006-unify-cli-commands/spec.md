# Feature Specification: Unify CLI commands into single entrypoint

**Feature Branch**: `006-unify-cli-commands`  
**Created**: 2025-10-10  
**Status**: Draft  
**Input**: User description: "Unify CLI commands - unify CLI into single entrypoint 'raindrop-enhancer' with subcommands: export, sync, capture, migrate, tag"

## Clarifications

### Session 2025-10-10

- Q: Preferred migration strategy for the old console scripts? → A: D
- Q: Preferred behavior when optional dependencies are missing? → A: A


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

## ⚡ Quick Guidelines
- ✅ Focus on WHAT users need and WHY
- ❌ Avoid HOW to implement (no tech stack, APIs, code structure)
- 👥 Written for business stakeholders, not developers

### Section Requirements
- **Mandatory sections**: Must be completed for every feature
- **Optional sections**: Include only when relevant to the feature
- When a section doesn't apply, remove it entirely (don't leave as "N/A")

### For AI Generation
When creating this spec from a user prompt:
1. **Mark all ambiguities**: Use [NEEDS CLARIFICATION: specific question] for any assumption you'd need to make
2. **Don't guess**: If the prompt doesn't specify something (e.g., "login system" without auth method), mark it
3. **Think like a tester**: Every vague requirement should fail the "testable and unambiguous" checklist item
4. **Common underspecified areas**:
   - User types and permissions
   - Data retention/deletion policies  
   - Performance targets and scale
   - Error handling behaviors
   - Integration requirements
   - Security/compliance needs

---

## User Scenarios & Testing *(mandatory)*

### Primary User Story
As a user of the CLI tools, I want a single, discoverable command `raindrop-enhancer` with multiple subcommands so I can run export, sync, capture, migrate and tagging flows using a consistent UX and shared configuration and help text.

### Acceptance Scenarios
1. **Given** the package is installed and on PATH, **When** the user runs `raindrop-enhancer export`, **Then** the existing behavior of `raindrop-export` runs (exporting collections) and returns the same exit code and output format as before.
2. **Given** the package is installed and on PATH, **When** the user runs `raindrop-enhancer sync`, **Then** the existing behavior of `raindrop-sync` runs (synchronization) and returns the same exit code and semantics.
3. **Given** the package is installed and on PATH, **When** the user runs `raindrop-enhancer capture`, **Then** the existing `capture-content` behavior runs and captures content as before.
4. **Given** the package is installed and on PATH, **When** the user runs `raindrop-enhancer migrate`, **Then** the existing `raindrop-migrate` behavior runs and performs migrations.
5. **Given** the package is installed and on PATH, **When** the user runs `raindrop-enhancer tag`, **Then** the existing `raindrop-tags` behavior runs and produces tags as before.

### Edge Cases
- Backwards compatibility: the old invocation names (`raindrop-export`, `raindrop-sync`, `capture-content`, `raindrop-migrate`, `raindrop-tags`) will be removed immediately as a breaking change. Release notes and upgrade/migration guidance MUST be provided to help users transition to `raindrop-enhancer <subcommand>`.
- Conflicting PATH: If `raindrop-enhancer` is not on PATH but old commands are, document migration steps.
- Missing dependencies: CLI should fail with clear error messages when optional components (e.g., dspy for tagging) are not available.

## Requirements *(mandatory)*

### Functional Requirements
- **FR-001**: The package MUST provide a single top-level console entrypoint named `raindrop-enhancer` that exposes subcommands: `export`, `sync`, `capture`, `migrate`, and `tag`.
- **FR-002**: Each subcommand MUST map to the existing CLI behavior currently implemented by the separate entrypoints: `raindrop-export`, `raindrop-sync`, `capture-content`, `raindrop-migrate`, `raindrop-tags`.
- **FR-003**: The top-level command MUST include a `--help` that lists subcommands and shows per-subcommand help consistent with existing CLI help texts.
- **FR-004**: The transition MUST preserve exit codes and output formats for compatibility with scripts and CI that rely on the old commands.
**FR-005**: Installing the package WILL NOT create the old console scripts; old scripts will be removed immediately (breaking change). Documentation, release notes, and migration instructions MUST clearly communicate this change and provide examples for replacing existing invocations with `raindrop-enhancer <subcommand>`.
- **FR-006**: The implementation MUST ensure optional features (e.g., tagging that depends on `dspy`) remain listed as subcommands; invoking a subcommand whose optional dependency is missing MUST print a clear, actionable error message (including the exact install command) and exit with a non-zero code. The error text and install guidance MUST also be present in the CLI help and in the documentation.
- **FR-007**: Command names MUST be succinct: prefer `capture` over `capture-content` and `tag` over `tags` unless there is a compelling reason to preserve pluralization.
- **FR-008**: Documentation, README, and installation notes MUST be updated to show the new invocation pattern and migration guidance.

*Example of marking unclear requirements:*
- **FR-009**: CLI MUST authenticate users using [NEEDS CLARIFICATION: does this change require any auth UX/behavior changes? currently uses env vars and tokens — confirm if unchanged]

### Key Entities *(include if feature involves data)*
- Not applicable — this is a UX/CLI interface change and does not introduce new data entities.

---

## Review & Acceptance Checklist
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
- [x] User description parsed
- [x] Key concepts extracted
- [x] Ambiguities marked
- [x] User scenarios defined
- [x] Requirements generated
- [x] Entities identified
- [ ] Review checklist passed

---

## Notes & Implementation Considerations
- Implementation should be done in a way that minimizes breakage for existing users. Suggested technical approach (for implementers): add a new console script `raindrop-enhancer` in `pyproject.toml` that delegates to existing functions, and keep existing console script entries for a deprecation period that either call the new command or print deprecation messages.

# Feature Specification: [FEATURE NAME]

**Feature Branch**: `[###-feature-name]`  
**Created**: [DATE]  
**Status**: Draft  
**Input**: User description: "$ARGUMENTS"

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

## ⚡ Quick Guidelines
- ✅ Focus on WHAT users need and WHY
- ❌ Avoid HOW to implement (no tech stack, APIs, code structure)
- 👥 Written for business stakeholders, not developers

### Section Requirements
- **Mandatory sections**: Must be completed for every feature
- **Optional sections**: Include only when relevant to the feature
- When a section doesn't apply, remove it entirely (don't leave as "N/A")

### For AI Generation
When creating this spec from a user prompt:
1. **Mark all ambiguities**: Use [NEEDS CLARIFICATION: specific question] for any assumption you'd need to make
2. **Don't guess**: If the prompt doesn't specify something (e.g., "login system" without auth method), mark it
3. **Think like a tester**: Every vague requirement should fail the "testable and unambiguous" checklist item
4. **Common underspecified areas**:
   - User types and permissions
   - Data retention/deletion policies  
   - Performance targets and scale
   - Error handling behaviors
   - Integration requirements
   - Security/compliance needs

---

## User Scenarios & Testing *(mandatory)*

### Primary User Story
[Describe the main user journey in plain language]

### Acceptance Scenarios
1. **Given** [initial state], **When** [action], **Then** [expected outcome]
2. **Given** [initial state], **When** [action], **Then** [expected outcome]

### Edge Cases
- What happens when [boundary condition]?
- How does system handle [error scenario]?

## Requirements *(mandatory)*

### Functional Requirements
- **FR-001**: System MUST [specific capability, e.g., "allow users to create accounts"]
- **FR-002**: System MUST [specific capability, e.g., "validate email addresses"]  
- **FR-003**: Users MUST be able to [key interaction, e.g., "reset their password"]
- **FR-004**: System MUST [data requirement, e.g., "persist user preferences"]
- **FR-005**: System MUST [behavior, e.g., "log all security events"]

*Example of marking unclear requirements:*
- **FR-006**: System MUST authenticate users via [NEEDS CLARIFICATION: auth method not specified - email/password, SSO, OAuth?]
- **FR-007**: System MUST retain user data for [NEEDS CLARIFICATION: retention period not specified]

### Key Entities *(include if feature involves data)*
- **[Entity 1]**: [What it represents, key attributes without implementation]
- **[Entity 2]**: [What it represents, relationships to other entities]

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
