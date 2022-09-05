from doctest import run_docstring_examples

def remove_odd_indices(lst, odd):
    """Remove elements of lst that have odd indices. Use recursion!

    >>> s = [1, 2, 3, 4]
    >>> t = remove_odd_indices(s, True)
    >>> s
    [1, 2, 3, 4]
    >>> t
    [1, 3]
    >>> l = [5, 6, 7, 8]
    >>> m = remove_odd_indices(l, False)
    >>> m
    [6, 8]
    >>> remove_odd_indices([9, 8, 7, 6, 5, 4, 3], False)
    [8, 6, 4]
    >>> remove_odd_indices([2], False)
    []

    """
    "*** YOUR CODE HERE ***"
    if not lst:
        return lst      # same as returning an empty list
    if odd:
        return [lst[0]] + remove_odd_indices(lst[1:], not odd)
    else:
        return remove_odd_indices(lst[1:], not odd)  



run_docstring_examples(remove_odd_indices, globals(), True)