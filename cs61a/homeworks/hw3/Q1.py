from doctest import run_docstring_examples
def num_eights(pos):
    """Returns the number of times 8 appears as a digit of pos.

    >>> num_eights(3)
    0
    >>> num_eights(8)
    1
    >>> num_eights(88888888)
    8
    >>> num_eights(2638)
    1
    >>> num_eights(86380)
    2
    >>> num_eights(12345)
    0
    """
    "*** YOUR CODE HERE ***"
    if pos % 10 == 8:
        return 1 + num_eights(pos // 10)
    elif pos < 10:
        return 0
    else:
        return num_eights(pos // 10)
run_docstring_examples(num_eights, globals(), True)