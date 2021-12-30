# C-7.24
"""Give a complete implementation of the stack ADT using a singly linked list that includes a header sentinel."""
import collections
import html.parser


class Empty(Exception):
    pass


class LinkedStackADT:
    """
    >>> stack = LinkedStackADT()
    >>> stack.push(8)
    >>> stack.top()
    8
    >>> len(stack)
    1
    >>> stack.pop()
    8
    >>> len(stack)
    0
    >>> stack.push(9)
    >>> stack.push(5)
    >>> stack.push(6)
    >>> len(stack)
    3
    >>> stack.is_empty()
    False
    >>> stack.top()
    6
    >>> stack.pop()
    6
    >>> len(stack)
    2
    >>> stack.pop()
    5
    >>> len(stack)
    1
    >>> stack.pop()
    9
    >>> stack.is_empty()
    True
    """
    class _Node:
        __slots__ = '_element', '_next'

        def __init__(self, e, next=None):
            self._element = e
            self._next = next

        def element(self):
            return self._element

    def __init__(self):
        self._header = self._Node(None)
        self._size = 0

    def __len__(self):
        return self._size

    def top(self):
        if self.is_empty():
            raise Empty("List is empty.")
        return self._first().element()

    def push(self, e):
        first = None if self.is_empty() else self._first()
        new_node = self._Node(e, next=first)
        self._header._next = new_node
        self._size += 1

    def pop(self):
        if self.is_empty():
            raise Empty("List is empty.")
        value = self.top()
        next = self._first()._next
        self._header._next = next
        self._size -= 1
        return value

    def is_empty(self):
        return self._size == 0

    def _first(self):
        if self.is_empty():
            raise Empty("List is empty.")
        return self._header._next

# C-7.25
"""Give a complete implementation of the queue ADT using a singly linked list that includes a header sentinel."""




class LinkedQueueADT:
    """
    >>> queue = LinkedQueueADT()
    >>> len(queue)
    0
    >>> queue.enqueue(5)
    >>> queue.first()
    5
    >>> queue.enqueue(7)
    >>> queue.first()
    5
    >>> len(queue)
    2
    >>> queue.enqueue(10)
    >>> queue.first()
    5
    >>> queue.dequeue()
    5
    >>> queue.first()
    7
    >>> len(queue)
    2
    >>> queue.dequeue()
    7
    >>> queue.dequeue()
    10
    >>> queue.is_empty()
    True
    >>> queue.enqueue(7)
    >>> queue.enqueue(9)
    >>> new_queue = LinkedQueueADT()
    >>> new_queue.enqueue(8)
    >>> new_queue.enqueue(11)
    >>> queue.concatenate(new_queue)
    >>> len(queue)
    4
    >>> len(new_queue)
    0
    >>> queue.first()
    7
    >>> queue.dequeue()
    7
    >>> queue.dequeue()
    9
    >>> queue.dequeue()
    8
    >>> queue.dequeue()
    11
    >>> queue.is_empty()
    True
    """
    class _Node:
        __slots__ = '_element', '_next'

        def __init__(self, e, next=None):
            self._element = e
            self._next = next

        def element(self):
            return self._element

    def __init__(self):
        self._header = self._Node(None)
        self._tail = None
        self._size = 0

    def __len__(self):
        return self._size

    def first(self):
        return self._first_node().element()

    def enqueue(self, e):
        new_node = self._Node(e)
        if self.is_empty():
            self._header._next = new_node
        else:
            self._tail._next = new_node
        self._tail = new_node
        self._size += 1

    def dequeue(self):
        value = self._first_node()
        next_node = value._next
        self._header._next = next_node
        self._size -= 1
        if self.is_empty():
            self._tail = None
        return value.element()


    def is_empty(self):
        return self._size == 0

    def concatenate(self, q2):
        self._tail._next = q2._first_node()
        self._tail = q2._tail
        q2._header._next = None
        q2._tail = None
        self._size += len(q2)
        q2._size = 0

    def _first_node(self):
        if self.is_empty():
            raise Empty("List is empty.")
        return self._header._next


# C-7.26
"""Implement a method, concatenate(Q2) for the LinkedQueue class that takes all elements of LinkedQueue Q2 and appends
them to the end of the original queue. The operation should run in O(1) time and should result in Q2 being an empty queue.
"""

# Implemented above!

# C-7.27
"""Give a recursive implementation of a singly linked list class, such that an instance of a nonempty list stores its
first element and a reference to a list of remaining list elements."""

