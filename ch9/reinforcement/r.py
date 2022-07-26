# R-9.1
"""
How long would it take to remove the ceiling(log n) smallest elements from a heap that contains n entries, using the remove_min
operation?
"""

# Since remove_min is an O(log(n)) operation, removing log(n) elements should take log(n) * log(n)  time. Or (log(n))^2


# R-9.2
"""
Suppose you label each position p of a binary tree T with a key equal to its preorder rank. Under what circumstances
is p a heap?
"""

"""
                1
            2          5
        3     4
"""

# p will remain a heap so long as it is complete. That is the to say the last preorder element resides in the leftmost
# position in that level.


# R-9.3
"""
What does each remove_min call return within the following sequence of priority queue ADT methods: 
"""


"""                 
                                Return Value                Priority Queue
add(5,A)                                                    [{5,A}]
add(4,B)                                                    [{4,B}, {5,A}]
add(7,F)                                                    [{4,B}, {5,A}, {7,F}]
add(1,D)                                                    [{1,D}, {4,B}, {7,F}, {5,A}]
remove_min()                    {1,D}                       [{4,B}, {5,A}, {7,F}]
add(3,J)                                                    [{3,J}, {4,B}, {7,F}, {5,A}]
add(6,L)                                                    [{3,J}, {4,B}, {7,F}, {5,A}, {6,L}]
remove_min()                    {3,J}                       [{4,B}, {5,A}, {7,F}, {6,L}]
remove_min()                    {4,B}                       [{5,A}, {6,L}, {7,F}]
add(8,G)                                                    [{5,A}, {6,L}, {7,F}, {8,G}]
remove_min()                    {5,A}                       [{6,L}, {8,G}, {7,F}]
add(2,H)                                                    [{2,H}, {6,L}, {7,F}, {8,G}]
remove_min()                    {2,H}                       [{6,L}, {8,G}, {7,F}]
remove_min()                    {6,L}                       [{7,F}, {8,G}]
"""

# R-9.4
"""
An airport is developing a computer simulation of air-traffic control that handles events such as landings and takeoffs.
Each event has a time stamp that denotes the time when the event will occur. The simulation program needs to efficiently
perform the following two fundamental operations:
    * Insert an event with a given time stamp (that is, add a future event)
    * Extract the event with smallest time stamp (that is, determine the next event to process).

Which data structure should be used for the above operations? Why?
"""

# A heap is a good way to store this data.
# This is because the add operation would take a maximum of O(log(n)) time, and extracting the smallest time stamp
# would also take O(log(n)) time.

# Unsorted/sorted lists would be poorly suited to this situation, since an unsorted list would take O(n) time to get
# the smallest time stamp, whereas a sorted list would take O(n) would to add


# R-9.5
"""
The min method for the UnsortedPriorityQueue class executes in O(n) time. Give a simple modification to the class so 
that min runs in O(1) time. Explain any necessary modifications to other methods of the class.
"""

# A simple modification would be so that the element is sorted when it's added to the list, making the class a
# sorted priority queue. This will turn _add from an O(1) to an O(n) function, but will turn min into a O(1) function.


# R-9.6
"""
Can you adapt your solution to the previous problem to make remove_min run in O(1) time for the UnsortedPriorityQueue
class? Explain your answer.
"""

# Yes, since finding min() takes O(1), remove_min should take O(1) time too. The list would still be sorted when
# when the minimum element is removed.

# R-9.7
"""
Illustrate the execution of the selection-sort algorithm on the following input sequence:
(22,15,36,44,10,3,9,13,29,25)
"""


