from doctest import run_docstring_examples

def merge(lst1, lst2):
    """Merges two sorted lists.

    >>> s1 = [1, 3, 5]
    >>> s2 = [2, 4, 6]
    >>> merge(s1, s2)
    [1, 2, 3, 4, 5, 6]
    >>> s1
    [1, 3, 5]
    >>> s2
    [2, 4, 6]
    >>> merge([], [2, 4, 6])
    [2, 4, 6]
    >>> merge([1, 2, 3], [])
    [1, 2, 3]
    >>> merge([5, 7], [2, 4, 6])
    [2, 4, 5, 6, 7]
    >>> merge([2, 3, 4], [2, 4, 6])
    [2, 2, 3, 4, 4, 6]
    """
    "*** YOUR CODE HERE ***"

    lst = lst1 + lst2

    def sort_list(lst,i=1):
        if i == 0:
            return sort_list(lst,i+1)
        if len(lst) == i:
            return lst
        elif lst[i] < lst[i-1]:
            x,y = lst[i], lst[i-1]
            lst[i-1] = x
            lst[i] = y
            return sort_list(lst,i-1)
        else:
            return sort_list(lst,i+1)
    
    return sort_list(lst)

    

run_docstring_examples(merge, globals(), True)