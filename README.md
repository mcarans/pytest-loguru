[![Build Status](https://github.com/mcarans/pytest-loguru/workflows/build/badge.svg)](https://github.com/mcarans/pytest-loguru/actions?query=workflow%3Abuild)
[![PyPI](https://img.shields.io/pypi/v/pytest-loguru.svg)](https://pypi.python.org/pypi/pytest-loguru)
[![Conda Version](https://img.shields.io/conda/vn/conda-forge/pytest-loguru.svg)](https://anaconda.org/conda-forge/pytest-loguru)
[![Coverage Status](https://codecov.io/gh/mcarans/pytest-loguru/branch/main/graph/badge.svg?token=JpWZc5js4y)](https://codecov.io/gh/mcarans/pytest-loguru)
[![Ruff](https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/astral-sh/ruff/main/assets/badge/v2.json)](https://github.com/astral-sh/ruff)

### pytest-loguru

A pytest plugin to add support for loguru to pytest's caplog fixture.

You can install it from pypi with:
```
pip install pytest-loguru
```
and from conda-forge with:
```
conda install -c conda-forge pytest-loguru
```

Note that coverage is 100% but the coverage tool is confused by the fixture decorator.
