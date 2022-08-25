from doctest import run_docstring_examples
from operator import index

def even_weighted(s):
    """
    >>> x = [1, 2, 3, 4, 5, 6]
    >>> even_weighted(x)
    [0, 6, 20]
    """
    return [i*s.index(i) for i in s if s.index(i) % 2 == 0 ]
    
run_docstring_examples(even_weighted, globals(), True)