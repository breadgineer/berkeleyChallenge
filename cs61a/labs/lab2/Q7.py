from doctest import run_docstring_examples
def cycle(f1, f2, f3):
    """Returns a function that is itself a higher-order function.

    >>> def add1(x):
    ...     return x + 1
    >>> def times2(x):
    ...     return x * 2
    >>> def add3(x):
    ...     return x + 3
    >>> my_cycle = cycle(add1, times2, add3)
    >>> identity = my_cycle(0)
    >>> identity(5)
    5
    >>> add_one_then_double = my_cycle(2)
    >>> add_one_then_double(1)
    4
    >>> do_all_functions = my_cycle(3)
    >>> do_all_functions(2)
    9
    >>> do_more_than_a_cycle = my_cycle(4)
    >>> do_more_than_a_cycle(2)
    10
    >>> do_two_cycles = my_cycle(6)
    >>> do_two_cycles(1)
    19

    """
    "*** YOUR CODE HERE ***"
    # def ret_fn(n):
    #         def ret(x):
    #             if n == 0:
    #                 return x
    #             return cycle(f2, f3, f1)(n - 1)(f1(x))
    #         return ret
    # return ret_fn

    return lambda n: lambda x: x if n == 0 else cycle(f2, f3, f1)(n - 1)(f1(x))