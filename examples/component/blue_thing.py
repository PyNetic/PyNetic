pynetic.html import Div, Strong, Input  # type: ignore
from pynetic.css import CSS  # type: ignore

make_blue = CSS(
    {
        "color": "blue",
    },
)

BlueThing = Div(Strong("Blue thing", style=make_blue))
