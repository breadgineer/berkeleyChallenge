from doctest import run_docstring_examples

def count_k(n, k):
    """ Counts the number of paths up a flight of n stairs
    when taking up to and including k steps at a time.
    >>> count_k(3, 3) # 3, 2 + 1, 1 + 2, 1 + 1 + 1
    4
    >>> count_k(4, 4)
    8
    >>> count_k(10, 3)
    274
    >>> count_k(300, 1) # Only one step at a time
    1
    """
    "*** YOUR CODE HERE ***"
    # if k == 1:
    #     return 1
    # elif k == 2:
    #     if n == 1:
    #         return 1
    #     elif n == 2:
    #         return 2
    #     else:
    #         return count_k(n-1, k) + count_k(n-2, k)
    # else:
    #     return count_k(n,k-1) + count_k(n,k-2) 

    if n == 0:
        return 1
    elif n < 0:
        return 0
    else:
        total = 0
        i = 1
        while i <= k:
            total += count_k(n - i, k)
            i += 1
        return total