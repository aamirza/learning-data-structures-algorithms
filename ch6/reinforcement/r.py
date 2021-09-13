# R-6.1
"""What values are returned during the following series of stack operations, if executed upon an initially empty
stack?

push(5), push(3), pop(), push(2), push(8), pop(), pop(), push(9), push(1), pop(), push(7), push(6), pop(), pop(),
push(4), pop(), pop()"""

"""
push(5) - [5]
push(3) = [5, 3]
pop() - 3
push(2) - [5, 2]
push(8) - [5, 2, 8]
pop() - 8
pop() - 2
push(9) - [5, 9]
push(1) - [5, 9, 1]
pop() - 1
push(7) - [5, 9, 7]
push(6) - [5, 9, 7, 6]
pop() - 6
pop() - 7
push(4) - [5, 9, 4]
pop() - 4
pop() - 9
"""


# R-6.2
"""Suppose an initially empty stack S has executed a total of 25 push operations, 12 top operations, and 10 pop 
operations, 3 of which raised Empty errors that were caught and ignored. What is the current size of S?"""

# Since you had 25 push operations, and 7 pop operations that were actually succeesful, there would be 25 - 7 = 18
# elements in the stack.

# R-6.3
"""Implement a function with signature transfer(S, T) that transfers all elements from stack S onto stack T, so that 
the element that starts at the top of S is the first to be inserted onto T, and the element at the bottom of S ends up 
up at the top of T."""

from collections import deque

def transfer(S: deque, T: deque):
    """
    >>> a = deque([5, 9, 2, 4, 5, 7])
    >>> b = deque()
    >>> transfer(a, b)
    >>> a
    deque([])
    >>> b
    deque([7, 5, 4, 2, 9, 5])
    """
    while len(S) > 0:
        T.append(S.pop())

# R-6.4
"""Give a recursive method for removing all the elements from a stack."""

def remove_all_from_stack(stack: deque):
    """
    >>> a = deque([5, 9, 2, 4, 5, 7])
    >>> remove_all_from_stack(a)
    >>> a
    deque([])
    """
    if len(stack) == 0:
        return
    else:
        stack.pop()
        remove_all_from_stack(stack)

# R-6.5
"""Implement a function that reverses a list of elements by pushing them onto a stack in one order, and writing them 
back to the list in reversed order."""

def reverse_list(L):
    """
    >>> L  = [10, 4, 6, 3, 2, 9]
    >>> reverse_list(L)
    >>> L
    [9, 2, 3, 6, 4, 10]
    """
    S = deque()
    new_S = deque()
    j = 0
    while len(L) > 0:
        S.append(L.pop())
    while len(S) > 0:
        new_S.append(S.pop())
    while len(new_S) > 0:
        L.append(new_S.pop())

# R-6.6
"""Give a precise and complete definition of the concept of matching for grouping symbols in an arithmetic expression. 
Your definition may be recursive."""

# Not sure what this is asking

# R-6.7
"""What values are returned during the following sequence of que operations, if executed on an initially empty queue?"""

"""
enqueue(5) - [5]
enqueue(3) - [5, 3]
dequeue() - 5
enqueue(2) - [3, 2]
enqueue(8) - [3, 2, 8]
dequeue() - 3
dequeue() - 2
enqueue(9) - [8, 9]
enqueue(1) - [8, 9, 1]
dequeue() - 8
enqueue(7) - [9, 1, 7] 
enqueue(6) - [9, 1, 7, 6]
dequeue() -  9
dequeue() - 1
enqueue(4) - [7, 6, 4]
dequeue() - 7
dequeue() - 6
"""

# R-6.8
"""Suppose an initially empty queue Q has executed a total of 32 enqueue operations, 10 first operations, and 15 dequeue
operations, 5 of which raised Empty errors that were caught and ignored. What is the current size of Q?"""

# There were 32 elements enqueued into the queue, 10 which were dequeued (!5 - 5), so there are 22 elements remaining.

# R-6.9
"""Had the queue of the previous problem been an instance of ArrayQueue that used an initial array capacity of 30, and 
had its size never been greater than 30, what would be the final value of the _front instance variable?"""

# Seeing as dequeue was called successfully 10 times, front should equal 10.


# R-6.10
"""
Consider what happens if the loop in the ArrayQueue._resize method at lines 53-55 of Code Fragment 6.7 had been 
implemented as:

for k in range(self._size):
    self._data[k] = old[k]
"""

