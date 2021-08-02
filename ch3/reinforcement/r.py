# R-3.2
"""
The number of operations executed by algorithm A and B is 8n log n and 2n^2, respectively. Determine n_0 such that A
is better than B for n >= n0
"""

# 8 n log n = 2n^2
# n log n = n^2 / 4
# log n = n / 4
# n = 4 log n
# 4 = n / log n
# if n = 2, then n / log n = 2
# if n = 3, then 3 / log 3
# if n = 4, then 4 / 2
# if n = 8, then 8 / 3
# if n = 16, then 16 / 4 = 4

# When n = 16, A will be less than or equal to ("better than") B.

# R-3.3
import math

"""
The number of operations executed by algorithms A and B is 40n^2 and 2n^3, respectively. Determine n_0 such that A is
better than B for n >= n_0
"""


# 40n^2 = 2n^3
# 40 = 2n
# n = 20

# When n = 20, A will be less than or equal to ("better than") B.

# R-3.4
"""Give an example of a function that is plotted the same on a log-log scale as it is on a standard scale"""

# An a*n function, where a is a constant, is an example of a function that would have the same shape on both
# a log-log scale and a standard scale. The reason for this is that the slope is equal to a on both scales.
# 10^2 would be plot onto a*10^2 and 10^3 would plot to a*10^3 and so on.

# R-3.5.
"""Explain why the plot of the function n^c is a straight line with slope c on a log-log scale"""


# When you take the log of n^c and log of y, you get log y = c log n.
# c = log y / log n
# In other words, in a log-log graph, the slop (log y / log n) is equal to the constant value c.

# R-3.6.
"""What is the sum of all the even numbers from 0 to 2n, for any positive integer n?"""

# Sum of even numbers = 2 + 4 + 6... + 2n.
# Or 2(1 + 2 + 3... + n) = 2(n(n+1)/2)
# = n(n+1)

# R-3.7.
"""
Show that the following statements are equivalent:

a) The running time of an algorithm A is always O(f(n))
b) In the worst case, the running time of algorithm A is O(f(n))
"""

# A is O(f(n)) means there exists a constant c such that A <= cf(n) with a number n >= n_0.
# This means that A is always upper-bounded by f(n) from n > n_0.
# As n grows larger and larger and A takes longer to run, f(n) will always serve as an upper bound to how long the
# function can run. So in the worst case scenario, the running time of algorithm A is O(f(n)) (upper bounded by f(n))

# R-3.8
"""
Order the following functions by asymptotic growth rate.

4n log n + 2n
2^10
2^(log n)
3n + 100 log n
4n
2^n
n^2 + 10n
n^3
n log n
"""

# 4n log n + 2n is O(n log n)
# 2^10 is O(a)
# 2^(log n) is O(n)
# 3n + 100 log n is O(n)
# 4n is O(n)
# 2^n is O(2^x)
# n^2 + 10n is O(n^2)
# n^3 is O(n^3)
# n log n is O(n log n)

# 2^n
# n^3
# n^2 + 10n
# 4n log n + 2n
# n log n
# 4n
# 3n + 100 log n
# 2^log n
# 2^10

# R-3.9
"""Show that if d(n) is O(f(n)), then ad(n) is O(f(n)), for any constant a > 0."""

# If d(n) is O(f(n)) then that means d(n) <= cf(n) for an n0 where n >= n0.
# ad(n) <= acf(n) also for an n0 where n >= 0
# Or ad(n) <= c'f(n)
# In other ad(n) is also O(f(n)).

# R-3.10.
"""Show that if d(n) is O(f(n)) and e(n) is O(g(n)), then the product d(n)e(n) is O(f(n)g(n))"""

# d(n) <= cf(n) for n >= n0
# e(n) <= c'g(n) for n >= n1
# That means d(n)e(n) <= c c' f(n)g(n) for n >= n2
# Let cc' = c''
# d(n)e(n) <= c''f(n)g(n)
# Therefore d(n)e(n) is O(f(n)g(n))

# R-3.11
"""Show that if d(n) is O(f(n)) and e(n) is O(g(n)), then d(n) + e(n) is O(f(n) + g(n))"""

