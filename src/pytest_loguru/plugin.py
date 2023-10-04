from typing import Iterator  # pragma: no cover

import pytest  # pragma: no cover
from _pytest.logging import LogCaptureFixture  # pragma: no cover
from loguru import logger  # pragma: no cover


@pytest.fixture
def caplog(caplog: LogCaptureFixture) -> Iterator[LogCaptureFixture]:
    """Emitting logs from loguru's logger.log means that they will not show up in
    caplog which only works with Python's standard logging. This adds the same
    LogCaptureHandler being used by caplog to hook into loguru.

    Args:
        caplog (LogCaptureFixture): caplog fixture

    Yields:
        LogCaptureFixture
    """

    def filter_(record):
        return record["level"].no >= caplog.handler.level

    handler_id = logger.add(
        caplog.handler, level=0, format="{message}", filter=filter_
    )
    yield caplog
    logger.remove(handler_id)
