"""Give three examples of life critical software"""

def life_critical_software():
    return [
        "Programmable dialysis machine",
        "Ventillator",
        "Automatic braking system",
    ]


"""Give an example of a software application in which adaptability can mean the difference between a prolonged
lifetime of sales and bankruptcy"""

def adaptability():
    return "Adaptability is writing your code so that it is future-proof as possible. An example of this can be an " \
           "e-commerce website that allows multiple payment methods and has the ability to easily add more (via the " \
           "software architecture) compared to a website where a single payment method is hardcoded in and it is " \
           "difficult to add a new one."


"""Describe a component from a text-editor GUI and the methods that it encapsulates"""

def text_editor_gui():
    class WordCounter():
        def __init__(self, document):
            self._document = document

        def get_word_count(self):
            pass

        def get_character_count(self):
            pass

        def get_paragraph_count(self):
            pass

        def get_page_count(self):
            pass

        def get_space_count(self):
            pass

        def get_character_count_without_spaces(self):
            return self.get_character_count() - self.get_space_count()

"""Write a Python class, Flower, that has three instance variables of type str, int and float, that respectively 
represent the name of the flower, its number of petals, and its price."""


class Flower():
    def __init__(self, name, num_petals=0, price=-1):
        self._name = name
        self._num_petals = num_petals
        self._price = price

    def set_name(self, name):
        self._name = name

    def set_num_petals(self, num_petals):
        self._num_petals = num_petals

    def set_price(self, price):
        self._price = price

    def get_name(self):
        return self._name

    def get_num_petals(self):
        return self._num_petals

    def get_price(self):
        return self._price


"""Use the techniques of Section 1.7 to revise the charge and make_payment methods of the CreditCard class to ensure
that the caller sends a number as a parameter"""


def charge(self, amount):
    try:
        amount = float(amount)
    except ValueError:
        print("Invalid amount.")

# make_payment in then ext question.


"""If the parameter to make_payment method of the CreditCard class were a negative number that would have the effect
of raising the balance of hte account. Revise the implementation so that it raises a ValueError if a negative number
is sent."""


def make_payment(self, amount):
    try:
        amount = float(amount)
        if amount < 0:
            raise ValueError
    except ValueError:
        print("Invalid amount attempted to charge. Payment will not go through.")


"""The CreditCard class of Section 2.3 initializes the balance of a new account to zero. Modify that class so that a 
new account can be given a nonzero balance using an optional fifth parameter to the constructor. The four-parameter
constructor syntax should continue to produce an account with zero balance."""


class CreditCard:
    def __init__(self, customer, bank, account, limit, balance=0):
        self._customer = customer
        self._bank = bank
        self._account = account
        self._limit = limit
        self._balance = balance

"""Modify the declaration of the first for loop in the CreditCard tests, from Code Fragment 2.3, so that it will 
eventually cause exactly one of the three credit cards to go over its credit limit. Which credit card is it?"""

def tests():
    # I didn't write this code.
    wallet = []
    wallet.append(CreditCard('John Bowman', 'California Savings', '5391 0375 9387 5309', 2500))
    wallet.append(CreditCard('John Bowman', 'California Federal', '3485 0399 3395 1954', 3500))
    wallet.append(CreditCard('John Bowman', 'California Finance', '5391 0375 9387 5309', 5000))

    for val in range(1, 59):
        wallet[0].charge(val)
        wallet[1].charge(2*val)
        wallet[2].charge(3*val)

"""
Thought process:
3 times as much gets charged for the 3rd wallet compared to the 1st, and 1.5 as much compared to the 2nd.

By the time 5000 is spent in the 3rd wallet, 1666.66 will be charged for the 1st wallet, and 3333.33 will be charged 
to the 2nd wallet. Therefore 3rd wallet runs out first.

This happens after 3n(n+1)/2 = 5000, 
or n^2 + n - 3333.33 = 0, 
or roughly (n + 58) (n - 57) 
or n = 59 attempts (59 > 58)
"""

