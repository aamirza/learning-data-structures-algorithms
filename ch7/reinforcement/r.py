# R-7.1
"""Give na algorithm for finding the second-to-last node in a single linked list in which the last node is indicated
by a next reference of None."""

class Empty(Exception):
    pass


class LinkedStack:
  """LIFO Stack implementation using a singly linked list for storage."""

  #-------------------------- nested _Node class --------------------------
  class _Node:
    """Lightweight, nonpublic class for storing a singly linked node."""
    __slots__ = '_element', '_next'         # streamline memory usage

    def __init__(self, element, next):      # initialize node's fields
      self._element = element               # reference to user's element
      self._next = next                     # reference to next node

  #------------------------------- stack methods -------------------------------
  def __init__(self):
    """Create an empty stack."""
    self._head = None                       # reference to the head node
    self._size = 0                          # number of stack elements

  def __len__(self):
    """Return the number of elements in the stack."""
    return self._size

  def is_empty(self):
    """Return True if the stack is empty."""
    return self._size == 0

  def push(self, e):
    """Add element e to the top of the stack."""
    self._head = self._Node(e, self._head)  # create and link a new node
    self._size += 1

  def top(self):
    """Return (but do not remove) the element at the top of the stack.

    Raise Empty exception if the stack is empty.
    """
    if self.is_empty():
      raise Empty('Stack is empty')
    return self._head._element              # top of stack is at head of list

  def pop(self):
    """Remove and return the element from the top of the stack (i.e., LIFO).

    Raise Empty exception if the stack is empty.
    """
    if self.is_empty():
      raise Empty('Stack is empty')
    answer = self._head._element
    self._head = self._head._next           # bypass the former top node
    self._size -= 1
    return answer


def get_nth_last(L, n=0):
    position = L.head
    stack = LinkedStack()
    while position.next is not None:
        stack.push(position)
        position = position.next
    while n != 0:
        value = stack.pop()
        n -= 1
    return n


# R-7.2
"""Describe a good algorithm for concatenating two singly linked lists L and M, given only references to the first node
of each list, into a single list L' that contains all the nodes of L followed by all the nodes of M."""

class LinkedList:
    class _Node:
        """Lightweight, nonpublic class for storing a singly linked node."""
        __slots__ = '_element', '_next'  # streamline memory usage

        def __init__(self, element, next):  # initialize node's fields
            self._element = element  # reference to user's element
            self._next = next

    def __init__(self):
        self._head = None
        self._tail = None
        self.size = 0

    def __len__(self):
        return self.size

    def is_empty(self):
        return len(self) == 0

    def append(self, e):
        node = self._Node(e, None)
        if self.is_empty():
            self._head = node
        self._tail._next = node
        self._tail = node
        self.size += 1






def join_lists(L, M):
    """Create a new list, add all of L to it, and then a reference to the head of M. This will concatenate the two lists

    WARNING: Will give an inaccurate size and _tail.
    """
    new_list = LinkedList()
    new_list.append(L)
    while L is not None:
        new_list.append(L.next)
        L = L.next
    new_list.append(M)
    return new_list


# R-7.3
"""Describe a recursive algorithm that counts number of nodes in a singly linked list."""

def count_nodes(L):
    if isinstance(L, LinkedList):
        L = L._head
    if L.next is not None:
        return 1 + count_nodes(L.next)

# R-7.4
"""Describe in detail how to swap two nodes x and y (and not just their contents) in a singly linked list L given
references only to x and y. Repeat this exercise for the case when L is a doubly linked list. Which algorithm
takes more time?"""

# If you wish to swap the nodes in their entirety, then you have to iterate through the node until the "next" property
# of a node is x or y (whichever comes first). Let's say the next for node N is x. You need to change N.next to point to
# y. You also need to set y.next to x.next, and x.next to y.next. Continue from x.next until N.next = y. You need to
# change that to equal x.

# For a doubly linked list, you don't need to iterate through the entire list. Just change x.prev.next to equal y,
# and x.next.prev = y. Do the same for y except make it equal x. Then you need to swap the contents of x and y including
# their next/prev elements.

# R-7.5
"""Implement a function that counts the number of nodes in a circularly linked list."""

def circular_list_node_count(L):
    count = 1
    node = L.head
    while node.next != L.head:
        count += 1
        node = L.next
    return count


# R-7.6
"""Suppose that x and y are references to nodes of circularly linked lists, although not necessarily the same list.
Describe a fast algorithm for telling if x and y belong to the same list."""

