"""Auto-loaded plugin for mdformat."""

from __future__ import annotations

import textwrap
from typing import Mapping

from markdown_it import MarkdownIt
from mdformat.renderer import RenderContext, RenderTreeNode
from mdformat.renderer.typing import Render

from .plugins import python_markdown_admon_plugin


def update_mdit(mdit: MarkdownIt) -> None:
    """Update the parser with supported formats."""
    mdit.use(python_markdown_admon_plugin)


def _render_admon(node: RenderTreeNode, context: RenderContext) -> str:
    """Render a `RenderTreeNode` of type `admonition`."""
    prefix = node.markup.split(" ")[0]
    title = node.info.strip()
    title_line = f"{prefix} {title}"

    elements: list[str] = []
    for child in node.children:
        rendered = child.render(context)
        if rendered:
            elements.append(rendered)
    separator = "\n\n"

    # Then indent to either 3 or 4 based on the length of the prefix
    #   For reStructuredText, '..' should be indented 3-spaces
    #       While '!!!', , '...', '???', '???+', etc. are indented 4-spaces
    indent = " " * (min(len(prefix), 3) + 1)
    content = textwrap.indent(separator.join(elements), indent)

    return title_line + "\n" + content if content else title_line


def _render_admon_title(
    node: RenderTreeNode,  # noqa: ARG001
    context: RenderContext,  # noqa: ARG001
) -> str:
    """Skip rendering the title when called from the `node.children`."""
    return ""


# A mapping from syntax tree node type to a function that renders it.
# This can be used to overwrite renderer functions of existing syntax
# or add support for new syntax.
RENDERERS: Mapping[str, Render] = {
    "admonition": _render_admon,
    "admonition_title": _render_admon_title,
}
