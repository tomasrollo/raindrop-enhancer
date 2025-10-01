def DummyDesc(x):
    print("[DEBUG DummyDesc] called with", x)
    return x


class DummySyncRunClass:
    completed_at = "2025-01-01T00:00:00Z"  # Add class attribute for SQLModel compatibility
    run_id = "dummy"  # Add class attribute for SQLModel compatibility

    def __init__(self, *a, **kw):
        print("[DEBUG DummySyncRunClass.__init__] called with", a, kw)
        self.run_id = "dummy"
        self.started_at = "2025-01-01T00:00:00Z"
        self.completed_at = "2025-01-01T00:00:00Z"
        self.mode = "full"
        self.links_processed = 0
        self.rate_limit_limit = 100
        self.rate_limit_remaining = 50
        self.rate_limit_reset = "2025-01-01T00:00:00Z"

    def where(self, *a, **kw):
        return self


class DummySelect:
    def __init__(self, *a, **kw):
        pass

    def where(self, *a, **kw):
        print("[DEBUG DummySelect.where] called with", a, kw)
        return self

    def order_by(self, *a, **kw):
        print("[DEBUG DummySelect.order_by] called with", a, kw)
        return self

    def first(self):
        print("[DEBUG DummySelect.first] self:", self)
        result = DummySyncRunClass()
        print("[DEBUG DummySelect.first] returning:", result, type(result))
        return result


import sys
import types
import pytest
from click.testing import CliRunner


class DummySyncRun:
    rate_limit_limit = 100
    rate_limit_remaining = 50
    rate_limit_reset = "2025-01-01T00:00:00Z"
    completed_at = "2025-01-01T00:00:00Z"
    mode = "full"
    links_processed = 0


class DummySession:
    def refresh(self, *a, **kw):
        print("[DEBUG DummySession.refresh] called with", a, kw)
        pass

    def commit(self, *a, **kw):
        print("[DEBUG DummySession.commit] called with", a, kw)
        pass

    def add(self, *a, **kw):
        print("[DEBUG DummySession.add] called with", a, kw)
        pass

    def __init__(self, *args, **kwargs):
        print("[DEBUG DummySession.__init__] called with", args, kwargs)

    def __enter__(self):
        print("[DEBUG DummySession.__enter__] called")
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        print("[DEBUG DummySession.__exit__] called")
        pass

    def exec(self, *a, **kw):
        print("[DEBUG DummySession.exec] called with", a, kw)
        # Return DummySelect, whose first() returns DummySyncRunClass instance
        return DummySelect()


import sys
import types
import pytest
from click.testing import CliRunner
from raindrop_enhancer.cli.main import app


def test_configure_command(tmp_path, monkeypatch):
    runner = CliRunner()
    config_path = tmp_path / "config.toml"
    monkeypatch.setattr("os.path.expanduser", lambda p: str(config_path))
    # Patch click.prompt to simulate user input for db_path and token
    prompts = iter(["test.db", "testtoken"])
    monkeypatch.setattr("click.prompt", lambda text, **kwargs: next(prompts))
    result = runner.invoke(app, ["--config", str(config_path), "configure"])
    if result.exit_code != 0:
        print("\n[DEBUG configure] output:\n", result.output)
        print("[DEBUG configure] exception:", result.exception)
    assert result.exit_code == 0
    assert config_path.exists()


