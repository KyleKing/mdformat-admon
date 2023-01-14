# Pre-Commit Test File

Testing `mdformat-admon` as a `pre-commit` hook (`tox -e py#-hook`)

## CommonMark

[Does not specify a syntax for admonitions](https://spec.commonmark.org)

## Python-Markdown

**STATUS: Full support for formatting by `mdformat-admon`**

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

## MKdocs

**STATUS: Fully supported**

Based on: https://squidfunk.github.io/mkdocs-material/reference/admonitions

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

## Github

**STATUS: Unsupported and will not modify**

> **Note**
> This is a note

> **Warning**
>
> This is a warning

## MyST

**STATUS: Unsupported and will not modify**

From: https://myst-parser.readthedocs.io/en/latest/syntax/roles-and-directives.html

```{directivename} arguments
---
key1: val1
key2: val2
---
This is
directive content
```

```{code-block} python
---
lineno-start: 10
emphasize-lines: 1, 3
caption: |
    This is my
    multi-line caption. It is *pretty nifty* ;-)
---
a = 2
print('my 1st line')
print(f'my {a}nd line')
```

```{admonition} My markdown link
Here is [markdown link syntax](https://jupyter.org)
```

```{eval-rst}
.. figure:: img/fun-fish.png
  :width: 100px
  :name: rst-fun-fish

  Party time!

A reference from inside: :ref:`rst-fun-fish`

A reference from outside: :ref:`syntax/directives/parsing`
```

````{note}
The warning block will be properly-parsed

   ```{warning}
   Here's my warning
   ```

But the next block will be parsed as raw text

    ```{warning}
    Here's my raw text warning that isn't parsed...
    ```
````

## Remark-Admonitions

**STATUS: Unsupported and will not modify**

From: https://github.com/elviswolcott/remark-admonitions

:::tip pro tip
`remark-admonitions` is pretty great!
:::

## reStructuredText

**STATUS: Unsupported and *will break*** like the 3rd, 4th, and 5th examples below

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

From: https://myst-parser.readthedocs.io/en/latest/syntax/roles-and-directives.html

```
.. directivename:: arguments
   :key1: val1
   :key2: val2

   This is
   directive content
```

## Obsidian

## (New) Callouts

**STATUS: Unsupported and *will break*** because `mdformat` adds extra characters

From: https://help.obsidian.md/How+to/Use+callouts

```
> [!INFO]
> Here's a callout block.
> It supports **markdown**, [[Internal link|wikilinks]], and [[Embed files|embeds]]!
> ![[og-image.png]]
```

```
> [!question] Can callouts be nested?
> > [!todo] Yes!, they can.
> > > [!example]  You can even use multiple layers of nesting.
```

## (Old) Plugin

**STATUS: Unsupported and will not modify**

From: https://github.com/valentine195/obsidian-admonition

```ad-<type> # Admonition type. See below for a list of available types.
title:                  # Admonition title.
collapse:               # Create a collapsible admonition.
icon:                   # Override the icon.
color:                  # Override the color.

Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nulla et euismod nulla.

```
