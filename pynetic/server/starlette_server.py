""""""

from collections.abc import AsyncGenerator
from importlib import import_module, reload
from os import path
from pathlib import Path
from sys import modules
from types import FunctionType, ModuleType
from typing import cast

from ..core import Application, Reference
from ..core.html import HTMLElement

current_working_directory = Path("./routes/")


class Transpiler:
    def __init__(self) -> None:
        self.files: dict[str, tuple[float, Page]] = {}
        pass

    async def sync_routes(self) -> None:
        """Loops through routes folder returning all python filepaths returning their relative link

        Automatically reloads the route on file change, add, or remove. And removes route on file deletion.
        """
        for file in current_working_directory.glob("**.py"):
            last_modified_date = file.stat().st_mtime
            route_name = f"/{file.relative_to('.').stem}"

            if route_name not in self.files:
                import_module(filename := file.name)
                for local in (
                    module := cast(ModuleType, eval(route_name))
                ).items():  # nosec: eval is safe here
                    if isinstance(local, Page):
                        self.files[route_name] = last_modified_date, local
                        break
                else:
                    raise Warning(
                        f"{filename} Does not contain a Page element. This module was not loaded."
                    )
            else:
                module = cast(ModuleType, eval(route_name))  # nosec: eval is safe here

            if self.files[route_name] != last_modified_date:
                reload(module)
