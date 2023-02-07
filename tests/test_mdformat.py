from pathlib import Path

import mdformat


def test_mdformat_text():
    """Verify that using mdformat works as expected."""
    content = (Path(__file__).parent / "pre-commit-test.md").read_text()

    result = mdformat.text(
        content,
        options={"end-of-line": "keep"},
        extensions={
            "admonition",
        },
    )

    assert result == content
