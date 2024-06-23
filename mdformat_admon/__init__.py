"""An mdformat plugin for admonitions."""

__version__ = "2.0.5"

from .plugin import RENDERERS, update_mdit

__all__ = ("RENDERERS", "update_mdit")