# You can either check if the head of the linked lists are the same. If the head isn't specified, then you would have
# to cycle through the list using the 'next' property until you find y (if starting with x). If you return to x without
# finding y, then the two nodes do not belong to the same list.


# R-7.7
"""Our CircularQueue class of Section 7.2.2 provides a rotate() method that has semantics equivalent to 
Q.enqueue(Q.dequeue()), for a nonempty queue. Implement such a method for the LinkedQueue class of Section 7.1.2 without
the creation of any new nodes."""

class LinkedQueue:
  """FIFO queue implementation using a singly linked list for storage."""

  #-------------------------- nested _Node class --------------------------
  class _Node:
    """Lightweight, nonpublic class for storing a singly linked node."""
    __slots__ = '_element', '_next'         # streamline memory usage

    def __init__(self, element, next):
      self._element = element
      self._next = next

  #------------------------------- queue methods -------------------------------
  def __init__(self):
    """Create an empty queue."""
    self._head = None
    self._tail = None
    self._size = 0                          # number of queue elements

  def __len__(self):
    """Return the number of elements in the queue."""
    return self._size

  def is_empty(self):
    """Return True if the queue is empty."""
    return self._size == 0

  def first(self):
    """Return (but do not remove) the element at the front of the queue.

    Raise Empty exception if the queue is empty.
    """
    if self.is_empty():
      raise Empty('Queue is empty')
    return self._head._element              # front aligned with head of list

  def dequeue(self):
    """Remove and return the first element of the queue (i.e., FIFO).

    Raise Empty exception if the queue is empty.
    """
    if self.is_empty():
      raise Empty('Queue is empty')
    answer = self._head._element
    self._head = self._head._next
    self._size -= 1
    if self.is_empty():                     # special case as queue is empty
      self._tail = None                     # removed head had been the tail
    return answer

  def enqueue(self, e):
    """Add an element to the back of queue."""
    newest = self._Node(e, None)            # node will be new tail node
    if self.is_empty():
      self._head = newest                   # special case: previously empty
    else:
      self._tail._next = newest
    self._tail = newest                     # update reference to tail node

  def rotate(self):
      self._tail = self._head
      self._head = self._head._next


# R-7.8
"""Describe a nonrecursive method for finding, by link hopping, the middle node of a doubly linked list with header and
trailer sentinels. In the case of even number of nodes, report the node slightly left of centre as the "middle". (Note:
this method must only use link hopping; it cannot use a counter.) What is the running time of this method?"""

# Since this is a doubly linked list, you can have two starting points, one starting at the header and the other at the
# trailer. From the trailer, you would hop to the previous node, and from the header you would hop to the next node.
# You would do this until you reach the same node; this would be the node in the middle, or left of centre in an even
# sized list. This method would take O(n) or O(1/2 n) time.

# R-7.9
"""Give a fast algorithm for concatenating two doubly linked lists L and M, with header and trailer sentinel nodes, into
a single list L'"""

def combine_doubly_linked_lists(L, M):
    new_L = L
    new_L.trailer = M.head
    new_L.trailer = M.trailer
    return new_L

# R-7.10
"""There seems to be some redundancy in the repertoire of the positional list ADT, as the operation L.add_first(e) could
be enacted by the alternative L.add_before(L.first(), e). Likewise, L.add_last(e) might be performed as 
L.add_after(L.last(), e). Explain why the methods add_first and add_last are necessary."""


class _DoublyLinkedBase:
  """A base class providing a doubly linked list representation."""

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


class PositionalList(_DoublyLinkedBase):
    """A sequential container of elements allowing positional access."""

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

        def __ge__(self, other):
            if type(other.element()) is type(self.element()):
                return self.element() >= other.element()
            else:
                raise TypeError

        def __gt__(self, other):
            if type(other.element()) is type(self.element()):
                return self.element() > other.element()
            else:
                raise TypeError

        def __lt__(self, other):
            if type(other.element()) is type(self.element()):
                return self.element() < other.element()
            else:
                raise TypeError

        def __le__(self, other):
            if type(other.element()) is type(self.element()):
                return self.element() <= other.element()
            else:
                raise TypeError

        def __eq__(self, other):
            """Return True if other is a Position representing the same location."""
            if type(other) is type(self):
                if type(other.element()) is type(self.element()):
                    return other.element() == self.element()
            return False

        def __ne__(self, other):
            """Return True if other does not represent the same location."""
            return not (self == other)  # opposite of __eq__

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

    def __reversed__(self):
        cursor = self.last()
        while cursor is not None:
            yield cursor.element()
            cursor = self.before(cursor)

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

    def max(self):
        return max(self)

    def find(self, e):
        cursor = self.first()
        while cursor is not None:
            if cursor.element() == e:
                return cursor
            cursor = self.after(cursor)
        return None

    def recursive_find(self, e, *, position=None):
        if position is None:
            position = self.first()
        elif self.after(position) is None:
            return None

        if position.element() == e:
            return position
        return self.recursive_find(e, position=self.after(position))



