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
stack.

Hint: Use a stack to reduce the problem to that of enumerating all permutations of the numbers {1,2,...,n−1}"""


from collections import deque

def permutate(number):
    nums = {x for x in range(1, number+1)}
    S = ArrayStack()

    for num in nums:
        S.push(([num], nums - {num}))

    while not S.is_empty():
        l, remaining = S.pop()
        if len(remaining) == 0:
            print(l)
        else:
            for n in remaining:
                l2 = l.copy()
                l2.append(n)
                S.push((l2, nums - set(l2)))

# C-6.21
"""Show how to use a stack S and a queue Q to generate all possible subsets of an n-element set T non-recursively

Hint: Use the stack to store the elements yet to be used to generate subsets and use the queue to store the subsets 
generated so far."""


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


def get_all_subsets(T: set):
    S = ArrayStack()  # Use S to store k, set, universe
    Q = ArrayQueue()

    S.push([[], {num for num in T}])

    while not S.is_empty():
        old_S, old_T = S.pop()
        if len(old_S) > 0:
            Q.enqueue(old_S)
        new_T = {element for element in old_T}
        for element in old_T:
            new_S = old_S + [element] if old_S else [element]
            new_T = new_T.difference({element})
            S.push([new_S, new_T])

    while not Q.is_empty():
        print(Q.dequeue())

get_all_subsets({1, 2, 3})

# C-6.22
"""
Postfix notation is an unambiguous way of writing an arithmetic expression without paranthesis. It is defined so that
Postfix notation is an unambiguous way of writing an arithmetic expres- sion without parentheses. It is defined so that 
if “(exp1)op(exp2)” is a normal, fully parenthesized expression whose operation is op, the postfix version of this is 
“pexp1 pexp2 op”, where pexp1 is the postfix version of exp1 and pexp2 is the postfix version of exp2. The postfix 
version of a sin- gle number or variable is just that number or variable. For example, the postfix version of 
“((5+2)∗(8−3))/4” is “5 2 + 8 3 − ∗ 4 /”. Describe a nonrecursive way of evaluating an expression in postfix notation.
"""

def postfix_calculator(postfix_expression):
    """
    >>> postfix_calculator("5 2 + 8 3 - * 4 /")
    8.75
    >>> postfix_calculator("5 7 + 8 10 + 2 * /") == 1/3 # (5 + 7)/(2 * (8 + 10))
    True
    """
    expression_list = postfix_expression.split(' ')
    expressions = deque()
    evaluated_expressions = deque()
    for expression in expression_list:
        try:
            expression = int(expression)
            expressions.append(expression)
        except ValueError:
            if expression not in ('+', '-', '*', '/'):
                raise ValueError('Invalid expression.')
            operand = expression
            if len(expressions) > 0:
                if len(expressions) > 1:
                    statement_to_evaluate = f'{expressions.popleft()} {operand} {expressions.popleft()}'
                elif len(expressions) == 1:
                    statement_to_evaluate = f'{evaluated_expressions.pop()} {operand} {expressions.popleft()}'
            else:
                statement_to_evaluate = f'{evaluated_expressions.popleft()} {operand} {evaluated_expressions.popleft()}'
            answer = eval(statement_to_evaluate)
            evaluated_expressions.append(answer)
    if len(evaluated_expressions) != 1:
        raise ValueError('Wrong number of parantheses')
    return evaluated_expressions.pop()


# C-6.23
"""Suppose you have three nonempty stacks R, S, and T. Describe a sequence of operations that results in S storing all
elements originally in T below all of S's original elements, with both sets of those elements in their original order.

