"""CLI entrypoint for raindrop_enhancer."""

from __future__ import annotations

import os
import sys
from contextlib import nullcontext
from typing import TextIO

import click

from .api.raindrop_client import RaindropClient
from .exporters.json_exporter import export_to_file
from .models import Raindrop, Collection, filter_active_raindrops


def _open_output(path: str) -> TextIO:
    if path == "-":
        return sys.stdout
    return open(path, "w", encoding="utf-8")


@click.command()
@click.option("--output", default="-", help="Output file path (`-` for stdout)")
@click.option("--quiet", is_flag=True, help="Suppress non-error output")
@click.option("--verbose", is_flag=True, help="Verbose output")
@click.option("--dry-run", is_flag=True, help="Validate without writing output")
@click.option("--pretty", is_flag=True, help="Pretty-print JSON output")
def main(output: str, quiet: bool, verbose: bool, dry_run: bool, pretty: bool) -> None:
    """Export all active raindrops to JSON.

    Reads `RAINDROP_TOKEN` from environment (or `.env` when using python-dotenv).
    """
    # Try to load .env if present
    try:
        from dotenv import load_dotenv

        load_dotenv()
    except Exception:
        pass

    token = os.getenv("RAINDROP_TOKEN")
    if not token:
        click.echo("Missing RAINDROP_TOKEN in environment", err=True)
        sys.exit(2)

    client = RaindropClient(token=token)

    try:
        collections = client.list_collections()
        all_items = []
        for c in collections:
            cid = c.get("_id") or c.get("id")
            if cid is None:
                continue
            for item in client.list_raindrops(int(cid)):
                all_items.append(item)

        # Filter and map to Raindrop dataclasses
        active = filter_active_raindrops(all_items)

        if dry_run:
            click.echo(f"Dry run: collected {len(active)} active raindrops")
            return

        ctx = nullcontext()
        with ctx if output != "-" else ctx as _:
            fh = _open_output(output)
            try:
                export_to_file(active, fh, pretty=pretty)
            finally:
                if fh is not sys.stdout:
                    fh.close()

    finally:
        client.close()


if __name__ == "__main__":
    main()
