"""Command line interface for the Raindrop Enhancer utility."""

from __future__ import annotations

import json
import logging
from dataclasses import dataclass
from datetime import datetime, timezone
from pathlib import Path
from typing import Any, Sequence

import click
import trafilatura
from rich.console import Console
from rich.table import Table

from raindrop_enhancer.api.client import RaindropClient
from raindrop_enhancer.services import sync as sync_service
from raindrop_enhancer.services.tagging import TaggingService
from raindrop_enhancer.util.config import ConfigManager, resolve_data_dir
from raindrop_enhancer.util.logging import (
    configure_logging,
    get_metrics,
    log_retry_event,
)


console = Console()


@dataclass(slots=True)
class CLIContext:
    json_output: bool
    verbose: bool
    quiet: bool
    dry_run: bool
    data_dir: Path | None


def _utc_now() -> datetime:
    return datetime.now(timezone.utc)


def _fetch_content(url: str) -> str:
    downloaded = trafilatura.fetch_url(url)
    if not downloaded:
        raise RuntimeError(f"Unable to fetch content from {url}")
    extracted = trafilatura.extract(
        downloaded,
        include_comments=False,
        include_links=False,
    )
    if not extracted:
        raise RuntimeError(f"Content extraction returned empty payload for {url}")
    return extracted


def _json_default(value: Any) -> Any:
    if isinstance(value, datetime):
        return value.isoformat()
    if isinstance(value, Path):
        return str(value)
    return value


def perform_sync(
    *,
    mode: str,
    config_manager: ConfigManager,
    data_dir_override: Path | None,
    collection_ids: Sequence[int] | None,
    since: datetime | str | None,
    batch_size: int,
    dry_run: bool,
) -> dict[str, Any]:
    """Orchestrate a sync run and return the structured summary."""

    state = config_manager.load()
    token = state.raindrop_token
    if not token:
        raise click.ClickException(
            "Raindrop token missing. Run `raindrop-enhancer configure --token ...` first."
        )

    data_dir = data_dir_override or state.data_dir
    data_dir = Path(resolve_data_dir(data_dir))
    data_dir.mkdir(parents=True, exist_ok=True)

    if not state.llm_api_base or not state.llm_api_key:
        raise click.ClickException(
            "LLM API credentials are not configured. Provide --llm-api-base and --llm-api-key via the configure command."
        )

    tagging = TaggingService(
        api_base=state.llm_api_base,
        api_key=state.llm_api_key,
        batch_size=batch_size,
        confidence_threshold=state.tag_confidence_threshold,
        max_tags=state.max_tags,
        on_retry=log_retry_event,
    )
    client = RaindropClient(token, on_retry=log_retry_event)

    try:
        kwargs = {
            "data_dir": data_dir,
            "api_client": client,
            "tagging_service": tagging,
            "content_fetcher": _fetch_content,
            "now": _utc_now,
            "collection_ids": list(collection_ids) if collection_ids else None,
            "batch_size": batch_size,
            "dry_run": dry_run,
        }

        if mode == "full":
            summary = sync_service.run_full_sync(**kwargs)
        elif mode == "incremental":
            summary = sync_service.run_incremental_sync(
                since=since,
                **kwargs,
            )
        else:
            raise click.ClickException(f"Unsupported sync mode: {mode}")
    finally:
        client.close()

    return summary


@click.group()
@click.option(
    "--json", "json_output", is_flag=True, help="Output machine-readable JSON."
)
@click.option("--verbose", is_flag=True, help="Increase log verbosity.")
@click.option("--quiet", is_flag=True, help="Suppress non-error output.")
@click.option("--dry-run", is_flag=True, help="Fetch data without writing to disk.")
@click.option(
    "--data-dir",
    type=click.Path(path_type=Path, file_okay=False),
    help="Override the configured data directory for this invocation.",
)
@click.pass_context
def app(
    ctx: click.Context,
    json_output: bool,
    verbose: bool,
    quiet: bool,
    dry_run: bool,
    data_dir: Path | None,
) -> None:
    """Raindrop Enhancer CLI entry point."""

    if verbose and quiet:
        raise click.UsageError("--verbose and --quiet are mutually exclusive")

    level = logging.INFO
    if verbose:
        level = logging.DEBUG
    elif quiet:
        level = logging.ERROR
    configure_logging(level)

    ctx.obj = CLIContext(
        json_output=json_output,
        verbose=verbose,
        quiet=quiet,
        dry_run=dry_run,
        data_dir=data_dir,
    )