class SinglyLinkedList:
    class _Node:
        def __init__(self, e, next=None):
            self._element = e
            self._next = next

        def element(self):
            return self._element

        def next_node(self):
            return self._next

    def __init__(self):
        self._head = None
        self._tail = None
        self._size = 0

    def __len__(self):
        return self._size

    def __iter__(self):
        cursor = self._head
        while cursor is not None:
            yield cursor
            cursor = cursor._next

    def is_empty(self):
        return len(self) == 0

    def _update_tail(self):
        if self.is_empty():
            raise Empty("List is empty.")
        start = self._head if self._tail is None else self._tail
        while start._next is not None:
            start = start._next
        self._tail = start

    def first(self):
        return self._head

    def last(self):
        return self._tail

    def add_first(self, e):
        new_node = self._Node(e, next=self._head)
        self._head = new_node
        self._size += 1
        self._update_tail()

    def add_last(self, e):
        if self.is_empty():
            self.add_first(e)
        else:
            new_node = self._Node(e)
            self._tail._next = new_node
            self._tail = new_node
            self._size += 1

    def remove_first(self):
        if self.is_empty():
            raise Empty('List is empty')
        value = self._head.element()
        self._head = self._head._next
        self._update_tail()
        self._size -= 1
        return value




# TODO: Not sure what is meant by "recursive" in this case.

# C-7.28
"""Describe a fast recursive algorithm for reversing a singly linked list."""

# Assuming no tail...

def reverse_singly_linked_list(L: SinglyLinkedList, *, start_node=None):
    """
    >>> sll = SinglyLinkedList()
    >>> sll.add_first(8)
    >>> sll.add_last(10)
    >>> sll.add_last(3)
    >>> sll.add_last(5)
    >>> [element.element() for element in sll]
    [8, 10, 3, 5]
    >>> reverse_singly_linked_list(sll)
    >>> [element.element() for element in sll]
    [5, 3, 10, 8]
    """
    first_node = False
    if start_node is None:
        start_node = L._head
        first_node = True
    next_node = start_node._next

    L.add_first(start_node.element())
    if first_node:
        L._tail = L._head
        L._tail._next = None

    if next_node is not None:
        reverse_singly_linked_list(L, start_node=next_node)





# C-7.29
"""Describe in detail an algorithm for reversing a singly linked list L using only a constant amount of additional space
and not using any recursion."""

def reverse_singly_linked_list2(L):
    """
    >>> sll = SinglyLinkedList()
    >>> sll.add_last(3)
    >>> sll.add_last(5)
    >>> sll.add_last(7)
    >>> [element.element() for element in sll]
    [3, 5, 7]
    >>> reverse_singly_linked_list2(sll)
    >>> [element.element() for element in sll]
    [7, 5, 3]
    """
    if len(L) <= 1:
        return
    start_node = L._head
    cursor = start_node
    prev_node = None
    while cursor is not None:
       next_node = cursor._next
       cursor._next = prev_node
       prev_node = cursor
       cursor = next_node
    L._tail = start_node
    L._head = prev_node

#C-7.30
"""Exercise P-6.35 describes a LeakyStack abstraction. Implement that ADT using a singly linked list for storage.

A stack with a maximum capacity limit, where the bottom element is popped when if the stack is overcapacity."""

class LeakyStack:
    """
    >>> leaky_deaky = LeakyStack(maxlen=3)
    >>> len(leaky_deaky)
    0
    >>> leaky_deaky.push(5)
    >>> len(leaky_deaky)
    1
    >>> leaky_deaky.push(7)
    >>> len(leaky_deaky)
    2
    >>> leaky_deaky.push(9)
    >>> len(leaky_deaky)
    3
    >>> leaky_deaky.push(10)
    >>> len(leaky_deaky)
    3
    >>> leaky_deaky.top()
    10
    >>> leaky_deaky.pop()
    10
    >>> len(leaky_deaky)
    2
    >>> leaky_deaky.push(8)
    >>> leaky_deaky.top()
    8
    >>> len(leaky_deaky)
    3
    >>> leaky_deaky.pop()
    8
    >>> len(leaky_deaky)
    2
    >>> leaky_deaky.pop()
    9
    >>> len(leaky_deaky)
    1
    >>> leaky_deaky.pop()
    7
    """
    def __init__(self, maxlen=10):
        self._stack = SinglyLinkedList()
        self._maxlen = maxlen

    def __len__(self):
        return len(self._stack)

    def top(self):
        return self._stack.first().element()

    def is_empty(self):
        return len(self) == 0

    def is_full(self):
        return len(self) >= self._maxlen

    def push(self, e):
        if self.is_full():
            new_list = SinglyLinkedList()
            for node in self._stack:
                if node is not self._stack.last():
                    new_list.add_last(node.element())
            self._stack = new_list
        self._stack.add_first(e)

    def pop(self):
        return self._stack.remove_first()

