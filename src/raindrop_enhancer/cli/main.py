import click
from pathlib import Path
from rich.console import Console
from ..util.config import ConfigManager
from ..domain.repositories import Repo
from ..services.tagging import TaggingService
from ..services.sync import run_full_sync, run_incremental_sync
from ..util.logging import setup_logging, inc_metric, get_metrics
import json
import os
from datetime import datetime, timedelta


@click.group()
@click.option(
    "--config",
    default="~/.config/raindrop-enhancer/config.toml",
    help="Config file path.",
)
@click.pass_context
def app(ctx, config):
    """Raindrop Enhancer CLI entry point."""
    setup_logging()
    ctx.ensure_object(dict)
    ctx.obj["config_path"] = Path(os.path.expanduser(config))
    ctx.obj["console"] = Console()


@app.command()
@click.option(
    "--mode",
    type=click.Choice(["full", "incremental"]),
    default="full",
    help="Sync mode.",
)
@click.option(
    "--since", type=str, help="Incremental: ISO date/time or e.g. '2d' for 2 days ago."
)
@click.option(
    "--export",
    type=click.Path(),
    default="raindrop_export.json",
    help="Export JSON path.",
)
@click.option("--dry-run", is_flag=True, help="Don't write outputs.")
@click.option("--json-output", is_flag=True, help="Output result as JSON.")
@click.pass_context
def sync(ctx, mode, since, export, dry_run, json_output):
    """Run a sync (full or incremental)."""
    config_path = ctx.obj["config_path"]
    console = ctx.obj["console"]
    config = ConfigManager(config_path).read()
    repo = Repo(config.get("db_path", "raindrop.db"))
    repo.setup()
    tagging = TaggingService(llm_client=None)  # Replace with real LLM client
    export_path = Path(export)
    import logging

    logger = logging.getLogger("raindrop_enhancer")
    if mode == "full":
        result = run_full_sync(repo, tagging, export_path, dry_run=dry_run)
    else:
        if since:
            if since.endswith("d"):
                dt = datetime.utcnow() - timedelta(days=int(since[:-1]))
            else:
                dt = datetime.fromisoformat(since)
        else:
            dt = datetime.utcnow() - timedelta(days=1)
        result = run_incremental_sync(
            repo, tagging, export_path, since=dt, dry_run=dry_run
        )
    inc_metric("sync_runs")
    logger.info(f"Sync completed: {result}")
    # Show metrics and rate-limit telemetry if available
    metrics = get_metrics()
    if json_output:
        result["metrics"] = metrics
        click.echo(json.dumps(result, indent=2))
    else:
        console.print(f"[bold green]Sync complete:[/bold green] {result}")
        console.print(f"[cyan]Metrics:[/cyan] {metrics}")
    # Show last rate-limit telemetry if available
    from ..domain.entities import SyncRun
    from sqlmodel import Session, select
    from sqlalchemy import desc

    with Session(repo.engine) as session:
        last_run = session.exec(
            select(SyncRun).order_by(desc(getattr(SyncRun, "completed_at")))
        ).first()
        if last_run and last_run.rate_limit_limit:
            console.print(
                f"[yellow]Rate limit:[/yellow] {last_run.rate_limit_remaining}/{last_run.rate_limit_limit} resets at {last_run.rate_limit_reset}"
            )


@app.command()
@click.pass_context
def configure(ctx):
    """Configure CLI settings interactively."""
    config_path = ctx.obj["config_path"]
    console = ctx.obj["console"]
    db_path = click.prompt("SQLite DB path", default="raindrop.db")
    token = click.prompt("Raindrop API token", hide_input=True)
    config = {"db_path": db_path, "token": token}
    ConfigManager(config_path).write(config)
    console.print(f"[bold green]Config saved to {config_path}")


@app.command()
@click.pass_context
def status(ctx):
    """Show sync status summary."""
    config_path = ctx.obj["config_path"]
    console = ctx.obj["console"]
    config = ConfigManager(config_path).read()
    repo = Repo(config.get("db_path", "raindrop.db"))
    repo.setup()
    # Show last SyncRun
    from ..domain.entities import SyncRun
    from sqlmodel import Session, select
    from sqlalchemy import desc

    with Session(repo.engine) as session:
        last_run = session.exec(
            select(SyncRun).order_by(desc(getattr(SyncRun, "completed_at")))
        ).first()
        if last_run:
            console.print(
                f"[bold]Last sync:[/bold] {last_run.mode} at {last_run.completed_at} ({last_run.links_processed} links)"
            )
            if last_run.rate_limit_limit:
                console.print(
                    f"[yellow]Rate limit:[/yellow] {last_run.rate_limit_remaining}/{last_run.rate_limit_limit} resets at {last_run.rate_limit_reset}"
                )
        else:
            console.print("No sync runs found.")


@app.command()
@click.pass_context
def reprocess(ctx):
    """Reprocess links and update status (stub)."""
    console = ctx.obj["console"]
    console.print("[yellow]Reprocess not yet implemented.[/yellow]")
