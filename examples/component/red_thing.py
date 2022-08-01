from pynetic.css import CSS  # type: ignore
from pynetic.html import strong  # type: ignore

make_red = CSS(
    {
        "color": "red",
    },
)

RedThing = strong("red thing", style=make_red)