For example, if R = [1, 2, 3], S = [4, 5], and T = [6, 7, 8, 9], the final configuration should have R = [1, 2, 3] and 
S = [6, 7, 8, 9, 4, 5]"""

def stack_transfer(R, S ,T):
    """
    >>> R = [1, 2, 3]
    >>> S = [4, 5]
    >>> T = [6, 7, 8, 9]
    >>> stack_transfer(R, S, T)
    >>> S
    [6, 7, 8, 9, 4, 5]
    >>> R
    [1, 2, 3]
    >>> T
    []
    >>> R = [5]
    >>> S = [7, 9, 2, 5]
    >>> T = [3, 7, 5, 5]
    >>> stack_transfer(R, S, T)
    >>> R
    [5]
    >>> S
    [3, 7, 5, 5, 7, 9, 2, 5]
    >>> T
    []
    """
    original_length = len(R)
    while len(S) > 0:
        R.append(S.pop())
    while len(T) > 0:
        R.append(T.pop())
    while len(R) != original_length:
        S.append(R.pop())


# C-6.24
"""Describe how to implement the stack ADT using a single queue as an instance variable, and only constant additional 
local memory within the method bodies. What is the running time of the push(), pop(), and top() methods for your design?
"""

class ArrayStackButActuallyQueue():
    def __init__(self):
        self._data = ArrayQueue()

    def __len__(self):
        return len(self._data)

    def pop(self):
        if self.is_empty():
            raise Empty('Stack is empty')
        return self._data.dequeue()

    def push(self, e):
        if self.is_empty():
            self._data.enqueue(e)
        else:
            new_queue = ArrayQueue()
            new_queue.enqueue(e)
            while not self._data.is_empty():
                new_queue.enqueue(self._data.dequeue())
            self._data = new_queue


    def top(self):
        if self.is_empty():
            raise Empty('Stack is empty')
        return self._data.first()

    def is_empty(self):
        return len(self) == 0

# curious_stack = ArrayStackButActuallyQueue()
# try:
#     curious_stack.pop()
# except Empty:
#     print('pass')
# curious_stack.push(5)
# print(curious_stack.top())
# curious_stack.push(10)
# print(curious_stack.top())
# print(curious_stack.pop())
# print(len(curious_stack))
# print(curious_stack.pop())
# print(curious_stack.is_empty())

# The running time of push is O(n) where n is the existing length of the stack.
# The running time of pop is O(1)
# The running time of top is O(1)

# C-6.25
"""Describe how to implement the queue ADT using two stacks as instance variables, such that all queue operations 
execute in amortized O(1) time. Give a formal proof of the amortized bound."""

class ArrayQueueButActuallyStack():
    """
    >>> disorganized_queue = ArrayQueueButActuallyStack()
    >>> len(disorganized_queue) == 0
    True
    >>> disorganized_queue.enqueue(5)
    >>> disorganized_queue.enqueue(6)
    >>> disorganized_queue.first()
    5
    >>> disorganized_queue.dequeue()
    5
    >>> len(disorganized_queue)
    1
    >>> disorganized_queue.first()
    6
    >>> len(disorganized_queue)
    1
    >>> disorganized_queue.enqueue(7)
    >>> disorganized_queue.first()
    6
    >>> disorganized_queue.enqueue(10)
    >>> disorganized_queue.enqueue(7)
    >>> disorganized_queue.enqueue(8)
    >>> len(disorganized_queue)
    5
    >>> disorganized_queue.first()
    6
    >>> disorganized_queue.dequeue()
    6
    >>> disorganized_queue.dequeue()
    7
    >>> disorganized_queue.dequeue()
    10
    >>> disorganized_queue.dequeue()
    7
    >>> disorganized_queue.dequeue()
    8
    >>> disorganized_queue.is_empty()
    True
    """
    def __init__(self):
        self._data = ArrayStack()
        self._storage = ArrayStack()

    def __len__(self):
        return len(self._data) + len(self._storage)

    def _need_to_transfer_storage(self):
        return len(self._data) == 0 and len(self._storage) >= 1

    def _transfer_storage(self):
        while len(self._storage) != 0:
            self._data.push(self._storage.pop())

    def enqueue(self, value):
        if len(self._storage) > 0 or len(self._data) >= 1:
            self._storage.push(value)
        elif len(self._data) == 0:
            self._data.push(value)

    def dequeue(self):
        if self.is_empty():
            Empty('Queue is empty')

        if self._need_to_transfer_storage():
            self._transfer_storage()

        return self._data.pop()

    def first(self):
        if self.is_empty():
            Empty("Queue is empty")

        if self._need_to_transfer_storage():
            self._transfer_storage()

        return self._data.top()


    def is_empty(self):
        return len(self._data) == 0 and len(self._storage) == 0

"""All of enqueue, dequeue and first take amoritized O(1) time.

With enqueue it is straightforward. The if conditions of checking lengths take O(1) time, and the pushing to a stack 
also takes O(1) time.

With dequeue, the first pop will be O(1). Once self._data is empty, all the elements in self._storage are transfered
onto self._data, this takes O(n) time where n is the length of self._storage. Then all subsequent pop operations take
O(1) time until self._data is empty.

