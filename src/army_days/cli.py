import os
import sys
from dataclasses import dataclass
from importlib.metadata import version as pkg_version
from typing import Annotated

import cappa
import yaml
import yaml.scanner
from pydantic_core import ValidationError

from .config import DEFAULT_CONFIG_FILES
from .core import compute_results, generate_default_configuration
from .models import DaysModel
from .output import output_events
from .utils import find_default_config_file


def run(army_days: "ArmyDays") -> None:
    if army_days.generate_sample:
        print(yaml.dump(generate_default_configuration().model_dump(mode="json")))
        return
    config_filename = army_days.filename or find_default_config_file()
    if not config_filename or not os.path.exists(config_filename):
        sys.stderr.write(f"\nConfiguration file: '{config_filename}' not found.\n")
        sys.exit(1)
    with open(config_filename) as file:
        try:
            data = DaysModel(**yaml.load(file.read().replace("\t", " "), yaml.SafeLoader))
        except (yaml.scanner.ScannerError, yaml.error.YAMLError, ValidationError) as ex:
            sys.stderr.write(f"\nError parsing configuration file: {file.name} error: {ex}\n")
            sys.exit(1)
        output_events(
            compute_results(data, show_past_days=army_days.show_past, show_all_future=army_days.show_all)
        )


@cappa.command(name="army-days", help="day countdown program (python edition)", invoke=run)
@dataclass
class ArmyDays:
    filename: Annotated[
        str,
        cappa.Arg(
            short="-f",
            long="--filename",
            help=f"configuration file; by default searches: {' '.join(DEFAULT_CONFIG_FILES)}.",
        ),
    ] = ""
    generate_sample: Annotated[
        bool,
        cappa.Arg(
            short="-g",
            long="--generate-sample",
            help="generate sample data in yaml format (sends to stdout).",
        ),
    ] = False
    show_past: Annotated[
        int | None,
        cappa.Arg(
            short="-p",
            long="--show-past",
            help="show past events within the past N days (use 0 to show all past events).",
        ),
    ] = None
    show_all: Annotated[
        bool,
        cappa.Arg(
            short="-a",
            long="--show-all",
            help="show all future events, bypassing max_days_future config limit.",
        ),
    ] = False


def main() -> None:
    cappa.invoke(ArmyDays, version=pkg_version("army-days"))
