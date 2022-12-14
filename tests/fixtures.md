
Simple admonition
.
!!! note
    *content*
.
!!! note
    *content*
.


Could contain block elements too
.
!!! note
    ### heading

    -----------

.
!!! note
    ### heading

    ______________________________________________________________________

.


Shows custom title
.
!!! note Custom title

    Some text

.
!!! note Custom title

    Some text

.


Shows no title
.
!!! note ""
    Some text

.
!!! note ""
    Some text

.


Closes block after 2 empty lines
.
!!! note
    Some text


    A code block
.
!!! note
    Some text


    A code block
.


Nested blocks
.
!!! note
    !!! note
        Some text

            code block
.
!!! note
    !!! note
        Some text

            code block
.


Consecutive admonitions
.
!!! note

!!! warning
.
!!! note

!!! warning
.


Marker may be indented up to 3 chars
.
   !!! note
       content
.
   !!! note
       content
.


But that's a code block
.
    !!! note
        content
.
    !!! note
        content
.


Some more indent checks
.
  !!! note
   not a code block

    code block
.
  !!! note
   not a code block

    code block
.


Type could be adjacent to marker
.
!!!note
   xxx

.
!!!note
   xxx

.


Type could be adjacent to marker and content may be shifted up to 3 chars
.
!!!note
      xxx

.
!!!note
      xxx

.


Or several spaces apart
.
!!!     note
        xxx
.
!!!     note
        xxx
.


Admonitions self-close at the end of the document
.
!!! note
    xxx
.
!!! note
    xxx
.


They could be nested in lists
.
- !!! note
      - a
      - b
- !!! warning
      - c
      - d
.
- !!! note
      - a
      - b
- !!! warning
      - c
      - d
.


Or in blockquotes
.
> !!! note
>     xxx
>     > yyy
>     zzz
>
.
> !!! note
>     xxx
>     > yyy
>     zzz
>
.


Renders unknown admonition type
.
!!! unknown title
    content
.
!!! unknown title
    content
.


Does not render
.
!!!
    content
.
!!!
    content
.
