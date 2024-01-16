# mdformat-admon

[![Build Status][ci-badge]][ci-link] [![PyPI version][pypi-badge]][pypi-link]

<!-- [![codecov.io][cov-badge]][cov-link]
[cov-badge]: https://codecov.io/gh/executablebooks/mdformat-admon/branch/main/graph/badge.svg
[cov-link]: https://codecov.io/gh/executablebooks/mdformat-admon
 -->

An [mdformat](https://github.com/executablebooks/mdformat) plugin for `admonitions`, a set of helpers for supporting new admonition syntaxes, and tool for rendering admonition HTML.

## `mdformat` Usage

Add this package wherever you use `mdformat` and the plugin will be auto-recognized. No additional configuration necessary. See [additional information on `mdformat` plugins here](https://mdformat.readthedocs.io/en/stable/users/plugins.html)

### Pre-Commit

```yaml
repos:
  - repo: https://github.com/executablebooks/mdformat
    rev: 0.7.16
    hooks:
      - id: mdformat
        additional_dependencies:
          - mdformat-admon
```

### pipx

```sh
pipx install mdformat
pipx inject mdformat mdformat-admon
```

## HTML Rendering

To generate HTML output, `python_markdown_admon_plugin` can be imported from `mdit_plugins`. More plugins will be added in the future. For more guidance on `MarkdownIt`, see the docs: <https://markdown-it-py.readthedocs.io/en/latest/using.html#the-parser>

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

## Extensibility

Because admonition syntax varies wildly between implementations, this package provides a set of helpers for building new admonition parsers under `mdformat_admon.factories`.

- Supported by `mdformat-admon`
    - [python-markdown](https://python-markdown.github.io/extensions/admonition)
- Supported by other packages
    - [`mdformat-mkdocs`](https://github.com/KyleKing/mdformat-mkdocs)
        - [MKDocs](https://squidfunk.github.io/mkdocs-material/reference/admonitions)
- Currently Unsupported (or at least not known to be supported)
    - [Github](https://github.com/orgs/community/discussions/16925)
    - [MyST](https://myst-parser.readthedocs.io/en/latest/syntax/roles-and-directives.html)
    - [Remark-Admonitions](https://github.com/elviswolcott/remark-admonitions)
    - [pymdown-extensions](https://facelessuser.github.io/pymdown-extensions/extensions/blocks/plugins/admonition)
    - [reStructuredText](https://docutils.sourceforge.io/docs/ref/rst/directives.html#specific-admonitions) (Note: this plugin *may break* these admonitions by removing or modifying indentation)
    - [Obsidian Callouts](https://help.obsidian.md/How+to/Use+callouts) (Note: this plugin *may break* these admonitions by adding extra characters)

See the example test file: [./tests/pre-commit-test.md](https://raw.githubusercontent.com/KyleKing/mdformat-admon/main/tests/pre-commit-test.md)

## Contributing

See [CONTRIBUTING.md](https://github.com/KyleKing/mdformat-admon/blob/main/CONTRIBUTING.md)

[ci-badge]: https://github.com/kyleking/mdformat-admon/workflows/CI/badge.svg?branch=main
[ci-link]: https://github.com/kyleking/mdformat-admon/actions?query=workflow%3ACI+branch%3Amain+event%3Apush
[pypi-badge]: https://img.shields.io/pypi/v/mdformat-admon.svg
[pypi-link]: https://pypi.org/project/mdformat-admon
