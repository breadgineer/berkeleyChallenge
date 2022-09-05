from doctest import run_docstring_examples
from genericpath import exists

class VendingMachine:
    """A vending machine that vends some product for some price.

    >>> v = VendingMachine('candy', 10)
    >>> v.vend()
    'Nothing left to vend. Please restock.'
    >>> v.add_funds(15)
    'Nothing left to vend. Please restock. Here is your $15.'
    >>> v.restock(2)
    'Current candy stock: 2'
    >>> v.vend()
    'Please update your balance with $10 more funds.'
    >>> v.add_funds(7)
    'Current balance: $7'
    >>> v.vend()
    'Please update your balance with $3 more funds.'
    >>> v.add_funds(5)
    'Current balance: $12'
    >>> v.vend()
    'Here is your candy and $2 change.'
    >>> v.add_funds(10)
    'Current balance: $10'
    >>> v.vend()
    'Here is your candy.'
    >>> v.add_funds(15)
    'Nothing left to vend. Please restock. Here is your $15.'

    >>> w = VendingMachine('soda', 2)
    >>> w.restock(3)
    'Current soda stock: 3'
    >>> w.restock(3)
    'Current soda stock: 6'
    >>> w.add_funds(2)
    'Current balance: $2'
    >>> w.vend()
    'Here is your soda.'
    """
    "*** YOUR CODE HERE ***"

    def __init__(self,item,price) :
        self.item = item
        self.price = price
        self.stock = 0
        self.funds = 0

    def vend(self):
        if self.stock == 0:
            return 'Nothing left to vend. Please restock.'
        difference = self.price - self.funds
        if difference > 0:
            return f'Please update your balance with ${difference} more funds.'
        message = f'Here is your {self.item}'
        if difference != 0:
            message += f' and ${-difference} change'
        self.funds = 0
        self.stock -= 1
        return message + '.'


    def restock(self,quantity):
        self.stock += quantity
        return f'Current {self.item} stock: {self.stock}'

    def add_funds(self,cash):
        if self.stock > 0:
            self.funds += cash
            return f'Current balance: ${self.funds}'
        else:
            return f'Nothing left to vend. Please restock. Here is your ${cash}.'



        

run_docstring_examples(VendingMachine, globals(), True)