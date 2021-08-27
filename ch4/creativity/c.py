import math

# C-4.9
"""Write a short recursive Python function that finds the minimum and maximum and values in a sequence without 
using any loops."""

def find_min_max(S, max=-math.inf, min=math.inf):
    '''
    >>> find_min_max([9,4,56,43,22,55,34])
    (56, 4)
    '''
    if S[0] > max:
        max = S[0]
    if S[0] < min:
        min = S[0]
    if len(S) == 1:
        return (max, min)
    return find_min_max(S[1:], max, min)

# C-4.10
"""Describe a recursive algorithm to compute the integer part of the base-two logarithm of n using only addition
and integer division"""

# Start the number of steps at 0.
# You would integer divide the integer by 2 (n // 2). Add + 1 to the number of steps.
# If the result of the division is 1, return the number of steps.
# Else do a recursion, using the result of the n // 2 division and the number of steps as input.
# The number of steps will be the floor of the answer.

def floor_log2(number):
    '''
    >>> floor_log2(30)
    4
    >>> floor_log2(242)
    7
    '''
    if number <= 1:
        return 0
    new_number = number // 2
    return 1 + floor_log2(new_number)

# C-4.11
"""Describe an efficient recursive function for solving the element uniqueness problem, which runs in time that is at
most O(n^2) in the worst case without sorting."""

def all_elements_unique(S, index=0):
    """
    >>> all_elements_unique([5, 6, 7, 8])
    True
    >>> all_elements_unique([9, 4, 3, 4, 2, 6])
    False
    """
    if index == len(S) - 1:
        return True
    else:
        for i in range(index+1, len(S)):
            if S[i] == S[index]:
                return False
    return all_elements_unique(S, index+1)

# C-4.12
"""Give a recursive algorithm to compute the product of two positive integers, m and n, using only addition and 
subtraction"""

def multiply(n, m):
    """
    >>> multiply(5, 3)
    15
    >>> multiply(12, 7)
    84
    """
    if m == 0:
        return 0
    return n + multiply(n, m-1)

# C-4.13
"""In Section 4.2 we prove by induction that the number of lines printed by a call to draw_interval(c) is 2^c - 1.
Another interesting question i how many dashes are printed during that process. Prove by induction that the number of 
dashes printed by draw_interval(c) is 2^(c+1) - c - 2"""

# TODO: Later

# C-4.14
"""In the Towers of Hanoi puzzle, we are given a platform with three pegs, a, b, and c, sticking out of it. On peg a
is a stack of n disks, each larger than the next, so that the smallest is on top and the largest is on the bottom. The
puzzle is to move all the disks from peg a to peg c, moving one disk at a time, so that we never place a larger disk
on top of a smaller one. Describe a recursive algorithm for solving the Towers of Hanoi puzzle for arbitrary n."""

# If Tower B and C are empty:
#   Move peg from A to B, and another to C
# If Tower B and C are occupied:
#   Move peg from Tower B to C,
#   Then move that collective peg to Tower B.
# If Tower B is occupied but not C:
#   Move peg from Tower A to C.

# C-4.15
"""Write a recursive function that will output all the subsets of a set of n elements (without repeating any subsets)"""

def get_all_subsets(k, S, universe):
    if k == 1:
        pass
    else:
        for element in universe:
            new_S = S + [element]
            print(new_S)
            new_universe = universe.difference({element})
            k -= 1
            if k > 1:
                get_all_subsets(k, new_S, new_universe)
            k = len(universe)
            universe = universe.difference({element})


# C-4.16
"""Write a short recursive Python function that takes a character string s and outputs its reverse. For example, the 
reverse of pots&pans would be snap&stop"""

def reverse_string(s):
    """
    >>> reverse_string('pots&pans')
    'snap&stop'
    >>> reverse_string('gotmilk')
    'klimtog'
    """
    stop = len(s) - 1
    if stop == 0:
        return s
    return s[stop] + reverse_string(s[1:stop]) + s[0]


# C-4.17
"""Write a short recursive Python function that determines if a string s is a palindrome"""
def is_palindrome(s):
    """
    >>> is_palindrome('racecar')
    True
    >>> is_palindrome('lalal')
    True
    >>> is_palindrome('lalala')
    False
    >>> is_palindrome('ss')
    True
    """
    if len(s) <= 1:
        return True
    if s[0] != s[-1]:
        return False
    return is_palindrome(s[1:-1])


