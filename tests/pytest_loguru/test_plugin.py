"""Logging caplog test"""
import logging

from loguru import logger

from pytest_loguru.plugin import caplog


class TestLogging:
    def test_setup_logging(self, caplog):
        with caplog.at_level(logging.ERROR):
            text = "Division by zero!"

            def divide(a, b):
                return a / b

            try:
                divide(2, 0)
            except ZeroDivisionError:
                logger.exception(text)

            assert text in caplog.text
