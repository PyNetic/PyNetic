from pynetic import Reference  # type: ignore
from pynetic.html import SELECT, OPTION  # type: ignore

from red_thing import RedThing
from green_thing import GreenThing
from blue_thing import BlueThing

options = [
    {"color": "red", "component": RedThing},
    {"color": "green", "component": GreenThing},
    {"color": "blue", "component": BlueThing},
]

selected = Reference(options[0])

Component = SELECT(
    *(OPTION(selected["color"], value=option) for option in options),
)
