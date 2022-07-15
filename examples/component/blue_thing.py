from pynetic.html import strong  # type: ignore
from pynetic.css import CSS  # type: ignore

make_blue = CSS(
    {
        "color": "blue",
    },
)

BlueThing = strong("Blue thing", style=make_blue)
