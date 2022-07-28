"""CSS Extensions for easily wrapping an element for styling"""

from enum import Enum

from .html import HTMLElement
from .css import percent, pixels, hsl


class FlexProperties(Enum):
    """Reference Mozilla
    
    Link:
        https://developer.mozilla.org/en-US/docs/Web/CSS/flex
    """
    # Keyword Values
    auto = "auto"
    initial = "initial"
    none = "none"
    
    # Global Values
    inherit = "inherit"
    initial = "initial"
    revert = "revert"
    revert_layer = "revert-layer"
    unset = "unset"
    
    # Other
    min_content = "min-content"


def Center(element: HTMLElement) -> HTMLElement:
    """Centers an Element using traditional means
    
    Got this implementation from StackOverflow answer:
    
    Link:
        https://stackoverflow.com/a/18618259/225020
    """
    return element.style(
        {
            "display": "inline-block",
            "text-align": "center"
            "::before": {
                "content": "",
                "display": "inline-block",
                "height": percent(100),
                "vertical-align": "middle",
                "width": px(0),
            }
        }
    )

def CenterFlex(element: HTMLElement) -> HTMLElement:
    """Centers an Element by wrapping it in a flex box
    
    Got this implementation from the same StackOverflow answer as `Center`:
    
    Link:
        https://stackoverflow.com/a/18618259/225020
    """
    return element.style(
        {
          "align-items": "center",
          "display": "flex",
          "justify-content": "center",
        }
    )

def Flex(
    flex_grow: str | int | FlexValues = FlexProperties.auto,
    flex_shrink: str | int | None = None,
    flex_basis: str | int | None = None,
    /,
) -> Callable[[str | HTMLElement], HTMLElement]:
    """Defines the flex properties of an element.
    If element is type `str` then it wraps it in a `Div`
    
    *For use within an element with a style of flex (or use html_extensions.FlexBox)*
    
    Args:
        flex_grow (str | int | FlexProperties):
        flex_shrink (str | int | None = None):
        flex_basis (str | int | None = None):
    
    Usage:
        ```Python
        FlexBox(
            Flex(FlexValues.min_content)("Hello World")
            ...
        )
        ```
    """
    new_style = {"flex-grow": flex_grow}
    
    if flex_shrink is not None:
        new_style["flex-shrink"] = flex_shrink
    
    if flex_basis is not None:
        new_style["flex-basis"] = flex_basis
    
    def MakeFlex(element: str | HTMLElement) -> HTMLElement:
        if isinstance(element, str):
            element = Div(element)

        return element.style(new_style)
    
    
