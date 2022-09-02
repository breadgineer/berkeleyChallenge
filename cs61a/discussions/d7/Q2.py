from Tree import Tree
from doctest import run_docstring_examples

def max_path_sum(t):
    """Return the maximum path sum of the tree.

    >>> t = Tree(1, [Tree(5, [Tree(1), Tree(3)]), Tree(10)])
    >>> max_path_sum(t)
    11
    """
    "*** YOUR CODE HERE ***"
    if t.is_leaf():
        return t.label
    else:
        return t.label + max([max_path_sum(branch) for branch in t.branches])


run_docstring_examples(max_path_sum, globals(), True)