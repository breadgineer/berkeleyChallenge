from doctest import run_docstring_examples
from Link import Link
from Tree import Tree
def slice_link(link, start, end):
    """Slices a Link from start to end (as with a normal Python list).
    >>> from Link import Link
    >>> link = Link(3, Link(1, Link(4, Link(1, Link(5, Link(9))))))
    >>> new = slice_link(link, 1, 4)
    >>> print(new)
    <1 4 1>
    """
    if end == 0:
        return Link.empty
    elif start == 0:
        return Link(link.first, slice_link(link.rest, 0, end-1))
    else:
        return slice_link(link.rest, start-1, end-1)

run_docstring_examples(slice_link, globals(), True)