"""
Implement the __sub__ method for the Vector class of Section 2.3.3, so that the expression u-v returns a new vector
representing the difference between two vectors.
"""

class Vector:
    """Represent a vector in a multidimensional space."""
    def __init__(self, *args):
        if len(args) == 1:
            self._coords = [0] * args[0]
        elif len(args) > 1:
            self._coords = list(args)

    def __len__(self):
        """Return the dimension of the vector."""
        return len(self._coords)

    def __getitem__(self, j):
        """Return jth coordinate of vector."""
        return self._coords[j]

    def __setitem__(self, j, val):
        """Set jth coordinate of vector to given value."""
        self._coords[j] = val

    def __add__(self, other):
        """Return sum of two vectors."""
        if len(self) != len(other):
            # relies on __len__ method
            raise ValueError("dimensions must agree")
        result = Vector(len(self))  # start with vector of zeros
        for j in range(len(self)):
            result[j] = self[j] + other[j]
        return result

    def __radd__(self, other):
        return self + other

    def __sub__(self, other):
        """Subtract vector from another"""
        if len(self) != len(other):
            raise ValueError("dimensions must agree")
        result = Vector(len(self))
        for j in range(len(self)):
            result[j] = self[j] - other[j]
        return result

    def __neg__(self):
        result = Vector(len(self))
        for j in range(len(self)):
            result[j] = -1 * self._coords[j]
        return result

    def __mul__(self, other):
        if isinstance(other, (int, float)):
            other = [other] * len(self)  # Create a new vector composed entirely of the multiple

        result = Vector(len(self))
        for j in range(len(self)):
            result[j] = self._coords[j] * other[j]
        return result

    def __rmul__(self, multiple):
        return self * multiple

    def __eq__(self, other):
        """Return True if vector has same coordinates as other."""
        return self._coords == other._coords

    def __ne__(self, other):
        """Return True if vector differs from other."""
        return not self == other  # rely on existing __eq__ definition

    def __str__(self):
        """Produce string representation of vector."""
        return  '<' + str(self._coords)[1:-1] + '>' # adapt list representation


"""Implement the __neg__ method"""

# Implemented above!

"""In section 2.3.3, we note that our Vector class supports a syntax such that v = u + [5, 3, 10, -2, 1], in which the
sum of a vector and list returns a new vector. However, the syntax v = [5, 3, 10, -2, 1] + u is illegal. Explain how
the Vector class definition can be revised so that this syntax generates a new vector."""

# Implemented above!


"""Implement the __mul__ method for the Vector class of Section 2.3.3, so that the expression v * 3 returns a new vector
with coordinates that are 3 times the respective coordinates of v."""

# Implemented above!

"""The exercise above asks for an implementation of __mul__, to provide support for the syntax v * 3. Implement the
__rmul__ method, to provide additional support for syntax 3 * v"""

# Implemented above!

"""Implement the __mul__ method for the Vector class, so that the expression u * v returns a scalar that represents 
the dot product of the vectors."""

# Implemented above!

"""The Vector class provides a constructor that takes an integer d, and produces a d-dimensional vector with all 
coordinates equal to 0. Another convenient form for creating a new vector would be to send the constructor a parameter
that is some iterable type representing a sequence of numbers. Modify the constructor so that either an iterable or
integer is acceptable."""

# Implemented above! I used *args instead of taking an iterable, since that feels more intuitive.

"""Our Range class relies on the formula

max(0, (stop - start + step - 1) // step)

to compute the number of elements in the range. Justify this formula, in your own words."""

# TODO: skip for now

"""Give a short fragment of Python code that uses the progression classes from Section 2.4.2 to find the 8th value
of a Fibonacci progression that starts with 2 and 2 as its first value"""

# for index, x in enumerate(FibonacciProgression(2, 2)):
#     if index == 7:
#         return x
# 2, 2, 4, 6, 10, 16, 26, 42

