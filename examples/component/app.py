from pynetic import Reference, Component, Page, MakeReference  # type: ignore
from pynetic.html import SELECT, OPTION  # type: ignore

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
    SELECT(
        *(OPTION(selected["color"], value=option) for option in options),
    ),
    title="My Title",
)