It is the same with first."""


# C-6.26
"""Describe how to implement the double-ended queue ADT using two stacks as instance variables. What are the running
times of the methods?"""

class ArrayDequeueButActuallyStack:
    """
    >>> dq = ArrayDequeueButActuallyStack()
    >>> dq.is_empty()
    True
    >>> dq.appendleft(5)
    >>> dq.append(7)
    >>> dq.pop()
    7
    >>> len(dq)
    1
    >>> dq.last()
    5
    >>> dq.first()
    5
    >>> dq.appendleft(8)
    >>> dq.appendleft(9)
    >>> dq.last()
    5
    >>> dq.popleft()
    9
    >>> dq.pop()
    5
    >>> dq.pop()
    8
    >>> dq.is_empty()
    True
    >>> dq.append(8)
    >>> dq.append(4)
    >>> dq.first()
    8
    """
    def __init__(self):
        self._left = ArrayStack()
        self._right = ArrayStack()

    def __len__(self):
        return len(self._left) + len(self._right)

    def _left_is_empty(self):
        return len(self._left) == 0

    def _right_is_empty(self):
        return len(self._right) == 0

    def _transfer_right_to_left(self):
        while not self._right.is_empty():
            self._left.push(self._right.pop())

    def _transfer_left_to_right(self):
        while not self._left.is_empty():
            self._right.push(self._left.pop())

    def _need_to_transfer_right_to_left(self):
        return self._left_is_empty() and not self._right_is_empty()

    def _need_to_transfer_left_to_right(self):
        return self._right_is_empty() and not self._left_is_empty()

    def _raise_error_if_empty(self):
        if self.is_empty():
            raise Empty('deque is empty')

    def appendleft(self, e):
        self._left.push(e)

    def append(self, e):
        self._right.push(e)

    def popleft(self):
        self._raise_error_if_empty()

        if self._need_to_transfer_right_to_left():
            self._transfer_right_to_left()

        return self._left.pop()

    def pop(self):
        self._raise_error_if_empty()

        if self._need_to_transfer_left_to_right():
            self._transfer_left_to_right()
            
        return self._right.pop()

    def first(self):
        self._raise_error_if_empty()
        
        if self._need_to_transfer_right_to_left():
            self._transfer_right_to_left()
        
        return self._left.top()

    def last(self):
        self._raise_error_if_empty()
        
        if self._need_to_transfer_left_to_right():
            self._transfer_left_to_right()
        
        return self._right.top()

    def is_empty(self):
        return len(self) == 0

# The amoritized running time is O(1) for all operations. However, constanty doing first() and last() operations will
# result in O(n) running time.

# C-6.27
"""Suppose you have a stack S containing n elements and a queue Q that is initally empty. Describe how you can use
Q to scan S to see if it contains a certain element x, with additional constraint that you algorithm must return the
elements back to S in their original order. You may only use S and Q, and a constant number of other variables."""

def find_in_stack(S, x):
    """
    >>> s = ArrayStack()
    >>> s.push(5)
    >>> s.push(87)
    >>> s.push(9)
    >>> s.push(10)
    >>> s.push(10)
    >>> find_in_stack(s, 87)
    3
    >>> find_in_stack(s, 39)
    -1
    >>> find_in_stack(s, 10)
    0
    """
    Q = ArrayQueue()
    i = 0
    try:
        while S.top() != x:
            Q.enqueue(S.pop())
            i += 1
    except Empty:
        i = -1

    pass_through = 0
    NEEDED_PASS_THROUGHS = 1
    q_len = len(Q)
    while not Q.is_empty():
        S.push(Q.dequeue())
        if Q.is_empty() and pass_through < NEEDED_PASS_THROUGHS:
            pass_through += 1
            while len(Q) != q_len:
                Q.enqueue(S.pop())
    return i


# C-6.28
"""Modify the ArrayQueue implementation so that the queue's capacity is limited to maxlen elements, where maxlen is an 
optional parameter to the constructor (that defaults to None). If enqueue is called when the queue is at full capacity,
throw a Full exception (defined similarly to empty)."""

class ArrayQueueBoring:
    """
    >>> q = ArrayQueueBoring(maxlen=3)
    >>> q.is_empty()
    True
    >>> q.enqueue(3)
    >>> q.enqueue(2)
    >>> q.dequeue()
    3
    >>> q.first()
    2
    >>> len(q)
    1
    >>> q.enqueue(3)
    >>> q.first()
    2
    >>> q.enqueue(5)
    >>> len(q)
    3
    >>> q.enqueue(4) # doctest: +IGNORE_EXCEPTION_DETAIL
    Traceback (most recent call last):
    c.Full: Queue is full.
    >>> q.dequeue()
    2
    >>> q.first()
    3
    >>> q.dequeue()
    3
    >>> q.first()
    5
    >>> q.dequeue()
    5
    >>> q.is_empty()
    True
    >>> q.dequeue() # doctest: +IGNORE_EXCEPTION_DETAIL
    Traceback (most recent call last):
    c.Empty: Queue is empty.
    >>> q2 = ArrayQueueBoring()
    >>> q2.is_empty()
    True
    >>> q.enqueue(3)
    >>> q.first()
    3
    >>> q.enqueue(2)
    >>> len(q)
    2
    >>> q.dequeue()
    3
    >>> q.enqueue(3)
    >>> q.first()
    2
    >>> len(q)
    2
    >>> q.dequeue()
    2
    >>> q.dequeue()
    3
    >>> q.dequeue() # doctest: +IGNORE_EXCEPTION_DETAIL
    Traceback (most recent call last):
    c.Empty: Queue is empty
    """
    def __init__(self, maxlen=None):
        self._data = [None] * maxlen if maxlen else []
        self._maxlen = maxlen
        self._n = 0
        self._start = 0

    def __len__(self):
        return self._n

    def _clean(self):
        """Remove all Nones from list if more than half of list is None."""
        if not self._maxlen and self._start > self._n:
            self._data = self._data[self._start:]
            self._start = 0

    def enqueue(self, e):
        if not self._maxlen:
            self._data.append(e)
            self._n += 1
        elif self._n < self._maxlen:
            self._data[(self._n + self._start) % self._maxlen] = e
            self._n += 1
        else:
            raise Full("Queue is full.")

    def dequeue(self):
        if self.is_empty():
            raise Empty("Queue is empty.")

        value = self._data[self._start]
        self._data[self._start] = None
        self._start += 1
        if self._maxlen:
            self._start = self._start % self._maxlen
        self._n -= 1
        self._clean()
        return value

    def first(self):
        if self.is_empty():
            raise Empty("Queue is empty")

        return self._data[self._start]


    def is_empty(self):
        return self._n == 0


# C-6.29
"""In certain applications of the queue ADT, it is common to repeatedly dequeue an element, process it in some way, and 
then immediately enqueue the same element. Modify the ArrayQueue implementation to include a rotate() method that has 
semantics identical to the combination, Q.enqueue(Q.dequeue()). However, your implementation should be more efficient
 than making two separate calls (for example, because there is no need to modify size)."""

class RotatableQueue(ArrayQueueBoring):
    """
    >>> q = RotatableQueue()
    >>> q.enqueue(5)
    >>> q.enqueue(3)
    >>> q.enqueue(2)
    >>> q.first()
    5
    >>> q.rotate()
    >>> q.first()
    3
    >>> len(q)
    3
    >>> q.rotate()
    >>> q.first()
    2
    >>> q.rotate()
    >>> q.first()
    5
    >>> len(q)
    3
    >>> q.rotate()
    >>> q.dequeue()
    3
    >>> q.dequeue()
    2
    >>> q.dequeue()
    5
    >>> q.rotate() # doctest: +IGNORE_EXCEPTION_DETAIL
    Traceback (most recent call last):
    c.Empty: Queue is empty
    """
    def __init__(self, maxlen=None):
        super().__init__(maxlen)

    def rotate(self):
        # Dequeue, then enqueue the same element.
        if self.is_empty():
            raise Empty("Queue is empty.")

        if self._maxlen:
            self._start += 1
            self._start = self._start % self._maxlen
        else:
            # It is more efficient to modify the size than to move everything around if queue has a limitless length.
            self.enqueue(self.dequeue())

# C-6.30
"""Alice has two queues, Q and R, which can store integers. Bob gives Alice 50 odd integers and 50 even integers and 
insists that she store all 100 integers in Q and R. They then play a game where Bob picks Q or R at random and then 
applies the round-robin scheduler, described in the next chapter, to the chosen queue a random number of times. If the 
last number to be processed at the end of this game was odd, Bob wins. Otherwise, Alice wins. How can Alice allocate 
integers to queues to optimize her chances of winning? What is her chance of winning?"""


# What is Round-Robin Scheduler?

# A round-robin scheduler could be implemented with the queue ADT, by repeatedly performing the following steps on
# queue Q:
    # 1. e = Q.dequeue()
    # 2. Service element e.
    # 3. Q.enqueue()

# So basically, Bob is going to rotate queues a random number of times. Bob wins if the last integer was odd.

# If one Q is full of even numbers and R is full of odd numbers, then the chance of winning is 50%.

# First create a queue of just one number that is even. That automatically creates a minimum 50% chance of winning.
# The next queue will have 49 even numbers and 50 odd numbers. There is a 49/99 chance of winning, or 49.5% chance.
# The chance of winning now will be 1 - (1/2 * 50/99) = 74.75% chance of winning.
