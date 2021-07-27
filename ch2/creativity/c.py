"""Creativity questions"""

"""Suppose you are on the design team for a new e-book reader. What are the primary classes and methods that the
Python software for your reader will need? You should include an inheritance diagram for this code, but you do
not need to write any actual code. Your software architecture should at least include ways for customers to buy
new books, view their list of purchased books, and read their purchased books."""

# TODO: Finish later... but it's like my Bookworm program, which you can also create a UML diagram for.

"""Exercises R-2.12 uses the __mul__ method to support multiplying a Vector by a number, while Exercise R-2.14 uses
the __mul__ method t o support computing a dot product of two vectors. Give a single implementation of Vector.__mul__
that uses run-time type checking to support both syntaxes u * v and u * k, where u and v designate vector instances
and k represents a number."""

# Already implemented.

"""The SequenceIterator class of Section 2.3.4 provides what is known as a forward iterator. Implement a class named
ReversedSequenceIterator that serveres as a reverse iterator fo any Python sequence type. The first call to next should
return the last element of the sequence, the second call to next should return the second-to-last element and so forth.
"""

class SequenceIterator:
    """An iterator for any of Python's sequence types"""
    def __init__(self, sequence):
        """Create an iterator for the given sequence."""
        self._seq = sequence  # keep a reference to the underlying data
        self._k = -1  # will increment to 0 on first call to next

    def __next__(self):
        self._k += 1
        if self._k < len(self._seq):
            return (self._seq[self._k])  # Return the data element
        else:
            raise StopIteration()

    def __iter__(self):
        """By convention, an iterator must return itself as an iterator."""
        return self


class ReversedSequenceIterator:
    def __init__(self, sequence):
        self._seq = sequence
        self._k = 0

    def __next__(self):
        self._k -= 1
        if abs(self._k) <= len(self._seq):
            return(self._seq[self._k])
        else:
            raise StopIteration()

    def __iter__(self):
        return self


"""In Section 2.3.5, we note that our version of the Range class has implicit support for iteration, due to its explicit
support of both __len__ and __getitem__. The class also receivs implicit support of the Boolean test, "k in r" for 
Range r. This test is evaluated based on a forward iterator through the range, as evidence by the relative quickness of
the test 2 in Range(100000000) vers 9999999 in Range(100000000). Provide a more efficient implementation of the 
__contains__ method to determine whether a particular value lies within a given range. """

