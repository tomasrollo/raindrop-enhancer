# Quickstart — LLM-Assisted Link Tagging

Follow these steps to exercise the new tagging workflow end-to-end once implementation is complete.

## 1. Prepare environment
1. Install dependencies: `uv sync`
2. Export model credentials (example uses OpenAI):
   ```bash
   export RAINDROP_DSPY_MODEL=openai:gpt-4o-mini
   export OPENAI_API_KEY=sk-your-key
   ```
3. Ensure the Raindrop cache database exists with captured content markdown: run existing sync + content capture commands.

## 2. Dry-run tagging
```bash
uv run raindrop-enhancer tags generate --dry-run --limit 5 --verbose
```
- Confirms CLI wiring, displays Rich progress, and prints preview tags without DB writes.
- Expect summary JSON (when `--json` used) to list `generated`, `skipped_existing`, and `failed` counts.

## 3. Persist tags for untagged links
```bash
uv run raindrop-enhancer tags generate --limit 100
```
- Processes 100 untagged links (or all if fewer).
- Writes normalized tags to `auto_tags_json` and metadata to `auto_tags_meta_json`.
- Command exits `0` when all processed; returns non-zero if any unexpected error occurs (LLM errors reported but do not fail unless `--fail-on-error` flag is supplied later).

## 4. Inspect stored tags
```bash
uv run python - <<'PY'
from raindrop_enhancer.storage.sqlite_store import SQLiteStore
from pathlib import Path
store = SQLiteStore(Path.home()/'.local/share/raindrop_enhancer/raindrops.db')
store.connect()
rows = store.conn.execute('SELECT raindrop_id, auto_tags_json, auto_tags_meta_json FROM raindrop_links WHERE auto_tags_json IS NOT NULL LIMIT 5').fetchall()
for row in rows:
    print(row['raindrop_id'], row['auto_tags_json'], row['auto_tags_meta_json'])
store.close()
PY
```
- Verifies persisted JSON and metadata.

## 5. Rerun to confirm idempotency
```bash
uv run raindrop-enhancer tags generate --limit 50
```
- Should skip links already tagged (reported in summary) and exit quickly.

## 6. Cleanup / reset (optional)
```bash
uv run raindrop-enhancer tags reset --raindrop-id 12345
```
- Example follow-up command (if implemented) to clear auto tags for a specific link.
- Ensures migrations left manual tags untouched.

## Expected outputs
- Rich progress bar updates with completed/remaining counts.
- Summary table in stdout and optional JSON structure containing: `processed`, `generated`, `skipped_existing`, `failed`, `duration_seconds`, `model`.
- Log warnings for links whose `content_markdown` is missing or too short.
