from blue_thing import BlueThing
from green_thing import GreenThing
from red_thing import RedThing

from pynetic import For, MakeReference, Page  # type: ignore
from pynetic.html import Option, Select  # type: ignore

options = [
    {"color": "red", "component": RedThing},
    {"color": "green", "component": GreenThing},
    {"color": "blue", "component": BlueThing},
]

with MakeReference():
    selected = options[1]


app = Page(
    Select(For(options, None, lambda option: Option(selected["color"], value=option))),
    title="My Title",
)
