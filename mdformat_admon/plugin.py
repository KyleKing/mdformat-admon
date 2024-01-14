import textwrap
from typing import List, Mapping

from markdown_it import MarkdownIt
from mdformat.renderer import RenderContext, RenderTreeNode
from mdformat.renderer.typing import Render

from .plugins import mkdocs_admon_plugin, python_markdown_admon_plugin


def update_mdit(mdit: MarkdownIt) -> None:
    """Update the parser with supported formats."""
    mdit.use(python_markdown_admon_plugin)
    mdit.use(mkdocs_admon_plugin)


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

    elements: List[str] = []
    for child in node.children:
        rendered = child.render(context)
        if rendered:
            elements.append(rendered)
    separator = "\n\n"

    # Then indent to either 3 or 4 based on the length of the prefix
    #   Possible prefixes: '!!!', '???', '???+', etc.
    indent = " " * (min(len(prefix), 3) + 1)
    content = textwrap.indent(separator.join(elements), indent)

    return title_line + "\n" + content if content else title_line


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
