from doctest import run_docstring_examples

def is_prime(n):
    """
    >>> is_prime(2)
    True
    >>> is_prime(10)
    False
    >>> is_prime(4)
    False
    >>> is_prime(1) # one is not a prime number!!
    False
    """
    "*** YOUR CODE HERE ***"
    def check_prime(x=n-1):
        a = False
        if n == 1:
            a = False
        elif x <= 2:
            a = True
        elif (n % x == 0) :
            a = False
        else:
            check_prime(x-1)
        return a

    return check_prime()



run_docstring_examples(is_prime, globals(), True)
