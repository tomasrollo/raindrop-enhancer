# Quickstart: Handling YouTube Videos

This guide demonstrates how to use the YouTube video handling feature.

## Prerequisites

- The application is installed and configured.

## Steps

1.  **Add a YouTube Link**: Use the CLI to add a new Raindrop with a YouTube video URL.

    ```bash
    uv run python main.py sync --add-link "https://www.youtube.com/watch?v=dQw4w9WgXcQ"
    ```

2.  **Verify Content**: Check the `content_markdown` for the newly added Raindrop. It should contain the title and description of the YouTube video.

    ```
    # Rick Astley - Never Gonna Give You Up (Official Music Video)

    The official video for “Never Gonna Give You Up” by Rick Astley...
    ```
