""""""

from __future__ import annotations

from reference import Reference

class Session:
    """Represents client session
    Holds all references (variables) and handles all events.
    """
    def __init__(self) -> None:
        self.references: list[Reference] = []
        