class Range:
    """A class that mimic's the built-in range class."""
    def __init__(self, start, stop=None, step=1):
        """Initialize a Range instance.

        Semantics is similar to built-in range class.
        """
        if step == 0:
            raise ValueError('step cannot be 0')

        if stop is None:
            start, stop = 0, start

        # calculate the effective length once
        self._length = max(0, (stop - start + step -1) // step)

        # need knowledge of start and step to support __getitem__
        self._start = start
        self._step = step

    def __contains__(self, item):
        return (item - self._start) % self._step == 0

    def __len__(self):
        """Return number of entries in the range."""
        return self._length

    def __getitem__(self, k):
        """Return entry at index k (using standard interpretation if negative)."""
        if k < 0:
            k += len(self)

        if not 0 <= k < self.length:
            raise IndexError('index out of range')

        return self._start + k * self._step


"""The PredatoryCreditCard class of Section 2.4.1 provides a process_month method that models the completion of a 
monthly cycle. Modify the class so that once a customer has made ten calls to charge in the currrent month, each
additional call to that function results in an additional $1 surcharge."""


class CreditCard:
    def __init__(self, customer, bank, account, limit, balance=0):
        self._customer = customer
        self._bank = bank
        self._account = account
        self._limit = limit
        self._balance = balance

    def get_customer(self):
        return self._customer

    def get_bank(self):
        return self._bank

    def get_account(self):
        return self._account

    def get_balance(self):
        return self._balance

    def charge(self, price):
        if price + self._balance > self._limit:
            return False
        else:
            self._add_to_balance(price)
            return True

    def make_payment(self, amount):
        self._balance -= amount

    def _set_balance(self, balance):
        self._balance = balance

    def _add_to_balance(self, amount):
        self._set_balance(self._balance + amount)


class PredatoryCreditCard(CreditCard):
    def __init__(self, customer, bank, account, limit, apr, balance=0, min_monthly_payment=0.1):
        super().__init__(customer, bank, account, limit, balance)
        self._apr = apr
        self._monthly_calls = 0
        self._monthly_payment = 0
        self._late_fee = 50
        self._min_monthly_payment = min_monthly_payment

    def charge(self, price):
        self._monthly_calls += 1
        success = super().charge(price)
        if not success:
            self._add_to_balance(5)
        return success

    def process_month(self):
        if self._balance > 0:
            monthly_factor = pow(1 + self._apr, 1/12)
            super()._set_balance(self.get_balance() * monthly_factor)

        # If made more than 10 charges, charge additional $1 for each charge.
        if self._monthly_calls > 10:
            super()._add_to_balance(self._monthly_calls - 10)
        self._monthly_calls = 0

        # If minimum amount not paid, charge late fee.
        if self._monthly_payment < (self.get_balance() * self._min_monthly_payment):
            super()._add_to_balance(self._late_fee)
        self._monthly_payment = 0

    def make_payment(self, amount):
        super().make_payment(amount)
        self._monthly_payment += amount


"""Modify the PredatoryCreditCard class from Section 2.4.1 so that a customer is assigned a minimum monthly payment, as
a percentage of the balance, and so that a late fee is assessed if the customer does not subsequently pay that minimum
amount before the next monthly cycle."""

# Implemented above!

"""At the close of Section 2.4.1, we suggest a model in which the CreditCard class supports a nonpublic method, 
_set_balance(b), that could be used by subclasses to affect a change to the balance, without directly accessing the
_balance data member. Implement such a model, revising both the CreditCard and PredatoryCreditCard classes accordingly
"""

# Implemented above!

"""
Write a Python class that extends the Progression class so that each value in the progression is the absolute value of 
the difference between the previous two values. 
"""

class Progression:
    """Iterator producing a generic progression.

    Default iterator produces the whole numbers 0, 1, 2, ...
    """
    def __init__(self, start=0):
        """Initialize current to the first value of the progression."""
        self._current = start

    def _advance(self):
        """Update self._current to a new value.

        This should be overriden by a subclass to customize progression.

        By convention, ifcurrent is set to None, this designates the end of a finite progression."""
        self._current += 1

    def __next__(self):
        """Return the next element, or else raise StopIteration error."""
        if self._current is None:
            raise StopIteration()
        else:
            answer = self._current
            self._advance()
            return answer

    def __iter__(self):
        """By convention, an iterator must return itself as an iterator."""
        return self

    def print_progression(self, n):
        """Print next n values of the progression."""
        print(' '.join(str(next(self)) for j in range(n)))


class DifferenceProgression(Progression):
    def __init__(self, first=2, second=200):
        difference = second - first
        super().__init__(difference)
        self._previous_number = second

    def _advance(self):
        self._current, self._previous_number = abs(self._current - self._previous_number), self._current
        if self._current == 0 and self._previous_number == 0:
            self._current = None


"""Write a Python class that extends the Progression class so that each value in the progression is the square root
of the previous value. (Note that you can no longer represent each value with an integer.) Your construct should accept
an optional parameter specifying the start value, using 65,536 as a default."""

class SquareRootProgression(Progression):
    def __init__(self, start_value=65536):
        super().__init__(start_value)

    def _advance(self):
        self._current = self._current ** 0.5


if __name__ == "__main__":
    sequence = [1, 2, 3, 4, 5]
    assert list(SequenceIterator(sequence)) == [1, 2, 3, 4, 5]
    assert list(ReversedSequenceIterator(sequence)) == [5, 4, 3, 2, 1]

    a = Range(5, 59, 9)
    assert 23 in a
    assert 27 not in a
    assert 9999999 in Range(10000000)

    diff_progression = DifferenceProgression()
    assert [next(diff_progression) for x in range(5)] == [198, 2, 196, 194, 2]

    root_progression = SquareRootProgression()
    assert [next(root_progression) for x in range(5)] == [65536, 256, 16, 4, 2]
