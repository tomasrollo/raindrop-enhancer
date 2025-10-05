# CLI Contract: `capture-content`

## Command Synopsis
```
uv run capture-content [OPTIONS]
```

## Description
Fetch readable Markdown content for saved links stored locally, persisting results into the sqlite database. Skips links with existing content unless `--refresh` is provided. Returns aggregated statistics and optional JSON output.

## Options
| Flag | Type | Required | Default | Description |
|------|------|----------|---------|-------------|
| `--refresh` | boolean | No | `False` | Overwrite stored Markdown for all processed links before capturing again. |
| `--dry-run` | boolean | No | `False` | Do not mutate the database; display which links would be processed. |
| `--limit INTEGER` | integer | No | `None` | Maximum number of uncaptured links to process this run. |
| `--json` | boolean | No | `False` | Emit machine-readable JSON summary to stdout instead of human-formatted text. |
| `--verbose` | count | No | `0` | Increase logging verbosity (stackable). |
| `--quiet` | boolean | No | `False` | Suppress non-error output. |
| `--timeout FLOAT` | float | No | `10.0` | Per-link fetch timeout in seconds; must be >0. |

Standard global flags (`--help`, `--version`) remain available per CLI conventions.

## Inputs
- Implicit: sqlite database configured via existing CLI context/environment variables.
- Optional: `RAINDROP_ENHANCER_CONFIG` env pointing to alternative config (loaded automatically).

## Outputs
- **Human-readable mode**: Rich-rendered table summarizing counts plus per-link status lines routed to stdout.
- **JSON mode** (`--json`): single JSON document structured per schema below returned on stdout; errors still go to stderr.

### JSON Schema
```json
{
  "type": "object",
  "required": ["session", "attempts"],
  "properties": {
    "session": {
      "type": "object",
      "required": [
        "started_at",
        "completed_at",
        "links_processed",
        "links_succeeded",
        "links_skipped",
        "links_failed",
        "exit_code"
      ],
      "properties": {
        "started_at": {"type": "string", "format": "date-time"},
        "completed_at": {"type": "string", "format": "date-time"},
        "links_processed": {"type": "integer", "minimum": 0},
        "links_succeeded": {"type": "integer", "minimum": 0},
        "links_skipped": {"type": "integer", "minimum": 0},
        "links_failed": {"type": "integer", "minimum": 0},
        "exit_code": {"type": "integer", "enum": [0, 1]},
        "notes": {"type": "array", "items": {"type": "string"}}
      }
    },
    "attempts": {
      "type": "array",
      "items": {
        "type": "object",
        "required": ["link_id", "status"],
        "properties": {
          "link_id": {"type": "integer", "minimum": 1},
          "url": {"type": "string", "format": "uri"},
          "status": {"type": "string", "enum": ["success", "skipped", "failed"]},
          "retry_count": {"type": "integer", "minimum": 0, "maximum": 1},
          "error_type": {"type": "string"},
          "error_message": {"type": "string"}
        }
      }
    }
  }
}
```

## Exit Codes
| Code | Meaning |
|------|---------|
| `0` | Command completed and at least one link succeeded or no links required processing. |
| `1` | All processed links failed to capture content. |

## Error Handling
- Network/HTTP/timeout failures are retried once automatically; persistent failures are reported in summary with `status="failed"`.
- Invalid options raise usage error with exit code `2` (Click default) before processing begins.
- Database write errors abort the command, emit error message to stderr, and exit with status `1`.

## Compatibility & Versioning Notes
- Command is idempotent by default; reruns without `--refresh` skip links with populated Markdown.
- Output fields are backward compatible; new optional fields may be appended but existing names will not change without deprecation.
