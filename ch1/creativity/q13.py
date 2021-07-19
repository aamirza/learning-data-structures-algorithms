"""
Write a pseudo-code description of a function that reverses a list of n integers, so that the numbers are listed in the
opposite order they were before, and compare this method to an equivalent Python function for doing the same thing.
"""
import time


def reverse_ints(ints):
    '''
    >>> a = [6, 7, 3, 2, 1]
    >>> reversed_a = reverse_ints(a)
    >>> reversed_a == [1, 2, 3, 7, 6]
    True
    >>> a.reverse()
    >>> reversed_a == a
    True
    '''
    return ints[-1::-1]


"""
Write a short Python function that takes a sequence of integer values and determines if there is a distinct pair of
numbers in the sequence whose product is odd.
"""

def has_odd_products(ints):
    """
    Checks if there is a distinct pair of numbers in the sequence whose product is odd.

    To do this, there must be at least two odd numbers.
    >>> a = [2] * 99999
    >>> has_odd_products(a)
    False
    >>> a.append(9)
    >>> a.append(11)
    >>> has_odd_products(a)
    True
    """
    ints = set(ints)
    odd_number_count = 0
    for element in ints:
        if element % 2 == 1:
            odd_number_count += 1
            if odd_number_count >= 2:
                return True
    return False


"""
Demonstrate how to use Python's list comprehension syntax to produce the list [0, 2, 6, 12, 20, 30, 42, 56, 72, 90]
"""

def product_number_list():
    """
    >>> product_number_list()
    [0, 2, 6, 12, 20, 30, 42, 56, 72, 90]
    """
    return [x**2 + x for x in range(10)]

"""
Write a Python program that repeatedly reads lines from standard input until an EOFError is raised, and then outputs
those lines in reverse order (a user can indicate end of input by typing ctrl-D)
"""