# d(n) <= cf(n) for n >= n0
# e(n) <= c'g(n) for n >= n1
# d(n) + e(n) <= cf(n) + c'g(n) for n >= n2
# Say that there is a c'' such that c'' > c and c'' > c'
# d(n) + e(n) <= c''f(n) + c''g(n)
# d(n) + e(n) <= c''(f(n) + g(n)) for n >= n2
# In other words, d(n) + e(n) is O(f(n) + g(n))

# R-3.12
"""Show that if d(n) is O(f(n)) and e(n) is O(g(n)), then d(n) - e(n) is not necessarily O(f(n) - g(n))"""

# Say that d(n) - e(n) is O(f(n) - g(n))
# Say that d(n) = 2n, and e(n) = n. d(n) is O(n) and e(n) is O(n)
# d(n) - e(n) = n. O(f(n) - g(n)) on the other hand would equal O(n - n) = O(0)
# But n is not not O(o).
# Therefore, d(n) - e(n) is not necessarily O(f(n) - g(n))


# R-3.13
"""Show that d(n) is O(f(n)) and f(n) is O(g(n)), then d(n) is O(g(n))"""

# If d(n) is O(f(n)), then d(n) <= cf(n) for n >= n0
# If f(n) is O(g(n)) then f(n) <= c'g(n) for n >= n1.
# Therefore d(n) <= cf(n) <= cc'g(n)
# Take c'' = cc'.
# Therefore d(n) <= c''g(n) for n >= n2.
# And so d(n) is also O(g(n))

# R-3.14
"""Show that O(max{f(n), g(n)} = O(f(n) + g(n))"""

# O(max{f(n), g(n)}) is O(f(n) + g(n)) if
# max{f(n), g(n)} <= c(f(n) + g(n)) for n = n0.

# Assuming f(n) and g(n) are always positive (which they would be since time cannot be negative), this should be true,
# since individually f(n) <= f(n) + g(n) and g(n) <= f(n) + g(n). So the maximum of either should be upper bounded by
# f(n) + g(n).
# Therefore max{f(n), g(n)} is O(f(n), g(n))

# R-3.15
"""Show that f(n) is O(g(n)) if and only if g(n) is Ω(f(n))"""

# If g(n) is Ω(f(n)), then that means g(n) >= cf(n) for n >= n_0.
# Since cf(n) <= g(n), it would also mean that f(n) <= (1/c)g(n). Take c' = 1/c.
# That means f(n) is also O(g(n))

# R-3.16
"""Show that if p(n) is a polynomial in n, then log p(n) is O(log n)"""

# Let's p(n) is a polynomial of the mth degree. We would say that p(n) is O(n^m).
# In other words, p(n) <= c * n^m for an n >= n0.
# Taking the log of both and assuming they are both always more than 1, you get log p(n) <= log (cn^m).
# This gives us log p(n) <= log c + log n^m
# Or p(n) <= log c + m log n.
# Since log c and m are both constants, this satisfies the rule that p(n) is upper bounded by log n.
# Therefore, log p(n) is O(log n).

# R-3.17
"""Show that (n + 1)^5 is O(n^5)"""

# (n + 1)^5 =  n^5 + 5n^4 + 10nˆ3 + 10n^2 + 5n + 1
# n^5 + 5n^4 + 10n^3 + 10n^2 + 5n + 1 <= (1 + 5 + 10 + 10 + 5 + 1)n^5 <= 32n^5
# (n +1)^5 <= 32n^5.
# Therefore (n + 1)^5 is log(n^5)

# R-3.18.
"""Show that 2^(n+1) is O(2^n)"""

# 2^(n+1) = 2^n * 2^1 = 2 * 2^n
# 2 * 2^n <= c * 2^n for n >= n0.
# Therefore, 2^(n+1) is O(2^n).

# R-3.19
"""Show that n is O(n log n)"""

# If n is O(n log n), then n <= c n log n.
# Or 1 <= c log n for for n >= 1.
# Take n = 2 and c > 1, then 1 <= c is true.
# Therefore n is upper bounded by n log n for n > 1. And so n is O(n log n)

# R-3.20
"""Show that n^2 is Ω(n log n)"""

# If n^2 is lower-bounded by n log n, then
# n^2 >= cn log n.
# n >= c log n.
# This is true for c = 1 and n >= 1.
# Therefore n^2 is lower bounded by n log n at n >= 1.
# Therefore n^2 is Ω(n log n)

