"""Logging caplog test"""
import logging

from loguru import logger

from pytest_loguru.plugin import caplog  # noqa: F401


class TestLogging:
    def test_setup_logging(self, caplog):  # noqa: F811
        with caplog.at_level(logging.ERROR):
            text = "Division by zero!"
            text2 = "shouldn't be logged"

            def divide(a, b):
                return a / b

            try:
                divide(2, 0)
            except ZeroDivisionError:
                logger.exception(text)

            assert text in caplog.text

            logger.info(text2)
            assert text2 not in caplog.text
