from doctest import run_docstring_examples

def pascal(row, column):
    """Returns the value of the item in Pascal's Triangle
    whose position is specified by row and column.
    >>> pascal(0, 0)    # The top left (the point of the triangle)
    1
    >>> pascal(0, 5)	# Empty entry; outside of Pascal's Triangle
    0
    >>> pascal(3, 2)	# Row 3 (1 3 3 1), Column 2
    3
    >>> pascal(4, 2)     # Row 4 (1 4 6 4 1), Column 2
    6
    """
    "*** YOUR CODE HERE ***"
    pascalNumbers = [1]
    def calculate_pascal(row):
        if column == 0:
            return 1
        elif row == 0:
            return 0
        else:
            return [pascal(row-1, column)] + [pascal(row-1, column-1)]
    pascalNumbers = pascalNumbers + [calculate_pascal(row)]
    return pascalNumbers
# run_docstring_examples(pascal, globals(), True)
print(pascal(2,3))