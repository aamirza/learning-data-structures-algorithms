# C-3.35
"""Assuming it is possible to sort n numbers in O(n log n) time, show that it is possible to solve the three-way set
disjointness problem in O(n log n) time."""
import math
import random


def disjoint(A, B, C):
    A = sorted(A)
    B = sorted(B)
    C = sorted(C)
    for a in A:
        lower_b = 0
        upper_b = len(B)
        b = int(upper_b / 2)
        while b != lower_b:
            if a == B[b]:
                # repeat binary search loop for c
                pass
            elif a < B[b]:
                upper_b = b
                b = int((upper_b + lower_b) / 2)
            elif a > B[b]:
                lower_b = b
                b = int((upper_b + lower_b) / 2)
    return False

# Sorting takes O(n log n) time.
# With our sets sorted, we can loop through A n times. Instead of looping through B n times, we can use a binary search
# starting in the middle of B. If b is more than a, then we'll know a potential match is in an earlier index, and
# if b is less than a, then we'll know it is in a later index. Binary searches have a time complexity of O(log n),
# generally. The process is repeated for C.

# n log n + n(log n(log n)) = n log n + n log (n(log n)) is O(n log n)

# C-3.36
"""Describe an efficient algorithm for finding the ten largest elements in a sequence of size n. What is the running
time of your algorithm?"""

# This algorithm can be done in O(n) time.
# First initialize a list that will hold the ten maximum numbers.
# Then iterate through the sequence and find the maximum number and its position.
# Remove the number from the sequence and add to the list of maximum numbers.
# Repeat this 10 times.

# An alternative that would take O(n log n) time but may be more efficient in some cases
# Sort the data
# Use list comprehensions to get the last 10 elements.

# The second algorithm is more efficient so long as 10 n < n log n, where n is the size of the sequence.

# C-3.37
"""Give an example of a positive function f(n) such that f(n) is neither O(n) nor Ω(n)"""

# An exponentially growing oscillating function would be an example of a function that's neither upper nor lower bounded
# by n. For example x^2 * (sin(x) + 1)

# C-3.38
"""Show that sum_(i=1)^(n) i^2 is O(n^3)"""

# A way to calculate the sum is to take the integral. In this case you would get n^3 / 3 + C where C is a constant.
# This number would be less than taking the sum, but would grow at the same rate.
# We can say that (n^3)/3 + C <= cn^3
# Or sum_(i=1)^n is O(n^3)

# C-3.39
"""Show that sum_(i=1)^(n) i/(2^i) < 2 (Hint: Try to, term by term, bound this sum with a geometric progression"""

# TODO: Come back to this later.

# C-3.40
"""Show that log_b f(n) is Θ(log f(n)) if b > 1 is a constant."""

# Θ(log f(n)) means
# c' log f(n) <= log_b f(n) <= c'' log f(n) for n >= n0.
# log_b x = log_2 x / log_2 b
# log_2 b is a constant.
# Take constants c' and c'' such that
# c' <= 1 / log b <= c''
# And c' log f(x) <= log f(x) / log b <= c'' log f(x) will be true.
# And thus log_b f(x) is Θ(log f(x))

# C-3.41
"""Describe an algorithm for finding both the minimum and maximum of n numbers using fewer than 3n/2 comparisons.
(Hint: First, construct a group of candidate minimums and a group of candidate maximums)"""

# Check the first number. All numbers lower will go into a list, all numbers higher will go in another list.
# This is n comparisons.

