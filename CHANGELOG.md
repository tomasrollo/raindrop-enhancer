# Changelog

## Unreleased

### Breaking changes

- Replace legacy console scripts with a single entrypoint `raindrop-enhancer` (subcommands: `export`, `sync`, `capture`, `migrate`, `tag`).

  Rationale: simplify CLI surface and make it easier to add subcommands and global flags.

  Migration notes:
  - Existing scripts and CI that invoke `raindrop-export`, `raindrop-sync`, `capture-content`, `raindrop-migrate`, or `raindrop-tags` must be updated to call `raindrop-enhancer <subcommand>`.
  - Example replacements (macOS/BSD sed shown; adjust for GNU sed on Linux):

```bash
rg -l "raindrop-export" | xargs sed -i '' 's/raindrop-export/raindrop-enhancer export/g'
rg -l "raindrop-sync" | xargs sed -i '' 's/raindrop-sync/raindrop-enhancer sync/g'
rg -l "capture-content" | xargs sed -i '' 's/capture-content/raindrop-enhancer capture/g'
rg -l "raindrop-migrate" | xargs sed -i '' 's/raindrop-migrate/raindrop-enhancer migrate/g'
rg -l "raindrop-tags" | xargs sed -i '' 's/raindrop-tags/raindrop-enhancer tag/g'
```

- Note: this is a breaking change — bump the package major version when releasing.
