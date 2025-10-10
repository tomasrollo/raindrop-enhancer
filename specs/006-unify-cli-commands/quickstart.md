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

Examples:

```bash
# Export collections
raindrop-enhancer export --collection "reading-list"

# Sync local store
raindrop-enhancer sync --incremental

# Capture content
raindrop-enhancer capture https://example.com/article

# Run migrations
raindrop-enhancer migrate

# Generate tags (requires dspy)
raindrop-enhancer tag --source local
```

## Migration notes
This release removes legacy console scripts (`raindrop-export`, `raindrop-sync`, `capture-content`, `raindrop-migrate`, `raindrop-tags`). Update existing scripts and CI to use the new `raindrop-enhancer <subcommand>` invocations. Example sed command to update simple scripts:

```bash
# replace raindrop-export occurrences with raindrop-enhancer export
rg -l "raindrop-export" | xargs sed -i '' 's/raindrop-export/raindrop-enhancer export/g'
```

````