def test_sync_command(tmp_path, monkeypatch):

    # Patch DB/session modules for CLI before any raindrop_enhancer import
    sqlmodel_mod = types.ModuleType("sqlmodel")
    setattr(sqlmodel_mod, "Session", DummySession)

    class DummySQLModel:
        class metadata:
            @staticmethod
            def create_all(engine):
                print("[DEBUG DummySQLModel.metadata.create_all] called with", engine)

    setattr(sqlmodel_mod, "SQLModel", DummySQLModel)

    def dummy_create_engine(*a, **kw):
        print("[DEBUG dummy_create_engine] called with", a, kw)

        class DummyEngine:
            def connect(self):
                class DummyConn:
                    def exec_driver_sql(self, sql):
                        print("[DEBUG DummyConn.exec_driver_sql] called with", sql)

                    def __enter__(self):
                        return self

                    def __exit__(self, exc_type, exc_val, exc_tb):
                        pass

                    def close(self):
                        pass

                    in_transaction = False

                return DummyConn()

        return DummyEngine()

    setattr(sqlmodel_mod, "create_engine", dummy_create_engine)
    import traceback

    def dummy_select(*a, **kw):
        print("[DEBUG dummy_select] called with", a, kw)
        traceback.print_stack(limit=5)
        return DummySelect()

    setattr(sqlmodel_mod, "select", dummy_select)
    sqlalchemy_mod = types.ModuleType("sqlalchemy")
    setattr(sqlalchemy_mod, "desc", DummyDesc)
    entities_mod = types.ModuleType("entities")

    class DummyEntity:
        pass

    setattr(entities_mod, "LinkRecord", DummyEntity)
    setattr(entities_mod, "Collection", DummyEntity)
    setattr(entities_mod, "TagSuggestion", DummyEntity)
    setattr(entities_mod, "ConfigSettings", DummyEntity)
    setattr(entities_mod, "LinkCollectionLink", DummyEntity)
    setattr(entities_mod, "SyncRun", DummySyncRunClass)
    monkeypatch.setitem(sys.modules, "sqlmodel", sqlmodel_mod)
    monkeypatch.setitem(sys.modules, "sqlalchemy", sqlalchemy_mod)
    monkeypatch.setitem(sys.modules, "raindrop_enhancer.domain.entities", entities_mod)

    # Only import after all monkeypatching
    import importlib
    import raindrop_enhancer.domain.repositories as repo_mod
    import raindrop_enhancer.services.tagging as tagging_mod
    import raindrop_enhancer.cli.main as cli_main_mod

    importlib.reload(repo_mod)
    importlib.reload(tagging_mod)
    importlib.reload(cli_main_mod)
    from raindrop_enhancer.cli.main import app
    from raindrop_enhancer.domain.repositories import Repo
    from raindrop_enhancer.services.tagging import TaggingService

    # Patch run_full_sync and run_incremental_sync to avoid calling real implementation
    monkeypatch.setattr(
        "raindrop_enhancer.services.sync.run_full_sync",
        lambda *a, **kw: {"processed": 0, "exported": 0, "dry_run": True},
    )
    monkeypatch.setattr(
        "raindrop_enhancer.services.sync.run_incremental_sync",
        lambda *a, **kw: {"processed": 0, "exported": 0, "dry_run": True},
    )
    # Patch logging/metrics utilities to dummies
    monkeypatch.setattr("raindrop_enhancer.util.logging.inc_metric", lambda *a, **kw: None)
    monkeypatch.setattr("raindrop_enhancer.util.logging.get_metrics", lambda *a, **kw: {})

    class DummyLogger:
        def info(self, *a, **kw):
            pass

        def debug(self, *a, **kw):
            pass

        def warning(self, *a, **kw):
            pass

        def error(self, *a, **kw):
            pass

    monkeypatch.setattr("raindrop_enhancer.util.logging.setup_logging", lambda *a, **kw: DummyLogger())

    # Patch create_engine to return a dummy engine
    class DummyEngine:
        def connect(self):
            class DummyConn:
                in_transaction = False

                def exec_driver_sql(self, sql):
                    pass

                def __enter__(self):
                    return self

                def __exit__(self, exc_type, exc_val, exc_tb):
                    pass

                def close(self):
                    pass

            return DummyConn()

    monkeypatch.setattr("raindrop_enhancer.domain.repositories.create_engine", lambda *a, **kw: DummyEngine())

    runner = CliRunner()
    config_path = tmp_path / "config.toml"
    # Write a minimal config
    config_path.write_text("db_path = 'test.db'\ntoken = 'abc'\n")
    db_path = tmp_path / "test.db"
    # Patch Repo to avoid real DB
    monkeypatch.setattr(Repo, "setup", lambda self: None)
    monkeypatch.setattr(Repo, "list_links", lambda self: [])
    monkeypatch.setattr(Repo, "get_links_updated_since", lambda self, dt: [])
    # Patch TaggingService
    monkeypatch.setattr(TaggingService, "suggest_tags_for_content", lambda self, content: [])

    # Import app only after all monkeypatching and reloads
    from raindrop_enhancer.cli.main import app

    result = runner.invoke(app, ["--config", str(config_path), "sync", "--dry-run", "--json-output"])
    if result.exit_code != 0:
        print("\n[DEBUG sync] output:\n", result.output)
        print("[DEBUG sync] exception:", result.exception)
        if result.exception:
            print("[DEBUG sync] exception type:", type(result.exception))
    assert result.exit_code == 0
    assert "Sync complete" in result.output or "processed" in result.output


def test_status_command(tmp_path, monkeypatch):
    # Patch logging/metrics utilities to dummies
    monkeypatch.setattr("raindrop_enhancer.util.logging.inc_metric", lambda *a, **kw: None)
    monkeypatch.setattr("raindrop_enhancer.util.logging.get_metrics", lambda *a, **kw: {})
    monkeypatch.setattr("raindrop_enhancer.util.logging.setup_logging", lambda *a, **kw: None)

    # Patch create_engine to return a dummy engine
    class DummyEngine:
        def connect(self):
            class DummyConn:
                in_transaction = False

                def exec_driver_sql(self, sql):
                    pass

                def __enter__(self):
                    return self

                def __exit__(self, exc_type, exc_val, exc_tb):
                    pass

                def close(self):
                    pass

            return DummyConn()

    class DummySelect:
        def order_by(self, *a, **kw):
            return self

    sqlmodel_mod = types.ModuleType("sqlmodel")
    setattr(sqlmodel_mod, "Session", DummySession)
    setattr(sqlmodel_mod, "select", lambda *a, **kw: DummySelect())
    monkeypatch.setattr("raindrop_enhancer.domain.repositories.create_engine", lambda *a, **kw: DummyEngine())
    runner = CliRunner()
    config_path = tmp_path / "config.toml"
    config_path.write_text("db_path = 'test.db'\ntoken = 'abc'\n")
    db_path = tmp_path / "test.db"
    from raindrop_enhancer.domain.repositories import Repo

    monkeypatch.setattr(Repo, "setup", lambda self: None)
    # Patch DB/session modules for CLI only
    sqlmodel_mod = types.ModuleType("sqlmodel")
    setattr(sqlmodel_mod, "Session", DummySession)
    setattr(sqlmodel_mod, "select", lambda *a, **kw: DummySelect())
    sqlalchemy_mod = types.ModuleType("sqlalchemy")
    setattr(sqlalchemy_mod, "desc", lambda x: x)
    entities_mod = types.ModuleType("entities")
    setattr(entities_mod, "SyncRun", DummySyncRun)
    monkeypatch.setitem(sys.modules, "sqlmodel", sqlmodel_mod)
    monkeypatch.setitem(sys.modules, "sqlalchemy", sqlalchemy_mod)
    monkeypatch.setitem(sys.modules, "raindrop_enhancer.domain.entities", entities_mod)
    result = runner.invoke(app, ["--config", str(config_path), "status"])
    if result.exit_code != 0:
        print("\n[DEBUG status] output:\n", result.output)
        print("[DEBUG status] exception:", result.exception)
    assert result.exit_code == 0
    assert "No sync runs found" in result.output or "Last sync" in result.output
