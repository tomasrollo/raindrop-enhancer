"""Raindrop API client stubs."""

import requests


class RaindropClient:
    def __init__(self, token: str):
        self.token = token
        self.base = "https://api.raindrop.io/rest/v1"
        self.session = requests.Session()
        self.session.headers.update({"Authorization": f"Bearer {token}"})

    def list_collections(self):
        """Return a minimal collections response (placeholder).

        A later task will implement real HTTP pagination and header capture.
        Keeping a simple dict here so contract tests can assert the response
        shape during early integration.
        """
        return {"result": True, "items": []}

    def list_raindrops(self, collection_id: int, **params):
        return {"result": True, "items": []}
