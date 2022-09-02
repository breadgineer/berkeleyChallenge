from Tree import Tree
from doctest import run_docstring_examples

def find_path(t, x):
    """
    >>> t = Tree(2, [Tree(7, [Tree(3), Tree(6, [Tree(5), Tree(11)])]), Tree(15)])
    >>> find_path(t, 5)
    [2, 7, 6, 5]
    >>> find_path(t, 10)  # returns None
    """

    # if t.is_leaf() and t.label != x:
    #     return ""
    # else:
    #     return[t.label] + [find_path(branch,x) for branch in t.branches]

    if t.label == x:
        return [t.label]
    for b in t.branches:
        path = find_path(b, x)
        if path:
            return [t.label] + path


run_docstring_examples(find_path, globals(), True)