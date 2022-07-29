"""Functions used in CLI"""

from pathlib import Path

import click
import pip


def setup_poetry(path: Path, name: str, description: str, version: str):
    try:
        import poetry
    except ImportError:
        if not click.prompt(
            "Poetry is not installed. Do you wish to install poetry?",
            type=bool,
            confirmation_prompt="This will install Poetry using pip do you wish to continue?",
        ):
            pip.main(["install", "poetry"])
    finally:
        del poetry

        from clikit.io.console_io import ConsoleIO
        from poetry.config.config import Config
        from poetry.config.config_source import ConfigSource
        from poetry.factory import Factory
        from poetry.installation.installer import Installer
        from poetry.utils.env import EnvManager

    poetry = Factory().create_poetry(path)

    config_source = ConfigSource()
    config_source.add_property("name", name)
    config_source.add_property("description", description)
    config_source.add_property("version", version)

    installer = Installer(
        io := ConsoleIO(),
        EnvManager(poetry).create_venv(io),
        poetry.package,
        poetry.locker,
        poetry.pool,
        Config().set_config_source(config_source),
    )
    installer.update(True).run()
