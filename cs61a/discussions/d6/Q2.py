from Q1 import Cat
# from doctest import run_docstring_examples
class NoisyCat(Cat):
    """A Cat that repeats things twice."""
    def __init__(self, name, owner, lives=9):
        # Is this method necessary? Why or why not?
        "*** YOUR CODE HERE ***"
        super().__init__(name,owner,lives)

    def talk(self):
        """Talks twice as much as a regular cat.
        >>> NoisyCat('Magic', 'James').talk()
        Magic says meow!
        Magic says meow!
        """
        "*** YOUR CODE HERE ***"
        super().talk() 
        super().talk()
# run_docstring_examples(Cat, globals(), True) 

a = NoisyCat('Thomas', 'Tammy')
a.talk()