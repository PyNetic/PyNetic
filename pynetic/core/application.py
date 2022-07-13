"""Represents a client session"""

from .reference import Reference


class Application:
    """Represents a client session"""

    references: dict[str, Reference] = {}

    def __init__(self) -> None:
        pass
