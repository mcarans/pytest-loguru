import pytest  # pragma: no cover
from _pytest.fixtures import SubRequest  # pragma: no cover
from loguru import logger  # pragma: no cover


@pytest.fixture
def caplog(request: SubRequest) -> None:
    """Emitting logs from loguru's logger.log means that they will not show up in
    caplog which only works with Python's standard logging. This adds the same
    LogCaptureHandler being used by caplog to hook into loguru.

    Args:
        request (SubRequest): SubRequest fixture to look up fixture

    Returns:
        None
    """

    orig_caplog = request.getfixturevalue("caplog")

    def filter_(record):
        return record["level"].no >= orig_caplog.handler.level


    handler_id = logger.add(
        orig_caplog.handler, level=0, format="{message}", filter=filter_
    )
    yield orig_caplog
    logger.remove(handler_id)
