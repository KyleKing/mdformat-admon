_SHOW_TEXT = True  # PLANNED: Make configurable based on pytest CLI


def _show_indent(content: str) -> None:
    for line in content.split("\n"):
        print(line)


def print_text(output: str, expected: str) -> None:
    if _SHOW_TEXT:
        print("--  Output  --")
        _show_indent(output.strip())
        print("-- Expected --")
        _show_indent(expected.strip())
        print("--  <End>   --")
