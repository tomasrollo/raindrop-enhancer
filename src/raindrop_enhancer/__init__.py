"""raindrop_enhancer package.

Expose unified CLI entrypoint symbol for project.scripts `raindrop-enhancer`.
The top-level Click group `cli` provides subcommands: export, sync, capture,
and tag.
"""

from . import cli as cli  # re-export the cli module so package import yields the module

__all__ = ["cli"]