def find_min_max(s):
    # Split the table into two.
    # Compare first number of first list to that of second list. Whichever is higher/lower goes into a list of maximums
    # or minimums. (n/2 comparisons).
    # Find the maximum from the maximum table and the minimum from the minimum table. (n/2 comparisons each)
    # Total of 3n/2 comparisons
    # Do recursively for fewer than 3n/2 comparisons.
    # TODO: Make recursive.
    # If length is odd, compare to last value.
    first_list_length = int((len(s) / 2))
    second_list_length = len(s)
    first_list = s[:first_list_length]
    second_list = s[first_list_length:second_list_length]
    candidate_maximums = []
    candidate_minimums = []
    comparison_count = 0
    i = 0
    for i, value in enumerate(first_list):
        comparison_count += 1
        if value > second_list[i]:
            candidate_minimums.append(second_list[i])
            candidate_maximums.append(value)
        else:
            candidate_minimums.append(value)
            candidate_maximums.append(second_list[i])
    if len(s) % 2 == 1:
        comparison_count += 1
        if s[-1] < candidate_maximums[0]:
            candidate_minimums.append(s[-1])
        else:
            candidate_maximums.append(s[-1])

    max_value = -math.inf
    min_value = math.inf

    for number in candidate_maximums:
        comparison_count += 1
        if number > max_value:
            max_value = number

    for number in candidate_minimums:
        comparison_count += 1
        if number < min_value:
            min_value = number

    print(comparison_count)
    return max_value, min_value

print(find_min_max([random.randrange(0, 100) for x in range(20)]))  # 30 comparisons
print(find_min_max([random.randrange(0, 100) for x in range(100)])) # 150 comparisons
print(find_min_max([random.randrange(0, 100) for x in range(3)])) # 5 comparisons

# C-3.42
"""Bob built a Web site and gave the URL only to his n friends, which he numbered from 1 to n. He told friend number i
that he/she can visit the Web site at most i times. Now Bab has a counter, C, keeping track of the total number of 
visits to the site (but not the identities of who visits). What is the minimum value for C such that Bob can know that 
one of his friends has visited his/her maximum allowed number of times?"""

# If all of Bob's friends visit a maximum of i times as they were told to, the total visitor count would be
# n(n + 1)/2. Any number higher than this and someone exceeded their alotted number of visits.


# C-3.43
"""Draw a visual justification of Proposition 3.3 analogous to that of Figure 3.3(b) for the case when n is odd."""

# You would simply split the last bar in the bar chart in half. One half would go on the top, and the other on the
# bottom. That way you are still multiplying n + 1 by n/2  to get n(n+1) / 2

# C-3.44
"""Communication security is extremely important in computer networks, and one way many network protocols achieve 
security is to encrypt mesages. Typical cryptographic schemes for the secure transmission of messages over such 
networks are based on the fact that no efficient algorithms are known for factoring large integers. Hence if we can
represent a secret message by a large prime number p, we can transmit, over the network, the number r = p * q where
q > p is another large prime number that acts as the encryption key. An eavesdropper who obtains the transmitted number
r on the network would have to factor r in order to figure out the secret message p. 

Using factoring to figure out a message is very difficult without knowing the encryption keey q. To understand why, 
consider the following naive algorithm:

for p in range(2, r):
  if r % p == 0:
    return 'The secret message is p!'
"""

# 23 and 29 are prime numbers. r = 23 * 29 = 667

"""a. Suppose that the eavesdropper uses the above algorithm and has a computer that can carry out in 1 microsecond 
a division between two integers of up to 100 bits each. Give an estimate of the time that it will take in the worst
case to decipher the secret message p if the transmitted message r has 100 bits."""

# r is 2^100 - 1 = 1.27e30.
# When q = p, q^2 = r.
# sqrt(r) = 1.13e15
# But q > p, and so q > 1.13e15 and p < 1.13e15.
# Regardless, in the worst case, 1.13e15 operations need to be conducted to get to p.
# It would take 1.13e15 microseconds, or 1.13e9 seconds, or 13031 days or more than 35 years to find out p.

"""b. What is the worst-case time complexity of the above algorithm? Since the input to the algorithm is just one large
number r, assume the input size n is the number of bytes needed to store r, that is, n = floor(log_2 r / 8) + 1, and 
that each division takes time O(n)."""

# TODO: Not sure what this is asking?

# C-3.45
"""A sequence S contains n - 1 unique integers in the range [0, n - 1], that is, there is one number from this range
that is not in S. Design an O(n)-time algorithm for finding that number. You are only allowed to use O(1) additional
space besides the sequence S itself."""

# Calculate the expected sum of S using n(n+1)/2. Take the sum of the range [0, n - 1]. Calculate the difference between
# these two- that is the number that is not in S.

