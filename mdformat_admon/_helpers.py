"""General Helpers."""

from __future__ import annotations

from collections.abc import Mapping
from typing import Any

from . import __plugin_name__

ContextOptions = Mapping[str, Any]


def get_conf(options: ContextOptions, key: str) -> bool | str | int | None:
    """Read setting from mdformat configuration Context."""
    cli_or_toml = (
        options["mdformat"].get("plugin", {}).get(__plugin_name__, {}).get(key)
    )
    if cli_or_toml is None:
        return options["mdformat"].get(key)  # From API
    return cli_or_toml
