from doctest import run_docstring_examples
from re import T
def double_eights(n):
    """Return true if n has two eights in a row.
    >>> double_eights(8)
    False
    >>> double_eights(88)
    True
    >>> double_eights(2882)
    True
    >>> double_eights(880088)
    True
    >>> double_eights(12345)
    False
    >>> double_eights(80808080)
    False
    """
    "*** YOUR CODE HERE ***"
    firstNumber = n % 10
    secondNumber = (n // 10) % 10
    if n < 10:
        print(False)
    elif firstNumber == secondNumber:
        print(True)
    else:
        double_eights(n//10)
