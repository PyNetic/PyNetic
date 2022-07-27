"""Represents a client session"""

from pathlib import Path
from importlib import import_module

from .component import Component
from .reference import Reference


class Application:
    """Represents a client session"""

    references: dict[str, Reference] = {}

    def __init__(self) -> None:
        self._components = set()

    def build(self) -> str | None:
        routes_folder = Path().absolute().joinpath("routes")

        for route_path in routes_folder.glob("*.py"):
            route = import_module(str(route_path))
            component = next(
                component
                for component in reversed(route.__dict__.values())
                if isinstance(component, Component)
            )
            self._components.add(component)
