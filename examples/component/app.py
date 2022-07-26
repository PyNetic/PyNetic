from pynetic import For, Page, MakeReference  # type: ignore
from pynetic.html import Select, Option  # type: ignore

from red_thing import RedThing
from green_thing import GreenThing
from blue_thing import BlueThing

options = [
    {"color": "red", "component": RedThing},
    {"color": "green", "component": GreenThing},
    {"color": "blue", "component": BlueThing},
]

with MakeReference():
    selected = options[1]


app = Page(
    Select(
        For(options, None, lambda option: Option(selected["color"], value=option))
    ),
    title="My Title",
)
