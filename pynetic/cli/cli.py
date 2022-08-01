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

    cookiecutter("https://github.com/pynetic/PyNetic-Templates/tree/main/base-application")

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
