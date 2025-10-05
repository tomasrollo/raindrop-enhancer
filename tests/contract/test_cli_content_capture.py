import json
import sqlite3
from pathlib import Path

import pytest
from click.testing import CliRunner

from raindrop_enhancer.cli import capture_content


def test_capture_content_dry_run_json(tmp_path: Path):
    """Run `capture-content` in dry-run + JSON mode and assert the JSON shape."""
    runner = CliRunner()
    db = tmp_path / "test.db"

    result = runner.invoke(
        capture_content,
        ["--db-path", str(db), "--dry-run", "--limit", "2", "--json"],
    )

    assert result.exit_code == 0
    # Should emit a JSON document
    payload = json.loads(result.output)
    assert "session" in payload
    assert "attempts" in payload
    assert isinstance(payload["attempts"], list)
