# pytest-loguru

A pytest plugin to add support for [loguru](https://github.com/Delgan/loguru) to pytest's `caplog` fixture. It hooks loguru into pytest's standard `LogCaptureFixture` so that `caplog` captures loguru log records just like standard Python `logging` records.

## Development

### Environment

Development is currently done using Python 3.12. The environment can be created with:

```shell
uv sync
```

This creates a `.venv` folder with the versions specified in the project's `uv.lock` file.

### Pre-commit

pre-commit will be installed when syncing uv. It is run every time you make a git commit if you call it like this:

```shell
pre-commit install
```

With pre-commit, all code is formatted according to [ruff](https://docs.astral.sh/ruff/) guidelines, and the `uv.lock` file is kept up-to-date.

To check if your changes pass pre-commit without committing, run:

```shell
pre-commit run --all-files
```

### Packages

[uv](https://github.com/astral-sh/uv) is used for package management. If you've introduced a new package to the source code (i.e. anywhere in `src/`), please add it to the `project.dependencies` section of `pyproject.toml` with any known version constraints.

To add packages required only for testing or development, add them to the `[dependency-groups]` section in `pyproject.toml`.

Any changes to the dependencies will be automatically reflected in `uv.lock` with `pre-commit`, but you can re-generate the file without committing by executing:

```shell
uv lock --upgrade
```

### Project

[uv](https://github.com/astral-sh/uv) is used for project management. The project can be built using:

```shell
uv build
```

Linting and syntax checking can be run with:

```shell
uv run ruff format --check
uv run ruff check
```

Tests can be executed using:

```shell
uv run pytest
```
