"""Python-Markdown Admonition Plugin."""

from markdown_it.rules_block import StateBlock

from mdformat_admon.factories import (
    AdmonitionData,
    admon_plugin_factory,
    new_token,
    parse_possible_whitespace_admon_factory,
    parse_tag_and_title,
)

PREFIX = "admonition"
"""Prefix used to differentiate the parsed output."""


def format_python_markdown_admon_markup(
    state: StateBlock,
    start_line: int,
    admonition: AdmonitionData,
) -> None:
    """Format markup."""
    tags, title = parse_tag_and_title(admonition.meta_text)
    tag = tags[0]

    with new_token(state, PREFIX, "div") as token:
        token.markup = admonition.markup
        token.block = True
        token.attrs = {"class": " ".join(["admonition", *tags])}
        token.meta = {"tag": tag}
        token.info = admonition.meta_text
        token.map = [start_line, admonition.next_line]

        if title:
            title_markup = f"{admonition.markup} {tag}"
            with new_token(state, f"{PREFIX}_title", "p") as tkn_title:
                tkn_title.markup = title_markup
                tkn_title.attrs = {"class": "admonition-title"}
                tkn_title.map = [start_line, start_line + 1]

                tkn_inline = state.push("inline", "", 0)
                tkn_inline.content = title
                tkn_inline.map = [start_line, start_line + 1]
                tkn_inline.children = []

        state.md.block.tokenize(state, start_line + 1, admonition.next_line)

    state.parentType = admonition.old_state.parent_type
    state.lineMax = admonition.old_state.line_max
    state.blkIndent = admonition.old_state.blk_indent
    state.line = admonition.next_line


def admonition_logic(
    state: StateBlock,
    start_line: int,
    end_line: int,
    silent: bool,
) -> bool:
    """Parse Python Markdown-style Admonitions.

    `python-markdown style admonitions
    <https://python-markdown.github.io/extensions/admonition>`.

    .. code-block:: md

        !!! note
            *content*

    """
    parse_possible_whitespace_admon = parse_possible_whitespace_admon_factory(
        markers={"!!!"},
    )
    result = parse_possible_whitespace_admon(state, start_line, end_line, silent)
    if isinstance(result, AdmonitionData):
        format_python_markdown_admon_markup(state, start_line, admonition=result)
        return True
    return result


python_markdown_admon_plugin = admon_plugin_factory(PREFIX, admonition_logic)
