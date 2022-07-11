""""""

from importlib import import_module, reload
from os import path
from sys import modules
from pathlib import Path
from typing import Generator

from ..core import Session, Reference
from ..core.html import HTMLElement

from starlette.applications import Starlette
from starlette.responses import JSONResponse
from starlette.routing import Route
import uvicorn

current_working_directory = Path("./routes/")


class Application(Starlette):
    
    def __init__(self) -> None:
        self.files: dict[str, float] = {}
        pass
    
    async def get_routes() -> Generator[str, None, None]:
        """Loops through routes folder returning all python filepaths returning their relative link

        Automatically reloads the route on file change, add, or remove. And removes route on file deletion.
        """
        last_modified_date = file.stat().st_mtime()
        for file in .glob("**.py"):
            if (route_name := f"/{file.relative_to(".").stem}") not in files:
                import_module(name)
                self.files[route_name] = last_modified_date
            else:
                if self.files[name] != last_modified_date:
                    reload(route_name)
            
            
        yield 
