from doctest import run_docstring_examples

def unique_digits(n):
    """Return the number of unique digits in positive integer n.

    >>> unique_digits(8675309) # All are unique
    7
    >>> unique_digits(1313131) # 1 and 3
    2
    >>> unique_digits(13173131) # 1, 3, and 7
    3
    >>> unique_digits(10000) # 0 and 1
    2
    >>> unique_digits(101) # 0 and 1
    2
    >>> unique_digits(10) # 0 and 1
    2
    """
    "*** YOUR CODE HERE ***"
    unique = 0
    while n > 0:
        k = n % 10
        n = n // 10
        if not has_digit(n,k):
            unique = unique + 1
    print(unique)

def has_digit(n, k):
    """Returns whether K is a digit in N.
    >>> has_digit(10, 1)
    True
    >>> has_digit(12, 7)
    False
    """
    "*** YOUR CODE HERE ***"

    currentDigit = n % 10

    if n == 0:
        return False
    elif k == currentDigit:
        return True
    else:
        n = n // 10
        has_digit(n,k)

        
# run_docstring_examples(unique_digits, globals(), True)
unique_digits(100000)