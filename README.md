# mdformat-admon

[![Build Status][ci-badge]][ci-link]

<!-- [![codecov.io][cov-badge]][cov-link]
[cov-badge]: https://codecov.io/gh/executablebooks/mdformat-admon/branch/main/graph/badge.svg
[cov-link]: https://codecov.io/gh/executablebooks/mdformat-admon
 -->

[![PyPI version][pypi-badge]][pypi-link]

An [mdformat](https://github.com/executablebooks/mdformat) plugin for admonitions.

## Usage

Add this package wherever you use `mdformat` and the plugin will be auto-recognized. No additional configuration necessary. See [additional information on `mdformat` plugins here](https://mdformat.readthedocs.io/en/stable/users/plugins.html)

### Pre-commit

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

## Caveats

This plugin currently only supports admonitions that start with `!!! ...` and won't modify admonitions for Github, which should cover most use cases. Future work is planned for other types.

See the example test file: [./tests/pre-commit-test.md](https://raw.githubusercontent.com/KyleKing/mdformat-admon/main/tests/pre-commit-test.md)

As a quick summary:

- [python-markdown](https://python-markdown.github.io/extensions/admonition/): are fully supported by `mdformat-admon` and tested extensively in [./tests/fixtures.md](https://raw.githubusercontent.com/KyleKing/mdformat-admon/main/tests/fixtures.md)
- [MKdocs](https://squidfunk.github.io/mkdocs-material/reference/admonitions): Only `!!!`-blocks are supported (#9)
- [Github](https://github.com/orgs/community/discussions/16925): Unsupported and will not modify
- [reStructuredText](https://docutils.sourceforge.io/docs/ref/rst/directives.html#specific-admonitions): Unsupported and *will break*
- [MyST](https://myst-parser.readthedocs.io/en/latest/syntax/roles-and-directives.html): Unsupported and will not modify
- [Remark-Admonitions](https://github.com/elviswolcott/remark-admonitions): Unsupported and will not modify
- [Obsidian Callouts](https://help.obsidian.md/How+to/Use+callouts): Unsupported and *will break* because `mdformat` adds extra characters

## Contributing

See [CONTRIBUTING.md](https://github.com/KyleKing/mdformat-admon/blob/main/CONTRIBUTING.md)

[ci-badge]: https://github.com/executablebooks/mdformat-admon/workflows/CI/badge.svg?branch=main
[ci-link]: https://github.com/executablebooks/mdformat/actions?query=workflow%3ACI+branch%3Amain+event%3Apush
[pypi-badge]: https://img.shields.io/pypi/v/mdformat-admon.svg
[pypi-link]: https://pypi.org/project/mdformat-admon
