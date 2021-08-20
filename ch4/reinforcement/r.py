import math

# R-4.1
"""Describe a recursive algorithm for finding the maximum element in a sequence, S, of n elements. What is your
running time and space usage?"""


def find_max(S, n, max=-math.inf):
    """
    >>> find_max([98, 7, 654, 8, 112], 5)
    654
    >>> find_max([98, 4, 192, 445, 893], 5)
    893
    >>> find_max([98, 4, 192, 445, 893], 4)
    445
    """
    if S[n-1] > max:
        max = S[n-1]
    if n == 1:
        return max
    return find_max(S, n-1, max=max)

# This runs in O(n) time and since it is a tail recursion, it takes up O(n) space.


# R-4.2
"""Draw the recursion trace for the computation of power(2, 5), using the traditional function implemented in Code
Fragment 4.12"""

# power(2, 5) returns 2 * (16) = 32
# power(2, 4) returns 2 * (8) = 16
# power(2, 3) returns 2 * (4) = 8
# power(2, 2) returns 2 * (2) = 4
# power(2, 1) returns 2 * 1 = 2
# power(2, 0) returns 1

# R-4.3
"""Draw the recursion trace for the computation of power(2, 18) using the repeated squaring algorithm, as implemented
in Code Fragment 4.12"""


def power(x, n):
    """Computer the value x**n for integer n."""
    if n == 0:
        return 1
    else:
        partial = power(x, n // 2)
        result = partial * partial
        if n % 2 == 1:
            result *= x
        return result

# power(2, 18) returns (512 * 512) = 262144
# power(2, 9) returns (16 * 16) * 2 = 512
# power(2, 4) returns (4 * 4) = 16
# power(2, 2) returns (2 * 2) = 4
# power(2, 1) returns (1 * 1) * 2 = 2
# power(2, 0) returns 1


# R-4.4
"""Draw the recursion trace for the execution of the function reverse(S, 0, 5) (Code Fragment 4.10) on 
S = [4, 3, 6, 2, 6]"""

def reverse(S, start, stop):
    """Reverse elements in implicit slice S[start:stop]"""
    if start < stop - 1:
        S[start], S[stop - 1] = S[stop - 1], S[start]
        reverse(S, start+1, stop-1)

# reverse([4, 3, 6, 2, 6], 0, 5)
# reverse([6, 3, 6, 2, 4], 1, 4)
# reverse([6, 2, 6, 3, 4], 2, 3)

# Linear recursion means no single line straight recursion trace.

# R-4.5
"""Draw the recursion trace for the execution of the function PuzzleSolve(3, S, U) (Code Fragment 4.14), where S is
empty and U = {a, b, c, d}"""
import math

# R-4.1
"""Describe a recursive algorithm for finding the maximum element in a sequence, S, of n elements. What is your
running time and space usage?"""


def find_max(S, n, max=-math.inf):
    """
    >>> find_max([98, 7, 654, 8, 112], 5)
    654
    >>> find_max([98, 4, 192, 445, 893], 5)
    893
    >>> find_max([98, 4, 192, 445, 893], 4)
    445
    """
    if S[n-1] > max:
        max = S[n-1]
    if n == 1:
        return max
    return find_max(S, n-1, max=max)

# This runs in O(n) time and since it is a tail recursion, it takes up O(n) space.


# R-4.2
"""Draw the recursion trace for the computation of power(2, 5), using the traditional function implemented in Code
Fragment 4.12"""

# power(2, 5) returns 2 * (16) = 32
# power(2, 4) returns 2 * (8) = 16
# power(2, 3) returns 2 * (4) = 8
# power(2, 2) returns 2 * (2) = 4
# power(2, 1) returns 2 * 1 = 2
# power(2, 0) returns 1

# R-4.3
"""Draw the recursion trace for the computation of power(2, 18) using the repeated squaring algorithm, as implemented
in Code Fragment 4.12"""


def power(x, n):
    """Computer the value x**n for integer n."""
    if n == 0:
        return 1
    else:
        partial = power(x, n // 2)
        result = partial * partial
        if n % 2 == 1:
            result *= x
        return result

# power(2, 18) returns (512 * 512) = 262144
# power(2, 9) returns (16 * 16) * 2 = 512
# power(2, 4) returns (4 * 4) = 16
# power(2, 2) returns (2 * 2) = 4
# power(2, 1) returns (1 * 1) * 2 = 2
# power(2, 0) returns 1


# R-4.4
"""Draw the recursion trace for the execution of the function reverse(S, 0, 5) (Code Fragment 4.10) on 
S = [4, 3, 6, 2, 6]"""

def reverse(S, start, stop):
    """Reverse elements in implicit slice S[start:stop]"""
    if start < stop - 1:
        S[start], S[stop - 1] = S[stop - 1], S[start]
        reverse(S, start+1, stop-1)

# reverse([4, 3, 6, 2, 6], 0, 5)
# reverse([6, 3, 6, 2, 4], 1, 4)
# reverse([6, 2, 6, 3, 4], 2, 3)

# Linear recursion means no single line straight recursion trace.

#R-4.6
"""Describe a recursive function for computing the nth Harmonic number"""

def harmonic_number(n):
    """
    >>> harmonic_number(1)
    1
    >>> harmonic_number(2)
    1.5
    >>> harmonic_number(3) == 11/6
    True
    """
    if n == 1:
        return 1
    else:
        return harmonic_number(n-1) + 1/n


# R-4.7
"""Describe a recursive function for converting a string of digits into the integer it represents. For example, 
'13531' represents the integer 13,531."""

def recusrive_int(string, starting_value=0):
    """
    >>> recusrive_int('13531')
    13531
    >>> recusrive_int('2958483292')
    2958483292
    """
    if len(string) == 0:
        return starting_value
    else:
        digits = len(string)
        remaining_value = (int(string[0]) * (10**(digits-1))) + starting_value
        return recusrive_int(string[1:], starting_value=remaining_value)




#R-4.6
"""Describe a recursive function for computing the nth Harmonic number"""

def harmonic_number(n):
    """
    >>> harmonic_number(1)
    1
    >>> harmonic_number(2)
    1.5
    >>> harmonic_number(3) == 11/6
    True
    """
    if n == 1:
        return 1
    else:
        return harmonic_number(n-1) + 1/n


# R-4.7
"""Describe a recursive function for converting a string of digits into the integer it represents. For example, 
'13531' represents the integer 13,531."""

def recusrive_int(string, starting_value=0):
    """
    >>> recusrive_int('13531')
    13531
    >>> recusrive_int('2958483292')
    2958483292
    """
    if len(string) == 0:
        return starting_value
    else:
        digits = len(string)
        remaining_value = (int(string[0]) * (10**(digits-1))) + starting_value
        return recusrive_int(string[1:], starting_value=remaining_value)


# R-4.8
"""Isabel has an interesting way of summing up the values in a sequence A of n integers, where n is a power of two. She
creates a new sequence B of half the size of A and sets B[i] = A[2i] + A[2i + 1], for i = 0, 1,...,(n/2) - 1. If B has
size 1, then she outputs B[0]. Otherwise, she replaced A with B, and repeats the process. What is the running time of 
her algorithm?"""

# A = [5, 3, 2, 4]
# B = [8, 6]

# A = [7, 3, 6, 3, 2, 2, 4, 5]
# B = [10, 9, 4, 9]

# Initializing B takes n/2 time.
# Summing up the first time takes n time.
# Then n/2 time
# then n/4 time...
# n/2 + (n + n/2 + n/4)
# n/2 + n(1 + 1/2 + 1/4 + 1/8...)
# This appears to be an O(n log n) algorithm.
