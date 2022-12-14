from Tree import Tree
from doctest import run_docstring_examples

def height(t):
    """Return the height of a tree.

    >>> t = Tree(3, [Tree(5, [Tree(1)]), Tree(2)])
    >>> height(t)
    2
    >>> t = Tree(3, [Tree(1), Tree(2, [Tree(5, [Tree(6)]), Tree(1)])])
    >>> height(t)
    3
    """
    "*** YOUR CODE HERE ***"
    if t.is_leaf():
        return 0
    else:
        return 1 + max([height(branch) for branch in t.branches])

run_docstring_examples(height, globals(), True)
