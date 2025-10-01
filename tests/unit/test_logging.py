import logging
from raindrop_enhancer.util.logging import setup_logging, inc_metric, get_metrics


def test_structured_logging_and_metrics(caplog):
    logger = setup_logging(json_logs=False)
    with caplog.at_level(logging.INFO):
        logger.info("test message")
    assert any("test message" in m for m in caplog.text.splitlines())
    inc_metric("foo")
    inc_metric("foo", 2)
    metrics = get_metrics()
    assert metrics["foo"] == 3
