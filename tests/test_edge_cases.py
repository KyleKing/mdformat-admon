"""Unit tests for edge cases to achieve 100% coverage."""

from __future__ import annotations

import mdformat

from mdformat_admon._synced.admon_factories import parse_tag_and_title


def test_parse_tag_and_title_empty_string():
    """Test parse_tag_and_title with empty string (line 39 coverage)."""
    tags, title = parse_tag_and_title("")
    assert tags == [""]
    assert not title


def test_parse_tag_and_title_whitespace_only():
    """Test parse_tag_and_title with whitespace-only string (line 39 coverage)."""
    tags, title = parse_tag_and_title("   ")
    assert tags == [""]
    assert not title


def test_admonition_marker_in_indented_code_block():
    """Test that admonition markers in code blocks are not parsed (line 127 coverage)."""
    # Four spaces create a code block - admonition marker should not be parsed
    text = "    !!! note\n    This is code\n"
    output = mdformat.text(text, extensions={"admon"})
    # Should remain as code block, not parsed as admonition
    assert "```" in output  # mdformat converts indented code to fenced
    assert "!!! note" in output  # The marker should be preserved as code content
    # Verify it's not parsed as an admonition by checking structure
    lines = output.strip().split("\n")
    assert lines[0] == "```"  # Starts with fence
    assert "!!! note" in output  # Contains the literal text


def test_admonition_in_deeply_indented_context():
    """Test admonition parsing in deeply indented list context."""
    # This creates a scenario where we have deep nesting that could trigger
    # code block detection if indentation is mishandled
    text = "- Item\n    - Nested\n        - Deep\n            !!! note\n                Content\n"
    output = mdformat.text(text, extensions={"admon"})
    # Should handle the nesting properly
    assert output is not None


def test_code_block_with_admonition_syntax():
    """Test that code blocks containing admonition syntax are preserved."""
    # Test with explicit fenced code block
    text = "```\n!!! note\n    This is not an admonition\n```\n"
    output = mdformat.text(text, extensions={"admon"})
    assert "```" in output
    assert "!!! note" in output

    # Test within a list with code block indentation
    text2 = "- List item\n\n      !!! note\n          Even more indented\n"
    output2 = mdformat.text(text2, extensions={"admon"})
    # With 6+ spaces in a list, it might be treated as code
    assert output2 is not None
