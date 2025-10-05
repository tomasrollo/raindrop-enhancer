"""Content capture helpers (Trafilatura integration).

Lightweight package providing fetcher and runner for capture-content command.
"""

from .fetcher import TrafilaturaFetcher
from .capture_runner import CaptureRunner

__all__ = ["TrafilaturaFetcher", "CaptureRunner"]
