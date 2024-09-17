# Army Days (Python version)

## Overview

A command-line program to display the number of days until certain events. This program (hence its name) is also based on the West Point requirement that first year cadets have to be able to recite "the days". Part of that tradition is that if it is past noon at the time, you subtract a day but add "and a butt". As most people aren't concerned about being West Point style, this is an optional feature that can be enabled via a flag. Past events can optionally be displayed via configuration.

## Installing as a CLI Tool

For regular usage, it's useful to install the program using either [pipx](https://github.com/pypa/pipx) or [uv tool](https://docs.astral.sh/uv/guides/tools/#installing-tools) or just run directly with [uvx](https://docs.astral.sh/uv/guides/tools/).

## Usage

### Example output

```text
❯ army-days
 Days
89 days until Army beats the hell out of Navy.
100 days until Christmas.
```

### Help

Once installed, you can run the command with the `--help` option.

```shell
❯ army-days --help
Usage: army-days [OPTIONS]

Options:
  --version              Show the version and exit.
  -f, --filename PATH    configuration file; by default searches: ./days.yaml
                         ./days.json ~/days.yaml ~/days.json ~/.days.yaml
                         ~/.days.json.
  -g, --generate-sample  generate sample data in yaml format (sends to
                         stdout).
  --help                 Show this message and exit.
```

### Configuration / Input file

By default (as the help indicates), army-days looks for a configuration file in this order:

* days.yaml or days.json in the current working directory.
* days.yaml or days.json in the user's home directory.
* .days.yaml or .days.json in the user's home directory.

You can override the name of the configuration file via the `-f` / `--filename` option.

### Sample Configuration File Generation

To generate a sample configuration file:

```shell
army-days -g > days.yaml
```

The sample file will look similar to this:

```yaml
config:
  show_completed: false
  use_army_butt_days: false
entries:
- date: '2025-09-15T00:00:00'
  title: your one year anniversary of using army-days
```

> [!NOTE]
> You do *not* need a time as part of the date field. So for simplicity, you can just leave off the time portion. In fact, if you use a timezone aware timestamp, you might end up with some unusual behavior as army-days first converts it to a local timestamp.

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
