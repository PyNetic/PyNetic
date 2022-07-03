from pynetic.html import div, br, area

import pytest


@pytest.mark.asyncio
async def test_uninitialized_element():
    assert await div._render_as_html() == "<Uninitialized div Element>"
    assert await div.foo._render_as_html() == "<Uninitialized div Element>"


@pytest.mark.asyncio
async def test_element_content():
    assert await div("Some content")._render_as_html() == "<div>Some content</div>"


@pytest.mark.asyncio
async def test_element_class():
    assert await div.foo()._render_as_html() == '<div class="foo"></div>'


@pytest.mark.asyncio
async def test_element_multiple_class():
    assert await div.foo.bar()._render_as_html() == '<div class="foo bar"></div>'


@pytest.mark.asyncio
async def test_element_id():
    assert await div["baz"]()._render_as_html() == '<div id="baz"></div>'


@pytest.fixture
def non_closing_element():
    return br()


@pytest.mark.asyncio
async def test_non_closing_element(non_closing_element):
    assert await non_closing_element._render_as_html() == "<br>"


@pytest.mark.asyncio
async def test_child_elements():
    assert await div(div())._render_as_html() == "<div><div></div></div>"
