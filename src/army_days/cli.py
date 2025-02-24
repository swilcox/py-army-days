import os
import sys
from dataclasses import dataclass
from importlib.metadata import version
from pathlib import Path
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


@dataclass
class Arguments:
    filename: Annotated[
        Path | None,
        cappa.Arg(
            short=True,
            long=True,
            help=f"configuration file; by default searches: {"\n".join(DEFAULT_CONFIG_FILES)}.",
        ),
    ] = None
    generate_sample: Annotated[
        bool,
        cappa.Arg(
            long=True,
            show_default=False,
            help="generate a sample YAML file",
        ),
    ] = False


def _main(args: Arguments):
    if args.generate_sample:
        print(yaml.dump(generate_default_configuration().model_dump(mode="json")))
    else:
        config_filename = args.filename or find_default_config_file()
        if not config_filename or not os.path.exists(config_filename):
            sys.stderr.write(f"\nConfiguration file: '{config_filename}' not found.\n")
            sys.exit(1)
        with open(config_filename) as file:
            try:
                data = DaysModel(**yaml.load(file.read().replace("\t", " "), yaml.SafeLoader))
            except (yaml.scanner.ScannerError, yaml.error.YAMLError, ValidationError) as ex:
                sys.stderr.write(f"\nError parsing configuration file: {file.name} error: {ex}\n")
                sys.exit(1)
            output_events(compute_results(data))


def main():
    _main(cappa.parse(Arguments, backend=cappa.backend, version=version(__package__)))


if __name__ == "__main__":
    main()