# R-3.21
"""Show that n log n is Ω(n)"""

# If n log n is lower bounded by n then
# n log n >= cn
# log n >= c. This is true if c = 1 and n >= 2
# Therefore n log n is lower bounded by n when n >= 2
# Therefore n log n is Ω（n）

# R-3.22
"""Show that ceil(f(n)) is O(f(n)), if f(n) is a positive nondecreasing function that is always greater than 1."""

# If ceil(f(n) is O(f(n)), that means
# ceil(f(n)) <= c f(n) for n >= n0.
# Take c = 2 for example.
# base case, f(n) = 1. Then ceil(f(n)) = 1 and c f(n) = 2.
# Take f(n) = 1.5, then ceil(1.5) = 2 and c f(n) = 3
# And so on...
# We see that ceil(f(n)) is upper-bounded by c f(n).
# Therefore ceil(f(n)) is O(f(n))

# R-3.23
"""Give a big-Oh characterization, in terms of n, of the running time of the example1 function shown in Code Fragment
3.10."""

def example1(S):
    """Return the sum of the elements in Sequence."""
    n = len(S)
    total = 0
    for j in range(n):
        total += S[j]
    return total

# n = len(S) is a primitive operation
# total = 0 is a primitive operation
# for j in range(n) runs n times.
    # total += S[j] is a primitive operation
# return is a primitive operation
# a + a + n(a) + a where a is a constant
# na + 3a
# na + 3a <= cn where c >= 4a
# This function runs in O(n) time.

# R-3.24
"""Give a big-Oh characterization, in terms of n of the running time of the example2 function shown in Code Fragment
3.10"""

def example2(S):
    n = len(S)
    total = 0
    for j in range(0, n, 2):
        total += S[j]
    return total

# Same as above, except the for loop runs n/2 times.
# (1/2a)n + 3a
# (1/2a)n + 3a <= cn where c >= 4a
# This function also runs in O(n) time.

# R-3.25.

def example3(S):
    """Return the sum of the prefix sums of sequence S"""
    n = len(S)
    total = 0
    for j in range(n):
        for k in range(1+j):
            total += S[k]
    return total

# This runs in O(n^2) time. The for loop runs n(n) or n^2 times in the worst case scenario.

# R-3.26.

def example4(S):
    n = len(S)
    prefix = 0
    total = 0
    for j in range(n):
        prefix += S[j]
        total += prefix
    return total

# The for-loop runs n times. The rest are primitive operations.
# The run time of this algorithm is O(n).

# R-3.27

def example5(S):
    """Return the number of elements in B equal to the sum of prefix sums in A"""
    n = len(A)
    count = 0
    for i in range(n):
        total = 0
        for j in range(n):
            for k in range(1+j):
                total += A[k]
        if B[i] == total:
            count += 1
    return count

# R-3.28

"""For each function f(n) and time t in the following table, determine the largest size n of a problem P that can be
solved in time t if the algorithm for solving P takes f(n) microseconds (one entry is already completed).

a) 1 second
b) 1 hour
c) 1 month
d) 1 century"""

# log n
    # log n would solve a problem of size 10^300000 in 1 second.
    # log n would solve a problem of size 3600 * 10^300000 in 1 hour
    # log n would solve a problem of size 30 * 24 * 3600 * 10^300000 in 1 month
    # log n would solve a problem of size 1200 * 30 * 24 * 3600 * 10^300000 in 1 century
# n
    # n would solve a problem of size of 1 million in 1 second
    # n would solve a problem size of 3.6 billion in 1 hour
    # n would solve a problem size of 2.592e12 in 1 month.
    # n would solve a problem size of 3.1104e15 in 1 century.
# n log n
    # Solve by iteration...
    # n log n would solve a problem size of 62746 in 1 second
    # n log n would have a problem size of 1.33e8 in 1 hour
    # n log n would have a problem size of 7.19e10 in 1 month
    # n log n would have a problem size of 6.86e13 in 1 century
# n^2
    # n^2 would solve a problem size of 1,000 in 1 second
    # n^2 would solve a problem size of 60,000 in 1 hour
    # n^2 would solve a problem size of 1,609,968 in 1 month
    # n^2 would solve a problem size of 11,466,783 in 1 century
