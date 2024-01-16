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
    model = YOLO('yolov8n-seg.pt')

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
   model = YOLO('yolov8n-seg.pt')

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
