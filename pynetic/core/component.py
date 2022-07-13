"""Component definitions for HTML elements"""

from typing import Protocol
from lxml.html import builder as HTMLBuilder
from .html import *


class Component(Protocol):
    """Class protocol for html elements"""

    _tag: str = "html"
    _self_closing: bool = False
    _children: list[str | HTMLElement]
    _id: str
    _styles: {}
    _on_mount: on_mount
    _on_unmount: on_unmount
    _on_render: on_render
    _call_tag: methodcaller(self._tag)

    def bundle(self) -> tuple[str, dict[str, str], str]:
        """_summary_

        Returns:
            tuple[str, dict[str, str], str]: _description_
        """
        rendered_html = HTMLBuilder.HTML()
