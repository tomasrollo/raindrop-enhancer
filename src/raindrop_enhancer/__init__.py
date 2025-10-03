"""raindrop_enhancer package.

Expose CLI entrypoint symbol for project.scripts `raindrop-export`.
"""

from .cli import main  # re-export for entrypoint

__all__ = ["main"]