class Color(Enum):
    """Reference W3C
    
    Link:
        https://www.w3.org/wiki/CSS/Properties/color/keywords
    """
    
    # Basic Colors
    black = hsl(0, 0, 0)
    silver = hsl(192, 192, 192)
    gray = hsl(128, 128, 128)
    white = hsl(255, 255, 255)
    maroon = hsl(128, 0, 0)
    red = hsl(255, 0, 0)
    purple = hsl(128, 0, 128)
    fuchsia = hsl(255, 0, 255)
    green = hsl(0, 128, 0)
    lime = hsl(0, 255, 0)
    olive = hsl(128, 128, 0)
    yellow = hsl(255, 255, 0)
    navy = hsl(0, 0, 128)
    blue = hsl(0, 0, 255)
    teal = hsl(0, 128, 128)
    aqua = hsl(0, 255, 255)
    aliceblue = hsl(240,248,255)
    
    # Extended Colors
    antiquewhite = hsl(250,235,215)
    aqua = hsl(0,255,255)
    aquamarine = hsl(127,255,212)
    azure = hsl(240,255,255)
    beige = hsl(245,245,220)
    bisque = hsl(255,228,196)
    black = hsl(0,0,0)
    blanchedalmond = hsl(255,235,205)
    blue = hsl(0,0,255)
    blueviolet = hsl(138,43,226)
    brown = hsl(165,42,42)
    burlywood = hsl(222,184,135)
    cadetblue = hsl(95,158,160)
    chartreuse = hsl(127,255,0)
    chocolate = hsl(210,105,30)
    coral = hsl(255,127,80)
    cornflowerblue = hsl(100,149,237)
    cornsilk = hsl(255,248,220)
    crimson = hsl(220,20,60)
    cyan = hsl(0,255,255)
    darkblue = hsl(0,0,139)
    darkcyan = hsl(0,139,139)
    darkgoldenrod = hsl(184,134,11)
    darkgray = hsl(169,169,169)
    darkgreen = hsl(0,100,0)
    darkgrey = hsl(169,169,169)
    darkkhaki = hsl(189,183,107)
    darkmagenta = hsl(139,0,139)
    darkolivegreen = hsl(85,107,47)
    darkorange = hsl(255,140,0)
    darkorchid = hsl(153,50,204)
    darkred = hsl(139,0,0)
    darksalmon = hsl(233,150,122)
    darkseagreen = hsl(143,188,143)
    darkslateblue = hsl(72,61,139)
    darkslategray = hsl(47,79,79)
    darkslategrey = hsl(47,79,79)
    darkturquoise = hsl(0,206,209)
    darkviolet = hsl(148,0,211)
    deeppink = hsl(255,20,147)
    deepskyblue = hsl(0,191,255)
    dimgray = hsl(105,105,105)
    dimgrey = hsl(105,105,105)
    dodgerblue = hsl(30,144,255)
    firebrick = hsl(178,34,34)
    floralwhite = hsl(255,250,240)
    forestgreen = hsl(34,139,34)
    fuchsia = hsl(255,0,255)
    gainsboro = hsl(220,220,220)
    ghostwhite = hsl(248,248,255)
    gold = hsl(255,215,0)
    goldenrod = hsl(218,165,32)
    gray = hsl(128,128,128)
    green = hsl(0,128,0)
    greenyellow = hsl(173,255,47)
    grey = hsl(128,128,128)
    honeydew = hsl(240,255,240)
    hotpink = hsl(255,105,180)
    indianred = hsl(205,92,92)
    indigo = hsl(75,0,130)
    ivory = hsl(255,255,240)
    khaki = hsl(240,230,140)
    lavender = hsl(230,230,250)
    lavenderblush = hsl(255,240,245)
    lawngreen = hsl(124,252,0)
    lemonchiffon = hsl(255,250,205)
    lightblue = hsl(173,216,230)
    lightcoral = hsl(240,128,128)
    lightcyan = hsl(224,255,255)
    lightgoldenrodyellow = hsl(250,250,210)
    lightgray = hsl(211,211,211)
    lightgreen = hsl(144,238,144)
    lightgrey = hsl(211,211,211)
    lightpink = hsl(255,182,193)
    lightsalmon = hsl(255,160,122)
    lightseagreen = hsl(32,178,170)
    lightskyblue = hsl(135,206,250)
    lightslategray = hsl(119,136,153)
    lightslategrey = hsl(119,136,153)
    lightsteelblue = hsl(176,196,222)
    lightyellow = hsl(255,255,224)
    lime = hsl(0,255,0)
    limegreen = hsl(50,205,50)
    linen = hsl(250,240,230)
    magenta = hsl(255,0,255)
    maroon = hsl(128,0,0)
    mediumaquamarine = hsl(102,205,170)
    mediumblue = hsl(0,0,205)
    mediumorchid = hsl(186,85,211)
    mediumpurple = hsl(147,112,219)
    mediumseagreen = hsl(60,179,113)
    mediumslateblue = hsl(123,104,238)
    mediumspringgreen = hsl(0,250,154)
    mediumturquoise = hsl(72,209,204)
    mediumvioletred = hsl(199,21,133)
    midnightblue = hsl(25,25,112)
    mintcream = hsl(245,255,250)
    mistyrose = hsl(255,228,225)
    moccasin = hsl(255,228,181)
    navajowhite = hsl(255,222,173)
    navy = hsl(0,0,128)
    oldlace = hsl(253,245,230)
    olive = hsl(128,128,0)
    olivedrab = hsl(107,142,35)
    orange = hsl(255,165,0)
    orangered = hsl(255,69,0)
    orchid = hsl(218,112,214)
    palegoldenrod = hsl(238,232,170)
    palegreen = hsl(152,251,152)
    paleturquoise = hsl(175,238,238)
    palevioletred = hsl(219,112,147)
    papayawhip = hsl(255,239,213)
    peachpuff = hsl(255,218,185)
    peru = hsl(205,133,63)
    pink = hsl(255,192,203)
    plum = hsl(221,160,221)
    powderblue = hsl(176,224,230)
    purple = hsl(128,0,128)
    red = hsl(255,0,0)
    rosybrown = hsl(188,143,143)
    royalblue = hsl(65,105,225)
    saddlebrown = hsl(139,69,19)
    salmon = hsl(250,128,114)
    sandybrown = hsl(244,164,96)
    seagreen = hsl(46,139,87)
    seashell = hsl(255,245,238)
    sienna = hsl(160,82,45)
    silver = hsl(192,192,192)
    skyblue = hsl(135,206,235)
    slateblue = hsl(106,90,205)
    slategray = hsl(112,128,144)
    slategrey = hsl(112,128,144)
    snow = hsl(255,250,250)
    springgreen = hsl(0,255,127)
    steelblue = hsl(70,130,180)
    tan = hsl(210,180,140)
    teal = hsl(0,128,128)
    thistle = hsl(216,191,216)
    tomato = hsl(255,99,71)
    turquoise = hsl(64,224,208)
    violet = hsl(238,130,238)
    wheat = hsl(245,222,179)
    white = hsl(255,255,255)
    whitesmoke = hsl(245,245,245)
    yellow = hsl(255,255,0)
    yellowgreen = hsl(154,205,50

