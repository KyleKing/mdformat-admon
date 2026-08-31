# mdformat-admon

[![Build Status][ci-badge]][ci-link] [![PyPI version][pypi-badge]][pypi-link]

<!-- [![codecov.io][cov-badge]][cov-link]
[cov-badge]: https://codecov.io/gh/executablebooks/mdformat-admon/branch/main/graph/badge.svg
[cov-link]: https://codecov.io/gh/executablebooks/mdformat-admon
 -->

An [mdformat](https://github.com/executablebooks/mdformat) plugin for formatting [`python-markdown` `admonitions`](https://python-markdown.github.io/extensions/admonition) and rendering the associated HTML.

> [!WARNING]
> `mdformat-admon` and `mdformat-mkdocs>=4.0.0` are no longer compatible. If you have both, you'll want to remove `mdformat-admon`
>
> The stylistic formatting for `mkdocs` differs from Python Markdown ([#22](https://github.com/KyleKing/mdformat-admon/pull/22)), so this package is now *only* for Python Markdown without mkdocs.

## `mdformat` Usage

Add this package wherever you use `mdformat`; it auto-recognizes the plugin, no configuration needed. See [more on `mdformat` plugins](https://mdformat.readthedocs.io/en/stable/users/plugins.html)

### pre-commit / prek

```yaml
repos:
  - repo: https://github.com/executablebooks/mdformat
    rev: 1.0.0
    hooks:
      - id: mdformat
        additional_dependencies:
          - mdformat-admon
```

### uvx

```sh
uvx --with=mdformat-admon mdformat
```

Or with pipx:

```sh
pipx install mdformat
pipx inject mdformat mdformat-admon
```

## HTML Rendering

To generate HTML output, import `python_markdown_admon_plugin` from `mdit_plugins`. More plugins will be added in the future. For more on `MarkdownIt`, see the docs: <https://markdown-it-py.readthedocs.io/en/latest/using.html#the-parser>

```py
from markdown_it import MarkdownIt
from mdformat_admon.mdit_plugins import python_markdown_admon_plugin

md = MarkdownIt()
md.use(python_markdown_admon_plugin)

text = '!!! note ""\n    *content*'
md.render(text)
# <div class="admonition note">
# <p><em>content</em></p>
# </div>
```

## Contributing

See [CONTRIBUTING.md](https://github.com/kyleking/mdformat-admon/blob/main/CONTRIBUTING.md)

[ci-badge]: https://github.com/kyleking/mdformat-admon/actions/workflows/tests.yml/badge.svg?branch=main
[ci-link]: https://github.com/kyleking/mdformat-admon/actions?query=workflow%3ACI+branch%3Amain+event%3Apush
[pypi-badge]: https://img.shields.io/pypi/v/mdformat-admon.svg
[pypi-link]: https://pypi.org/project/mdformat-admon
