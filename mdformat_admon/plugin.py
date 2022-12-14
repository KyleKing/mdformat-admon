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
    # FIXME: children
    # > return "\n\n".join([child.markup for child in node.children])

    print(node.pretty())  # FYI: Debugging

    separator = "\n"
    indent = " " * 4  # FIXME: Make this configurable?
    body = ""
    with context.indented(len(indent)):  # TODO: What is this for?
        elements = [child.render(context) for child in node.children[1:]]
        body += textwrap.indent((separator + separator).join(elements), indent)
    first_line = node.children[0].markup
    result = separator.join([first_line, body])
    breakpoint()
    return result


# A mapping from syntax tree node type to a function that renders it.
# This can be used to overwrite renderer functions of existing syntax
# or add support for new syntax.
RENDERERS: Mapping[str, Render] = {"admonition": _render_admon}
