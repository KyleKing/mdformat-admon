# Test file

add your syntax here

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

**STATUS: Unsupported and *may break***

From: https://docutils.sourceforge.io/docs/ref/rst/directives.html#specific-admonitions

.. contents::

.. contents:: Table of Contents

.. contents:: Here's a very long Table of
   Contents title

.. contents:: Table of Contents
   :depth: 2

## MKdocs

**STATUS: Partially supported, but *may break***

Based on: https://squidfunk.github.io/mkdocs-material/reference/admonitions/#removing-the-title

### Default

!!! note

    Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nulla et euismod
    nulla. Curabitur feugiat, tortor non consequat finibus, justo purus auctor
    massa, nec semper lorem quam in massa.


### Collapsible


??? note

    Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nulla et euismod
    nulla. Curabitur feugiat, tortor non consequat finibus, justo purus auctor
    massa, nec semper lorem quam in massa.


???+ note

    Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nulla et euismod
    nulla. Curabitur feugiat, tortor non consequat finibus, justo purus auctor
    massa, nec semper lorem quam in massa.

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
