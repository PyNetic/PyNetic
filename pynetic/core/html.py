"""pynetic HTML builtins

HTML tags act as components and as page elements depending upon use and location. TBC...
"""

from __future__ import annotations

from collections.abc import Callable, Iterable
from typing import Any, Type, TypeAlias

from css import Style  # type: ignore
from lxml.html import builder as HTMLBuilder

__code: TypeAlias = Any


class HTMLElement:
    """The Base HTML element in which all other elements derive from

    Args:
        children (str | HTMLElement, optional):
            Sub-elements to render within this element
        classes (str | Iterable[str], optional):
            Custom HTML classes to use in rendered HTML
        id (str): Custom HTML id to use in rendered HTML
    """

    _tag: str = "html"
    _self_closing: bool = False

    def __init__(
        self,
        *__children: str | HTMLElement,
        classes: str | Iterable[str] = "",
        children: Iterable[str | HTMLElement] = "",
        id: str | None = None,
        styles: Iterable[Style],
        **kwargs: str | Callable,
    ) -> None:
        self._id = id
        self._content: str = ""
        self._children = list(children)
        self._named_children: dict[str, str] = {}
        self._events: dict[str, Callable] = {}
        self.elements: list[HTMLElement] = []
        self._styles = {}

        for name, value in kwargs.items():
            if isinstance(value, str):
                self._named_children[name] = value

            if isinstance(value, Callable):
                self._events[name] = value

        for child in __children:
            if isinstance(child, str) and self._content == "":
                self._content = child

            if isinstance(child, (HTMLElement, Style)):
                self._children.append(child)

        self._classes = (
            [classes.replace("_", "-")]
            if isinstance(classes, str)
            else [_class.replace("_", "-") for _class in classes]
        )

    def style(self, **kwargs: str) -> HTMLElement:
        """Apply CSS styling to the current element

        Returns:
            HTMLElement: _description_
        """
        self._styles.update(kwargs)
        return self

    def render(self, tree: HTMLBuilder) -> tuple[HTMLElement, CSSClass, __code]:  # type: ignore
        """_summary_
        Args:
            minified (bool):
                If True, minifies elements when rendering, otherwise returns human readable syntax.
        Returns:
            tuple[str, dict[str, str], str]: tuple of rendered (html, css, js)
        """
        rendered_html = getattr(HTMLBuilder, self._tag.upper())(
            self,
            *(
                child.render()  # type: ignore
                for child in self._children
                if isinstance(child, (HTMLElement, Style))
            ),
        )


def define_element(tag: str, docstring: str, is_self_closing: bool = False) -> type[HTMLElement]:
    class TaggedHTMLElement(HTMLElement):
        _tag: str = tag
        _self_closing = not is_self_closing

        def __repr__(self):
            return f"<html {tag.lower()} element>"

    TaggedHTMLElement.__doc__ = docstring

    return TaggedHTMLElement