# add_first and add_last are necessary in the case of the list being empty. If L.add_before(L.first(), e) is performed
# when the list is empty, there is no L.first(), and this would return None, which wouldn't work.


# R-7.11
"""Implement a function, with calling syntax max(L) that returns the maximum element from a PositionalList instance L
containing comparable elements."""


# Implemented above with ge, gt, le, lt.

def test_max_list(*numbers):
    """
    >>> test_max_list(10, 1, 4, 5, 18, 23, 59, 39, 2, 8, 18)
    59
    """
    L = PositionalList()
    for number in numbers:
        L.add_first(number)
    return max(L)

# R-7.12
"""Redo the previous problem with max as a method of the PositionalList class, so that calling syntax L.max() is 
supported"""

def test_max_list_method(*numbers):
    """
    >>> test_max_list_method(10, 1, 4, 5, 18, 23, 59, 39, 2, 8, 18)
    59
    """
    L = PositionalList()
    for number in numbers:
        L.add_first(number)
    return L.max()

# R-7.13
"""Update the PositionalList class to support an additional method find(e) which returns the position of the (first 
occurrence of) element e in the list (or None if not found)"""

def test_find(to_find, *numbers):
    """
    >>> test_find(5, 2, 4, 6, 4, 4, 9) is None
    True
    >>> test_find(5, 7, 3, 5, 10, 3, 3).element() == 5
    True
    """
    L = PositionalList()
    for number in numbers:
        L.add_first(number)
    return L.find(to_find)

# R-7.14
"""Repeat the previous process using recursion. Your method should not contain any loops. How much space does your 
method use in addition to the space used for L?"""

def test_recursive_find(to_find, *numbers):
    """
    >>> test_recursive_find(5, 2, 4, 6, 4, 4, 9) is None
    True
    >>> test_recursive_find(5, 7, 3, 5, 10, 3, 3).element() == 5
    True
    """
    L = PositionalList()
    for number in numbers:
        L.add_first(number)
    return L.recursive_find(to_find)

# No additional space is used.

# R-7.15
"""Provide support for a __reversed__ method of the PositionalList class that is similar to the given __iter__, but that
iterates the elements in reversed order."""

def test_reverse(*numbers):
    """
    >>> test_reverse(10, 6, 2, 4, 5, 52)
    [52, 5, 4, 2, 6, 10]
    """
    L = PositionalList()
    for number in numbers:
        L.add_first(number)
    return [reverse_number for reverse_number in L]


# R-7.16
"""Describe an implementation of the PositionalList methods add_last and add_before realized by using only methods in 
the set {is_empty, first, last, prev, next, add_after and add_first}."""


class PositionalList2(_DoublyLinkedBase):
    """A sequential container of elements allowing positional access."""

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

        def __ge__(self, other):
            if type(other.element()) is type(self.element()):
                return self.element() >= other.element()
            else:
                raise TypeError

        def __gt__(self, other):
            if type(other.element()) is type(self.element()):
                return self.element() > other.element()
            else:
                raise TypeError

        def __lt__(self, other):
            if type(other.element()) is type(self.element()):
                return self.element() < other.element()
            else:
                raise TypeError

        def __le__(self, other):
            if type(other.element()) is type(self.element()):
                return self.element() <= other.element()
            else:
                raise TypeError

        def __eq__(self, other):
            """Return True if other is a Position representing the same location."""
            if type(other) is type(self):
                if type(other.element()) is type(self.element()):
                    return other.element() == self.element()
            return False

        def __ne__(self, other):
            """Return True if other does not represent the same location."""
            return not (self == other)  # opposite of __eq__

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

    def __reversed__(self):
        cursor = self.last()
        while cursor is not None:
            yield cursor.element()
            cursor = self.before(cursor)

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
        # return self._insert_between(e, self._trailer._prev, self._trailer)
        if self.is_empty():
            self.add_first(e)
        else:
            self.add_after(self.last(), e)

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
