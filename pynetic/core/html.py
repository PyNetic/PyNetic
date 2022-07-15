"""pynetic HTML builtins

HTML tags act as components and as page elements depending upon use and location. TBC...
"""

from __future__ import annotations
from typing import Any, Callable, Iterable, Type, TypeAlias

from lxml.html import builder as HTMLBuilder

from css import Style  # type: ignore

__code: TypeAlias = Any


class HTMLElement:
    """The Base HTML element in which all other elements derive from

    Args:
        children (str | HTMLElement, optional):
            Sub-elements to render within this element
        classes (str | Iterable[str], optional):
            Custom HTML classes to use in rendered HTML
        id (str): Custom HTML id to use in rendered HTML
    """

    _tag: str = "html"
    _self_closing: bool = False

    def __init__(
        self,
        *__children: str | HTMLElement,
        classes: str | Iterable[str] = "",
        children: Iterable[str | HTMLElement] = "",
        id: str | None = None,
        styles: Iterable[Style],
        **kwargs: str | Callable,
    ) -> None:
        self._id = id
        self._content: str = ""
        self._children = list(children)
        self._named_children: dict[str, str] = {}
        self._events: dict[str, Callable] = {}
        self.elements: list[HTMLElement] = []
        self._styles = {}

        for name, value in kwargs.items():
            if isinstance(value, str):
                self._named_children[name] = value

            if isinstance(value, Callable):
                self._events[name] = value

        for child in __children:
            if isinstance(child, str) and self._content == "":
                self._content = child

            if isinstance(child, (HTMLElement, Style)):
                self._children.append(child)

        self._classes = (
            [classes.replace("_", "-")]
            if isinstance(classes, str)
            else [_class.replace("_", "-") for _class in classes]
        )

    def style(self, **kwargs: str) -> HTMLElement:
        """Apply CSS styling to the current element

        Returns:
            HTMLElement: _description_
        """
        self._styles.update(kwargs)
        return self

    def render(self) -> tuple[HTMLElement, CSSClass, __code]:  # type: ignore
        """_summary_
        Args:
            minified (bool):
                If True, minifies elements when rendering, otherwise returns human readable syntax.
        Returns:
            tuple[str, dict[str, str], str]: tuple of rendered (html, css, js)
        """
        rendered_html = getattr(HTMLBuilder, self._tag.upper())(
            self,
            *(
                child.render()  # type: ignore
                for child in self._children
                if isinstance(child, (HTMLElement, Style))
            ),
        )


def define_element(tag: str, docstring: str, is_self_closing: bool = False) -> Type[HTMLElement]:
    class TaggedHTMLElement(HTMLElement):
        _tag: str = tag
        _self_closing = not is_self_closing

        def __repr__(self):
            return f"<html {tag.lower()} element>"

    TaggedHTMLElement.__doc__ = docstring

    return TaggedHTMLElement


"""
---------------------------------------------------------------------------------------
    HTML Elements

    Source: https://developer.mozilla.org/en-US/docs/Web/HTML/Element
---------------------------------------------------------------------------------------
"""

