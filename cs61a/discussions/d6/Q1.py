from doctest import run_docstring_examples
from pet import Pet
class Cat(Pet):

    def __init__(self, name, owner, lives=9):
        "*** YOUR CODE HERE ***"
        super().__init__(name,owner)
        self.lives = lives

    def talk(self):
        """Print out a cat's greeting.

        >>> Cat('Thomas', 'Tammy').talk()
        Thomas says meow!
        """
        "*** YOUR CODE HERE ***"
        print(self.name + " says meow!")

    def lose_life(self):
        """Decrements a cat's life by 1. When lives reaches zero,
        is_alive becomes False. If this is called after lives has
        reached zero, print 'This cat has no more lives to lose.'
        """
        "*** YOUR CODE HERE ***"
        if self.lives == 0:
            self.is_alive = False
            self.lives -= 1
        elif self.lives < 0:
            print("This cat has no more lives to lose.")
            self.lives = 0
        else:
            self.lives -= 1

run_docstring_examples(Cat, globals(), True) 
