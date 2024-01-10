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

    children = [*node.children]

    # If a content tab (an admonition subtype: https://squidfunk.github.io/mkdocs-material/reference/content-tabs/#usage), then the '=== <...>' element will always be the second item
    child_2 = children[1] if len(children) > 1 else None
    with context.indented(0):
        is_content_tab = child_2 and (child_2.render(context) or "").startswith("=== ")

    # Render the children to strings
    elements: List[str] = []
    for child in children:
        rendered = child.render(context)
        # These code blocks need a custom 4-space indent that .render incorrectly handles (#17)
        if is_content_tab and child.tag == "code":
            rendered = textwrap.indent(child.content, " " * 4).rstrip()
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
