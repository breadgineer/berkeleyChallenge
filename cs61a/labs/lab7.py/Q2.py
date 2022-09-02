from doctest import run_docstring_examples
from Link import Link
from Tree import Tree

def store_digits(n):
    """Stores the digits of a positive number n in a linked list.

    >>> s = store_digits(1)
    >>> s
    Link(1)
    >>> store_digits(2345)
    Link(2, Link(3, Link(4, Link(5))))
    >>> store_digits(876)
    Link(8, Link(7, Link(6)))
    >>> # a check for restricted functions
    >>> import inspect, re
    >>> cleaned = re.sub(r"#.*\\n", '', re.sub(r'"{3}[\s\S]*?"{3}', '', inspect.getsource(store_digits)))
    >>> print("Do not use str or reversed!") if any([r in cleaned for r in ["str", "reversed"]]) else None
    >>> link1 = Link(3, Link(Link(4), Link(5, Link(6))))
    """
    "*** YOUR CODE HERE ***"

    # if n == 0:
    #     return Link.empty
    # else:
    #     return Link(n%10,store_digits(n//10))

    result = Link.empty
    while n > 0:
        result = Link(n % 10, result)
        n //= 10
    return result


run_docstring_examples(store_digits, globals(), True)