# n^3
    # n^3 would solve a problem size of 100 in 1 second
    # n^3 would solve a problem size of 1,532 in 1 hour
    # n^3 would solve a problem size of 13,736 in 1 month
    # n^3 would solve a problem size of 50,850 in 1 century

def nlogn(n):
    return n * math.log2(n)


def nlogn_time(time):
    n = time / 2
    upper_n = time
    lower_n = 0
    while abs(time - nlogn(n)) > 1:
        if nlogn(n) > time:
            upper_n = n
            n = (n + lower_n) / 2
        elif nlogn(n) < time:
            lower_n = n
            n = (n + upper_n ) / 2
    return n

print(nlogn_time(1000000))
print(nlogn_time(1e6 * 3600))
print(nlogn_time(1e6 * 3600 * 24 * 30))
print(nlogn_time(1e6 * 3600 * 24 * 365.242 * 100))

# R-3.29
"""Algorithm A executes an O(log n)-time computation for each entry of an n-element sequence. What is its worst-case 
running-time?"""

# If each entry of the sequence is calculated in O(log n) time, we can say for array of size n that the algorithm takes
# n ( O(log n) + O(log n) + O(log n) ) time to run. This makes the algorithm dependent on the size n of the sequence.
# The algorithm would run in O(n log n) in the worst case.

# R-3.30
"""Given an n-element sequence S, Algorithm B chooses log n elements in S at random and executes an O(n)-time 
calculation for each. What is the worst-case running time of Algorithm B?"""

# As S gets larger, algorithm B running time increases by O(log n), but is executed n times. Thus the worst-case running
# time of Algorithm B should be O(n log n).

# R-3.31
"""Given an n-element sequence S of integers, Algorithm C executes an O(n)-time computation for each even number in S, 
and an O(log n)-time computation for each odd number in S. What are the best-case and worst-case running times of 
Algorithm C?"""

# In the worst case scenario, all integers in a sequence S are event. In this case, the algorithm runs in O(n) time.
# In the best case scenario, all integers are odd. In this case, the algorithm runs in Ω(log n) time.

# R-3.32
"""Given an n-element sequence S, Algorithm D calls Algorithm E on each element S[i]. Algorithm E runs in O(i) time when
it is called on element S[i]. What is the worst-case running time of Algorithm D?"""

# Algorithm E is called on each element of S, and runs in O(i) time. Given a sequence length of n, then Algorithm E
# should run n-times in O(i). This gives a worst-case running time of O(ni) for Algorithm D.

# R-3.33
"""Al and Bob are arguing about their algorithms. Al claims his O(n log n)-time method is always faster than Bob's
O(n^2)-time method. To settle the issue, they perform a set of experiments. To Al's dismay, they find that if n < 100,
the O(n^2)-time algorithm runs faster, and only when n >= 100 is the O(n log n)-time one better. Explain how this is
possible."""

# O(n log n) means there exists an upper-bound of cn log n on Al's algorithm, and O(n^2) means there exists an upper
# bound of c'n log n on Bob's algorithm. If c is much larger than c', then it is possible that Al's algorithm can take
# longer than Bob's for a small number of n. In this case...

# c n log n >= c'n^2.
# 100c log 100 >= c' * (100^2)
# c log 100 >= 100 c'
# 6.643 c >= 100 c'
# c >= 15.05 c'

# If c ~= 15.05 c' or (100 / log 100)c' then O(n log n) can be worse than O(n^2) for n <= 100.

# R 3.34
"""There is a well-known city whose inhabitants have the reputation of enjoying a meal only if that meal is the best
they have experienced in their life. Otherwise, they hate it. Assuming meal quality is distributed uniformly across a
person's life, describe the expected number of times inhabitants of this city are happy with their meals?"""

# In the beginning, there is a 100% (1/1) chance they'll enjoy their meal. In the second, there is a 50% chance (1/2).
# Then a 33% chance (1/3)...

# There is a 1/n chance they enjoy each new meal, where n is the number of meals they've had before. To get the expected
# number of times

def disjoint(A, B, C):
    for a in A:
        for b in B:
            if a == b:
                for c in C:
                    if a == c:
                        return False
    return True