# C-7.31
"""Design a forward list ADT that abstracts the operations on a singly linked list, much as the positional list ADT 
abstracts a doubly linked list, with a notion of a designated "cursor" position in the list."""

# The SinglyLinkedList class fulfills this.

# C-7.32
"""Design a circular positional list ADT that abstracts a circularly linked list in the same way a positional list ADT
abstracts a doubly linked list, with a notion of a designated "cursor" position with the list."""


class CircularlyLinkedList(SinglyLinkedList):
    """
    >>> circle = CircularlyLinkedList()
    >>> circle.add_first(7)
    >>> circle.add_last(10)
    >>> circle.last().element()
    10
    >>> circle.last().next_node() is circle.first()
    True
    >>> for node in circle:
    ...   print(node.element())
    7
    10
    """
    def __init__(self):
        super().__init__()

    def __len__(self):
        return self._size

    def __iter__(self):
        cursor = self._head
        first_pass = True
        while cursor is not self._head or first_pass:
            first_pass = False
            yield cursor
            cursor = cursor._next

    def add_first(self, e):
        new_node = self._Node(e, next=self._head)
        self._head = new_node
        self._size += 1
        if self._tail is None:
            self._tail = self._head
        self._tail._next = self._head

    def add_last(self, e):
        if self.is_empty():
            self.add_first(e)
        else:
            new_node = self._Node(e, next=self._head)
            self._tail._next = new_node
            self._tail = new_node
            self._size += 1

    def remove_first(self):
        if self.is_empty():
            raise Empty('List is empty')
        value = self._head.element()
        if len(self) > 1:
            self._head = self._head._next
            self._tail._next = self._head
        else:
            self._head = None
            self._tail = None
        self._size -= 1
        return value

# C.7-33

"""Modify the _DoublyLinkedBase class to include a reverse method that reverses the order of the list, yet without 
creating or destroying any nodes."""

class _DoublyLinkedBase:
  """
  A base class providing a doubly linked list representation.
  """

  #-------------------------- nested _Node class --------------------------
  # nested _Node class
  class _Node:
    """Lightweight, nonpublic class for storing a doubly linked node."""
    __slots__ = '_element', '_prev', '_next'            # streamline memory

    def __init__(self, element, prev, next):            # initialize node's fields
      self._element = element                           # user's element
      self._prev = prev                                 # previous node reference
      self._next = next                                 # next node reference

  #-------------------------- list constructor --------------------------

  def __init__(self):
    """Create an empty list."""
    self._header = self._Node(None, None, None)
    self._trailer = self._Node(None, None, None)
    self._header._next = self._trailer                  # trailer is after header
    self._trailer._prev = self._header                  # header is before trailer
    self._size = 0                                      # number of elements

  #-------------------------- public accessors --------------------------

  def __len__(self):
    """Return the number of elements in the list."""
    return self._size

  def is_empty(self):
    """Return True if list is empty."""
    return self._size == 0

  #-------------------------- nonpublic utilities --------------------------

  def _insert_between(self, e, predecessor, successor):
    """Add element e between two existing nodes and return new node."""
    newest = self._Node(e, predecessor, successor)      # linked to neighbors
    predecessor._next = newest
    successor._prev = newest
    self._size += 1
    return newest

  def _delete_node(self, node):
    """Delete nonsentinel node from the list and return its element."""
    predecessor = node._prev
    successor = node._next
    predecessor._next = successor
    successor._prev = predecessor
    self._size -= 1
    element = node._element                             # record deleted element
    node._prev = node._next = node._element = None      # deprecate node
    return element                                      # return deleted element

  def reverse(self):
      if self._size <= 1:
          return
      start = self._header._next
      self._header._next = self._trailer._prev
      self._trailer._prev = start
      cursor = start
      while cursor._element is not None:
          next = cursor._next
          prev = cursor._prev
          cursor._next = prev if prev is not None else self._trailer
          cursor._prev = next if next is not None else self._header
          cursor = next


