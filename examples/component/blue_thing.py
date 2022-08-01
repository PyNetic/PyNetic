from pynetic.css import CSS  # type: ignore
from pynetic.html import Component, Div, Input, Strong  # type: ignore

make_blue = CSS(
    {
        "color": "blue",
    },
)

BlueThing = Component(
    Div(
        Strong("Blue thing", style=make_blue),
    )
)
