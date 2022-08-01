from pynetic.css import CSS  # type: ignore
from pynetic.html import strong  # type: ignore

make_green = CSS(color="green")

GreenThing = strong("green thing", style=make_green)
