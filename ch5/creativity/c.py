# C-5.13
"""In the experiment of Code Fragment 5.1, we begin with an empty list. If data were initially constructed with nonempty
length, does this affect the sequence of values at which the underlying array is expanded? Perform your own experiments,
and comment on any relationship you see between the initial length and the expansion sequence. """
# import random
# import sys
# n = 30
# data = [None] * 80
# for k in range(n):
#     a = len(data)
#     b = sys.getsizeof(data)
#     print('Length: {0:3d}; Size in bytes: {1:4d}'.format(a, b))
#     data.append(None)
import copy
import math
import random
import time

"""The list always expands after the first append. How many appends you can do before the list expands again depends on 
initial size of the array. Larger values does seem to lead to a larger expansion sequence.

Overall, initializing the array seems to take up more memory than starting from nothing."""

# C-5.14
"""The shuffle method supported by the random module, takes a Python list and rearranges it so that every possible 
ordering is equally likely. Implement your own version of such a function. You may rely on randrange(n) function of the 
random module, which returns a random number between 0 and n-1 inclusive."""

def shuffle(S):
    length = len(S)
    for n in range(length):
        remaining = length - n
        random_element = random.randrange(remaining)
        popped = S.pop(random_element)
        S.append(popped)


# C-5.15
"""Consider an implementation of a dynamic array, but instead of copying the elements into an array of double the size 
(that is, from N to 2N) when its capacity is reached, we copy the elements into an array with ceil(N/4) additional cells,
going from capcity N to capacity N + ciel(N/4). Prove that performing a sequence of n append operations still runs in 
O(n) time in this case"""

# Say each append still costs 1 cyberdollar. Going from k to k + ceil(k/4) costs ceil(k/4) cyberdollars.
# Make each append cost 2 cyberdollars. By the time you need to expand you will add ceil(n/4) new cells to the array.
# When the array has an overflow at ceil(n/4) {1, 2, 3, 4, 5, 7, 9, 12, 15, 19, 24, 30, etc.} It should have enough
# cyberdollars stored to make the expansion. That is ceil(n/4) <= n, which is true.
# Therefore making each append cost 2n works out. Therefore the sequence performs at O(n)

# C-5.16
"""Implement a pop method for the DynamicArray class, given in Code Fragment 5.3, that removes the last element of an 
array and that shrinks the capacity, N, of the array by half any time the number of elements in the array goes below N/4
"""

import ctypes

