"""Contract tests against the Raindrop OpenAPI specification."""

from __future__ import annotations

from functools import lru_cache
from pathlib import Path

import pytest
import yaml


SPEC_PATH = (
    Path(__file__).resolve().parents[2]
    / "specs"
    / "001-build-an-application"
    / "contracts"
    / "raindrop_api.yaml"
)


@pytest.fixture(scope="module")
def raindrop_spec() -> dict:
    return load_spec()


@lru_cache
def load_spec() -> dict:
    with SPEC_PATH.open("r", encoding="utf-8") as handle:
        return yaml.safe_load(handle)


def test_openapi_root_metadata(raindrop_spec: dict) -> None:
    assert raindrop_spec["openapi"].startswith("3."), (
        "OpenAPI document must declare version 3.x"
    )
    info = raindrop_spec["info"]
    assert info["title"] == "Raindrop Enhancer Integration"
    assert "rate limit" in info["description"].lower()
    servers = raindrop_spec.get("servers", [])
    assert any(
        server.get("url") == "https://api.raindrop.io/rest/v1" for server in servers
    ), "Production server base URL must be documented"


def test_collections_endpoint_contract(raindrop_spec: dict) -> None:
    paths = raindrop_spec["paths"]
    assert "/collections" in paths, "Collections endpoint must be documented"
    op = paths["/collections"]["get"]
    assert op["operationId"] == "listCollections"
    success = op["responses"]["200"]
    content = success["content"]["application/json"]["schema"]
    assert content["$ref"].endswith("#/components/schemas/CollectionList")
    _assert_rate_limit_headers(success)


def test_raindrops_endpoint_contract(raindrop_spec: dict) -> None:
    paths = raindrop_spec["paths"]
    assert "/raindrops/{collectionId}" in paths
    op = paths["/raindrops/{collectionId}"]["get"]
    params = {param["name"]: param for param in op.get("parameters", [])}
    assert "collectionId" in params and params["collectionId"]["in"] == "path"
    assert params["perpage"]["schema"]["maximum"] == 100
    success = op["responses"]["200"]
    content = success["content"]["application/json"]["schema"]
    assert content["$ref"].endswith("#/components/schemas/RaindropList")
    _assert_rate_limit_headers(success)


def test_components_define_expected_schemas(raindrop_spec: dict) -> None:
    components = raindrop_spec["components"]
    schemas = components["schemas"]
    raindrop = schemas["Raindrop"]
    assert set(raindrop["required"]) >= {
        "id",
        "title",
        "link",
        "tags",
        "created",
        "lastUpdate",
    }
    tag_items = raindrop["properties"]["tags"]
    assert tag_items["type"] == "array"
    collection = schemas["Collection"]
    assert collection["properties"]["lastUpdate"]["format"] == "date-time"


def test_security_scheme_enforces_bearer_auth(raindrop_spec: dict) -> None:
    security = raindrop_spec["components"]["securitySchemes"]["bearerAuth"]
    assert security["type"] == "http"
    assert security["scheme"] == "bearer"


def _assert_rate_limit_headers(response_section: dict) -> None:
    headers = response_section.get("headers", {})
    assert set(headers) >= {
        "X-RateLimit-Limit",
        "X-RateLimit-Remaining",
        "X-RateLimit-Reset",
    }, "All rate limit headers must be documented on success responses"
