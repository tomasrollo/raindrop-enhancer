````markdown
# Quickstart: `raindrop-enhancer` CLI

## Install
Install the package via the project's standard method (uv-managed or pip):

Example (uv):

```bash
uv add .
uv run pip install -e .
```

## Usage

The unified CLI exposes subcommands: `export`, `sync`, `capture`, `migrate`, `tag`.

Examples (using `uv run` wrapper):

```bash
# Export collections
uv run raindrop-enhancer export --collection "reading-list"

# Sync local store
uv run raindrop-enhancer sync --incremental

# Capture content
uv run raindrop-enhancer capture https://example.com/article

# Run migrations
uv run raindrop-enhancer migrate

# Generate tags (requires dspy)
uv run raindrop-enhancer tag --db-path ./tmp/raindrops.db --dry-run
```

## Migration notes
This release removes legacy console scripts (`raindrop-export`, `raindrop-sync`, `capture-content`, `raindrop-migrate`, `raindrop-tags`). Update existing scripts and CI to use the new `raindrop-enhancer <subcommand>` invocations.

Example sed/rg commands for macOS (BSD sed) to perform a project-wide replacement:

```bash
# replace raindrop-export occurrences with raindrop-enhancer export
rg -l "raindrop-export" | xargs sed -i '' 's/raindrop-export/raindrop-enhancer export/g'

# replace raindrop-sync with raindrop-enhancer sync
rg -l "raindrop-sync" | xargs sed -i '' 's/raindrop-sync/raindrop-enhancer sync/g'

# replace capture-content with raindrop-enhancer capture
rg -l "capture-content" | xargs sed -i '' 's/capture-content/raindrop-enhancer capture/g'

# replace raindrop-migrate with raindrop-enhancer migrate
rg -l "raindrop-migrate" | xargs sed -i '' 's/raindrop-migrate/raindrop-enhancer migrate/g'

# replace raindrop-tags generate with raindrop-enhancer tag
rg -l "raindrop-tags" | xargs sed -i '' 's/raindrop-tags/raindrop-enhancer tag/g'
```

````
