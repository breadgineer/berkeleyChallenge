from doctest import run_docstring_examples

def hailstone(n):
    """Yields the elements of the hailstone sequence starting at n.

    >>> for num in hailstone(10):
    ...     print(num)
    10
    5
    16
    8
    4
    2
    1
    """
    "*** YOUR CODE HERE ***"
    yield int(n)
    if n == 1:
        return None
    elif n % 2 == 0:
        yield from hailstone(n/2)
    else:
        yield from hailstone((n*3)+1)

run_docstring_examples(hailstone, globals(), True)