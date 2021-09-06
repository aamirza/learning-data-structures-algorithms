# R 5.1
"""Execute the experiment from Code Fragment 5.1 and compare the results
on your system to those we report in Code Fragment 5.2."""

# import sys
# data = []
# n = 500
# for k in range(n):
#     a = len(data)
#     b = sys.getsizeof(data)
#     print('Length: {0:3d}; Size in bytes: {1:4d}'.format(a, b))
#     data.append(None)

"""
Length:   0; Size in bytes:   56
Length:   1; Size in bytes:   88
Length:   2; Size in bytes:   88
Length:   3; Size in bytes:   88
Length:   4; Size in bytes:   88
Length:   5; Size in bytes:  120
Length:   6; Size in bytes:  120
Length:   7; Size in bytes:  120
Length:   8; Size in bytes:  120
Length:   9; Size in bytes:  184
Length:  10; Size in bytes:  184
Length:  11; Size in bytes:  184
Length:  12; Size in bytes:  184
Length:  13; Size in bytes:  184
Length:  14; Size in bytes:  184
Length:  15; Size in bytes:  184
Length:  16; Size in bytes:  184
Length:  17; Size in bytes:  248
Length:  18; Size in bytes:  248
Length:  19; Size in bytes:  248
Length:  20; Size in bytes:  248
Length:  21; Size in bytes:  248
Length:  22; Size in bytes:  248
Length:  23; Size in bytes:  248
Length:  24; Size in bytes:  248
Length:  25; Size in bytes:  312
Length:  26; Size in bytes:  312
"""


# R-5.2
"""In Code Fragment 5.1, we perform an experiment to compare the length of a Python list to its underlying memory usage.
Determining the sequene of array sizes requires a manual insepction of the output of the program. Redesign the 
experiment so that the program outputs only those values of k at which the existing capacity is exhausted. For example,
on a system consistent with the results of Code Fragment 5.2, your program should output that the sequence of array 
capacities are 0, 4, 8, 16, 25,...."""

# import sys
# data = []
# n = 500
# for k in range(n):
#     a = len(data)
#     b = sys.getsizeof(data)
#     data.append(None)
#     if sys.getsizeof(data) != b:
#         print('Length: {0:3d}; Size in bytes: {1:4d}'.format(a, b))

"""
Length:   0; Size in bytes:   56
Length:   4; Size in bytes:   88
Length:   8; Size in bytes:  120
Length:  16; Size in bytes:  184
Length:  24; Size in bytes:  248
Length:  32; Size in bytes:  312
Length:  40; Size in bytes:  376
Length:  52; Size in bytes:  472
Length:  64; Size in bytes:  568
Length:  76; Size in bytes:  664
Length:  92; Size in bytes:  792
Length: 108; Size in bytes:  920
Length: 128; Size in bytes: 1080
Length: 148; Size in bytes: 1240
Length: 172; Size in bytes: 1432
Length: 200; Size in bytes: 1656
Length: 232; Size in bytes: 1912
Length: 268; Size in bytes: 2200
Length: 308; Size in bytes: 2520
Length: 352; Size in bytes: 2872
Length: 400; Size in bytes: 3256
Length: 456; Size in bytes: 3704
"""

# R 5-3
"""Modify the experiment from Code Fragment 5.1 in order to demonstrate that Python’s list class occasionally shrinks 
the size of its underlying array when elements are popped from a list."""

# import sys
#
# n = 25
# data = [None] * n
#
# for k in range(n):
#     a = len(data)
#     b = sys.getsizeof(data)
#     print('Length: {0:3d}; Size in bytes: {1:4d}'.format(a, b))
#     data.pop()
#     # if sys.getsizeof(data) != b:
#     #     print('Length: {0:3d}; Size in bytes: {1:4d}'.format(a, b))

"""
Length:  25; Size in bytes:  256
Length:  24; Size in bytes:  256
Length:  23; Size in bytes:  256
Length:  22; Size in bytes:  256
Length:  21; Size in bytes:  256
Length:  20; Size in bytes:  256
Length:  19; Size in bytes:  256
Length:  18; Size in bytes:  256
Length:  17; Size in bytes:  256
Length:  16; Size in bytes:  256
Length:  15; Size in bytes:  256
Length:  14; Size in bytes:  256
Length:  13; Size in bytes:  256
Length:  12; Size in bytes:  256
Length:  11; Size in bytes:  184
Length:  10; Size in bytes:  184
Length:   9; Size in bytes:  184
Length:   8; Size in bytes:  184
Length:   7; Size in bytes:  152
Length:   6; Size in bytes:  152
Length:   5; Size in bytes:  120
Length:   4; Size in bytes:  120
Length:   3; Size in bytes:  120
Length:   2; Size in bytes:  120
Length:   1; Size in bytes:   88
"""

# R-5.4
"""Our DynamicArray class, as given in Code Fragment 5.3, does not support use of negative indices with __getitem__. 
Update that method to better match the semantics of a Python list."""

# import ctypes
#
# class DynamicArray:
#     def __init__(self):
#         self._n = 0
#         self._capacity = 1
#         self._A = self._make_array(self._capacity)
#
#     def __len__(self):
#         return self._n
#
#     def __getitem__(self, k):
#         if not (-1 * self._n) <= k < self._n:
#             raise IndexError('invalid index')
#         return self._A[k]
#
#     def append(self, obj):
#         if self._n == self._capacity:
#             self._resize(2 * self._capacity)
#         self._A[self._n] = obj
#         self._n += 1
#
#     def _resize(self, c):
#         B = self._make_array(c)
#         for k in range(self._n):
#             B[k] = self._A[k]
#         self._A = B
#         self._capacity = c
#
#     def _make_array(self, c):
#         return (c * ctypes.py_object)()


