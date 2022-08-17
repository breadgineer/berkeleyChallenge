from doctest import run_docstring_examples
def wears_jacket_with_if(temp, raining):
    """
    >>> wears_jacket_with_if(90, False)
    False
    >>> wears_jacket_with_if(40, False)
    True
    >>> wears_jacket_with_if(100, True)
    True
    """
    "*** YOUR CODE HERE ***"
    if temp <= 40 or raining:
        return True
    return False

run_docstring_examples(wears_jacket_with_if, globals(), True)