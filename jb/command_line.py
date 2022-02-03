
import os
import json

import typer
from rich import print_json
from rich.console import Console

from jb import utils

console = Console()
app = typer.Typer()


def _validate_dependencies_data(data):
    if not data or not isinstance(data, dict):
        raise ValueError("Invalid dependency file")

    dependencies = data.get('dependencies')
    if not dependencies or not isinstance(dependencies, dict):
        raise ValueError("Invalid dependency file")


def _get_dependencies_array(dependencies):
    return map(lambda dependency: f'{dependency[0].strip()}=={dependency[1].strip()}', dependencies.items())


def _install_dependency(dependency, hide_output=False):
    command = f'pip install {dependency}'
    if hide_output == True:
        command += ' > /dev/null 2>&1'

    return os.system(command)


@app.command(short_help="install python dependencies")
def install(dependency_file_path: str, hide_output: bool = typer.Option(False, help='Whether to show pip output or not')):
    try:
        raw_dependencies = utils.read(dependency_file_path)
        parsed_dependencies = json.loads(raw_dependencies)
        _validate_dependencies_data(parsed_dependencies)

        dependency_array = _get_dependencies_array(parsed_dependencies['dependencies'])

        dependencies_output = map(lambda dependency: (dependency, _install_dependency(dependency, hide_output)), dependency_array)
        failed_dependencies = list(filter(lambda dependency_output: dependency_output[1] != 0, dependencies_output))

        if len(failed_dependencies) > 0:
            dependencies_names = list(map(lambda dependency: dependency[0], failed_dependencies))
            output = '\n'.join(dependencies_names)
            console.print(f"\n[i][bold red]Dependencies failed to install:[/bold red][/i] \n{output}")
            return ""

        console.print("[green]Success")

    except json.JSONDecodeError as err:
        console.print(f"[bold red]Invalid dependency file, should be a valid JSON file[/bold red]")

    except ValueError as err:
        console.print(f"[bold red]{err}[/bold red]")

    except Exception as err:
        console.print(f"[bold red]{err}[/bold red]")


@app.command(short_help="print python dependencies")
def validate(dependency_file_path):
    try:
        raw_dependencies = utils.read(dependency_file_path)
        parsed_dependencies = json.loads(raw_dependencies)
        _validate_dependencies_data(parsed_dependencies)

        print_json(json.dumps(parsed_dependencies))

    except json.JSONDecodeError as err:
        console.print(f"[bold red]Invalid dependency file, should be a valid JSON file[/bold red]")

    except Exception as err:
        console.print(f"[bold red]{err}[/bold red]")


def main():
    app()
