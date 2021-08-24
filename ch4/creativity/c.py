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

def get_all_subsets(S, n=0):
    # 1, 2, 3, 4, 5
    # 1, 2, 3, 4
    # 1, 2, 3, 5
    # 1, 2, 4, 5
    # 1, 3, 4, 5
    # 2, 3, 4, 5
    # 1, 2, 3
    # 1, 2, 4
    # 1, 3, 4
    # 2, 3, 4
    # 1, 2, 5
    # 1, 3, 5
    # 2, 3, 5
    # 1, 4, 5
    # 2, 4, 5
    # 3, 4, 5

    # 1
    # 2
    # 3
    # 4
    # 5
    # 1, 2
    # 1, 3
    # 1, 4
    # 1, 5
    # 2, 3
    # 2, 4
    # 2, 5
    # 3, 4
    # 3, 5
    # 4, 5


    pass