# The data would be out of order, because the kth datapoint is not necessarily the kth item in the stack. You would also
# need a larger array

# R-6.11
"""
Give a simple adapter that implements our queue ADT while using a collections.deque instance for storage.
"""

from collections import deque


class ArrayQueue:
    def __init__(self):
        self._data = deque()

    def __str__(self):
        return f"Queue({self._data})"

    def __len__(self):
        return len(self._data)

    def enqueue(self, value):
        self._data.append(value)

    def dequeue(self):
        return self._data.popleft()

    def first(self):
        return self._data[0]

    def is_empty(self):
        return len(self._data) == 0


# R-6.12
"""What values are returned during the following sequence of deque ADT operations on an initially empty deque?"""

"""
add_first(4),     [4]
add_last(8),      [4, 8]
add_first(5),     [5, 4, 8]
back(),           8
delete_first(),   5
delete_last(),    8
add_first(5),     [5, 4]
back(),           4
delete_first(),   5
delete_last(),    4
add_last(7),      [7]
first(),          7
last(),           7
add_last(6),      [7, 6]
delete_first(),   7
delete_first()    6
"""

# R-6.13
"""Suppose you have a deque D containing the numbers (1, 2, 3, 4, 5, 6, 7, 8), in this order. Suppose further that you
have an initially empty queue Q. Give a code fragment that uses only D and Q (and no other variable) and results in D
storing the elements in the order (1, 2, 3, 5, 4, 6, 7, 8). [note 5 and 4 are swapped]"""

"""
D = deque([1, 2, 3, 4, 5, 6, 7, 8])
Q = ArrayQueue()


    # 1, 2, 3 // 4, 5, 6, 7, 8
    # [] // 4, 5, 6, 7, 8, 1, 2, 3
    # 4, 5 // 6, 7, 8, 1, 2, 3
    # [] // 4, 6, 7, 8, 1, 2, 3, 5
    # 4, 6, 7, 8 // 1, 2, 3, 5
    # [] // 1, 2, 3, 5, 4, 6, 7, 8

while D[0] != 4:
    Q.enqueue(D.popleft())
print(f"Step 1: {Q}, {D}")

while not Q.is_empty():
    D.append(Q.dequeue())
print(f"Step 2: {Q}, {D}")

while D[0] in (4, 5):
    Q.enqueue(D.popleft())
print(f"Step 3: {Q}, {D}")

while not Q.is_empty():
    if Q.first() == 4:
        D.appendleft(Q.dequeue())
    elif Q.first() == 5:
        D.append(Q.dequeue())
print(f"Step 4: {Q}, {D}")

while D[0] != 1:
    Q.enqueue(D.popleft())
print(f"Step 5: {Q}, {D}")

while not Q.is_empty():
    D.append(Q.dequeue())
print(f"Step 6: {Q}, {D}")
"""

# R-6.14
"""Repeat the previous problem using the deque D and an initially empty stack S.

Start: (1, 2, 3, 4, 5, 6, 7, 8)
Result: (1, 2, 3, 5, 4, 6, 7, 8)"""


"""
class ArrayStack:
    def __init__(self):
        self._data = deque()

    def __str__(self):
        return f"Stack({self._data})"

    def __len__(self):
        return len(self._data)

    def pop(self):
        return self._data.pop()

    def push(self, e):
        self._data.append(e)

    def first(self):
        return self._data[-1]

    def is_empty(self):
        return len(self._data) == 0



D = deque([1, 2, 3, 4, 5, 6, 7, 8])
S = ArrayStack()

def print_step(n):
    print(f"Step {n}: {S}, {D}")

# [] // 1, 2, 3, 4, 5, 6, 7, 8
# [1, 2, 3, 4, 5, 6, 7, 8] // []
# [1, 2, 3, 4, 5] // [6, 7, 8]
# [1, 2, 3] // 4, 6, 7, 8, 5
# [1, 2, 3, 5] // 4, 6, 7, 8
# [] // 1, 2, 3, 5, 4, 6, 7, 8



while len(D) != 0:
    S.push(D.popleft())
print_step(1)

while len(D) == 0 or D[0] != 6:
    D.appendleft(S.pop())
print_step(2)

while S.first() in (4, 5):
    if S.first() == 4:
        D.appendleft(S.pop())
    elif S.first() == 5:
        D.append(S.pop())
print_step(3)

if D[-1] == 5:
    S.push(D.pop())
print_step(4)

while len(S) != 0:
    D.appendleft(S.pop())
print_step(5)
"""
