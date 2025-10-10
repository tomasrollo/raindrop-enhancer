# CLI Contract: `tags generate`

## Purpose
Generate English Title Case tags (≤20 chars) for stored links that currently lack tags, leveraging DSPy-managed LLM inference. The command must be idempotent for already-tagged links and provide structured output for automation.

## Invocation
```
uv run raindrop-tags generate [OPTIONS]
```

## Options
| Flag | Type | Required | Default | Description |
|------|------|----------|---------|-------------|
| `--limit` | int | No | `None` (process all) | Maximum number of untagged links to process in this run. |
| `--dry-run` | bool | No | `False` | Generate tags and display results without updating the database. |
| `--json` | bool | No | `False` | Emit machine-readable JSON summary to stdout (prints human summary to stderr when enabled). |
| `--quiet` | bool | No | `False` | Suppress progress bar and non-critical logs. |
| `--verbose` | count | No | `0` | Increase verbosity (may show per-link prompt/response diagnostics). |
| `--progress-refresh` | float | No | `0.2` | Minimum seconds between Rich progress refreshes (tunable for slow terminals). |

## Inputs
- SQLite database at configured path containing `raindrop_links` rows.
- Each candidate row must have `content_markdown` populated.
- Environment variables:
  - `RAINDROP_DSPY_MODEL` (string, required): identifies DSPy LM backend.
  - Provider-specific credentials (e.g., `OPENAI_API_KEY`).

## Behavior
1. Establish SQLite connection, ensuring migration created `auto_tags_json` and `auto_tags_meta_json` columns.
2. Select links where `auto_tags_json IS NULL` (or optionally flagged for reset in future extensions).
3. For each link: construct DSPy input (title, url, markdown excerpt, collections) and invoke `dspy.Predictor` with `GenerateTags` signature.
4. Normalize tags (Title Case, ≤20 chars, deduplicate) and persist alongside metadata in a single `UPDATE` (unless `--dry-run`).
5. Emit Rich progress bar unless `--quiet` or `--json` (then degrade to textual counters).
6. Collect failures with reasons (`empty_content`, `llm_error`, `postprocess_error`) and include them in summary.
7. Exit codes:
   - `0`: Completed with zero unexpected errors (LLM failures allowed but reported).
   - `2`: Database migration/setup failure.
   - `3`: DSPy misconfiguration (missing model or credentials).
   - `4`: Unexpected runtime exception (stack trace logged when `--verbose`).

## Outputs
### Human-friendly (default)
```
Processed 125 links (generated: 92, skipped_existing: 28, failed: 5)
Top tags: research, ai, productivity
Failures:
 - 123456789: empty_content
 - 987654321: llm_error (context window exceeded)
Duration: 00:07:43 | Model: openai:gpt-4o-mini
```

### JSON (`--json`)
```json
{
  "processed": 125,
  "generated": 92,
  "skipped_existing": 28,
  "failed": 5,
  "failures": [
    {"raindrop_id": 123456789, "reason": "empty_content"}
  ],
  "duration_seconds": 463.7,
  "model": "openai:gpt-4o-mini"
}
```

## Testing Notes
- Contract tests must validate exit codes, summary structure, and JSON schema (field presence & types).
- Integration tests will stub DSPy so the CLI can run offline, ensuring deterministic outputs.
- Performance smoke test: dry-run with 50 synthetic links completes in ≤ 8 minutes and maintains memory usage < 150 MB.
