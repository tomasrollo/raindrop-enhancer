import click


@click.group()
def app():
    """Raindrop Enhancer CLI entry point."""
    pass


@app.command()
@click.option("--json", is_flag=True, help="Output JSON")
@click.option("--dry-run", is_flag=True, help="Don't write outputs")
def sync(json, dry_run):
    """Run a (placeholder) sync."""
    click.echo("sync: placeholder")
