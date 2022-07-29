"""CLI interface for PyNetic

Used as the starting point for a PyNetic application and for development and build purposes.

Commands:
    
    init:
        Initializes a template using command prompts
        
        Options:
            url: Initializes a template using cookie cutter library
        
        Usage:
            > pynetic init
            ...
    
    run:
        Runs either development server or build steps for production use
        
        Options:
            dev: Runs dev server. Hot reloads modules on file save.
            build: Builds Application for production
            
        Usage:
            > pynetic run dev
            ---- Running on http://localhost:8000 ----
            
            Or
            
            > pynetic run build
            ...
"""

from pathlib import Path

import click
from cookiecutter.main import cookiecutter
from cookiecutter.replay import get_file_name as get_cookiecutter_name

from ..core.application import Application
from .utils import setup_poetry

cwd = Path().cwd()


@click.group()
def pynetic() -> None:
    pass


@pynetic.command()
@click.argument("url", nargs=1, required=False)
def init(url: str | None) -> None:
    if url is not None:
        # TODO: Need to notify if file already exists
        return cookiecutter(url, skip_if_file_exists=True)

    name = click.prompt("Please give a name for the application", type=str, default="pynetic-app")
    description = click.prompt(
        "Please provide a description for the application", type=str, default=""
    )
    version = click.prompt("Please give a version for the application", type=str, default="0.1.0")
    version_control = click.prompt(
        "What version control library would you like to use?",
        type=click.Choice(["poetry"]),
        default="poetry",
    )

    if (project_path := cwd / name).exists():
        return click.echo(f'"{name}" already exists in this directory')

    cookiecutter()

    if version_control == "poetry":
        setup_poetry(project_path, name, description, version)

    # TODO: Work on other version controls


@click.group()
def run() -> None:
    click.echo("Please choose what you would like to run.")
    click.echo("-----------------------------------------")
    click.echo("Options:")
    click.echo("\tdev: Runs development server. Hot reloads modules on file save.")
    click.echo("\tbuild: Builds Application for production")


@run.command()
def dev() -> None:
    pass


@run.command()
def build() -> None:
    pass


if __name__ == "__main__":
    pynetic()