# C-4.18
"""Use recursion to write a Python function for determining if a string s has more vowels than consonants"""
def more_vowels_than_consonants(s, vowel_count=0, consonant_count=0):
    """
    >>> more_vowels_than_consonants('')
    False
    >>> more_vowels_than_consonants('h')
    False
    >>> more_vowels_than_consonants('ha')
    False
    >>> more_vowels_than_consonants('a')
    True
    >>> more_vowels_than_consonants('huehuehue')
    True
    >>> more_vowels_than_consonants('hahahaha')
    False
    """
    if len(s) == 0:
        return vowel_count > consonant_count
    if s[0] in ('a','e','i','o','u'):
        vowel_count += 1
    else:
        consonant_count += 1
    return more_vowels_than_consonants(s[1:], vowel_count, consonant_count)


# C-4.19
"""Write a short recursive Python function that rearranges a sequence of integer values so that all even values appear
before all the odd values."""

def all_even_before_odd(S, n=0):
    """
    >>> all_even_before_odd([2, 8, 4, 9, 2])
    [2, 8, 4, 2, 9]
    >>> all_even_before_odd([3, 7, 0, 2, 4, 3])
    [0, 2, 4, 3, 7, 3]
    """
    if n >= len(S):
        return []
    if S[n] % 2 == 1:
        return all_even_before_odd(S, n+1) + [S[n]]
    else:
        return [S[n]] + all_even_before_odd(S, n+1)


# C-4.20
"""Given an unsorted sequence, S, of integers and an integer k, describe a recursive algorithm for rearranging the 
elements in S so that all elements less than or equal to k come before any elements larger than k. What is the running 
time of your algorithm on a sequence of n values?"""

def sort_smaller_than_k(S, k, n=0):
    """
    >>> sort_smaller_than_k([2, 8, 4, 9, 2], 5)
    [2, 4, 2, 9, 8]
    >>> sort_smaller_than_k([3, 7, 0, 2, 4, 3], 6)
    [3, 0, 2, 4, 3, 7]
    """
    if n >= len(S):
        return []
    if S[n] > k:
        return sort_smaller_than_k(S, k, n+1) + [S[n]]
    else:
        return [S[n]] + sort_smaller_than_k(S, k, n+1)


# The running time is O(n).

# C-4.21
"""Suppose you are given an n-element sequence, S, given integers that are listed in increasing order. Given a number k,
describe a recursive algorithm to find two integers in S that sum to k, if such a pair exists. What is the running time of
your algorithm?"""

# Good idea to implement binary search

def sum_to_k(S, k, start, stop):
    """
    >>> sum_to_k([1, 4, 6, 7, 11, 13, 19], 17, 0, 7)
    [4, 13]
    >>> sum_to_k([6, 9, 10, 12, 29, 35, 83, 134], 15, 0, 8)
    [6, 9]
    >>> sum_to_k([3, 6, 10, 15, 29, 34, 44], 6, 0, 7)
    >>> sum_to_k([], 10, 0, 0)
    """
    if len(S) == 0:
        return None
    mid = (start + stop) // 2
    if start >= (stop - 1):
        return sum_to_k(S[1:], k, 0, len(S[1:]))
    if S[0] + S[mid] == k:
        return [S[0], S[mid]]
    elif S[0] + S[mid] > k:
        return sum_to_k(S, k, start, mid)
    elif S[0] + S[mid] < k:
        return sum_to_k(S, k, mid, stop)


# C-4.22
"""Develop a nonrecursive implementation of the version of power from Code Fragment 4.12 that uses repeated squaring."""

# Code Fragment 4.12

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

def nonrecursive_power(x, n):
    """
    >>> nonrecursive_power(2, 2)
    4
    >>> nonrecursive_power(2, 3)
    8
    >>> nonrecursive_power(2, 4)
    16
    >>> nonrecursive_power(2, 18)
    262144
    >>> nonrecursive_power(3, 3)
    27
    """
    result = 1
    k = 0
    while k < n:
        if k == 0 or (k * 2 > n):
            result *= x
            k += 1
        elif k * 2 <= n:
            result = result * result
            k *= 2
    return result


if __name__ == "__main__":
    get_all_subsets(5, [], {1, 2, 3, 4, 5})