@app.command()
@click.option("--token", type=str, help="Raindrop API token to store in config.")
@click.option(
    "--data-dir",
    type=click.Path(path_type=Path, file_okay=False),
    help="Persist configuration inside this directory.",
)
@click.option("--llm-api-base", type=str, help="Base URL for the LLM tagging API.")
@click.option("--llm-api-key", type=str, help="API key for the LLM tagging API.")
@click.option(
    "--tag-threshold",
    type=click.FloatRange(0.0, 1.0),
    help="Minimum confidence required for suggested tags.",
)
@click.option(
    "--max-tags",
    type=click.IntRange(0, 50),
    help="Maximum number of tags to keep per link.",
)
@click.pass_obj
def configure(
    ctx: CLIContext,
    token: str | None,
    data_dir: Path | None,
    llm_api_base: str | None,
    llm_api_key: str | None,
    tag_threshold: float | None,
    max_tags: int | None,
) -> None:
    """Persist CLI configuration such as tokens and thresholds."""

    manager = ConfigManager(data_dir or ctx.data_dir)
    updates: dict[str, Any] = {}
    if data_dir is not None:
        updates["data_dir"] = data_dir
    if token is not None:
        updates["raindrop_token"] = token
    if llm_api_base is not None:
        updates["llm_api_base"] = llm_api_base
    if llm_api_key is not None:
        updates["llm_api_key"] = llm_api_key
    if tag_threshold is not None:
        updates["tag_confidence_threshold"] = tag_threshold
    if max_tags is not None:
        updates["max_tags"] = max_tags

    state = manager.update(**updates)

    summary = {
        "data_dir": str(state.data_dir),
        "has_token": bool(state.raindrop_token),
        "llm_api_base": state.llm_api_base,
        "tag_confidence_threshold": state.tag_confidence_threshold,
        "max_tags": state.max_tags,
    }

    if ctx.json_output:
        click.echo(json.dumps(summary, default=_json_default))
    else:
        console.print("[green]Configuration updated successfully.[/green]")
        for key, value in summary.items():
            console.print(f" - {key}: {value}")


@app.command()
@click.option(
    "--mode",
    type=click.Choice(["full", "incremental"], case_sensitive=False),
    required=True,
    help="Select full or incremental synchronisation.",
)
@click.option(
    "--collection-id",
    "collection_ids",
    type=int,
    multiple=True,
    help="Limit the sync to specific collection IDs.",
)
@click.option(
    "--since",
    type=str,
    help="Override the incremental since timestamp (ISO-8601).",
)
@click.option(
    "--batch-size",
    type=click.IntRange(1, 100),
    default=50,
    show_default=True,
    help="Batch size for tagging requests and Raindrop pagination.",
)
@click.pass_obj
def sync(
    ctx: CLIContext,
    mode: str,
    collection_ids: tuple[int, ...],
    since: str | None,
    batch_size: int,
) -> None:
    """Synchronise Raindrop collections and enrich tags."""

    manager = ConfigManager(ctx.data_dir)

    try:
        summary = perform_sync(
            mode=mode.lower(),
            config_manager=manager,
            data_dir_override=ctx.data_dir,
            collection_ids=collection_ids,
            since=since,
            batch_size=batch_size,
            dry_run=ctx.dry_run,
        )
    except click.ClickException:
        raise
    except Exception as exc:  # pragma: no cover - defensive guard
        raise click.ClickException(str(exc)) from exc

    if ctx.json_output:
        click.echo(json.dumps(summary, default=_json_default))
        get_metrics().clear()
    else:
        _render_sync_summary(summary)


@app.command()
@click.option("--id", "raindrop_id", type=int, required=True, help="Raindrop link ID")
@click.option(
    "--reason", type=str, help="Optional note recorded for the reprocess run."
)
@click.pass_obj
def reprocess(ctx: CLIContext, raindrop_id: int, reason: str | None) -> None:
    """Reprocess a single Raindrop link through the enrichment pipeline."""

    manager = ConfigManager(ctx.data_dir)
    state = manager.load()
    if not state.raindrop_token:
        raise click.ClickException(
            "Raindrop token missing. Configure credentials before reprocessing."
        )
    if not state.llm_api_base or not state.llm_api_key:
        raise click.ClickException(
            "LLM API credentials missing. Configure --llm-api-base and --llm-api-key first."
        )

    data_dir = ctx.data_dir or state.data_dir
    data_dir = Path(resolve_data_dir(data_dir))
    data_dir.mkdir(parents=True, exist_ok=True)

    tagging = TaggingService(
        api_base=state.llm_api_base,
        api_key=state.llm_api_key,
        batch_size=25,
        confidence_threshold=state.tag_confidence_threshold,
        max_tags=state.max_tags,
        on_retry=log_retry_event,
    )
    client = RaindropClient(state.raindrop_token, on_retry=log_retry_event)

    try:
        summary = sync_service.run_reprocess(
            data_dir=data_dir,
            raindrop_id=raindrop_id,
            api_client=client,
            tagging_service=tagging,
            content_fetcher=_fetch_content,
            now=_utc_now,
            dry_run=ctx.dry_run,
        )
        if reason:
            summary["reason"] = reason
    finally:
        client.close()

    if ctx.json_output:
        click.echo(json.dumps(summary, default=_json_default))
        get_metrics().clear()
    else:
        _render_reprocess_summary(summary)


