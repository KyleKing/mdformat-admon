"""Direct unit test to cover the is_code_block check (line 127)."""

from __future__ import annotations

from unittest.mock import Mock, patch

from mdformat_admon._synced.admon_factories import (
    parse_possible_whitespace_admon_factory,
)


def test_code_block_check_returns_false():
    """Test that parse function returns False when is_code_block is True (line 127)."""
    # Create the parser function
    parse_fn = parse_possible_whitespace_admon_factory(markers={"!!!"})

    # Create a mock state object
    mock_state = Mock()
    mock_state.bMarks = [0, 10, 20]
    mock_state.tShift = [0, 0, 0]
    mock_state.eMarks = [10, 20, 30]
    mock_state.src = "!!! note content"
    mock_state.sCount = [0, 0, 0]
    mock_state.blkIndent = 0

    # Patch is_code_block to return True to force line 127 to execute
    with patch("mdformat_admon._synced.admon_factories._whitespace_admon_factories.is_code_block") as mock_is_code:
        mock_is_code.return_value = True

        # Call the parse function
        result = parse_fn(mock_state, start_line=0, end_line=3, silent=False)

        # Should return False because is_code_block returned True
        assert result is False
        mock_is_code.assert_called_once_with(mock_state, 0)