class PositionalList(_DoublyLinkedBase, collections.Iterator):
    """A sequential container of elements allowing positional access.

    >>> pl = PositionalList()
    >>> _ = pl.add_last(10) # doctest:+ELLIPSIS
    >>> _ = pl.add_last(8)
    >>> _ = pl.add_last(17)
    >>> for node in pl:
    ...   print(node)
    10
    8
    17
    >>> pl.reverse()
    >>> for node in pl:
    ...   print(node)
    17
    8
    10
    >>> _ = pl.add_last(5)
    >>> for node in pl:
    ...   print(node)
    17
    8
    10
    5
    >>> pl.swap(pl.first(), pl.last())
    >>> pl.first().element()
    5
    >>> second = pl.after(pl.first())
    >>> second.element()
    8
    >>> before_second = pl.before(second)
    >>> before_second.element()
    5
    >>> third = pl.after(second)
    >>> third.element()
    10
    >>> fourth = pl.after(third)
    >>> fourth.element()
    17
    >>> next(pl)
    5
    >>> next(pl)
    8
    >>> next(pl)
    10
    >>> next(pl)
    17
    >>> next(pl) # last
    Traceback (most recent call last):
    StopIteration
    """

    # -------------------------- nested Position class --------------------------
    class Position:
        """An abstraction representing the location of a single element.

        Note that two position instaces may represent the same inherent
        location in the list.  Therefore, users should always rely on
        syntax 'p == q' rather than 'p is q' when testing equivalence of
        positions.
        """

        def __init__(self, container, node):
            """Constructor should not be invoked by user."""
            self._container = container
            self._node = node

        def element(self):
            """Return the element stored at this Position."""
            return self._node._element

        def __eq__(self, other):
            """Return True if other is a Position representing the same location."""
            return type(other) is type(self) and other._node is self._node

        def __ne__(self, other):
            """Return True if other does not represent the same location."""
            return not (self == other)  # opposite of __eq__

    # ------------------------------- iterators -------------------------------------

    def __init__(self):
        super().__init__()
        self.cursor = None

    def __next__(self):
        if self.cursor is None and not self.is_empty():
            self.cursor = self.first()
        elif self.cursor.element() is not None:
            self.cursor = self.after(self.cursor)

        if self.cursor is None:
            raise StopIteration
        return self.cursor.element()

    # ------------------------------- utility methods -------------------------------
    def _validate(self, p):
        """Return position's node, or raise appropriate error if invalid."""
        if not isinstance(p, self.Position):
            raise TypeError('p must be proper Position type')
        if p._container is not self:
            raise ValueError('p does not belong to this container')
        if p._node._next is None:  # convention for deprecated nodes
            raise ValueError('p is no longer valid')
        return p._node

    def _make_position(self, node):
        """Return Position instance for given node (or None if sentinel)."""
        if node is self._header or node is self._trailer:
            return None  # boundary violation
        else:
            return self.Position(self, node)  # legitimate position

    # ------------------------------- accessors -------------------------------
    def first(self):
        """Return the first Position in the list (or None if list is empty)."""
        return self._make_position(self._header._next)

    def last(self):
        """Return the last Position in the list (or None if list is empty)."""
        return self._make_position(self._trailer._prev)

    def before(self, p):
        """Return the Position just before Position p (or None if p is first)."""
        node = self._validate(p)
        return self._make_position(node._prev)

    def after(self, p):
        """Return the Position just after Position p (or None if p is last)."""
        node = self._validate(p)
        return self._make_position(node._next)

    def __iter__(self):
        """Generate a forward iteration of the elements of the list."""
        cursor = self.first()
        while cursor is not None:
            yield cursor.element()
            cursor = self.after(cursor)

    # ------------------------------- mutators -------------------------------
    # override inherited version to return Position, rather than Node
    def _insert_between(self, e, predecessor, successor):
        """Add element between existing nodes and return new Position."""
        node = super()._insert_between(e, predecessor, successor)
        return self._make_position(node)

    def add_first(self, e):
        """Insert element e at the front of the list and return new Position."""
        return self._insert_between(e, self._header, self._header._next)

    def add_last(self, e):
        """Insert element e at the back of the list and return new Position."""
        return self._insert_between(e, self._trailer._prev, self._trailer)

    def add_before(self, p, e):
        """Insert element e into list before Position p and return new Position."""
        original = self._validate(p)
        return self._insert_between(e, original._prev, original)

    def add_after(self, p, e):
        """Insert element e into list after Position p and return new Position."""
        original = self._validate(p)
        return self._insert_between(e, original, original._next)

    def delete(self, p):
        """Remove and return the element at Position p."""
        original = self._validate(p)
        return self._delete_node(original)  # inherited method returns element

    def replace(self, p, e):
        """Replace the element at Position p with e.

        Return the element formerly at Position p.
        """
        original = self._validate(p)
        old_value = original._element  # temporarily store old element
        original._element = e  # replace with new element
        return old_value  # return the old element value

    def swap(self, p, q):
        # 17, 8, 10, 5
        #import pdb; pdb.set_trace()
        neighbouring_nodes = {
            'p': {
                'predecessor': None,
                'successor': None,
            },
            'q': {
                'predecessor': None,
                'successor': None
            }
        }

        for swap_nodes in (p, q):
            neighbouring_node = neighbouring_nodes['p'] if swap_nodes == p else neighbouring_nodes['q']
            try:
                neighbouring_node['predecessor'] = self.before(swap_nodes)._node
            except AttributeError:
                neighbouring_node['predecessor'] = self._header

            try:
                neighbouring_node['successor'] = self.after(swap_nodes)._node
            except AttributeError:
                neighbouring_node['successor'] = self._trailer


        # if p._node._next != q and p._node._prev != q and q._node._prev != p and q._node._next != p:
        #     # Make sure nodes are not neighbours
        #     p_predecessor = self.before(p)._node
        #     p_successor = self.after(p)._node
        #     q_predecessor = self.before(q)._node
        #     q_successor = self.after(q)._node
        # else:
        #     # Swapping neighbouring nodes
        #     p_predecessor = self.before(p)._node if self.before(p) != q else p._node
        #     p_successor = self.after(p)._node if self.after(p) != q else p._node
        #     q_predecessor = self.before(q)._node if self.before(q) != p else q._node
        #     q_successor = self.after(q)._node if self.after(q) != p else q._node
        #
        # if p_predecessor is None:
        #     p_predecessor = self._header
        # if q_predecessor is None:
        #     q_predecessor = self._header
        # if p_successor is None:
        #     p_successor = self._trailer
        # if q_successor is None:
        #     q_successor = self._trailer

        p_node = self._validate(p)  # 17
        q_node = self._validate(q)  # 5

        neighbouring_nodes['p']['predecessor']._next = q_node
        neighbouring_nodes['p']['successor']._prev = q_node
        neighbouring_nodes['q']['predecessor']._next = p_node
        neighbouring_nodes['q']['successor']._prev = p_node

        p_node._prev = neighbouring_nodes['q']['predecessor']
        p_node._next = neighbouring_nodes['q']['successor']
        q_node._prev = neighbouring_nodes['p']['predecessor']
        q_node._next = neighbouring_nodes['p']['successor']

        # p_predecessor._next = q_node
        # p_successor._prev = q_node
        # q_predecessor._next = p_node
        # q_successor._prev = p_node
        #
        # p_node._prev = q_predecessor
        # p_node._next = q_successor
        # q_node._prev = p_predecessor
        # q_node._next = p_successor


