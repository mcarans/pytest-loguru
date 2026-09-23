# Contributing

The development workflow (setting up the environment with `uv sync`,
installing and running pre-commit, running the tests with `uv run pytest`,
managing dependencies and building with `uv build`) is documented in the
[Development](README.md#development) section of the README.

Please make sure `pre-commit run --all-files` and `uv run pytest` pass
before opening a pull request; CI runs both.
