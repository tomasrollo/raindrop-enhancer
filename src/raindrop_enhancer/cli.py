"""CLI entrypoint for raindrop_enhancer."""

from __future__ import annotations

import os
import sys
from contextlib import nullcontext
from typing import TextIO
import logging

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
@click.option(
    "--enforce-rate-limit/--no-enforce-rate-limit",
    default=False,
    help="Enforce spacing to respect default rate-limit",
)
@click.option(
    "--rate-limit",
    default=120,
    help="Requests per minute to honor when enforcing rate-limit",
)
def main(
    output: str,
    quiet: bool,
    verbose: bool,
    dry_run: bool,
    pretty: bool,
    enforce_rate_limit: bool,
    rate_limit: int,
) -> None:
    """Export all active raindrops to JSON.

    Reads `RAINDROP_TOKEN` from environment (or `.env` when using python-dotenv).
    """
    # Attempt to load a local .env file if present. This is useful for
    # interactive use. We avoid loading .env while running under pytest so
    # tests can control the environment deterministically.
    try:
        from dotenv import load_dotenv
    except Exception:
        load_dotenv = None

    if (
        load_dotenv is not None
        and os.path.exists(".env")
        and "pytest" not in sys.modules
    ):
        load_dotenv()

    token = os.getenv("RAINDROP_TOKEN")
    if not token:
        click.echo("Missing RAINDROP_TOKEN in environment", err=True)
        sys.exit(2)

    client = RaindropClient(
        token=token,
        enforce_rate_limit=enforce_rate_limit,
        rate_limit_per_min=rate_limit,
    )

    # Configure logging based on flags
    # - --verbose turns on debug logging from the client
    # - --quiet suppresses non-error output (keeps warnings/errors only)
    if quiet:
        logging.basicConfig(level=logging.WARNING)
    elif verbose:
        logging.basicConfig(level=logging.DEBUG)
    else:
        # Default: only show warnings/errors unless verbose requested
        logging.basicConfig(level=logging.WARNING)

    # Metrics / observability
    retries = []
    requests_made = 0

    def on_retry(url: str, attempt: int, delay: float) -> None:
        retries.append((url, attempt, delay))
        if verbose and not quiet:
            # Print retry events to stderr so they don't mix with JSON/stdout
            click.echo(
                f"Retrying {url} (attempt {attempt}) - sleeping {delay:.2f}s",
                err=True,
            )

    def on_request(url: str) -> None:
        nonlocal requests_made
        requests_made += 1
        if verbose and not quiet:
            click.echo(f"Request: {url}", err=True)

    client.on_retry = on_retry
    client.on_request = on_request

    try:
        collections = client.list_collections()
        # The Raindrop 'Unsorted' collection uses id -1 and is not always
        # returned by the /collections endpoint. Ensure we always fetch it
        # so users don't miss those raindrops.
        try:
            has_unsorted = any(
                (c.get("_id") == -1 or c.get("id") == -1) for c in collections
            )
        except Exception:
            has_unsorted = False
        if not has_unsorted:
            collections.append({"_id": -1})
        all_items = []
        start = None
        try:
            from rich.progress import (
                Progress,
                SpinnerColumn,
                TextColumn,
                BarColumn,
                TimeElapsedColumn,
            )

            use_rich = True
        except Exception:
            use_rich = False

        import time

        start = time.time()
        if use_rich and not quiet:
            with Progress(
                SpinnerColumn(),
                TextColumn("{task.description}"),
                BarColumn(),
                TimeElapsedColumn(),
            ) as progress:
                task = progress.add_task(
                    "Fetching collections and raindrops", total=len(collections) or None
                )
                for c in collections:
                    cid = c.get("_id") or c.get("id")
                    if cid is None:
                        continue
                    for item in client.list_raindrops(int(cid)):
                        all_items.append(item)
                    progress.advance(task)
        else:
            for c in collections:
                cid = c.get("_id") or c.get("id")
                if cid is None:
                    continue
                for item in client.list_raindrops(int(cid)):
                    all_items.append(item)

        elapsed = time.time() - start if start is not None else 0.0

        # Filter and map to Raindrop dataclasses
        active = filter_active_raindrops(all_items)

        if dry_run:
            click.echo(f"Dry run: collected {len(active)} active raindrops")
            click.echo(
                f"Requests made: {requests_made}; Retries: {len(retries)}; Elapsed: {elapsed:.2f}s"
            )
            return

        ctx = nullcontext()
        with ctx if output != "-" else ctx as _:
            fh = _open_output(output)
            try:
                export_to_file(active, fh, pretty=pretty)
            finally:
                if fh is not sys.stdout:
                    fh.close()

        # Summary metrics
        if not quiet:
            click.echo(
                f"Exported {len(active)} raindrops from {len(collections)} collections"
            )
            click.echo(
                f"Requests made: {requests_made}; Retries: {len(retries)}; Elapsed: {elapsed:.2f}s"
            )

    finally:
        client.close()


if __name__ == "__main__":
    main()
