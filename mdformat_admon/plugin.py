from typing import Mapping

from markdown_it import MarkdownIt
from mdformat.renderer import RenderContext, RenderTreeNode
from mdformat.renderer.typing import Render
from mdit_py_plugins.admon import admon_plugin


def update_mdit(mdit: MarkdownIt) -> None:
    """Update the parser,"""
    mdit.use(admon_plugin)


def _render_admon(node: RenderTreeNode, context: RenderContext) -> str:
    """Render a `RenderTreeNode` of type `admon`.

    Based on:

    - https://github.com/hukkin/mdformat-gfm/blob/cf316a121b6cf35cbff7b0ad6e171f287803f8cb/src/mdformat_gfm/plugin.py
    - https://github.com/hukkin/mdformat-toc/blob/42624b6f3468da4f793ec7425da872b030714774/mdformat_toc/plugin.py
    - https://github.com/executablebooks/mdformat-footnote/blob/80852fc20cfba7fd0330b9ac7a1a4df983542942/mdformat_footnote/plugin.py

    """
    return node.markup + "\n" + node.markup  # FIXME: Implement!


# A mapping from syntax tree node type to a function that renders it.
# This can be used to overwrite renderer functions of existing syntax
# or add support for new syntax.
RENDERERS: Mapping[str, Render] = {"admon": _render_admon}
