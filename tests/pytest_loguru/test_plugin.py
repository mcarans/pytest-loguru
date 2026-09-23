"""Logging caplog tests

The plugin is exercised through ``pytester`` so that the inner test runs
only see ``caplog`` via the ``pytest11`` entry point declared in
``pyproject.toml``. Nothing here imports the fixture directly, so the
suite fails if that entry point is broken or removed.
"""

pytest_plugins = ["pytester"]


def run_inner(pytester, source):
    pytester.makepyfile(source)
    return pytester.runpytest("-p", "no:cacheprovider")


def test_plugin_is_registered_via_entry_point(pytester):
    result = run_inner(
        pytester,
        """
        def test_registered(pytestconfig):
            import pytest_loguru.plugin as plugin

            assert pytestconfig.pluginmanager.is_registered(plugin)
        """,
    )
    result.assert_outcomes(passed=1)


def test_exception_is_captured(pytester):
    result = run_inner(
        pytester,
        """
        import logging

        from loguru import logger


        def test_exception(caplog):
            with caplog.at_level(logging.ERROR):
                try:
                    1 / 0
                except ZeroDivisionError:
                    logger.exception("Division by zero!")

                logger.info("shouldn't be logged")

            assert "Division by zero!" in caplog.text
            assert "shouldn't be logged" not in caplog.text
        """,
    )
    result.assert_outcomes(passed=1)


def test_records_and_messages(pytester):
    result = run_inner(
        pytester,
        """
        import logging

        from loguru import logger


        def test_records(caplog):
            caplog.set_level(logging.DEBUG)
            logger.debug("first")
            logger.warning("second")

            assert caplog.messages == ["first", "second"]
            assert [r.levelno for r in caplog.records] == [
                logging.DEBUG,
                logging.WARNING,
            ]
            assert [r.levelname for r in caplog.records] == [
                "DEBUG",
                "WARNING",
            ]
        """,
    )
    result.assert_outcomes(passed=1)


def test_level_boundaries(pytester):
    result = run_inner(
        pytester,
        """
        import logging

        import pytest
        from loguru import logger


        def emit_all():
            logger.info("below")
            logger.warning("at")
            logger.error("above")


        def test_at_level(caplog):
            with caplog.at_level(logging.WARNING):
                emit_all()
            assert caplog.messages == ["at", "above"]


        def test_set_level(caplog):
            caplog.set_level(logging.WARNING)
            emit_all()
            assert caplog.messages == ["at", "above"]


        @pytest.mark.parametrize(
            "level, expected",
            [
                ("SUCCESS", ["success", "warning"]),
                ("CRITICAL", []),
            ],
        )
        def test_loguru_specific_levels(caplog, level, expected):
            caplog.set_level(logger.level(level).no)
            logger.info("info")
            logger.success("success")
            logger.warning("warning")
            assert caplog.messages == expected
        """,
    )
    result.assert_outcomes(passed=4)


def test_handler_removed_after_teardown(pytester):
    result = run_inner(
        pytester,
        """
        from loguru import logger

        state = {}


        def test_first(caplog):
            state["handler"] = caplog.handler
            state["handlers"] = len(logger._core.handlers)
            logger.info("during first")
            assert caplog.messages == ["during first"]


        def test_second():
            # No caplog here: the sink added for test_first must be gone.
            assert len(logger._core.handlers) == state["handlers"] - 1
            logger.info("after first")
            messages = [r.getMessage() for r in state["handler"].records]
            assert "after first" not in messages
        """,
    )
    result.assert_outcomes(passed=2)
