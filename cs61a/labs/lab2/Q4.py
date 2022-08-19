from operator import add, mul, mod
from doctest import run_docstring_examples
def lambda_curry2(func):
    """
    Returns a Curried version of a two-argument function FUNC.
    >>>
    >>> curried_add = lambda_curry2(add)
    >>> add_three = curried_add(3)
    >>> add_three(5)
    8
    >>> curried_mul = lambda_curry2(mul)
    >>> mul_5 = curried_mul(5)
    >>> mul_5(42)
    210
    >>> lambda_curry2(mod)(123)(10)
    3
    """
    "*** YOUR CODE HERE ***"
    return lambda x : lambda y: func(x,y)

    #This is the same!
    # def func2(x):
    #     def func3(y):
    #         return func(x,y)
    #     return func3
    # return func2