# C-7.34
"""Modify the PositionalList class to support a method swap(p, q) that causes the underlying nodes referenced by 
positions p and q to be exchanged for each other. Relink the existing nodes; do not create any new nodes."""

# Implemented above!


# C-7.35
"""To implement the iter method of the PositionalList class, we relied on the convenience of Python's generator syntax
and the yield statement. Give an alternative implementation of iter by designing a nested iterator class."""

# Implemented above!

# C-7.36
"""Give a complete implementation of the positional list ADT using a doubly linked list that does not include any 
sentinel nodes"""

# TODO: Maybe later, maybe not

# C-7.37
"""Implement a function that accepts a PositionalList L of n integers sorted in nondecreasing order, and another value
V, and determines in O(n) time if there are two elements of L that sum precisely to V. The function should return a 
pair of positions of such elements, if found, or None otherwise."""

# -2 0 1 3 4 4 6 7 8 10 11 14
# 19
# -2 + 0 = -2
# -2 + 1 = -1
# -2 + 3 = 1
# -2 + 4 = 2
# -2 + 4 = 2
# -2 + 6 = 4
# -2 + 7 = 5
# -2 + 8 = 6
# -2 + 10 = 8
# -2 + 11 = 9
# -2 + 14 = 12
# 0 + 14 = 14
# 0 + 14 = 14
# 1 + 14 = 15
# 3 + 14 = 17
# 4 + 14 = 18
# 6 + 14 = 20
# 6 + 11 = 17
# 7 + 11 = 18
# 7 + 14 = 21
# 8 + 14 = 22
# 8 + 11 = 19

