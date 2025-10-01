"""Repository implementation for SQLite using SQLModel."""

from typing import Optional
from pathlib import Path

from sqlmodel import create_engine, SQLModel, Session

from raindrop_enhancer.domain.entities import SQLModel as _SQLModel  # type: ignore


class Repo:
    def __init__(self, path: str):
        self.path = path
        self.db_url = f"sqlite:///{path}"
        self.engine = None

    def setup(self):
        """Create the SQLite database file, enable WAL, and create tables."""
        db_path = Path(self.path)
        db_path.parent.mkdir(parents=True, exist_ok=True)

        # Create engine and enable WAL mode
        self.engine = create_engine(self.db_url, connect_args={"check_same_thread": False})
        with self.engine.connect() as conn:
            # Use driver-level exec to run PRAGMA without SQLModel/SQLAlchemy typing issues
            conn.exec_driver_sql("PRAGMA journal_mode=WAL;")
            conn.commit()

        SQLModel.metadata.create_all(self.engine)

    def upsert_link(self, link):
        if self.engine is None:
            raise RuntimeError("Repo not setup")
        with Session(self.engine) as session:
            session.add(link)
            session.commit()