def missing_number(S):
    expected_sum = (len(S) * (len(S) + 1)) / 2
    actual_sum = sum(S)
    return expected_sum - actual_sum

# C-3.46
"""Al says he can prove that all sheep in a flock are the same colour:

Base case: One sheep. It is clearly the same colour as itself.
Induction step: A flock of n sheep. Take a sheep, a, out. The remaining n - 1 are all the same colour by induction. Now
put sheep a back in and take out a different sheep, b. By induction, the n-1 sheep (now with a) are all the same colour.
Therefore, all the sheep in the flock are the same colour. What is wrong with Al's justification?"""

# He didn't prove that the n - 1 sheep are all the same colour.

# C-3.47
"""Let S be a set of n lines in the plane such that no two are parallel and no three meet in the same point. Show, 
by induction, that the lines in S determine Θ(n^2) intersection points."""

# No lines are parallel i.e. they all meet each other at some point. But no three meet in the same point
# within the plane.

# Base case: Let a line a, meet all other lines n - 1 once, but not all at the same time. It would have n - 1
# intersections.
# Induction step: Say all lines are like this in the worst-case. You would get n * (n - 1) intersections.
# Or n^2 - n intersections.
# n^2 - n <= cn^2 for c = 1 and n >= 1
# n^2 - n <= cn^2 for c = 2 and n >= 1
# And so the number of intersections are bounded by　Θ(n^2).

# C-3.48
"""Consider the following 'justification' that the Fibonacci function, F(n) is O(n):
Base case (n <= 2): F(1) = 1 and F(2) = 2.
Induction step (n > 2): Assume claim true for n' < n. Consider n. F(n) = F(n -2) + F(n - 1). By induction, F(n-2) is
O(n - 2) and F(n - 1) is O(n - 1). Then F(n) is O((n-2) + (n-1)), by the identity presented in Exercise R-3.11. Therefore,
F(n) is O(n).

What is wrong with this justification."""

# F(n - 2) being O(n - 2) and F(n - 1) being O(n - 1) was not justified.  The n in O(n) is not the same n as in F(n)

# C-3.49.
"""Consider the Fibonacci function F(n). Show by induction that F(n) is Ω((3/2)^n) or Ω(1.5^n）"""

# Base case: F(2) = 2, F(1) = 1. These are both less than 1.5^n.
# F(3) = 3, 1.5^3 = 27/8
# F(4) = 5, 1.5^4 = 81/16
# F(5) = 8, 1.5^5 = 243/32.
# F(5) >= 3/2^5.

# Induction step: We claim F(n) is Ω(3/2^n) for n > 5.
# F(n) = F(n-2) + F(n-1)
# Then (3/2)^(n-2) + (3/2)^(n-1) >= (3/2)^n
# (3/2)^n * (3/2)^-2 + (3/2)^n * (3/2)^-1 >= (3/2)^n
# (3/2)^n((3/2)^-2 + (3/2)^-1) >= (3/2)^n
# (3/2)^n(4/9 + 2/3)
# = 10/9 (3/2)^n >= (3/2)^n
# Which is true.

# C-3.50
"""Let p(x) be a polynomial of degree n. Sigma_(i=0)^(n) a_i x^i
a) Describe a simple O(n^2)-time algorithm for computing p(x)"""

# a is a sequence of length n
# def computer_polynomial(a):
#   n = len(a)
#   total = 0
#   for i in range(n):
#     ai = a[i]
#     xi = 1
#     for x in range(i):
#       xi *= x
#     total += a * xi
#   return total
#
#  The first loop makes n passes, and the inner loop makes 1 + 2 + 3 +... + n passes.
# n + n(n+1)/2 passes in total. Or O(n^2)

"""b) Describe an O(n log n)-time algorithm for computing p(x), based upon a more efficient calculation of x^i"""

# TODO: Why create a convoluted O(n log n) algorithm when there's a straightforward O(n) algorithm? :thinking:

# C-3.51
"""Show the summation Sigma_(i=1)^(n) log i is O(n log n)"""

