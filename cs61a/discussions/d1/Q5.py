from doctest import run_docstring_examples

def fizzbuzz(x):
    """
    >>> result = fizzbuzz(16)
    1
    2
    fizz
    4
    buzz
    fizz
    7
    8
    fizz
    buzz
    11
    fizz
    13
    14
    fizzbuzz
    16
    >>> result is None  # No return value
    True
    """
    "*** YOUR CODE HERE ***"
    def step(n=1):
        if n <= x:
            if n % 3 == 0 and n % 5 == 0:
                print("fizzbuzz")
            elif n % 3 == 0:
                print("fizz")
            elif n % 5 == 0:
                print("buzz")
            else:
                print(n)
            step(n+1)
        else:
            return
    step()

run_docstring_examples(fizzbuzz, globals(), True)
