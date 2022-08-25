from doctest import run_docstring_examples

import functools
def count_palindromes(L):
    """The number of palindromic words in the sequence of strings
    L (ignoring case).

    >>> count_palindromes(("Acme", "Madam", "Pivot", "Pip"))
    2
    """
    return len(list(filter(lambda x: x == x[::-1],map(lambda x: x.lower(),L))))
    
run_docstring_examples(count_palindromes, globals(), True)