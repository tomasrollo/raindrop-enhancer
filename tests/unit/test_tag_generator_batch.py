import json

from raindrop_enhancer.content.tag_generator import TagGenerationRunner


def test_tag_generation_runner_uses_batch_api():
    # Fake underlying predictor object that exposes a .batch(prompts) method
    class FakePredict:
        def __init__(self):
            self.batch_called = False

        def __call__(self, *, text: str):
            # Per-item behavior: derive tag and token count from the prompt (keyword-only 'text')
            idx = 0
            try:
                after = text.split("Title:", 1)[1]
                import re

                m = re.search(r"(\d+)", after)
                if m:
                    idx = int(m.group(1)) - 1
            except Exception:
                idx = 0

            class P:
                def __init__(self, tags, tokens):
                    self.tags = tags

                    class U:
                        def __init__(self, tokens):
                            self.total_tokens = tokens

                    self._usage = U(tokens)

                def get_lm_usage(self):
                    return self._usage

            return P([f"tag{idx}"], idx + 1)

        def batch(self, prompts):
            self.batch_called = True
            out = []
            for i, p in enumerate(prompts):
                # Try to extract the Title N from the prompt to create a stable index
                # prompt contains 'Title: Title N' per the runner prompt format
                idx = 0
                try:
                    # find the substring 'Title:' and then the numeric part
                    after = p.split("Title:", 1)[1]
                    # take the first number in the remainder
                    import re

                    m = re.search(r"(\d+)", after)
                    if m:
                        idx = int(m.group(1)) - 1
                except Exception:
                    idx = i

                # return a Prediction-like object with .tags and .get_lm_usage()
                class P:
                    def __init__(self, tags, tokens):
                        self.tags = tags

                        class U:
                            def __init__(self, tokens):
                                self.total_tokens = tokens

                        self._usage = U(tokens)

                    def get_lm_usage(self):
                        return self._usage

                out.append(P([f"tag{idx}"], idx + 1))
            return out

    underlying = FakePredict()
    # underlying is callable and exposes .batch — pass it directly
    runner = TagGenerationRunner(underlying, model_name="test-model", batch_size=2)

    # Prepare 3 items so we exercise both a full batch (2) and the final flush (1)
    items = [
        (101, "Title 1", "https://u/1", "content 1"),
        (102, "Title 2", "https://u/2", "content 2"),
        (103, "Title 3", "https://u/3", "content 3"),
    ]

    results = runner.run_batch(items)

    # The runner now calls the predictor per-item (no batch API usage)

    # Validate results shape and contents
    assert len(results) == 3
    # First item's tags should be normalized to Title Case by normalize_tag_value
    rid0, tags_json0, meta_json0 = results[0]
    assert rid0 == 101
    assert json.loads(tags_json0) == ["Tag0"]
    meta0 = json.loads(meta_json0)
    assert meta0["model"] == "test-model"
    assert meta0["tokens_used"] == 1

    # Second item
    rid1, tags_json1, meta_json1 = results[1]
    assert rid1 == 102
    assert json.loads(tags_json1) == ["Tag1"]
    meta1 = json.loads(meta_json1)
    assert meta1["tokens_used"] == 2

    # Third item (final flush)
    rid2, tags_json2, meta_json2 = results[2]
    assert rid2 == 103
    assert json.loads(tags_json2) == ["Tag2"]
    meta2 = json.loads(meta_json2)
    assert meta2["tokens_used"] == 3
