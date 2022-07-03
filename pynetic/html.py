"""HTML tag elements"""

from typing import Dict, List, Sequence, Union, cast

__all__ = (
    "base",
    "head",
    "link",
    "meta",
    "style",
    "title",
    "body",
    "address",
    "article",
    "aside",
    "footer",
    "header",
    "h1",
    "h2",
    "h3",
    "h4",
    "h5",
    "h6",
    "main",
    "nav",
    "section",
    "hr",
    "blockquote",
    "dd",
    "div",
    "dl",
    "dt",
    "figcaption",
    "figure",
    "li",
    "ol",
    "p",
    "pre",
    "ul",
    "br",
    "a",
    "abbr",
    "b",
    "bdi",
    "bdo",
    "cite",
    "code",
    "data",
    "em",
    "i",
    "kbd",
    "mark",
    "q",
    "rp",
    "rt",
    "ruby",
    "s",
    "samp",
    "small",
    "span",
    "strong",
    "sub",
    "sup",
    "time",
    "u",
    "var",
    "wbr",
    "area",
    "img",
    "audio",
    "map",
    "track",
    "video",
    "portal",
    "source",
    "iframe",
    "embed",
    "object",
    "param",
    "picture",
)

default = object()


class HTMLElement:
    """_summary_"""

    def __init__(self, tag: str, requires_closing_tag: bool = True) -> None:
        self.__tag: str = tag
        self.__requires_closing_tag: bool = requires_closing_tag
        self.__is_base_element: bool = True

        self.__reset()

    def __call__(
        self,
        *children: Union[str, "HTMLElement"],
        classes: Union[str, Sequence[str], None] = None,
        id: Union[str, None] = None,
        **params: Union[str, Sequence[str]],
    ) -> "HTMLElement":
        if self.__is_base_element:
            self = HTMLElement(self.__tag, self.__requires_closing_tag)
            self.__is_base_element = False

        self.__params = params
        self.__children = children
        if classes is not None:
            self.__classes = [classes] if isinstance(classes, str) else list(classes)

        if id is not None:
            self.__id = id

        self.__finalized = True
        self.__is_base_element = False

        return self

    async def _render_as_html(self, is_repr=False) -> str:
        """Renders the element and sub-elements for display

        Returns:
            str: The rendered output of the element
        """
        if not self.__finalized:
            unrendered_html = f"<Uninitialized {self.__tag} Element>"
            self.__reset()
            return unrendered_html

        rendered_html = self._pre_render_html()

        for child in self.__children:
            if isinstance(child, str):
                rendered_html += child

            elif isinstance(child, HTMLElement):
                child_html = await child._render_as_html()
                print(child_html)
                rendered_html += child_html

        if self.__requires_closing_tag:
            rendered_html += f"</{self.__tag}>"

        self.__reset()

        return rendered_html

    def _pre_render_html(self, is_repr: bool = False):
        closing_tag = f"</{self.__tag}>"

        pre_rendered_html = f"<{self.__tag}"

        if self.__classes:
            pre_rendered_html += f' class="{" ".join(self.__classes)}"'

        if self.__id != "":
            pre_rendered_html += f' id="{self.__id}"'

        if self.__params != {}:
            formatted_params = {
                arg: param if isinstance(param, str) else " ".join(param)
                for arg, param in self.__params.items()
            }
            pre_rendered_html += f" {', '.join(formatted_params)}>"

        pre_rendered_html += ">"

        if is_repr:
            pre_rendered_html += "..." + closing_tag
            self.__reset()

        return pre_rendered_html

    def __reset(self) -> None:
        self.__finalized: bool = False
        self.__classes: List[str] = []
        self.__id: str = ""
        self.__params: Dict[str, Union[str, Sequence[str]]] = {}

    def __getattr__(self, __name: str) -> "HTMLElement":
        if __name.startswith("_") or __name in self.__dict__:
            raise AttributeError("Class names cannot begin with an underscore")

        if self.__is_base_element:
            self = HTMLElement(self.__tag, self.__requires_closing_tag)
            self.__is_base_element = False

        self.__classes.append(__name)
        return self

    def __getitem__(self, __name: str) -> "HTMLElement":
        if self.__is_base_element:
            self = HTMLElement(self.__tag, self.__requires_closing_tag)
            self.__is_base_element = False

        self.__id = __name
        return cast("HTMLElement", self)

    def __repr__(self) -> str:
        repr_html = self._pre_render_html(True)

        return repr_html


"""
---------------------------------------------------------------------------------------
    HTML Elements
---------------------------------------------------------------------------------------
"""

# Top-level tags
base = HTMLElement("base")
head = HTMLElement("head")
link = HTMLElement("link")
meta = HTMLElement("meta")
style = HTMLElement("style")
title = HTMLElement("title")

# Content sectioning
body = HTMLElement("body")
address = HTMLElement("address")
article = HTMLElement("article")
aside = HTMLElement("aside")
footer = HTMLElement("footer")
header = HTMLElement("header")
h1 = HTMLElement("h1")
h2 = HTMLElement("h2")
h3 = HTMLElement("h3")
h4 = HTMLElement("h4")
h5 = HTMLElement("h5")
h6 = HTMLElement("h6")
main = HTMLElement("main")
nav = HTMLElement("nav")
section = HTMLElement("section")

# Text content
hr = HTMLElement("hr", requires_closing_tag=False)

blockquote = HTMLElement("blockquote")
dd = HTMLElement("dd")
div = HTMLElement("div")
dl = HTMLElement("dl")
dt = HTMLElement("dt")
figcaption = HTMLElement("figcaption")
figure = HTMLElement("figure")
li = HTMLElement("li")
ol = HTMLElement("ol")
p = HTMLElement("p")
pre = HTMLElement("pre")
ul = HTMLElement("ul")

# Inline text semantics
br = HTMLElement("br", requires_closing_tag=False)

a = HTMLElement("a")
abbr = HTMLElement("abbr")
b = HTMLElement("b")
bdi = HTMLElement("bdi")
bdo = HTMLElement("bdo")
cite = HTMLElement("cite")
code = HTMLElement("code")
data = HTMLElement("data")
em = HTMLElement("em")
i = HTMLElement("i")
kbd = HTMLElement("kbd")
mark = HTMLElement("mark")
q = HTMLElement("q")
rp = HTMLElement("rp")
rt = HTMLElement("rt")
ruby = HTMLElement("ruby")
s = HTMLElement("s")
samp = HTMLElement("samp")
small = HTMLElement("small")
span = HTMLElement("span")
strong = HTMLElement("strong")
sub = HTMLElement("sub")
sup = HTMLElement("sup")
time = HTMLElement("time")
u = HTMLElement("u")
var = HTMLElement("var")
wbr = HTMLElement("wbr")

# Image and video
area = HTMLElement("area", requires_closing_tag=False)
img = HTMLElement("img", requires_closing_tag=False)

audio = HTMLElement("audio")
map = HTMLElement("map")
track = HTMLElement("track")
video = HTMLElement("video")

# Embedded content
portal = HTMLElement("portal", requires_closing_tag=False)
source = HTMLElement("source", requires_closing_tag=False)
iframe = HTMLElement("iframe", requires_closing_tag=False)

embed = HTMLElement("embed")
object = HTMLElement("object")
param = HTMLElement("param")
picture = HTMLElement("picture")
