import json
from pathlib import Path

import click

from raindrop_enhancer.util.config import (
    get_or_create_config,
    write_config,
    validate_config,
)
from raindrop_enhancer.api.client import RaindropClient
from raindrop_enhancer.services.sync import run_full_sync
from raindrop_enhancer.util.logging import structured
from raindrop_enhancer.domain.repositories import Repo


@click.group()
def app():
    """Raindrop Enhancer CLI entry point."""
    pass


@app.command()
@click.option("--token", required=False, help="Raindrop API token")
@click.option("--data-dir", required=False, type=click.Path(), help="Data directory")
@click.option("--llm-api-base", required=False, help="LLM API base URL")
@click.option("--llm-api-key", required=False, help="LLM API key")
def configure(token, data_dir, llm_api_base, llm_api_key):
    """Write CLI configuration to data directory."""
    path = Path(data_dir) if data_dir else Path.home() / ".raindrop_enhancer"
    cfg_path = path / "config.toml"
    cfg = get_or_create_config(cfg_path)
    if token:
        cfg["token_path"] = str(path / "token.txt")
        (path / "token.txt").write_text(token)
    if llm_api_base:
        cfg["llm_api_base"] = llm_api_base
    if llm_api_key:
        cfg["llm_api_key"] = llm_api_key
    if data_dir:
        cfg["data_dir"] = data_dir

    validate_config(cfg)
    write_config(cfg_path, cfg)
    click.echo(json.dumps({"status": "ok", "config": cfg}))


@app.command()
@click.option(
    "--mode",
    type=click.Choice(["full", "incremental"]),
    default="full",
    help="Sync mode",
)
@click.option("--data-dir", required=False, type=click.Path(), help="Override data dir")
@click.option("--json", "as_json", is_flag=True, help="Output JSON")
@click.option("--dry-run", is_flag=True, help="Don't write outputs")
def sync(mode, data_dir, as_json, dry_run):
    """Run full or incremental sync."""
    # Load configuration
    cfg_path = Path(data_dir or Path.home() / ".raindrop_enhancer") / "config.toml"
    cfg = get_or_create_config(cfg_path)

    token_path = cfg.get("token_path")
    token = None
    if token_path:
        try:
            token = Path(token_path).read_text().strip()
        except Exception:
            token = None

    client = RaindropClient(token or "")
    repo = Repo(cfg.get("data_dir", ":memory:") + "/db.sqlite")
    repo.setup()

    if mode == "full":
        result = run_full_sync(
            repo=repo,
            client=client,
            export_path=Path(cfg.get("data_dir", ".")) / "exports" / "latest.json",
            dry_run=dry_run,
        )
    else:
        result = {"processed": 0, "note": "incremental not implemented"}

    if as_json:
        click.echo(json.dumps(result))
    else:
        click.echo(
            f"Processed: {result.get('processed')}, export_count: {result.get('export_count')}"
        )
        # emit structured telemetry for downstream tooling
        try:
            structured(
                "sync.summary",
                run_id=result.get("run_id"),
                processed=result.get("processed"),
                export_count=result.get("export_count"),
                duration_seconds=result.get("duration_seconds"),
                rate_limit=result.get("rate_limit"),
            )
        except Exception:
            pass


@app.command()
@click.option("--limit", default=10, help="Number of recent runs (not implemented)")
@click.option("--json", "as_json", is_flag=True, help="Output JSON")
def status(limit, as_json):
    """Show latest sync status (placeholder)."""
    result = {"recent_runs": []}
    if as_json:
        click.echo(json.dumps(result))
    else:
        click.echo("No sync runs recorded yet.")
