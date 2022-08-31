from doctest import run_docstring_examples
def flatten(x):
    """Returns a flattened version of list s.

    >>> flatten([1, 2, 3])     # normal list
    [1, 2, 3]
    >>> x = [1, [2, 3], 4]     # deep list
    >>> flatten(x)
    [1, 2, 3, 4]
    >>> x # Ensure x is not mutated
    [1, [2, 3], 4]
    >>> x = [[1, [1, 1]], 1, [1, 1]] # deep list
    >>> flatten(x)
    [1, 1, 1, 1, 1, 1]
    >>> x
    [[1, [1, 1]], 1, [1, 1]]
    """
    "*** YOUR CODE HERE ***"
    s = list(x)
    def _flatten(s):
        if not s:
            return []
        elif type(s[0]) is list:
            return _flatten(s[0]) + _flatten(s[1:])
        else:
            return [s[0]] + _flatten(s[1:])

    return _flatten(s)


run_docstring_examples(flatten, globals(), True) 