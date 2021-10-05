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