"""When using the ArithmeticProgression class of Section 2.4.2 with an increment of 128 and a start of 0, how many
calls to next can we make before we reach an integer of 2^63 or larger?"""

# 128 + 128 + 128...
# 128n
# 2^63 = 128n
# n = 2^63/128
# n = (7.21 * 10^16) + 1  # because we have to include 0

"""
What are some potential efficiency disadvantages of having very deep inheritance trees, that is, a large set of classes,
A, B, C, and so on, such that B extends A, C extends B, D extends C, etc.?
"""

# When looking for the right method or property, the Python interpreter first checks the base class, and failing that,
# checks all base classes that were inherited from. This time it takes to retrieve the right method/property increases
# as the nesting gets deeper.
#
# Also deep inheritance trees are more difficult for humans to understand.

"""
What are some potential efficiency disadvantages of having very shallow inheritance trees, that is, a large set of
classes A, B, C, and so on, such that all of these extend a single class, Z?
"""

# Not much code gets reused.

"""
The collections.Sequence abstract base class does not provide support for comparing two sequences to each other. Modify
our Sequence class from Code Fragment 2.14 to include a definition for the __eq__ method, so that expresion seq1 == seq2
will return True precisely when the two sequences are element by element equivalent.
"""

from abc import ABCMeta, abstractmethod


class Sequence(metaclass=ABCMeta):
    """Our own version of collections.Sequence abstract base class"""

    @abstractmethod
    def __len__(self):
        """Return the length of the sequence"""

    @abstractmethod
    def __getitem(self, j):
        """Returns the element at index j of the sequence."""

    def __eq__(self, other):
        if len(self) != len(other):
            return False

        for j in range(len(self)):
            if self[j] != other[j]:
                return False
        return True

    def __lt__(self, other):
        for j in range(len(self)):
            if self[j] < other[j]:
                return True
            elif self[j] > other[j]:
                return False
        return False

    def __contains__(self, val):
        """Return True is val found in the sequence; False otherwise."""
        for j in range(len(self)):
            if self[j] == val:
                return True
        return False

    def index(self, val):
        """Return the number of elements equal to a given value."""
        for j in range(len(self)):
            if self[j] == val:
                return j
        raise ValueError('value not in sequence')

    def count(self, val):
        """Return the number of elements equal to a given value."""
        k = 0
        for j in range(len(self)):
            if self[j] == val:
                k += 1
        return k


"""In similar spirit to the previous problem, augment the Sequence class with method __lt__, to support lexicographic
comparison seq1 < seq2"""

# implemented above!


# tests
if __name__ == "__main__":
    original = Vector(3)
    original[1] = 4
    original[2] = 1

    another = Vector(3)
    another[0] = 5
    another[1] = 2

    answer = Vector(3)
    answer[0], answer[1], answer[2] = -5, 2, 1

    assert (original - another) == answer, "Vectors don't match!"

    negative_original = Vector(3)
    negative_original[1], negative_original[2] = -4, -1
    assert -original == negative_original, "The negative of the vector isn't correct"
    assert original != negative_original, "The original value of the vector changed during negation"

    assert [5, 2, 4] + original == original + [5, 2, 4]

    same_vector = Vector(3)
    same_vector[0], same_vector[1], same_vector[2] = 0, 12, 3
    assert original * 3 == same_vector, f"{original * 3} and {same_vector} are not the same!"
    assert 3 * original == same_vector,  f"Right multiply is not working"

    multiplied_vector = Vector(3)
    multiplied_vector[0], multiplied_vector[1], multiplied_vector[2] = 0, 8, 0
    assert original * another == multiplied_vector, f"{original * another} and {multiplied_vector} are not the same!"

    assert Vector(0, 0, 0) == Vector(3)
    assert Vector(0, 4, 1) == original

    # Checking __mul__ for C-2.25
    assert Vector(1, 4, 3) * Vector(2, 5, 4) == Vector(2, 20, 12)
    assert Vector(5, 2, 8) * 3 == Vector(15, 6, 24)
