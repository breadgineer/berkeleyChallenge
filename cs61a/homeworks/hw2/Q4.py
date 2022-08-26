from doctest import run_docstring_examples
from math import prod
from operator import add, mul
from functions import *


def funception(func_a, start):
    """ Takes in a function (function A) and a start value.
    Returns a function (function B) that will find the product of
    function A applied to the range of numbers from
    start (inclusive) to stop (exclusive)

    >>> def func_a(num):
    ...     return num + 1
    >>> func_b1 = funception(func_a, 0)
    >>> func_b1(3)    # func_a(0) * func_a(1) * func_a(2) = 1 * 2 * 3 = 6
    6
    >>> func_b2 = funception(func_a, 1)
    >>> func_b2(4)    # func_a(1) * func_a(2) * func_a(3) = 2 * 3 * 4 = 24
    24
    >>> func_b3 = funception(func_a, 3)
    >>> func_b3(2)    # Returns func_a(3) since start > stop
    4
    >>> func_b4 = funception(func_a, -2)
    >>> func_b4(-3)    # Returns None since start < 0
    >>> func_b5 = funception(func_a, -1)
    >>> func_b5(4)    # Returns None since start < 0
    """
    "*** YOUR CODE HERE ***"
    def func_b(stop):
        if start < 0:
            return None
        elif start > stop:
            return func_a(start)
        else:
            return func_a(stop) * func_b(stop-1)
            
    return func_b
run_docstring_examples(funception, globals(), True)