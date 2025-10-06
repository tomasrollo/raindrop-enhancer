# Feature Specification: Handle Youtube Videos

**Feature Branch**: `004-handle-youtube-videos`  
**Created**: 2025-10-06
**Status**: Draft  
**Input**: User description: "Handle youtube videos - when the link is a Youtube video download the title and the description using the yt-dlp Python library. See @source_docs/yt-dlp_snippet.md for a code snippet of how to do it"

## Clarifications

### Session 2025-10-06
- Q: When a YouTube video's title or description cannot be fetched (e.g., it's private, deleted, or age-restricted), how should the system respond? → A: Store placeholders like `[YOUTUBE VIDEO NOT AVAILABLE]` in the title and description fields.
- Q: Where should the extracted YouTube title and description be stored? → A: store the title and description together in a Markdown format in the column 'content_markdown' in the database.
- Q: Should the system only handle YouTube links, or should it also attempt to extract content from other video platforms (e.g., Vimeo, Dailymotion)? → A: No, only focus on YouTube for this feature.
- Q: When a URL is identified as a potential YouTube link but is malformed (e.g., `youtube.com/wat_ch?v=...` instead of `youtube.com/watch?v=...`), how should the system handle it? → A: Log a warning and treat it as a non-YouTube URL.
- Q: How should the extracted YouTube title and description be formatted within the `content_markdown` field? → A: # {title}\n\n{description} (Title as H1, description as paragraph)
- Q: What should the system do if the yt-dlp library fails with an unexpected error (e.g., a network issue, a temporary YouTube outage, or a library bug)? → A: Store a different placeholder, like `[YOUTUBE METADATA FETCH FAILED]`.
- Q: To prevent the system from hanging on slow network requests, should there be a timeout for fetching YouTube metadata? → A: Yes, a 30-second timeout.

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
As a user, when I provide a link to a Youtube video, I want the system to extract the video's title and description so that I can have that information associated with the link.

### Acceptance Scenarios
1. **Given** a valid Youtube video URL, **When** the system processes the link, **Then** the video's title and description are saved.
2. **Given** a URL that is not a valid Youtube video, **When** the system processes the link, **Then** it is handled as a regular link without attempting to extract Youtube-specific metadata.

### Edge Cases
- If a Youtube video is private, deleted, or age-restricted, the system will store `[YOUTUBE VIDEO NOT AVAILABLE]` as the title and description.
- If a potential YouTube URL is malformed, the system will log a warning and treat it as a standard web link.
- If the `yt-dlp` library encounters an unexpected error during metadata extraction, the system will store `[YOUTUBE METADATA FETCH FAILED]` as the content.

## Requirements *(mandatory)*

### Functional Requirements
- **FR-001**: The system MUST identify if a given URL is a Youtube video link.
- **FR-002**: If the URL is a Youtube video, the system MUST extract the video title.
- **FR-003**: If the URL is a Youtube video, the system MUST extract the video description.
- **FR-004**: The extracted title and description MUST be combined into a Markdown format of `# {title}\n\n{description}` and stored in the `content_markdown` field associated with the original link.
- **FR-005**: If the URL is not a Youtube video, the system MUST process it as a standard web link.
- **FR-006**: In cases where a YouTube video's title or description cannot be fetched, the system MUST store the placeholder text `[YOUTUBE VIDEO NOT AVAILABLE]` in both the title and description fields.
- **FR-007**: If a URL appears to be a malformed YouTube link, the system MUST log a warning and treat it as a standard web link.
- **FR-008**: If the `yt-dlp` library fails with an unexpected error, the system MUST store the placeholder text `[YOUTUBE METADATA FETCH FAILED]` in the `content_markdown` field.

### Non-Functional Requirements
- **NFR-001**: Metadata extraction from YouTube MUST time out after 30 seconds.

## Out of Scope
- This feature will only support YouTube links. Other video platforms like Vimeo or Dailymotion are not in scope.

---
## Technical Notes
The user has specified that the `yt-dlp` library should be used. Here is a snippet for reference:
```python
from yt_dlp import YoutubeDL

url = "https://www.youtube.com/watch?v=YOUR_VIDEO_ID"

video_title = None
video_description = None

with YoutubeDL() as ydl:
    info_dict = ydl.extract_info(url, download=False)
    video_title = info_dict.get('title', None)
    video_description = info_dict.get('description', None)
```

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
