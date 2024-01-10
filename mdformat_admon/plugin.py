import textwrap
from typing import List, Mapping

from markdown_it import MarkdownIt
from mdformat.renderer import RenderContext, RenderTreeNode
from mdformat.renderer.typing import Render

# TODO: continue to ping mdit_py_plugins owner to release these changes
from ._local.mdit_py_plugins.admon import admon_plugin


def update_mdit(mdit: MarkdownIt) -> None:
    """Update the parser."""
    mdit.use(admon_plugin)


# PLANNED: replace with `str.removeprefix` when dropping Python 3.8
def _removeprefix(_str: str, prefix: str):
    return _str[len(prefix) :] if _str.startswith(prefix) else _str


# PLANNED: replace with `str.removesuffix` when dropping Python 3.8
def _removesuffix(_str: str, suffix: str):
    return _str[: -1 * len(suffix)] if _str.endswith(suffix) else _str


def _render_admon(node: RenderTreeNode, context: RenderContext) -> str:
    """Render a `RenderTreeNode` of type `admonition`.

    Primarily based on:

    - https://github.com/executablebooks/mdformat-footnote/blob/80852fc20cfba7fd0330b9ac7a1a4df983542942/mdformat_footnote/plugin.py#LL24-L40C29

    And based on:

    - https://github.com/hukkin/mdformat-gfm/blob/cf316a121b6cf35cbff7b0ad6e171f287803f8cb/src/mdformat_gfm/plugin.py
    - https://github.com/hukkin/mdformat-toc/blob/42624b6f3468da4f793ec7425da872b030714774/mdformat_toc/plugin.py
    - https://github.com/executablebooks/mdformat-footnote/blob/80852fc20cfba7fd0330b9ac7a1a4df983542942/mdformat_footnote/plugin.py

    """
    prefix = node.markup.split(" ")[0]
    title = node.info.strip()
    title_line = f"{prefix} {title}"

    # If a content tab is within an admonition (https://squidfunk.github.io/mkdocs-material/reference/content-tabs/#usage), then the '=== <...>' element will always be the first or second child
    is_content_tab = False
    for child in [*node.children][:2]:
        with context.indented(0):
            if (child.render(context) or "").startswith("=== "):
                is_content_tab = True
                break

    # FIXME: This feature should have actually been in `mdformat-mkdocs`
    MKDOCS_INDENT = " " * 4

    elements: List[str] = []
    for child in node.children:
        rendered = child.render(context)
        # These code blocks need a custom 4-space indent that .render incorrectly handles (#17)
        if is_content_tab and child.tag == "code":
            rendered = _removesuffix(_removeprefix(rendered, "````"), "````")
            rendered = textwrap.indent(rendered, MKDOCS_INDENT).strip()
            rendered = MKDOCS_INDENT + rendered
        if rendered:
            elements.append(rendered)
    separator = "\n\n"

    # Then indent to either 3 or 4 based on the length of the prefix
    #   Possible prefixes: '!!!', '...', '..', '???', '???+', etc.
    indent = " " * (min(len(prefix), 3) + 1)
    content = textwrap.indent(separator.join(elements), indent)

    tile_separator = "\n\n" if is_content_tab else "\n"
    return title_line + tile_separator + content if content else title_line


def _render_admon_title(node: RenderTreeNode, context: RenderContext) -> str:
    """Skip rendering the title when called from the `node.children`."""
    return ""


# A mapping from syntax tree node type to a function that renders it.
# This can be used to overwrite renderer functions of existing syntax
# or add support for new syntax.
RENDERERS: Mapping[str, Render] = {
    "admonition": _render_admon,
    "admonition_title": _render_admon_title,
}
