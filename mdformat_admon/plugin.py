import textwrap
from typing import Mapping

from markdown_it import MarkdownIt
from mdformat.renderer import RenderContext, RenderTreeNode
from mdformat.renderer.typing import Render
from mdit_py_plugins.admon import admon_plugin


def update_mdit(mdit: MarkdownIt) -> None:
    """Update the parser,"""
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
    separator = "\n\n"  # TODO: Is this configurable?
    indent = " " * 4  # FIXME: Is this configurable?
    title = node.children[0].render(context)  # or 'node.info.strip()'?
    body = f"{node.markup} {title}{separator}"
    with context.indented(len(indent)):  # Modifies context.env['indent_width']
        elements = [child.render(context) for child in [*node.walk()][1:]]
    body += textwrap.indent(separator.join(elements), indent)
    return body


# A mapping from syntax tree node type to a function that renders it.
# This can be used to overwrite renderer functions of existing syntax
# or add support for new syntax.
RENDERERS: Mapping[str, Render] = {"admonition": _render_admon}
