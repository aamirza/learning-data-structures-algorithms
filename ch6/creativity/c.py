# C-6.15
"""Suppose Alice has picked three distinct integers and placed them into a stack S in random order. Write a short,
straight-line piece of pseudo-code (with no loops or recursion) that uses only one comparison and only one variable x,
yet that results in variable x storing the largest of Alice's three integers with probability 2/3. Argue why your method
 is correct."""

# Pop the first number of the stack and assign it to x.
# Then compare S.first > x, if true then assign x to S.first
# Else x is the largest number.
# This will give you a 2/3 chance that x is the largest number.

# This is true because there is a 1/3 chance that each number in the queue is the largest one. If we are looking at 2
# numbers, then there is a 1/3 + 1/3 = 2/3 chance that the largest number is among them. Taking the largest one out of
# these two means there is a 2/3 chance that it is the largest one, with 1/3 chance that the remaining number is bigger.


# C-6.16
"""Modify the ArrayStack implementation so that the stack's capacity is limited to maxlen elements, where maxlen is
an optional parameter to the constructor (that defaults to None). If push is called when the stack is at full capacity,
throw a Full exception error."""

class Full(Exception):
    pass


class Empty(Exception):
    pass


class ArrayStack:
    def __init__(self, maxlen=None):
        self._data = [] if maxlen is None else [None] * maxlen
        self._maxlen = maxlen
        self._n = 0

    def __str__(self):
        return f"Stack({self._data[:self._n] if self._maxlen else self._data})"

    def __len__(self):
        return self._n if self._maxlen else len(self._data)

    def __eq__(self, other):
        if isinstance(other, list):
            return  self._data == other

    def pop(self):
        if self.is_empty():
            raise Empty('Stack is empty')

        if self._maxlen:
            value = self._data[self._n-1]
            self._data[self._n-1] = None
            self._n -= 1
        else:
            value = self._data.pop()
        return value

    def push(self, e):
        if self._maxlen and self._n == self._maxlen:
            raise Full

        if self._maxlen:
            self._data[self._n] = e
            self._n += 1
        else:
            self._data.append(e)

    def top(self):
        if self.is_empty():
            raise Empty('Stack is empty')
        return self._data[-1]

    def is_empty(self):
        return self._n == 0 if self._maxlen else len(self._data) == 0

# C-6.17
"""In the previous exercise, we assuem that the underlying list is initially empty. Redo the exercise, this time 
preallocating an underlying list with length equal to the stack's maximum capacity."""

# Implemented above!

# s = ArrayStack(maxlen=5)
# print(s)
# s.push(4)
# s.push(2)
# print(s)
# r = s.pop()
# print(r)
# print(s)
# print(len(s))
# s.push(5)
# s.push(9)
# s.push(8)
# s.push(6)
# print(s)
# print(s.pop())
# print(s.pop())
# print(s.pop())
# print(s.pop())
# print(s.pop())
# print(s.pop())

# C-6.18
"""
Show how to use the transfer function, described in Exercise R-6.3, and two temporary stacks, to replace the contents of
a given stack S with those same elements, but in reversed order.
"""

"""
from collections import deque


def transfer(S: deque, T: deque):
    while len(S) > 0:
        T.append(S.pop())

S = deque([5, 2, 9, 4])
T = deque([])

transfer(S, T)
S = T
print(S)
"""


# C-6.19
"""In Code Fragment 6.5 we assume that opening tags in HTML have form <name>, as with <li>. More generally, HTML allows
optional attributes to be expressed as part of an opening tag. The general form used is <name attribute1='value' 
attribute2='value2'>. Modify Code Fragment 6.5 so that it can properly match tags, even when an opening tag may include
one or more such attributes."""

def is_matched_html(raw):
    """Return True if all HTML tags are properly matched; False otherwise."""
    S = ArrayStack()
    j = raw.find('<')
    while j != -1:
        k = raw.find('>', j+1)
        if k == -1:
            return False
        tag = raw[j+1:k]
        if not tag.startswith('/'):
            tag_end_position = raw.find(' ', j+1)
            if tag_end_position == -1:
                tag_name = tag
            else:
                tag_name = raw[j+1:tag_end_position]
            print(tag_name)
            S.push(tag_name)
        else:
            if S.is_empty():
                return False
            if tag[1:] != S.pop():
                return False
        j = raw.find('<', k+1)
    return S.is_empty()

s = "<html lang='en'><table row=3><tr></tr></table></html>"

print(is_matched_html(s))

# C-6.20
"""Describe a nonrecursive algorithm for enumerating all permutations of the numbers {1, 2, ..., n} using an explicit
stack."""

# TODO: Super difficult! Come back to it later.
