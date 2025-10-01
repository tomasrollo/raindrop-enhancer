import json
from click.testing import CliRunner
from pathlib import Path

from raindrop_enhancer.cli.main import app


def test_configure_and_sync_dry_run(tmp_path: Path, monkeypatch):
    runner = CliRunner()
    cfg_dir = tmp_path / "data"
    # run configure
    result = runner.invoke(
        app, ["configure", "--token", "abc", "--data-dir", str(cfg_dir)]
    )
    assert result.exit_code == 0
    # create a fake sync command run (dry-run)
    result = runner.invoke(
        app, ["sync", "--dry-run", "--data-dir", str(cfg_dir), "--json"]
    )
    # sync may run without external network (client uses token), ensure command returns
    assert result.exit_code == 0
    out = json.loads(result.output)
    assert isinstance(out, dict)
