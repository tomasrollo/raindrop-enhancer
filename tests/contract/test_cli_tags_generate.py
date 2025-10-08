import json
import tempfile
from pathlib import Path

import click
from click.testing import CliRunner

from raindrop_enhancer.cli import tags_generate


def test_cli_tags_generate_option_parsing(monkeypatch, tmp_path: Path):
    # Create an empty DB via the existing SQLiteStore schema creation
    db = tmp_path / "links.db"

    # Monkeypatch the store to use a small in-memory predictor via env
    def fake_predictor(prompt: str):
        return ["auto tag 1", "auto tag 2"]

    # Ensure RAINDROP_DSPY_MODEL unset so CLI falls back to fake predictor behavior
    monkeypatch.delenv("RAINDROP_DSPY_MODEL", raising=False)

    runner = CliRunner()
    result = runner.invoke(tags_generate, ["--db-path", str(db), "--dry-run", "--json"])

    assert result.exit_code == 0
    payload = json.loads(result.output.strip())
    assert "processed" in payload and "generated" in payload
