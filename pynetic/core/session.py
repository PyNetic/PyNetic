"""Represents a client session"""

from .reference import Reference


class Session:
    """Represents a client session"""

    references: dict[str, Reference] = {}