"""
            Collection C                        Priority Queue Q
Input       (22,15,36,44,10,3,9,13,29,25)       ()
Phase 1
1           (15,36,44,10,3,9,13,29,25)          (22)
2           (36,44,10,3,9,13,29,25)             (22,15)
3           (44,10,3,9,13,29,25)                (22,15,36)
4           (10,3,9,13,29,25)                   (22,15,36,44)
5           (3,9,13,29,25)                      (22,15,36,44,10)
6           (9,13,29,25)                        (22,15,36,44,10,3)
7           (13,29,25)                          (22,15,36,44,10,3,9)
8           (29,25)                             (22,15,36,44,10,3,9,13)
9           (25)                                (22,15,36,44,10,3,9,13,29)
10          ()                                  (22,15,36,44,10,3,9,13,29,25)
Phase 2
1           (3)                                 (22,15,36,44,10,9,13,29,25)
2           (3,9)                               (22,15,36,44,10,13,29,25)
3           (3,9,10)                            (22,15,36,44,13,29,25)
4           (3,9,10,13)                         (22,15,36,44,29,25)
5           (3,9,10,13,15)                      (22,36,44,29,25)
6           (3,9,10,13,15,22)                   (36,44,29,25)
7           (3,9,10,13,15,22,25)                (36,44,29)
8           (3,9,10,13,15,22,25,29)             (36,44)
9           (3,9,10,13,15,22,25,29,36)          (44)
10          (3,9,10,13,15,22,25,29,36,44)       ()          
"""


# R-9.8
"""
Illustrate the execution of the selection-sort on the insertion-sort algorithm on the input sequence of the previous 
problem.
"""

"""
            Collection C                        Priority Queue Q
Input       (22,15,36,44,10,3,9,13,29,25)       ()
Phase 1
1           (15,36,44,10,3,9,13,29,25)          (22)
2           (36,44,10,3,9,13,29,25)             (15,22)
3           (44,10,3,9,13,29,25)                (15,22,36)
4           (10,3,9,13,29,25)                   (15,22,36,44)
5           (3,9,13,29,25)                      (10,15,22,36,44)
6           (9,13,29,25)                        (3,10,15,22,36,44)
7           (13,29,25)                          (3,9,10,15,22,36,44)
8           (29,25)                             (3,9,10,13,15,22,36,44)
9           (25)                                (3,9,10,13,15,22,29,36,44)
10          ()                                  (3,9,10,13,15,22,25,29,36,44)
Phase 2
1           (3)                                 (9,10,13,15,22,25,29,36,44)
2           (3,9)                               (10,13,15,22,25,29,36,44)
3           (3,9,10)                            (13,15,22,25,29,36,44)
4           (3,9,10,13)                         (15,22,25,29,36,44)
5           (3,9,10,13,15)                      (22,25,29,36,44)
6           (3,9,10,13,15,22)                   (25,29,36,44)
7           (3,9,10,13,15,22,25)                (29,36,44)
8           (3,9,10,13,15,22,25,29)             (36,44)
9           (3,9,10,13,15,22,25,29,36)          (44)
10          (3,9,10,13,15,22,25,29,36,44)       ()                       
"""

# R-9.9
"""
Give an example of a worst-case sequence with n elements for insertion-sort, and show that insertion-sort runs in 
Ω(n^2) time on such a sequence.
"""

# The worst-case example for an insertion-sort were if the numbers in the collection were in descending order.

# Take for example a collection C with 10 numbers in descending order. You take the first number from that collection
# and it to the priority queue. One number by itself is sorted, so this is 1 operation.

# When the second number is added to the priority queue, it must be compared with the number from the previous step. On
# deciding it is smaller, it will be added to the front of the queue. This is 2 operations.

# With a third number, it must compared to the two numbers in the previous step before it is added to the front. This is
# 3 operations...

# We see the familiar 1 + 2 + 3 + 4... + n operations. This type of collection will always be insert-sorted in Ω(n^2).


# R-9.10
"""
At which hpositions of a heap might the third smallest key be stored?
"""

# Any position at d = 1 would do. In the array, it could be at indexes 1 or 2 (2nd and 3rd positions)

# R-9.11
"""At which positions of a heap might the largest key be stored."""

"""
e.g.
        2
    5       67
7     8
"""

# What is true about the largest key is that it will always be a leaf position, meaning it can be found at the lowest
# depth or the second lowest depth.

# R-9.12
"""
Consider a situation in which a user has numeric keys and wishes to have a priority queue that is maximum-oriented. How
could a standard (min-oriented) priority queue be used for such a purpose?
"""

# Assuming the priority queue is already sorted, and the data is stored in a positiona list, you could just have
# a remove_max and max methods that return the tail of the list, the same way as returning the head when calling min()
# and remove_min().

# R-9.13
"""
Illustrate the execution of the in-place heap-sort algorithm on the following input sequence: 
(2,5,16,4,10,23,39,18,26,15).
"""

# Check Page 389.
# In place heap-sorting is when you first construct a heap, then deconstruct it using remove_min


"""
