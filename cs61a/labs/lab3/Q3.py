from doctest import run_docstring_examples

def paths(m, n):
    """Return the number of paths from one corner of an
    M by N grid to the opposite corner.

    >>> paths(2, 2)
    2
    >>> paths(5, 7)
    210
    >>> paths(117, 1)
    1
    >>> paths(1, 157)
    1
    """
    "*** YOUR CODE HERE ***"
    if (m == 1 or n == 1):
        return 1
    def calculate_paths(_m=1,_n=1):
        if (_m == m and _n == n):
            return 1
        elif (_m == m and _n != n): 
            return calculate_paths(_m,_n+1)
        elif (_m != m and _n == n):
            return calculate_paths(_m+1,_n)
        else:
            return calculate_paths(_m+1,_n) + calculate_paths(_m,_n+1)
    return calculate_paths()
run_docstring_examples(paths, globals(), True)