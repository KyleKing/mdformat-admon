
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



MKdocs Closed Collapsible Sections
.
??? note
    content
.
??? note
    content
.


MKdocs Open Collapsible Sections
.
???+ note
    content
.
???+ note
    content
.


Support Content Tabs (https://squidfunk.github.io/mkdocs-material/reference/content-tabs/#grouping-code-blocks). Resolves #17: https://github.com/KyleKing/mdformat-admon/issues/17
.
Ultralytics commands use the following syntax:

!!! Example

    === "CLI"

        ```bash
        yolo TASK MODE ARGS
        ```

    === "Python"

        ```python
        from ultralytics import YOLO

        # Load a YOLOv8 model from a pre-trained weights file
        model = YOLO('yolov8n.pt')

        # Run MODE mode using the custom arguments ARGS (guess TASK)
        model.MODE(ARGS)
        ```
.
Ultralytics commands use the following syntax:

!!! Example

    === "CLI"

        ```bash
        yolo TASK MODE ARGS
        ```

    === "Python"

        ```python
        from ultralytics import YOLO

        # Load a YOLOv8 model from a pre-trained weights file
        model = YOLO('yolov8n.pt')

        # Run MODE mode using the custom arguments ARGS (guess TASK)
        model.MODE(ARGS)
        ```
.

Example from Ultralytics Documentation (https://github.com/KyleKing/ultralytics/blob/0e7221fb62191e18e5ec4f7a9fe6d8927a4446c2/docs/zh/datasets/index.md#L105-L127)
.
### 优化和压缩数据集的示例代码

!!! Example "优化和压缩数据集"

    === "Python"

    ```python
    from pathlib import Path
    from ultralytics.data.utils import compress_one_image
    from ultralytics.utils.downloads import zip_directory

    # 定义数据集目录
    path = Path('path/to/dataset')

    # 优化数据集中的图像（可选）
    for f in path.rglob('*.jpg'):
        compress_one_image(f)

    # 将数据集压缩成 'path/to/dataset.zip'
    zip_directory(path)
    ```

通过遵循这些步骤，您可以贡献一个与 Ultralytics 现有结构良好融合的新数据集。
.
### 优化和压缩数据集的示例代码

!!! Example "优化和压缩数据集"

    === "Python"

        ```python
        from pathlib import Path
        from ultralytics.data.utils import compress_one_image
        from ultralytics.utils.downloads import zip_directory

        # 定义数据集目录
        path = Path('path/to/dataset')

        # 优化数据集中的图像（可选）
        for f in path.rglob('*.jpg'):
            compress_one_image(f)

        # 将数据集压缩成 'path/to/dataset.zip'
        zip_directory(path)
        ```

通过遵循这些步骤，您可以贡献一个与 Ultralytics 现有结构良好融合的新数据集。
.


Example of non-code content from Material-MKDocs documentation without admonitions
.
=== "Unordered list"

    * Sed sagittis eleifend rutrum
    * Donec vitae suscipit est
    * Nulla tempor lobortis orci

=== "Ordered list"

    1. Sed sagittis eleifend rutrum
    2. Donec vitae suscipit est
    3. Nulla tempor lobortis orci
.
=== "Unordered list"

```
* Sed sagittis eleifend rutrum
* Donec vitae suscipit est
* Nulla tempor lobortis orci
```

=== "Ordered list"

```
1. Sed sagittis eleifend rutrum
2. Donec vitae suscipit est
3. Nulla tempor lobortis orci
```
.


Example from Material-MKDocs documentation within an admonition
.
!!! example

    === "Unordered List"

        ```markdown
        * Sed sagittis eleifend rutrum
        * Donec vitae suscipit est
        * Nulla tempor lobortis orci
        ```

    === "Ordered List"

        ```markdown
        1. Sed sagittis eleifend rutrum
        2. Donec vitae suscipit est
        3. Nulla tempor lobortis orci
        ```
.
!!! example

    === "Unordered List"

        ```markdown
        * Sed sagittis eleifend rutrum
        * Donec vitae suscipit est
        * Nulla tempor lobortis orci
        ```

    === "Ordered List"

        ```markdown
        1. Sed sagittis eleifend rutrum
        2. Donec vitae suscipit est
        3. Nulla tempor lobortis orci
        ```
.