# Document metadata
base = define_element(
    "base",
    "The base URL to use for all relative URLs in a document. "
    "There can be only one <base> element in a document.",
)
HEAD = define_element(
    "head",
    "Machine-readable information (metadata) about the document, "
    "like its title, scripts, and style sheets.",
)
LINK = define_element(
    "link",
    "Specifies relationships between the current document and an external resource. "
    "This element is most commonly used to link to CSS, "
    'but is also used to establish site icons (both "favicon" style icons and icons '
    "for the home screen and apps on mobile devices) among other things.",
)
META = define_element(
    "meta",
    "Represents Metadata that cannot be represented by other HTML meta-related elements, "
    "like base, link, script, style or title.",
)
STYLE = define_element(
    "style",
    "Contains style information for a document, or part of a document. It contains CSS, "
    "which is applied to the contents of the document containing the <style> element.",
)
TITLE = define_element(
    "title",
    "Defines the document's title that is shown in a Browser's title bar or a page's tab. "
    "It only contains text; tags within the element are ignored.",
)
BODY = define_element(
    "body",
    "Represents the content of an HTML document. "
    "There can be only one <body> element in a document.",
)
ADDRESS = define_element(
    "address",
    "Indicates that the enclosed HTML provides contact information for a person or people, "
    "or for an organization.",
)
ARTICLE = define_element(
    "article",
    "Represents a self-contained composition in a document, page, application, or site, "
    "which is intended to be independently distributable or reusable (e.g., in syndication). "
    "Examples include: a forum post, a magazine or newspaper article, or a blog entry, "
    "a product card, a user-submitted comment, an interactive widget or gadget, "
    "or any other independent item of content.",
)
ASIDE = define_element(
    "aside",
    "Represents a portion of a document whose content is only indirectly related to the "
    "document's main content. Asides are frequently presented as sidebars or call-out boxes.",
)
FOOTER = define_element(
    "footer",
    "Represents a footer for its nearest ancestor sectioning content or sectioning root element. "
    "A <footer> typically contains information about the author of the section, "
    "copyright data or links to related documents.",
)
HEADER = define_element(
    "header",
    "Represents introductory content, typically a group of introductory or navigational aids. "
    "It may contain some heading elements but also a logo, a search form, an author name, "
    "and other elements.",
)
H1 = define_element("h1", "Section heading 1.")
h2 = define_element("h2", "Section heading 2.")
h3 = define_element("h3", "Section heading 3.")
h4 = define_element("h4", "Section heading 4.")
h5 = define_element("h5", "Section heading 5.")
h6 = define_element("h6", "Section heading 6.")
main = define_element(
    "main",
    "Represents the dominant content of the body of a document. "
    "The main content area consists of content that is directly related to or expands upon "
    "the central topic of a document, or the central functionality of an application.",
)
NAV = define_element(
    "nav",
    "Represents a section of a page whose purpose is to provide navigation links, "
    "either within the current document or to other documents. "
    "Common examples of navigation sections are menus, tables of contents, and indexes.",
)
SECTION = define_element(
    "section",
    "Represents a generic standalone section of a document, which doesn't have a more "
    "specific semantic element to represent it. "
    "Sections should always have a heading, with very few exceptions.",
)
BLOCKQUOTE = define_element(
    "blockquote",
    "Indicates that the enclosed text is an extended quotation. "
    "Usually, this is rendered visually by indentation (see Notes for how to change it). "
    "A URL for the source of the quotation may be given using the cite attribute, "
    "while a text representation of the source can be given using the cite element.",
)
DD = define_element(
    "dd",
    "Provides the description, definition, or value for the preceding term (dt) "
    "in a description list (dl).",
)
DIV = define_element(
    "div",
    "Is the generic container for flow content. It has no effect on the content or layout "
    "until styled in some way using CSS (e.g. styling is directly applied to it, "
    "or some kind of layout model like Flexbox is applied to its parent element).",
)
DL = define_element(
    "dl",
    "Represents a description list. The element encloses a list of groups of "
    "terms (specified using the dt element) and descriptions (provided by dd elements). "
    "Common uses for this element are to implement a glossary or to display metadata "
    "(a list of key-value pairs).",
)
DT = define_element(
    "dt",
    "Specifies a term in a description or definition list, and as such must be used "
    "inside a dl element. It is usually followed by a dd element; however, multiple "
    "<dt> elements in a row indicate several terms that are all defined by the "
    "immediate next dd element.",
)
FIGCAPTION = define_element(
    "figcaption",
    "Represents a caption or legend describing the rest of "
    "the contents of its parent figure element.",
)
FIGURE = define_element(
    "figure",
    "Represents self-contained content, potentially with an optional caption, "
    "which is specified using the figcaption element. The figure, its caption, "
    "and its contents are referenced as a single unit.",
)
HR = define_element(
    "hr",
    "Represents a thematic break between paragraph-level elements: for example, "
    "a change of scene in a story, or a shift of topic within a section.",
)
LI = define_element(
    "li",
    "Is used to represent an item in a list. It must be contained in a parent element: "
    "an ordered list (ol), an unordered list (ul), or a menu (menu). "
    "In menus and unordered lists, list items are usually displayed using bullet points. "
    "In ordered lists, they are usually displayed with an ascending counter on the left, "
    "such as a number or letter.",
)
MENU = define_element(
    "menu",
    "Is described in the HTML specification as a semantic alternative to ul, "
    "but treated by browsers (and exposed through the accessibility tree) as "
    "no different than ul. It represents an unordered list of items "
    "(which are represented by li elements).",
)
OL = define_element(
    "ol", "Represents an ordered list of items — typically rendered as a numbered list."
)
p = define_element(
    "p",
    "Represents a paragraph. Paragraphs are usually represented in visual media as "
    "blocks of text separated from adjacent blocks by blank lines and/or first-line indentation, "
    "but HTML paragraphs can be any structural grouping of related content, "
    "such as images or form fields.",
)
PRE = define_element(
    "pre",
    "Represents preformatted text which is to be presented exactly as written in the HTML file. "
    "The text is typically rendered using a non-proportional, or monospaced, font. "
    "Whitespace inside this element is displayed as written.",
)
UL = define_element(
    "ul", "Represents an unordered list of items, typically rendered as a bulleted list."
)
a = define_element(
    "a",
    "(or anchor element), with its href attribute, creates a hyperlink to web pages, files, "
    "email addresses, locations in the same page, or anything else a URL can address.",
)
ABBR = define_element(
    "abbr",
    "Represents an abbreviation or acronym; the optional title attribute can "
    "provide an expansion or description for the abbreviation. "
    "If present, title must contain this full description and nothing else.",
)
B = define_element(
    "b",
    "Is used to draw the reader's attention to the element's contents, "
    "which are not otherwise granted special importance. "
    "This was formerly known as the Boldface element, and most browsers still "
    "draw the text in boldface. However, you should not use <b> for styling text; "
    "instead, you should use the CSS font-weight property to create boldface text, "
    "or the strong element to indicate that text is of special importance.",
)
BDI = define_element(
    "bdi",
    "Tells the browser's bidirectional algorithm to treat the text it contains in "
    "isolation from its surrounding text. It's particularly useful when a website dynamically "
    "inserts some text and doesn't know the directionality of the text being inserted.",
)
BDO = define_element(
    "bdo",
    "Overrides the current directionality of text, "
    "so that the text within is rendered in a different direction.",
)
BR = define_element(
    "br",
    "Produces a line break in text (carriage-return). It is useful for writing a poem or "
    "an address, where the division of lines is significant.",
)
CITE = define_element(
    "cite",
    "Is used to describe a reference to a cited creative work, and must include "
    "the title of that work. The reference may be in an abbreviated form according to "
    "context-appropriate conventions related to citation metadata.",
)
CODE = define_element(
    "code",
    "Displays its contents styled in a fashion intended to indicate that the "
    "text is a short fragment of computer code. By default, "
    "the content text is displayed using the user agent default monospace font.",
)
DATA = define_element(
    "data",
    "Links a given piece of content with a machine-readable translation. "
    "If the content is time- or date-related, the time element must be used.",
)
DFN = define_element(
    "dfn",
    "Is used to indicate the term being defined within the context of a "
    "definition phrase or sentence. The p element, the dt/dd pairing, "
    "or the section element which is the nearest ancestor of the <dfn> is considered "
    "to be the definition of the term.",
)
EM = define_element(
    "em",
    "Marks text that has stress emphasis. The <em> element can be nested, "
    "with each level of nesting indicating a greater degree of emphasis.",
)
I = define_element(
    "i",
    "Represents a range of text that is set off from the normal text for some reason, "
    "such as idiomatic text, technical terms, taxonomical designations, among others. "
    "Historically, these have been presented using italicized type, which is the original "
    "source of the <i> naming of this element.",
)
KBD = define_element(
    "kbd",
    "Represents a span of inline text denoting textual user input from a keyboard, voice input, "
    "or any other text entry device. By convention, the user agent defaults to rendering the "
    "contents of a <kbd> element using its default monospace font, although this is not mandated "
    "by the HTML standard.",
)
MARK = define_element(
    "mark",
    "Represents text which is marked or highlighted for reference or notation purposes, "
    "due to the marked passage's relevance or importance in the enclosing context.",
)
Q = define_element(
    "q",
    "Indicates that the enclosed text is a short inline quotation. "
    "Most modern browsers implement this by surrounding the text in quotation marks. "
    "This element is intended for short quotations that don't require paragraph breaks; "
    "for long quotations use the blockquote element.",
)
RP = define_element(
    "rp",
    "Is used to provide fall-back parentheses for browsers that do not support display of "
    "ruby annotations using the ruby element. One <rp> element should enclose each of the opening "
    "and closing parentheses that wrap the rt element that contains the annotation's text.",
)
RT = define_element(
    "rt",
    "Specifies the ruby text component of a ruby annotation, which is used to provide "
    "pronunciation, translation, or transliteration information for East Asian typography. "
    "The <rt> element must always be contained within a ruby element.",
)
RUBY = define_element(
    "ruby",
    "Represents small annotations that are rendered above, below, or next to base text, "
    "usually used for showing the pronunciation of East Asian characters. "
    "It can also be used for annotating other kinds of text, but this usage is less common.",
)
S = define_element(
    "s",
    "Renders text with a strikethrough, or a line through it. Use the <s> element to represent "
    "things that are no longer relevant or no longer accurate. "
    "However, <s> is not appropriate when indicating document edits; for that, "
    "use the del and ins elements, as appropriate.",
)
SAMP = define_element(
    "samp",
    "Is used to enclose inline text which represents sample (or quoted) output from a "
    "computer program. Its contents are typically rendered using the browser's default monospaced "
    "font (such as Courier or Lucida Console).",
)
SMALL = define_element(
    "small",
    "Represents side-comments and small print, like copyright and legal text, "
    "independent of its styled presentation. By default, it renders text within it "
    "one font-size smaller, such as from small to x-small.",
)
SPAN = define_element(
    "span",
    "Is a generic inline container for phrasing content, which does not inherently "
    "represent anything. It can be used to group elements for styling purposes "
    "(using the class or id attributes), or because they share attribute values, such as lang. "
    "It should be used only when no other semantic element is appropriate. <span> "
    "is very much like a div element, but div is a block-level element whereas a <span> "
    "is an inline element.",
)
STRONG = define_element(
    "strong",
    "Indicates that its contents have strong importance, seriousness, or urgency. "
    "Browsers typically render the contents in bold type.",
)
SUB = define_element(
    "sub",
    "Specifies inline text which should be displayed as subscript for solely "
    "typographical reasons. Subscripts are typically rendered with a lowered "
    "baseline using smaller text.",
)
SUP = define_element(
    "sup",
    "Specifies inline text which is to be displayed as superscript for solely typographical "
    "reasons. Superscripts are usually rendered with a raised baseline using smaller text.",
)
TIME = define_element(
    "time",
    "Represents a specific period in time. It may include the datetime attribute to translate "
    "dates into machine-readable format, allowing for better search engine results or custom "
    "features such as reminders.",
)
U = define_element(
    "u",
    "Represents a span of inline text which should be rendered in a way that indicates that "
    "it has a non-textual annotation. This is rendered by default as a simple solid underline, "
    "but may be altered using CSS.",
)
VAR = define_element(
    "var",
    "Represents the name of a variable in a mathematical expression or a programming context. "
    "It's typically presented using an italicized version of the current typeface, "
    "although that behavior is browser-dependent.",
)
WBR = define_element(
    "wbr",
    "Represents a word break opportunity—a position within text where the browser may "
    "optionally break a line, though its line-breaking rules would not otherwise create a "
    "break at that location.",
)
AREA = define_element(
    "area",
    "Defines an area inside an image map that has predefined clickable areas. "
    "An image map allows geometric areas on an image to be associated with Hyperlink.",
)
AUDIO = define_element(
    "audio",
    "Is used to embed sound content in documents. It may contain one or more audio sources, "
    "represented using the src attribute or the source element: the browser will choose the most "
    "suitable one. It can also be the destination for streamed media, using a MediaStream.",
)
IMG = define_element("img", "Embeds an image into the document.")
map_ = define_element(
    "map", "Is used with area elements to define an image map (a clickable link area)."
)
track = define_element(
    "track",
    "Is used as a child of the media elements, audio and video. "
    "It lets you specify timed text tracks (or time-based data), "
    "for example to automatically handle subtitles. "
    "The tracks are formatted in WebVTT format (.vtt files) — Web Video Text Tracks.",
)
VIDEO = define_element(
    "video",
    "Embeds a media player which supports video playback into the document. "
    "You can use <video> for audio content as well, but the audio element may provide a "
    "more appropriate user experience.",
)
EMBED = define_element(
    "embed",
    "Embeds external content at the specified point in the document. This content is "
    "provided by an external application or other source of interactive content "
    "such as a browser plug-in.",
)
IFRAME = define_element(
    "iframe",
    "Represents a nested browsing context, embedding another HTML page into the current one.",
)
OBJECT_ = define_element(
    "object",
    "Represents an external resource, which can be treated as an image, "
    "a nested browsing context, or a resource to be handled by a plugin.",
)
PICTURE = define_element(
    "picture",
    "Contains zero or more source elements and one img element to offer alternative "
    "versions of an image for different display/device scenarios.",
)
PORTAL = define_element(
    "portal",
    "Enables the embedding of another HTML page into the current one for the purposes of "
    "allowing smoother navigation into new pages.",
)
SOURCE = define_element(
    "source",
    "Specifies multiple media resources for the picture, the audio element, or the video element. "
    "It is an empty element, meaning that it has no content and does not have a closing tag. "
    "It is commonly used to offer the same media content in multiple file formats in order to "
    "provide compatibility with a broad range of browsers given their differing support for image "
    "file formats and media file formats.",
)
SVG = define_element(
    "svg",
    "The svg element is a container that defines a new coordinate system and viewport. "
    "It is used as the outermost element of SVG documents, but it can also be used to embed an "
    "SVG fragment inside an SVG or HTML document.",
)
MATH = define_element(
    "math",
    "The top-level element in MathML is <math>. Every valid MathML instance must be "
    "wrapped in <math> tags. In addition you must not nest a second <math> element in another, "
    "but you can have an arbitrary number of other child elements in it.",
)
CANVAS = define_element(
    "canvas",
    "Use the HTML <canvas> element with either the canvas scripting API or the WebGL API to "
    "draw graphics and animations.",
)
NOSCRIPT = define_element(
    "noscript",
    "Defines a section of HTML to be inserted if a script type on the page is unsupported or "
    "if scripting is currently turned off in the browser.",
)
SCRIPT = define_element(
    "script",
    "Is used to embed executable code or data; this is typically used to embed or refer to "
    "JavaScript code. The <script> element can also be used with other languages, such as WebGL's "
    "GLSL shader programming language and JSON.",
)
DEL_ = define_element(
    "del",
    "Represents a range of text that has been deleted from a document. "
    'This can be used when rendering "track changes" or source code diff information, for example. '
    "The ins element can be used for the opposite purpose: to indicate text that has been added "
    "to the document.",
)
INS = define_element(
    "ins",
    "Represents a range of text that has been added to a document. "
    "You can use the del element to similarly represent a range of text that has been "
    "deleted from the document.",
)
CAPTION = define_element("caption", "Specifies the caption (or title) of a table.")
col = define_element(
    "col",
    "Defines a column within a table and is used for defining common semantics on all common cells. "
    "It is generally found within a colgroup element.",
)
COLGROUP = define_element("colgroup", "Defines a group of columns within a table.")
table = define_element(
    "table",
    "Represents tabular data — that is, information presented in a two-dimensional table comprised "
    "of rows and columns of cells containing data.",
)
TBODY = define_element(
    "tbody",
    "Encapsulates a set of table rows (tr elements), indicating that they comprise the body "
    "of the table (table).",
)
TD = define_element(
    "td", "Defines a cell of a table that contains data. It participates in the table model."
)
tfoot = define_element("tfoot", "Defines a set of rows summarizing the columns of the table.")
th = define_element(
    "th",
    "Defines a cell as header of a group of table cells. The exact nature of this group is "
    "defined by the scope and headers attributes.",
)
THEAD = define_element(
    "thead", "Defines a set of rows defining the head of the columns of the table."
)
tr = define_element(
    "tr",
    "Defines a row of cells in a table. The row's cells can then be established using a mix of td "
    "(data cell) and th (header cell) elements.",
)
BUTTON = define_element(
    "button",
    "Is an interactive element activated by a user with a mouse, keyboard, finger, voice command, "
    "or other assistive technology. Once activated, it then performs a programmable action, "
    "such as submitting a form or opening a dialog.",
)
DATALIST = define_element(
    "datalist",
    "Contains a set of option elements that represent the permissible or recommended options "
    "available to choose from within other controls.",
)
FIELDSET = define_element(
    "fieldset", "Is used to group several controls as well as labels (label) within a web form."
)
form = define_element(
    "form",
    "Represents a document section containing interactive controls for submitting information.",
)
INPUT_ = define_element(
    "input",
    "Is used to create interactive controls for web-based forms in order to accept data from the "
    "user; a wide variety of types of input data and control widgets are available, depending on "
    "the device and user agent. The <input> element is one of the most powerful and complex in "
    "all of HTML due to the sheer number of combinations of input types and attributes.",
)
LABEL = define_element("label", "Represents a caption for an item in a user interface.")
legend = define_element("legend", "Represents a caption for the content of its parent fieldset.")
meter = define_element(
    "meter", "Represents either a scalar value within a known range or a fractional value."
)
optgroup = define_element("optgroup", "Creates a grouping of options within a select element.")
option = define_element(
    "option",
    "Is used to define an item contained in a select, an optgroup, or a datalist element. "
    "As such, <option> can represent menu items in popups and other lists of items in an "
    "HTML document.",
)
OUTPUT = define_element(
    "output",
    "Is a container element into which a site or app can inject the results of a calculation "
    "or the outcome of a user action.",
)
PROGRESS = define_element(
    "progress",
    "Displays an indicator showing the completion progress of a task, typically displayed "
    "as a progress bar.",
)
SELECT = define_element("select", "Represents a control that provides a menu of options.")
textarea = define_element(
    "textarea",
    "Represents a multi-line plain-text editing control, useful when you want to allow "
    "users to enter a sizeable amount of free-form text, for example a comment on a "
    "review or feedback form.",
)
DETAILS = define_element(
    "details",
    "Creates a disclosure widget in which information is visible only when the widget is "
    'toggled into an "open" state. A summary or label must be provided using the summary element.',
)
DIALOG = define_element(
    "dialog",
    "Represents a dialog box or other interactive component, such as a dismissible alert, "
    "inspector, or subwindow.",
)
SUMMARY = define_element(
    "summary",
    "Specifies a summary, caption, or legend for a details element's disclosure box. "
    "Clicking the <summary> element toggles the state of the parent <details> element "
    "open and closed.",
)
SLOT = define_element(
    "slot",
    "Part of the Web Components technology suite—is a placeholder inside a web component "
    "that you can fill with your own markup, which lets you create separate DOM trees and "
    "present them together.",
)
TEMPLATE = define_element(
    "template",
    "Is a mechanism for holding HTML that is not to be rendered immediately when a page is "
    "loaded but may be instantiated subsequently during runtime using JavaScript.",
)
