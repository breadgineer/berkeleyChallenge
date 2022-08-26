from doctest import run_docstring_examples

def summation(n, term):
    """Return the sum of numbers 1 through n (including n) wíth term applied to each number.
    Implement using recursion!

    >>> summation(5, lambda x: x * x * x) # 1^3 + 2^3 + 3^3 + 4^3 + 5^3
    225
    >>> summation(9, lambda x: x + 1) # 2 + 3 + 4 + 5 + 6 + 7 + 8 + 9 + 10
    54
    >>> summation(5, lambda x: 2**x) # 2^1 + 2^2 + 2^3 + 2^4 + 2^5
    62

    """
    assert n >= 1
    "*** YOUR CODE HERE ***"
    
    def aux_summation(_n=1):
        if _n == n:
            return term(n)
        else:
            return term(_n) + aux_summation(_n + 1)
    
    return aux_summation()

run_docstring_examples(summation, globals(), True)