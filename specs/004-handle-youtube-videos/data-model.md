# Data Model: YouTube Content

## Entities

### Raindrop (Existing)

The existing `Raindrop` entity will be used. The feature will populate the `content_markdown` field for YouTube links.

- **`content_markdown` (Text)**: Stores the extracted YouTube video title and description in Markdown format: `# {title}\n\n{description}`.

## Validation Rules

- If a YouTube video is unavailable, `content_markdown` will store `[YOUTUBE VIDEO NOT AVAILABLE]`.
- If the metadata fetch fails, `content_markdown` will store `[YOUTUBE METADATA FETCH FAILED]`.

