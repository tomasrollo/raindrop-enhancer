"""Raindrop API client stubs."""

import requests


class RaindropClient:
    def __init__(self, token: str):
        self.token = token
        self.base = "https://api.raindrop.io/rest/v1"
        self.session = requests.Session()
        self.session.headers.update({"Authorization": f"Bearer {token}"})

    def list_collections(self):
        return {"result": True, "items": []}

    def list_raindrops(self, collection_id: int, **params):
        return {"result": True, "items": []}
