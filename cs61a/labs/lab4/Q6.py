from doctest import run_docstring_examples
class Minty:
    """A mint creates coins by stamping on years. The update method sets the mint's stamp to Minty.present_year.
    >>> mint = Minty()
    >>> mint.year
    2021
    >>> dime = mint.create('Dime')
    >>> dime.year
    2021
    >>> Minty.present_year = 2101  # Time passes
    >>> nickel = mint.create('Nickel')
    >>> nickel.year     # The mint has not updated its stamp yet
    2021
    >>> nickel.worth()  # 5 cents + (80 - 50 years)
    35
    >>> mint.update()   # The mint's year is updated to 2101
    >>> Minty.present_year = 2176     # More time passes
    >>> mint.create('Dime').worth()    # 10 cents + (75 - 50 years)
    35
    >>> Minty().create('Dime').worth()  # A new mint has the current year
    10
    >>> dime.worth()     # 10 cents + (155 - 50 years)
    115
    """
    present_year = 2021

    def __init__(self):
        self.update()

    def create(self, type):
        "*** YOUR CODE HERE ***"
        return Coin(self.year,type)


    def update(self):
        "*** YOUR CODE HERE ***"
        self.year = Minty.present_year
       

class Coin:
    cents = 50
    def __init__(self, year, type):
        "*** YOUR CODE HERE ***"
        denominations = {
            'Nickel':5,
            'Dime':10
        }
        self.cents = denominations[type] 
        self.year = year

    def worth(self):
        "*** YOUR CODE HERE ***"
        age =  Minty.present_year - self.year
        value = self.cents if age <= 50 else  self.cents + age - 50
        return value

run_docstring_examples(Minty, globals(), True) 