class DynamicArray:
    def __init__(self):
        self._n = 0
        self._capacity = 1
        self._A = self._make_array(self._capacity)

    def __len__(self):
        return self._n

    def __getitem__(self, k):
        if not (-1 * self._n) <= k < self._n:
            raise IndexError('invalid index')
        return self._A[k]

    def append(self, obj):
        if self._n == self._capacity:
            self._resize(2 * self._capacity)
        self._A[self._n] = obj
        self._n += 1

    def _resize(self, c):
        B = self._make_array(c)
        for k in range(self._n):
            B[k] = self._A[k]
        self._A = B
        self._capacity = c

    def _make_array(self, c):
        return (c * ctypes.py_object)()

    def pop(self):
        if self._n >= 1:
            self._n -= 1
            popped = self._A[self._n]
            self._A[self._n] = None
            if self._capacity > (self._n / 4):
                self._resize(self._capacity//2)
            return popped

# C-5.17
"""Prove that when using a dynamic array that grows and shrinks as in the previous exercise, the following series of 2n 
operations takes O(n) time: n append operations on an initially empty array, followed by n pop operations."""

# We have already proven that appending takes O(n) time amoritized, and popping from the end takes O(n) time amoritized.
# From a previous proof, we proved that if d(n) is O(f(n)) and e(n) is O(g(n)), then d(n) + e(n) is O(f(n) + g(n)).
# In this case, O(f(n) + g(n)) = O(n + n) = O(2n), which is O(n).

# C-5.18
"""Give a formal proof that any sequence of n append or pop operations on an initially empty dynamic array takes O(n) 
time, if using the strategy described in Exercise C-5.16."""

# If the array size doubles when it's full, and shrinks when it is smaller than N/4...
# We have already proven that n append operations takes O(n) time amoritized.
# When it comes to popping, we know each pop is 1 primitive operation. Once you get to the point where the array is
# small enough to resize, a new array of size N/4 is created, which takes O(n) time, all the elements are copied over,
# also n/4 operations or O(n) time. As the array gets smaller and smaller, the time it takes is less- n/8, n/16 and so on.
# Overall, the upper bound is O(n)

# C-5.19
"""Same question as above basically"""

# C.5-20
"""Consider a variant of Exercise C-5.16 in which an array of capacity N is resized to capacity previsely that of the 
number of elements, any time the number of elements in the array goes strictly below N/2. Show that there exists a 
sequence of n operations that requires Ω(n^2) operations."""

# If you appended up until the array expands at 2^i + 1,and popped at that moment, then the array would have to shrink.
# Continuously appending and popping at this point would mean each append and pop would require the array to shift size.
# Each pop operation would take 1 + N/2 + N/2 operations, or N + 1. Expanding the array would take N + N/2 + 1 operations,
# or 3/2 N + 1. Continuously adding this together (N + 1) + (3/2N + 1) + (N + 1) operations... This is Ω(n^2) operations.

# C-5.21
"""In Section 5.4.2, we described four different ways to compose a long string: (1) repeated concatenation, 
(2) appending to a temporary list and then joining, (3) using list comprehension with join, and (4) using generator 
comprehension with join. Develop an experiment to test the efficiency of all four of these approaches and report your 
findings."""

# N = 500000
# base_string = "=" * N


# String concatenation.

# new_string = ""
# start = time.time()
# for letter in base_string:
#     new_string += base_string
# end = time.time()
# elapsed = end - start
# print(elapsed)

# Appending to a temporary list and then joining

# new_string = []
#
# start = time.time()
# for letter in base_string:
#     new_string.append(base_string)
# ''.join(new_string)
# end = time.time()
# elapsed = end - start
# print(elapsed)

# List comprehension and then joining

# start = time.time()
# new_string = ''.join([letter for letter in base_string])
# end = time.time()
# elapsed = end - start
# print(elapsed)

# Generator comprehension and then joining

# start = time.time()
# new_string = ''.join(letter for letter in base_string)
# end = time.time()
# elapsed = end - start
# print(elapsed)


"""
                            500         5000        50000       500000
Concatenation               3.76e-4     4.14e-2     3.45
Temporary list              1.35e-4     2.54e-2     2.95
List comprehension          3.21e-5     2.61e-4     6.85e-3     2.82e-2
Generator comprehension     8.20e-5     5.69e-4     3.84e-3     4.56e-2
"""

#C-5.22
"""Develop an experiment to compare the relative efficiency of the extend method of Python versus using repeated calls 
to append to accomplish the equivalent task."""

# N = 10000000
#
# base = []
# to_append = [None] * N
#
# # Extend
#
# start = time.time()
# for appending in to_append:
#     base.append(appending)
# end = time.time()
# elapsed = end - start
# print(elapsed)

"""
            100         1000            10000           100000      1000000     10000000
Extend      2.86e-06    7.87e-06        2.57e-05        6.82e-04    1.06e-02    0.20
Append      2.88e-05    1.32e-04        1.58e-03        1.61e-02    0.14        1.37

"""

# C-5.25
"""The syntax data.remove(value) for Python list data removes only the first occurrence of element value from the list. 
Give na implementation of a function, with signature remove_all(data, value), that removes all occurrences from the 
given list, such that the worst case running time of the function is O(n) on a list with n elements. Not that it is not 
efficient enough to rely on repeated calls to remove."""


def remove_all(data, value):
    length = len(data)
    j = 0
    found = 0
    while j < length:
        if found:
            data[j-found] = data[j]
        if data[j] == value:
            found += 1
            data[j] = None
        j += 1
    while j < len(data) + found:
        data.pop()

# a = [2, 4, 6, 4, 2, 3, 9, 5, 7, 8, 3, 5, 6, 2]
# remove_all(a, 3)
# print(a)

# C-5.26
"""Let B be an array of size n >= 6 containing integers from 1 to n-5, inclusive, with exactly 5 repeated. Describe a 
good algorithm for finding the five integers in B that are repeated."""

def repeated_integers(B):
    repeat = [0] * len(B)
    repeated = []
    for integer in B:
        repeat[integer] += 1
        if repeat[integer] == 2:
            repeated.append(integer)
    return repeated


# N = 20
# random_list = [random.randrange(1, N-5) for n in range(N)]
# print(random_list)
# print(repeated_integers(random_list))

# C-5.27
"""Given a Python list L of n positive integers, each represented with k = ceil(log n) + 1 bits, describe an O(n)-time 
method for fiding a k-bit integer not in L."""

# If list size is 10, each integer will be 5 bits, or less than 2^5 - 1 = 31 and more than 2^4 = 16.

def k_bit_integer_not_in_list(L):
    bits = math.ceil(math.log2(len(L))) + 1
    max_number = 2**bits
    min_number = 2**(bits-1)
    found = {}
    for integer in L:
        found[integer] = True
    for x in range(min_number, max_number):
        if not found.get(x, False):
            return x

# N = 20
# bits = math.ceil(math.log2(N)) + 1
# max_number = 2**bits
# min_number = 2**(bits - 1)
# L = [random.randrange(min_number, max_number) for x in range(N)]
# print(L)
# print(k_bit_integer_not_in_list(L))

# C-5.28
"""Argue why any solution to the previous problem must run in Ω(n) time."""

# In my solution, the entire list is run through at least once in the "for integer in L" part, which takes a minimum of
# N time.  The for x in range(min_number, max_nmber) also takes only O(n) time in the worst case,
# since n numbers is the largest amount of numbers that can return True.

# C-5.29
"""A useful operation in databases is the natural join. If we view a database as a list of ordered pairs of objects, then the 
natural join of databases A and B is the list of all ordered triples (x, y, z) such that the pair (x, y) is in A and the
pair (y,z) is in B. Describe and analyze an efficient algorithm for computing the natural join of list A of n pairs and 
a list B of m pairs."""

"""
First sort the common column in the two tables, this should take n log n + m log m time. Then find which of the two 
is smaller, n or m. Let's say n is the smaller of the two. For each entry in list A, find the corresponding y in list B
using a binary search. This will take n log m time, as there are n elements each needing a log m time to find the 
corresponding column. Join the two.

Overall, this algorithm has an O(m log m) efficiency, assuming m is bigger than n. 
"""

# C-5.30
"""When Bob wants to send Alice a message M on the Internet, he breaks M into n data packets, numbers the packets 
consecutively, and injects them into the network. When the packets arrive at Alice's computer, they may be out of order,
so Alice must assemble the sequence of n packets in order before she can be sure she has the entire message. Describe an
efficient scheme for Alice to do this, assuming that she knows the value of n. What is the running time of this 
algorithm?"""

# Since she knows the value of n beforehand, she can initialize a new list of size n, taking O(n) time, and since the
# packets are numbered already, you can put them in the appropriate place easily, taking O(1) time for each, or O(n)
# overall. This would take O(n) time in total.

# C-5.31
"""Describe a way to use recursion to add all the numbers in an n x n data set, represented as a list of list."""

matrix = [
    [5, 3, 2],
    [9, 6, 1],
    [10, 5, 6]
]

def recursive_add(matrix):
    if isinstance(matrix, int):
        return matrix
    elif len(matrix) == 1 and isinstance(matrix[0], int):
        return matrix[0]
    elif not matrix:
        return 0
    elif len(matrix) >= 1:
        return recursive_add(matrix[0]) + recursive_add(matrix[1:])

print(recursive_add(matrix))
