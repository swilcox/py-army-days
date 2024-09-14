# Army Days (Python version)

## Overview

A command-line program to display the number of days until certain events. This program (hence its name) is also based on the West Point requirement that first year cadets have to be able to recite "the days". Part of that tradition is that if it is past noon at the time, you subtract a day but add "and a butt". As most people aren't concerned about being West Point style, this is an optional feature that can be enabled via a flag. Past events can optionally be displayed via configuration.

## Installing as a CLI Tool

For regular usage, it's useful to install the program using either [pipx](https://github.com/pypa/pipx) or [uv tool](https://docs.astral.sh/uv/guides/tools/#installing-tools).

## Development

This project uses [uv](https://github.com/astral-sh/uv) for dependency management and virtual environment management.

```shell
uv python install
uv sync
```

### Running tests

For basic tests with coverage:

```shell
uv run pytest --cov
```

And for tests with coverage and more verbose output also allowing stdout:

```shell
uv run pytest --cov -v -s
```

### Running the program

```shell
uv run army-days
```
