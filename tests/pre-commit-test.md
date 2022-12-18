# Pre-Commit Test File

Testing `mdformat-admon` as a `pre-commit` hook (`tox -e py#-hook`)

## `!!!`-based Admonitions

**STATUS: Full support for formatting by `mdformat-admon`**

### Python-Markdown

From: https://python-markdown.github.io/extensions/admonition/

!!! type "optional explicit title within double quotes"
    Any number of other indented markdown elements.

    This is the second paragraph.

!!! note
    You should note that the title will be automatically capitalized.

!!! danger "Don't try this at home"
    ...

!!! important ""
    This is an admonition box without a title.

!!! danger highlight blink "Don't try this at home"
    ...

## Github

**STATUS: Unsupported and will not modify**

> **Note**
> This is a note

> **Warning**
> This is a warning

## RST

**STATUS: Unsupported and *may break*** like the 3rd and 4th examples below

From: https://docutils.sourceforge.io/docs/ref/rst/directives.html#specific-admonitions

.. contents::

.. contents:: Table of Contents

```rst
.. contents:: Here's a very long Table of
   Contents title
```

```rst
.. contents:: Table of Contents
   :depth: 2
```

## MKdocs

**STATUS: ONly `!!!`-blocks are supported**

Based on: https://squidfunk.github.io/mkdocs-material/reference/admonitions/#removing-the-title

### Default

!!! note
    Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nulla et euismod
    nulla. Curabitur feugiat, tortor non consequat finibus, justo purus auctor
    massa, nec semper lorem quam in massa.

### Collapsible

Not currently supported

```md
??? note
    Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nulla et euismod
    nulla. Curabitur feugiat, tortor non consequat finibus, justo purus auctor
    massa, nec semper lorem quam in massa.
```

```md
???+ note
    Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nulla et euismod
    nulla. Curabitur feugiat, tortor non consequat finibus, justo purus auctor
    massa, nec semper lorem quam in massa.
```

### Inline

!!! info inline end
    Lorem ipsum dolor sit amet, consectetur
    adipiscing elit. Nulla et euismod nulla.
    Curabitur feugiat, tortor non consequat
    finibus, justo purus auctor massa, nec
    semper lorem quam in massa.

### Custom Type

!!! pied-piper "Pied Piper"
    Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nulla et
    euismod nulla. Curabitur feugiat, tortor non consequat finibus, justo
    purus auctor massa, nec semper lorem quam in massa.
