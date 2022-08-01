"""HTML Extensions for easily creating elements

These are abstractions from traditional HTML elements

With inspiration from Flutter
"""

from enum import Enum

from .html import Div, HTMLElement

# An alias for `html.Div` for readability purposes
Container = Div


class FlexDirection(Enum):
    """Reference Mozilla

    Link:
        https://developer.mozilla.org/en-US/docs/Web/CSS/flex-direction
    """

    # Row
    row = "row"
    vertical = "row"
    top_down = "row"

    # Row Reverse
    row_reverse = "row-reverse"
    vertial_reverse = "row-reverse"
    bottom_up = "row-reverse"

    # Column
    column = "column"
    horizontal = "column"
    left_to_right = "column"

    # Column Reverse
    column_reverse = "column_reverse"
    horizontal_reverse = "column_reverse"
    right_to_left = "column_reverse"


def FlexBox(
    direction: FlexDirection = FlexDirection.row,
    /,
) -> Callable[HTMLElement, HTMLElement]:
    """Returns a `Div` with a display of flex

    Args:
        direction (FlexDirection): Direction of the resulting Element

    Usage:
        TODO
    """

    def MakeFlexBox(*elements: str | HTMLElement) -> HTMLElement:
        return Div(
            *elements,
            style={"display": "flex"},
        )
