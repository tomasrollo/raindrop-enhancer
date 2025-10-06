"""YouTube extractor: identify YouTube links and extract metadata via yt-dlp.

This module provides:
- is_youtube_url(url) -> bool
- extract_metadata(url, timeout=30.0) -> dict with keys: title, description, error

The implementation imports `yt_dlp` at call time so tests can monkeypatch it.
"""

from __future__ import annotations

from typing import Optional
import re
import importlib

# Very small subset of youtube hostnames and short URL forms
_YOUTUBE_RE = re.compile(
    r"^(?:https?://)?(?:www\.|m\.)?(?:youtube\.com/(?:watch\?v=|shorts/)|youtu\.be/)(?P<id>[A-Za-z0-9_-]{4,})",
    re.IGNORECASE,
)


def is_youtube_url(url: str) -> bool:
    """Return True when the URL identifies as a YouTube video link."""
    if not url:
        return False
    return bool(_YOUTUBE_RE.search(url))


def extract_metadata(url: str, timeout: float = 30.0) -> dict:
    """Extract title and description for a YouTube URL using yt-dlp.

    Returns a dict: {"title": Optional[str], "description": Optional[str], "error": Optional[str]}

    On failure, `title` and `description` will be None and `error` will contain a short code/message.
    """
    if not is_youtube_url(url):
        return {"title": None, "description": None, "error": "not_youtube"}

    try:
        ytdlp = importlib.import_module("yt_dlp")
    except Exception as exc:
        return {"title": None, "description": None, "error": f"yt_dlp_missing:{exc}"}

    # Use a minimal yt-dlp options set to only fetch metadata
    ydl_opts = {
        "quiet": True,
        "skip_download": True,
        "nocheckcertificate": True,
        "socket_timeout": int(max(1, timeout)),
    }

    try:
        with ytdlp.YoutubeDL(ydl_opts) as ydl:
            info = ydl.extract_info(url, download=False)
            title = info.get("title") if isinstance(info, dict) else None
            description = info.get("description") if isinstance(info, dict) else None
            return {"title": title, "description": description, "error": None}
    except Exception as exc:  # pragma: no cover - integration behavior
        # Map common failure cases to short codes
        msg = str(exc)
        if "This video is unavailable" in msg or "HTTP Error 404" in msg:
            return {"title": None, "description": None, "error": "unavailable"}
        return {"title": None, "description": None, "error": msg}
