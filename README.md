[![Build Status](https://github.com/mcarans/pytest-loguru/actions/workflows/run-python-tests.yaml/badge.svg)](https://github.com/mcarans/pytest-loguru/actions/workflows/run-python-tests.yaml)
[![PyPI](https://img.shields.io/pypi/v/pytest-loguru.svg)](https://pypi.python.org/pypi/pytest-loguru)
[![Conda Version](https://img.shields.io/conda/vn/conda-forge/pytest-loguru.svg)](https://anaconda.org/conda-forge/pytest-loguru)
[![Coverage Status](https://coveralls.io/repos/github/mcarans/pytest-loguru/badge.svg?branch=main&ts=1)](https://coveralls.io/github/mcarans/pytest-loguru?branch=main)
[![Ruff](https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/astral-sh/ruff/main/assets/badge/v2.json)](https://github.com/astral-sh/ruff)
[![Downloads](https://img.shields.io/pypi/dm/pytest-loguru.svg)](https://pypistats.org/packages/pytest-loguru)

### pytest-loguru

A pytest plugin to add support for loguru to pytest's caplog fixture.

You can install it from pypi with:

```shell
pip install pytest-loguru
```

and from conda-forge with:

```shell
conda install -c conda-forge pytest-loguru
```

Note that coverage is 100% but the coverage tool is confused by the fixture decorator.

# Development

## Environment

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

With pre-commit, all code is formatted according to [ruff](https://docs.astral.sh/ruff/) guidelines.

To check if your changes pass pre-commit without committing, run:

```shell
pre-commit run --all-files
```

## Packages

[uv](https://github.com/astral-sh/uv) is used for package management. If you've introduced a new package to the source code (i.e. anywhere in `src/`), please add it to the `project.dependencies` section of `pyproject.toml` with any known version constraints.

To add packages required only for testing or development, add them to the `[dependency-groups]` section in `pyproject.toml`.

Any changes to the dependencies will be automatically reflected in `uv.lock` with `pre-commit`, but you can re-generate the file without committing by executing:

```shell
uv lock --upgrade
```

## Project

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
