# Admonition, Callout, and Alert Variations Test

Testing `mdformat-admon` as a `pre-commit` hook (`tox -e py#-hook`)

## Python-Markdown

From: <https://python-markdown.github.io/extensions/admonition>

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

## MKDocs

Based on: <https://squidfunk.github.io/mkdocs-material/reference/admonitions>

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

### 2023 Syntax

> [!NOTE]
> Useful information that users should know, even when skimming content.

> [!TIP]
> Helpful advice for doing things better or more easily.

> [!IMPORTANT]
> Key information users need to know to achieve their goal.

> [!WARNING]
> Urgent info that needs immediate user attention to avoid problems.

> [!CAUTION]
> Advises about risks or negative outcomes of certain actions.

### 2022 Syntax

> **Note**
> This is a note

> **Warning**
>
> This is a warning

## Directives

Variations of the CommonMark spec for fenced directives

### MyST

From: <https://myst-parser.readthedocs.io/en/latest/syntax/roles-and-directives.html>

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

### Markdown-It Containers

From: <https://github.com/markdown-it/markdown-it-container>

::: warning
*here be dragons*
:::

### reStructuredText

From: <https://docutils.sourceforge.io/docs/ref/rst/directives.html#specific-admonitions>

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

From: <https://myst-parser.readthedocs.io/en/latest/syntax/roles-and-directives.html>

```
.. directivename:: arguments
   :key1: val1
   :key2: val2

   This is
   directive content
```

### PyMDown

From: <https://facelessuser.github.io/pymdown-extensions/extensions/blocks/plugins/admonition/>

/// admonition | Some title
Some content
///

/// admonition | Some title
type: warning

Some content
///

/// note | Some title
Some content
///

/// some-custom-type | Some title
Some content
///

## Obsidian

### (New) Callouts

From: <https://help.obsidian.md/How+to/Use+callouts>

> [!info]
> Here's a callout block.
> It supports **Markdown**, \[[Internal link|Wikilinks]\], and \[[Embed files|embeds]\]!
> !\[[Engelbart.jpg]\]

> [!tip] Callouts can have custom titles
> Like this one.

> [!faq]- Are callouts foldable?
> Yes! In a foldable callout, the contents are hidden when the callout is collapsed.

> [!question] Can callouts be nested?
>
> > [!todo] Yes!, they can.
> >
> > > [!example] You can even use multiple layers of nesting.

### (Old) Obsidian Plugin Syntax

From: <https://github.com/valentine195/obsidian-admonition>

```ad-<type> # Admonition type. See below for a list of available types.
title:                  # Admonition title.
collapse:               # Create a collapsible admonition.
icon:                   # Override the icon.
color:                  # Override the color.

Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nulla et euismod nulla.

```

## Mozilla

From: <https://developer.mozilla.org/en-US/docs/MDN/Writing_guidelines/Howto/Markdown_in_MDN#notes_warnings_and_callouts>

> **Note:** This is how you write a note.
>
> It can have multiple lines.

> **Warning:** This is how you write a warning.
>
> It can have multiple paragraphs.

> **Callout:** **This is how you write a callout.**
>
> It can have multiple paragraphs.

> **Warnung:** So schreibt man eine Warnung.

> **Note:** This is how you write a note.
>
> It can contain code blocks.
>
> ```js
> const s = "I'm in a code block";
> ```
>
> Like that.
