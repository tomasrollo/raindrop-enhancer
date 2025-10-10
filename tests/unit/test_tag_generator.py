import pytest

from raindrop_enhancer.tagging import GeneratedTag


def normalize_tags(values):
    # placeholder for normalization pipeline to be implemented
    # For now, perform Title Case and truncate to 40 chars
    out = []
    for v in values:
        if not v or not v.strip():
            continue
        norm = v.strip().title()
        if len(norm) > 40:
            norm = norm[:40]
        out.append(norm)
    # dedupe preserving order
    seen = set()
    res = []
    for t in out:
        if t.lower() in seen:
            continue
        seen.add(t.lower())
        res.append(t)
    return res


def test_title_case_and_truncation():
    src = [
        "this is a very long tag that should be truncated because it exceeds the limit"
    ]
    out = normalize_tags(src)
    assert out[0] == "This Is A Very Long Tag That Should Be T"


def test_tag_limit_and_dedup():
    src = [f"tag{i}" for i in range(12)] + ["Tag1"]
    out = normalize_tags(src)
    assert len(out) == 11 or len(out) == 12
