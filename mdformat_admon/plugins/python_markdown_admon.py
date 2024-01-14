from markdown_it.rules_block import StateBlock

from ..factories import (
    AdmonitionData,
    admon_plugin_factory,
    new_token,
    parse_possible_whitespace_admon_factory,
    parse_tag_and_title,
)


def format_python_markdown_admon_markup(
    state: StateBlock,
    start_line: int,
    admonition: AdmonitionData,
) -> None:
    tags, title = parse_tag_and_title(admonition.meta_text)
    tag = tags[0]

    with new_token(state, "admonition", "div") as token:
        token.markup = admonition.markup
        token.block = True
        token.attrs = {"class": " ".join(["admonition", *tags])}
        token.meta = {"tag": tag}
        token.info = admonition.meta_text
        token.map = [start_line, admonition.next_line]

        if title:
            title_markup = f"{admonition.markup} {tag}"
            with new_token(state, "admonition_title", "p") as token:
                token.markup = title_markup
                token.attrs = {"class": "admonition-title"}
                token.map = [start_line, start_line + 1]

                token = state.push("inline", "", 0)
                token.content = title
                token.map = [start_line, start_line + 1]
                token.children = []

        state.md.block.tokenize(state, start_line + 1, admonition.next_line)

    state.parentType = admonition.old_state.parentType
    state.lineMax = admonition.old_state.lineMax
    state.blkIndent = admonition.old_state.blkIndent
    state.line = admonition.next_line


def admonition_logic(
    state: StateBlock,
    startLine: int,
    endLine: int,
    silent: bool,
) -> bool:
    parse_possible_whitespace_admon = parse_possible_whitespace_admon_factory(
        markers={"!!!"}
    )
    result = parse_possible_whitespace_admon(state, startLine, endLine, silent)
    if isinstance(result, AdmonitionData):
        format_python_markdown_admon_markup(state, startLine, admonition=result)
        return True
    return result


python_markdown_admon_plugin = admon_plugin_factory("admonition", admonition_logic)
