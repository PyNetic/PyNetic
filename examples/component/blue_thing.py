from this import d
from pynetic.html import strong  # type: ignore
from pynetic.css import CSS  # type: ignore

make_blue = CSS(
    {
        "color": "blue",
    },
)


@pynetic.prerender
def validate_email(e, *references):
    ...


BlueThing = div(strong("Blue thing", style=make_blue), input("Email", on_change=validate_email()))
