"""An mdformat plugin for `admonition`."""

__version__ = "2.1.1"

__plugin_name__ = "admonition"

# FYI see source code for available interfaces:
#   https://github.com/executablebooks/mdformat/blob/5d9b573ce33bae219087984dd148894c774f41d4/src/mdformat/plugins.py
from .plugin import RENDERERS, update_mdit

__all__ = ("RENDERERS", "update_mdit")
