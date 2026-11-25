# pytest-loguru

A pytest plugin to add support for [loguru](https://github.com/Delgan/loguru) to pytest's `caplog` fixture. It hooks loguru into pytest's standard `LogCaptureFixture` so that `caplog` captures loguru log records just like standard Python `logging` records.

## Development

The development workflow (setting up the environment with `uv sync`, running
pre-commit, managing dependencies, building, linting, running the tests and
checking that coverage stays at 100%) is documented in the
[Development](README.md#development) section of the README. Follow it from
there rather than keeping a copy here.
