from doctest import run_docstring_examples
def hailstone(n):
    """Print the hailstone sequence starting at n and return its
    length.

    >>> a = hailstone(10)
    10
    5
    16
    8
    4
    2
    1
    >>> a
    7
    >>> b = hailstone(1)
    1
    >>> b
    1
    """
    "*** YOUR CODE HERE ***"
    count = 1
    print(n)
    while n >1:
        if n % 2 == 0:
            n = n//2
        else:
            n = (n*3) + 1
        count = count + 1
        print(n)
    
    return count