from pynetic.html import strong  # type: ignore
from pynetic.css import CSS  # type: ignore

make_green = CSS(color="green")

GreenThing = strong("green thing", style=make_green)
