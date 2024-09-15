import sys

import click
import yaml
import yaml.scanner
from pydantic_core import ValidationError

from .core import compute_results
from .models import DaysModel
from .output import output_events


@click.command()
@click.version_option()
@click.option("-f", "--file", type=click.File("r"), default="days.yaml")
def main(file):
    with file:
        try:
            data = DaysModel(**yaml.load(file, yaml.SafeLoader))
        except (yaml.scanner.ScannerError, yaml.error.YAMLError, ValidationError) as ex:
            print(f"Error parsing configuration file: {file.name} error: {ex}")
            sys.exit(1)
        output_events(compute_results(data))
