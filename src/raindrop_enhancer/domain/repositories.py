"""Repository stubs for SQLite interaction."""


class Repo:
    def __init__(self, path):
        self.path = path

    def setup(self):
        pass

    def upsert_link(self, link):
        pass
