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


Removes extra quotes from the title
.
!!! danger "Don't try this at home"
    ...

.
!!! danger "Don't try this at home"
    ...

.


Parse additional classes to support Python markdown (https://github.com/executablebooks/mdit-py-plugins/issues/93#issuecomment-1601822723)
.
!!! a b c d inline-classes   "Note: note about "foo""
    ...

.
!!! a b c d inline-classes   "Note: note about "foo""
    ...

.


Closes block after 2 empty lines
.
!!! note
    Some text


    A code block
.
!!! note
    Some text

```
A code block
```
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

        ```
        code block
        ```
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
```
!!! note
    content
```
.


Some more indent checks
.
  !!! note
   not a code block

    code block
.
!!! note

not a code block

```
code block
```
.


Type could be adjacent to marker
.
!!!note
   xxx

.
!!! note
    xxx

.


Type could be adjacent to marker and content may be shifted up to 3 chars
.
!!!note
      xxx

.
!!! note
    xxx

.


Or several spaces apart
.
!!!     note
        xxx
.
!!! note
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
>
>     > yyy
>     > zzz
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


Abbreviated example from Ultralytics Documentation (https://github.com/ultralytics/ultralytics/blob/fd82a671015a30a869d740c45c65f5633d1d93c4/docs/en/guides/isolating-segmentation-objects.md#L15)
.
1. Load a model and run `predict()` method on a source.

    ```py
    from ultralytics import YOLO

    # Load a model
    model = YOLO("yolov8n-seg.pt")

    # Run inference
    result = model.predict()
    ```

    !!! question "No Prediction Arguments?"

        Without specifying a source, the example images from the library will be used:

        ```
        'ultralytics/assets/bus.jpg'
        'ultralytics/assets/zidane.jpg'
        ```

        This is helpful for rapid testing with the `predict()` method.

    For additional information about Segmentation Models, visit the [Segment Task](../tasks/segment.md#models) page. To learn more about `predict()` method, see [Predict Mode](../modes/predict.md) section of the Documentation.

    ---

2. Now iterate over the results and the contours.
.
1. Load a model and run `predict()` method on a source.

   ```py
   from ultralytics import YOLO

   # Load a model
   model = YOLO("yolov8n-seg.pt")

   # Run inference
   result = model.predict()
   ```

   !!! question "No Prediction Arguments?"
       Without specifying a source, the example images from the library will be used:

       ```
       'ultralytics/assets/bus.jpg'
       'ultralytics/assets/zidane.jpg'
       ```

       This is helpful for rapid testing with the `predict()` method.

   For additional information about Segmentation Models, visit the [Segment Task](../tasks/segment.md#models) page. To learn more about `predict()` method, see [Predict Mode](../modes/predict.md) section of the Documentation.

   ______________________________________________________________________

1. Now iterate over the results and the contours.
.


Deterministic indents for HTML (Snippet adapted from ULtralytics documentation)
.
### Object Isolation Options

!!! info "Full-size Image"
    !!! info "Inner"
        There are no additional steps required if keeping full size image.

        <figure markdown>
             ![Example Full size Isolated Object Image Black Background](https://github.com/ultralytics/ultralytics/assets/62214284/845c00d0-52a6-4b1e-8010-4ba73e011b99){ width=240 }
           <figcaption>Example full-size output</figcaption>
        </figure>
.
### Object Isolation Options

!!! info "Full-size Image"
    !!! info "Inner"
        There are no additional steps required if keeping full size image.

        <figure markdown>
             ![Example Full size Isolated Object Image Black Background](https://github.com/ultralytics/ultralytics/assets/62214284/845c00d0-52a6-4b1e-8010-4ba73e011b99){ width=240 }
           <figcaption>Example full-size output</figcaption>
        </figure>
.

Do not modify multi-line code from: https://github.com/KyleKing/mdformat-mkdocs/issues/23
.
!!! info
    ```python
    # Line 1


    # Line 4
    ```
.
!!! info
    ```python
    # Line 1


    # Line 4
    ```
.


Admonition within code fence should not be parsed
.
```markdown
!!! note
    This should not be parsed as an admonition
```
.
```markdown
!!! note
    This should not be parsed as an admonition
```
.


Deeply nested admonitions
.
!!! warning
    !!! info
        !!! tip
            This is deeply nested content

            - Item 1
            - Item 2
.
!!! warning
    !!! info
        !!! tip
            This is deeply nested content

            - Item 1
            - Item 2
.


Admonition with inline code in title
.
!!! note Check `this_function()` for details
    Content here
.
!!! note Check `this_function()` for details
    Content here
.


Admonition with special characters in title
.
!!! warning "Don't forget: save & commit!"
    Important reminder
.
!!! warning "Don't forget: save & commit!"
    Important reminder
.


Mixed content: lists, code blocks, and blockquotes
.
!!! info
    Here's a list:

    - Item 1
    - Item 2

    And some code:

    ```bash
    echo "hello"
    ```

    > A quote
.
!!! info
    Here's a list:

    - Item 1
    - Item 2

    And some code:

    ```bash
    echo "hello"
    ```

    > A quote
.


Admonition with table
.
!!! note
    | Column 1 | Column 2 |
    | -------- | -------- |
    | Value 1  | Value 2  |
.
!!! note
    | Column 1 | Column 2 |
    | -------- | -------- |
    | Value 1 | Value 2 |
.


Admonition with links and images
.
!!! tip
    Check out [this guide](https://example.com)

    ![Image](https://example.com/image.png)
.
!!! tip
    Check out [this guide](https://example.com)

    ![Image](https://example.com/image.png)
.


Multiple tag classes with special title
.
!!! warning important urgent "Critical: Review Required!"
    This admonition has multiple classes
.
!!! warning important urgent "Critical: Review Required!"
    This admonition has multiple classes
.


Empty admonition with title
.
!!! note Empty but titled
.
!!! note Empty but titled
.


Admonition with horizontal rules
.
!!! info
    Section 1

    ---

    Section 2
.
!!! info
    Section 1

    ______________________________________________________________________

    Section 2
.


Admonition with escaped characters
.
!!! note
    Use \*asterisks\* for emphasis

    Or \_underscores\_
.
!!! note
    Use \*asterisks\* for emphasis

    Or \_underscores\_
.


Admonition following paragraph without blank line
.
Some paragraph text
!!! note
    Content
.
Some paragraph text

!!! note
    Content
.


Consecutive different admonition types
.
!!! note
    First note

!!! warning
    Warning message

!!! tip
    Helpful tip

!!! danger
    Danger zone
.
!!! note
    First note

!!! warning
    Warning message

!!! tip
    Helpful tip

!!! danger
    Danger zone
.
