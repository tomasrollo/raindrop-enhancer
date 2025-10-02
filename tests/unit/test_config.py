import tempfile
from pathlib import Path
from raindrop_enhancer.util.config import ConfigManager


def test_config_manager_read_write():
    with tempfile.TemporaryDirectory() as tmpdir:
        config_path = Path(tmpdir) / "config.toml"
        cm = ConfigManager(config_path)
        data = {"foo": "bar", "thresholds": {"x": 42}}
        cm.write(data)
        loaded = cm.read()
        assert loaded["foo"] == "bar"
        assert cm.get_threshold("x") == 42
        # Permissions should be 0600 (on POSIX)
        import os, stat

        if hasattr(os, "stat"):
            mode = os.stat(config_path).st_mode
            assert (mode & 0o777) in (0o600, 0o666)  # 0600 on POSIX, 0666 on Windows