# -2 + 14 = 12
# 0 + 14 = 14
# 1 + 14 = 15
# 3 + 14 = 17
# 4 + 14 = 18
# 4 + 14 = 18
# 6 + 14 = 20
# 6 + 11 = 17
# 7 + 11 = 18
# 7 + 14 = 21
# 8 + 14 = 22
# 8 + 11 = 19

# Find 7
# -2 + 14 = 12
# -2 + 11 = 9
# -2 + 10 = 8
# -2 + 8 = 6
# 0 + 8 = 8
# 0 + 7 = 7


# Find 23
# -2 + 14 = 12
# 0 + 14 = 14
# 1 + 14 = 15
# 3 + 14 = 17
# 4 + 14 = 18
# 4 + 14 = 18
# 6 + 14 = 20
# 7 + 14 = 21
# 8 + 14 = 22
# 10 + 14 = 24
# 10 + 11 = 21
# 11 + 11 = 22
# 11 + 14 = 25
# 11 + 11 = 22
# 14 + 11 - None


def find_sum(L, V):
    """
    >>> L = PositionalList()
    >>> start = [-2, 0, 1, 3, 4, 4, 6, 7, 8, 10, 11, 14]
    >>> for element in start:
    ...   _ = L.add_last(element)
    >>> positions = find_sum(L, 19)
    >>> positions[0].element() == 8
    True
    >>> positions[1].element() == 11
    True
    >>> positions2 = find_sum(L, 7)
    >>> positions2[0].element()
    0
    >>> positions2[1].element()
    7
    >>> positions3 = find_sum(L, 23)
    >>> positions3 is None
    True
    """
    """
    :param L: Positional list ordered in non-decreasing order
    :param V: Sum you want to find
    :return: A tuple of two positions that sum up to V.
    """
    first_number = L.first()
    second_number = L.last()
    while first_number.element() + second_number.element() != V or first_number is second_number:
        summation = lambda: first_number.element() + second_number.element()

        if first_number == L.last():
            return None
        if first_number == second_number:
            second_number = L.after(second_number)

        if summation() < V:
            while summation() < V:
                if second_number != L.last():
                    second_number = L.after(second_number)
                else:
                    first_number = L.after(first_number)
                #summation = first_number.element() + second_number.element()
        elif summation() > V:
            while True:
                second_number = L.before(second_number)
                #summation = first_number.element() + second_number.element()
                if summation() < V:
                    first_number = L.after(first_number)
                    break
                elif summation() == V:
                    break
    return (first_number, second_number)


# C-7.38
"""There is a simple, but inefficient algorithm, called bubble-sort, for sorting a list L of n comparable elements.
This algorithms scans the list n - 1 times, where, in each scan, the algorithm compares the current element with the
next one and swaps them if they are out of order. Implement a bubble_sort function that takes a positional list L as a
parameter. What is the running time of this parameter, assuming the positional list implemented with a doubly linked 
list?"""


# 5 2 8 9 3 8 4 7 3
# 2 5 8 9 3 8 4 7 3
# 2 5 8 3 8 4 7 3 9
# 2 5 3 8 8 4 7 3 9
# 2 5 3 8 4 7 3 8 9
# 2 3 5 8 4 7 3 8 9
# 2 3 5 4 7 3 8 8 9
# 2 3 4 5 7 3 8 8 9
# 2 3 4 5 3 7 8 8 9
# 2 3 4 3 5 7 8 8 9
# 2 3 3 4 5 7 8 8 9

#
# def bubble_sort(L: PositionalList):
#     """
#     >>> numbers = [5, 2, 8, 9, 3, 8, 4, 7, 3]
#     >>> L = PositionalList()
#     >>> for n in numbers:
#     ...   _ = L.add_last(n)
#     >>> bubble_sort(L)
#     >>> for n in L:
#     ...   print(n)
#     2
#     3
#     3
#     4
#     5
#     7
#     8
#     8
#     9
#     """
#     if L.is_empty():
#         return
#     run_around = True
#     while run_around:
#         marker = L.first()
#         run_around = False
#         while marker != L.last():
#             pivot = L.after(marker)
#             if marker.element() > pivot.element():
#                 L.swap(marker, pivot)
#                 run_around = True
#             else:
#                 marker = pivot