@app.command()
@click.option(
    "--limit",
    type=click.IntRange(1, 50),
    default=10,
    show_default=True,
    help="Number of recent sync runs to display.",
)
@click.pass_obj
def status(ctx: CLIContext, limit: int) -> None:
    """Display recent sync runs and rate-limit telemetry."""

    manager = ConfigManager(ctx.data_dir)
    state = manager.load()
    data_dir = ctx.data_dir or state.data_dir
    data_dir = Path(resolve_data_dir(data_dir))

    summary = sync_service.status_summary(data_dir=data_dir, limit=limit)

    if ctx.json_output:
        click.echo(json.dumps(summary, default=_json_default))
    else:
        _render_status(summary)


def _render_sync_summary(summary: dict[str, Any]) -> None:
    console.print("[bold green]Sync completed successfully[/bold green]")
    details = Table(show_header=False, box=None)
    details.add_row("Mode", summary.get("mode", "?"))
    details.add_row("Processed", str(summary.get("processed", 0)))
    details.add_row("Skipped", str(summary.get("skipped", 0)))
    details.add_row("Manual review", str(summary.get("manual_review", 0)))
    details.add_row(
        "Rate limit remaining", str(summary.get("rate_limit_remaining", "-"))
    )
    if "rate_limit_limit" in summary:
        details.add_row("Rate limit limit", str(summary.get("rate_limit_limit", "-")))
    details.add_row(
        "Rate limit reset",
        _format_rate_limit_reset(summary.get("rate_limit_reset")),
    )
    details.add_row("Export path", summary.get("export_path") or "(dry run)")
    metrics_recorder = get_metrics()
    metrics_snapshot = metrics_recorder.snapshot()
    metrics_recorder.clear()
    api_counter = 0
    for key, value in metrics_snapshot.get("counters", {}).items():
        if key.startswith("raindrop.api_request"):
            api_counter += int(value)
    if api_counter:
        details.add_row("API requests", str(api_counter))
    console.print(details)


def _render_reprocess_summary(summary: dict[str, Any]) -> None:
    console.print("[bold cyan]Reprocess completed[/bold cyan]")
    details = Table(show_header=False, box=None)
    for key in [
        "previous_status",
        "new_status",
        "manual_review",
        "rate_limit_remaining",
        "rate_limit_limit",
        "rate_limit_reset",
    ]:
        if key in summary:
            details.add_row(key.replace("_", " ").title(), str(summary[key]))
    console.print(details)
    get_metrics().clear()


def _render_status(entries: list[dict[str, Any]]) -> None:
    if not entries:
        console.print("No sync history recorded yet.")
        return

    table = Table(title="Recent Sync Runs")
    table.add_column("Run ID", overflow="fold")
    table.add_column("Mode")
    table.add_column("Processed", justify="right")
    table.add_column("Manual", justify="right")
    table.add_column("Remaining", justify="right")
    table.add_column("Limit", justify="right")
    table.add_column("Reset")
    table.add_column("Completed")

    for entry in entries:
        table.add_row(
            entry.get("run_id", "-"),
            entry.get("mode", "-"),
            str(entry.get("links_processed", 0)),
            str(entry.get("manual_review", 0)),
            str(entry.get("rate_limit_remaining", "-")),
            str(entry.get("rate_limit_limit", "-")),
            _format_rate_limit_reset(entry.get("rate_limit_reset")),
            entry.get("completed_at") or "--",
        )

    console.print(table)


def _format_rate_limit_reset(value: Any) -> str:
    if value in (None, "", "-"):
        return "-"
    try:
        timestamp = int(value)
    except (TypeError, ValueError):
        return str(value)
    try:
        reset_time = datetime.fromtimestamp(timestamp, tz=timezone.utc)
    except (OSError, OverflowError, ValueError):
        return str(value)
    return reset_time.strftime("%Y-%m-%d %H:%M:%S UTC")