# R 5.5
"""Redo the justification of Proposition 5.1 assuming that hte cost of growing the array from size k to 2k is
3k cyberdollars. How much should each append operation be charged to make the amortization work?"""

# Going from k to 2k would cost k cyberdollars in the old proof. If we made it 3k cyberdollars, that means an expansion
# of k to 2k, or k additional cells would have 2k cyberdollars invested in it, 2 cyberdollars per cell. If it cost 1
# cyberdollar to append, we would have enough.

# R 5.6
"""Our implementation of insert for the DynamicArray class, as given in Code Fragment 5.5, has the following 
inefficiency. In the case when a re- size occurs, the resize operation takes time to copy all the elements from an old 
array to a new array, and then the subsequent loop in the body of insert shifts many of those elements. Give an improved 
implementation of the insert method, so that, in the case of a resize, the elements are shifted into their final 
position during that operation, thereby avoiding the subsequent shifting.
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

    def _resize_and_insert(self, c, k=None, value=None):
        B = self._make_array(c)
        index_shift = 0
        for index in range(self._n):
            if index == k:
                B[k] = value
                index_shift = 1
            B[index+index_shift] = self._A[index]
        self._A = B
        self._capacity = c

    def _resize(self, c):
        self._resize_and_insert(c)

    def _make_array(self, c):
        return (c * ctypes.py_object)()

    def insert(self, k, value):
        if self._n == self._capacity:
            self._resize_and_insert(2 * self._capacity, k=k, value=value)
        else:
            for j in range(self._n, k, -1):
                self._A[j] = self._A[j-1]
        self._A[k] = value
        self._n += 1


# R-5.7
"""Let A be an array of size n >= 2 containing integers from 1 to n - 1, inclusive, with exactly one repeated. Describe 
a fast algorithm for finding the integer A that is repeated."""


def find_repeat(S):
    n = len(S) - 1
    sum_minus_one = ((n*(n+1))/2)
    actual_sum = sum(S)
    missing_number = actual_sum - sum_minus_one
    return missing_number

#print(find_repeat([2, 4, 6, 3, 4, 1, 5]) == 4)

def find_repeat2(S):
    length = len(S)
    counter = [0]*length
    for element in S:
        if counter[element]:
            return element
        else:
            counter[element] = 1

# R-5.8
"""Experimentally evaluate the efficiency of the pop method of Python's list class when using varying indices as a 
parameter, as we did for insert on page 205."""

# import time
#
# N = 1000000
# data = [None] * N
# start = time.time()
# for n in range(N):
#     #data.pop()
#     data.pop(N//2)
#     #data.pop(0)
#     N -= 1
# end = time.time()
# elapse = end - start
# print(elapse)

"""
            100         1000        10000       100000
k = 0       1.48e-5     3.01e-4     2.03e-3     1.99e-2
k = n // 2  8.29e-5     3.57e-4     1.66e-2     1.059       
k = n       5.41e-5     7.84e-4     2.63e-2     2.483
"""

# R-5.9
"""
Explain the changes that would have to be made to the program of Code Fragment 5.11 so that it can perform the Caesar 
cipher for messages that are written in alphabet-based language other than English, such as Greek, Russian, or Hebrew.
"""

class CaesarCipher:
    def __init__(self, shift):
        encoder = [None] * 26
        decoder = [None] * 26
        for k in range(26):
            encoder[k] = chr((k + shift) % 26 + ord('A'))
            decoder[k] = chr((k - shift) % 26 + ord('A'))
        self._forward = ''.join(encoder)    # will store as string
        self._backward = ''.join(decoder)

    def encrypt(self, message):
        return self._transform(message, self._forward)

    def derypt(self, secret):
        return self._transform(secret, self._backward)

    def _transform(self, original, code):
        msg = list(original)
        for k in range(len(msg)):
            if msg[k].isupper():
                j = ord(msg[k]) - ord('A')
                msg[k] = code[j]
        return ''.join(msg)

"""For other languages, you will want to change the % 26 and * 26 to represent the number of characters in the other writing 
script, and ord('A') to be that of the other writing script as well. You may or may not need the .isupper() depending on
whether the writing system has uppercase letters or not. With that, the Caesar cipher should work for other alphabetic 
writing systems."""

# R-5.10
"""The constructor for the CaesarCipher class can be implemented with a two-line body by building the forward and 
backward strings using a combination of the join method and an an appropriate comprehension syntax. Give such an 
implementation."""

class CaesarCipher:
    def __init__(self, shift):
        self._forward = ''.join([chr((k + shift) % 26 + ord('A')) for k in range(26)])
        self._backward = ''.join([chr((k - shift) % 26 + ord('A')) for k in range(26)])

    def encrypt(self, message):
        return self._transform(message, self._forward)

    def derypt(self, secret):
        return self._transform(secret, self._backward)

    def _transform(self, original, code):
        msg = list(original)
        for k in range(len(msg)):
            if msg[k].isupper():
                j = ord(msg[k]) - ord('A')
                msg[k] = code[j]
        return ''.join(msg)

# R-5.11
"""Use standard control structures to compute the sum of all numbers in an n x n data set, represented as a list of 
lists."""

numbers = [
    [5, 9, 2],
    [8, 5, 3],
    [7, 6, 9],
]

total = 0
for number_list in numbers:
    for number in number_list:
       total += number
print(total)

# R-5.12
"""Describe how the built-in sum function can be combined with Python's list comprehension syntax to compute the sum of 
all numbers in an n x n data set, represented as a list of lists"""

print(sum([sum(number) for number in numbers]))