# Base case: n = 1.
# log 1 <= c * (1) log (1)
# 0 <= 0. Holds true.
# Induction step.
# Sigma_(i=1)^(n) log i = log 1 + log 2 + log 3 + ... + log (n - 1) + log n <= c * n log n
# By the identity that log_b ac = log_b a + log_b c we see that...
# Sigma_(i=1)^(n) log i = log (1 * 2 * 3 * 4 * ... * n -1 * n) = log n! < c * n log n
# n log n = log n^n
# log n! <= log n^n by definition since n! <= n^n since n * (n - 1) * (n - 2) ... (n - n) <= n * n * n * n
# And so Sigma_(i=1)^(n) log i is O(n log n)

# C-3.52
"""Show the summation Sigma_(i=1)^(n) log i is Ω(n log n)"""

# TODO: To be continued

# C-3.53
"""An evil king has n bottles of wine, and a spy has just poisoned one of them. Unfortunately, they do not know which 
one it is. The poison is very deadly; just one drop diluted even a billion to one will still kill. Even so, it takes a
full month for the poison to take effect. Design a scheme for determining exactly which one of the wine bottles was 
poisoned in just one month's time while expanding O(log n) taste testers."""

# log n taste testers... n bottles of wine. 1 is poisoned.
# 1/n bottles is poisoned. For each bottle drank, you add 1/n chance that you've drank the poisoned bottle.
# If no one dies, then the poison is in the remaining bottle(s).
# If n = 1, then there is a 1/1 chance that bottle is poisoned, In other words, it is certainly poisoned.
# If n = 2, then there is a 1/2 chance the bottle is poisoned. But you have log 2, or 1, taste tester. If they drink
# the bottle and die, then it is poison, if not, the other is poison.
# For n = 3, you have log 3 taste testers... 1.58? Take the ceiling. Same logic as n = 2 applies. If either die, poisoned
# bottle is found. If neither die, then the remaining bottle is poison.
# For n = 4, you have two testers. Have tester #1 drink bottle n = 1 and n = 2. Have tester #2 drink n = 2, n = 3.
# For n = 5, you have three testers. Have tester #1 drink n = 1, n = 2. Tester #2 drinks n = 2, n = 3. Tester #3
# drinks n = 4.
# For n = 6, you have three testers. Have tester #1 drink n = 1, n = 2. Tester #2 drinks n = 2, n = 3, n = 4. Tester #3
# drinks n = 4, n = 5.
# For n = 7, you have three testers. Have tester #1 drink 1, 2, 5. Tester #2 drinks 2, 3, 4.  #3 drinks 4, 5, 6.
# For n = 8, you have three testers. Tester #1 drinks 1, 2, 5, 7. Tester #2 drinks 2, 3, 4, 7. #3 drinks 4, 5, 6, 7
# For n = 9, you have four testers.
# For n = 11, you have four testers. T#1 drinks 1, 2, 4, 7. T#2 drinks 2, 3, 5, 8. T#3 drinks 4, 5
# For each additional tester. You can test for AND and OR configurations.
# a AND b
# ~a AND ~b = a OR b by DeMorgan's law.
# ~a AND b
# a AND ~b
# With 2 testers, there are 2 * 2 choices. You can test up to 4 bottles with that.
# With 3 testers, there are 2 * 2 * 2 choices. You can test up to 8 bottles with that.
# a AND b AND c
# ~a AND b AND c
# ~a AND ~b AND c
# ~a AND b AND ~c
# ~a AND ~b AND ~c
# a AND ~b AND c
# a AND ~b AND ~c
# a AND b AND ~c
# With 4 testers, there are 16 choices.
# With n testers, there are 2^n choices.

# You can test n bottles with log n tasters, because n tasters can taste 2^n bottles.
# log (2^n) = n.
# So n bottles can be tested n times by log n tasters.

# C-3.54
"""A sequence S contains n integers taken from the interval [0, 4n], with repetitions allowed. Describe an efficient
algorithm for determining an integer value k that occurs the most often in S. What is the running time of your 
algorithm?"""

# Initialize an empty dictionary
# Go through each number on the list. Add +1 to the dictionary each time it occurs.
# Go through the dictionary and find the maximum number.
# This would take O(n) time.
