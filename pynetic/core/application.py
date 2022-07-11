"""pynetic's Application class where the session is managed"""

from reference import Reference


class Application:
    references: dict[str, Reference] = {}
