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

def count_nodes(L):
    count = 1
    node = L.head
    while L.next != L.head:
        count += 1
        L = L.next
    return count
