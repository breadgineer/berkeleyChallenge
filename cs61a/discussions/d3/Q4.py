from doctest import run_docstring_examples

def is_prime(n):
    """Returns True if n is a prime number and False otherwise.

    >>> is_prime(2)
    True
    >>> is_prime(16)
    False
    >>> is_prime(521)
    True
    """
    "*** YOUR CODE HERE ***"
    def leprime(x):
        if x-1 == 1:
            print(True)
        elif n % (x-1) == 0:
            print(False)
        else:
            return leprime(x-1)
    
    
    leprime(n)
