import logging  # pragma: no cover
from typing import Iterator  # pragma: no cover

import pytest  # pragma: no cover
from loguru import logger  # pragma: no cover


def _add_sink(handler: logging.Handler) -> int:
    """Add ``handler`` as a loguru sink that honours the handler's level.

    The level is read on every record rather than once, because pytest
    changes it after the sink is added (``caplog.set_level``, and the
    logging plugin setting each handler's level at the start of a phase).

    Args:
        handler (logging.Handler): standard logging handler to feed

    Returns:
        int: the loguru handler id, for ``logger.remove``
    """

    def filter_(record):
        return record["level"].no >= handler.level

    return logger.add(handler, level=0, format="{message}", filter=filter_)


@pytest.fixture
def caplog(
    caplog: pytest.LogCaptureFixture,
) -> Iterator[pytest.LogCaptureFixture]:
    """Emitting logs from loguru's logger.log means that they will not show up in
    caplog which only works with Python's standard logging. This adds the same
    LogCaptureHandler being used by caplog to hook into loguru.

    Args:
        caplog (LogCaptureFixture): caplog fixture

    Yields:
        LogCaptureFixture
    """
    handler_id = _add_sink(caplog.handler)
    yield caplog
    logger.remove(handler_id)


@pytest.fixture(autouse=True)
def _loguru_report_and_live_logs(
    request: pytest.FixtureRequest,
) -> Iterator[None]:
    """Send loguru records to pytest's report and live-log handlers.

    This applies to every test, whether or not it requests ``caplog``, so
    loguru messages appear under "Captured log call" when a test fails and
    in the live log when ``log_cli`` is enabled, just like standard
    ``logging`` records.

    Args:
        request (FixtureRequest): request for the running test

    Yields:
        None
    """
    plugin = request.config.pluginmanager.getplugin("logging-plugin")
    if plugin is None:  # disabled with -p no:logging
        yield
        return
    handler_ids = [
        _add_sink(handler)
        for handler in (plugin.report_handler, plugin.log_cli_handler)
    ]
    yield
    for handler_id in handler_ids:
        logger.remove(handler_id)
