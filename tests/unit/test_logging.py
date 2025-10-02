import json

from raindrop_enhancer.util.logging import structured


def test_structured_emits_json(caplog):
    caplog.set_level("INFO")
    structured("test.event", a=1, b="x")
    # caplog records at least one message
    assert caplog.records
    found = False
    for rec in caplog.records:
        msg = rec.getMessage()
        try:
            payload = json.loads(msg)
            if payload.get("message") == "test.event":
                found = True
                assert payload.get("a") == 1
                assert payload.get("b") == "x"
        except Exception:
            continue
    assert found, "structured log not found in caplog"
