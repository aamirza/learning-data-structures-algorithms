# R-8.1
"""
The following questions refers to the tree of Figure 8.3.

a. Which node is the root?
b. What are the internal nodes?
c. How many descendants does node cs016/ have?
d. How many ancestors does node cs016/ have?
e. What are the siblings of node homeworks/?
f. Which nodes are in the subtree rooted at node projects/?
g. What is the depth of node papers/?
h. What is the height of the tree?
"""

# a) /user/rt/courses/
# b) All nodes with children, or all the directories... cs016/, cs252/, homeworks/, programs/, projects/, papers/, demos/
# c) cs016/ has 9 descendants.
# d) cs016/ has 1 ancestor, namely the root /user/rt/courses
# e) homeworks/ has two siblings, grades and programs/
# f) The subtree rooted at projects/ has 6 nodes, including projects/, papers/, demos/, buylow, sellhigh, market
# g) The depth of papers/ is 3.
# h) The height of the tree is 4.


# R-8.2
from ch8.binary_tree import BinaryTree
from ch8.euler_tour import BinaryEulerTour
from ch8.linked_binary_tree import LinkedBinaryTree

"""
Show a tree achieving the worst-case running time for algorithm depth.
"""

def depth(p):
    if T.is_root(p):
        return 0
    return depth(T.parent(p))

# The worst case running time for this algorithm would simply be if a tree T has one branch that continuously
# went downward

# Root
# Great great ... grandparent
# Great great ... grandparent
# ...
# Grandparent
# Parent
# Node

# With no other branches. In this case, the run time would be n - 1, or O(n), where n is the number of nodes.


# R-8.3
"""
Give a justification for Proposition 8.4.

Proposition 8.4: The height of a nonempty tree T is equal to the maximum of the depths of its leaf positions.
"""

# The depth of a position p has the following definition:
    # If p is the root, the depth is 0
    # Otherwise, the depth is 1 plus the depth of the parent.

# The height of a position p has the following definition
    # If p is a leaf, the height is 0.
    # Otherwise, the height is equal to 1 plus the maximum height of p's children.

# Proof by induction
# Base case: The root is the only node of T. In this case, the depth is 0, and the since the root is a leaf, the
# maximum height is also zero.
# Induction step: Say the depth of a leaf node in T is equal to N. Say this is also the maximum depth.
# Its height would thus equal 0. The height of its parent would equal 1, the height of the parent of that would be 2...
# Until you reach the root, whose height would be N.

# Thus, the root's height was equal to the maximum of the depth of its leaf position. This completes the induction step.


#R-8.4
"""
What is the running time of a call to T.height2(p) when called on a position p distinct from the root of T?
"""

# The running time of the algorithm is O(n + number of children + 1). A height other than the root would have fewer
# children, so it would run a constant factor quicker, or O(n') where n' is the number of nodes at the subtree rooted at
# p

# R-8.5
"""
Describe an algorithm, relying only on the BinaryTree operations, that counts the number of leaves in a binary tree
that are the left child of their respective parent.
"""

# An inorder traversal works best

def count_left_children(T):
    count = 0
    for p in T.positions():
        if T.is_leaf(p) and p == T.left(T.parent(p)):
            count += 1
    return count


# R-8.6
"""
Let T be an n-node binary tree that may be improper. Describe how to represent T by means of a proper binary tree T' 
with O(n) nodes.
"""

# O(n) nodes means we can indeed add some nodes to fill the gap. Add empty nodes whenever a node has only child.
# The worst case-scenario is doubling the number of nodes minus 1 (no need to add a node to the leaves), or O(2n - 1)
# In other words, O(n).

# R-8.7
"""
What are the minimum and maximum number of internal and external nodes in an improper binary tree with n nodes?
"""

# For internal nodes: h <= ni < 2^h - 1
# The MINIMUM would be a binary tree consisting of just the root. In this case, the height is 0 and there are no internal nodes.
# The MAXIMUM would be at least 2^h - 1.

# For external nodes: 1 <= 2^h
# The MINIMUM would be 1, in the case of a tree consisting of just the root, or an improper tree with just one leaf.
# The MAXIMUM would be 2^h - 1, not 2^h, because at least one leaf will be missing in an improper binary tree.


# R-8.8
"""
Answer the following questions so as to justify Proposition 8.8.

a. What is the minimum number of external nodes for a proper binary tree with height h? Justify your answer.
b. What is the maximum number of external nodes for a proper binary tree with height h? Justify your answer.
c. Let T be a proper binary tree with heigh h and n nodes. Show that

log(n + 1) - 1 <= h <= (n - 1)/2

d. For which values of n and h can the above lower and upper bounds on h be attained with equality?
"""

"""
a: The minimum number of external nodes in a proper binary tree is h + 1, where h is the height.
 
Proof by induction.
 
  BASE CASE
 
     A proper binary tree consisting of just the root. In this case, the height is 0 and the number of external nodes is
     one. 
     
     n_e = h + 1 = 0 + 1 = 1
 
 INDUCTION STEP
 
    By definition of a proper binary tree, each node must have either 0 or 2 children. In the case of where there are 
    n_e external nodes at height h, adding another level of depth (h + 1) would mean you need, at minimum, two new nodes.
    
    If h = n_e,
    then h + 1 <= n_e + 2
    n_e' = n_e + 2
    h + 1 < n_e'
    
    
    This completes the induction step.
"""

"""
b: The maximum number of external nodes in a proper binary tree is 2^h, where h is the height.

Proof by induction.

    BASE CASE
    
        A proper binary tree consisting of just the root. In this case, the height is 0 and the number of external nodes
        is one.
    
        n_e <= 2^h = 2^0 = 1
        1 <= 1
    
        This proves the base case.
    
    INDUCTION STEP
        
        For a proper binary tree with height h, the number of external nodes should 2^h. For h + 1, it would be 2^(h+1).
        
        For a height of h + 1, it would be 2^h * 2, because each node would have two children each. 
        Or in other words, 2^(h+1). 
        
        This completes the induction step.
    
"""

"""
c. Let T be a proper binary tree with heigh h and n nodes. Show that log(n + 1) - 1 <= h <= (n - 1)/2

Knowing that 2h + 1 <= n <= 2^(h+1) - 1
We arrive at h <= (n - 1)/2 and log(n + 1) - 1 <= h
Hence log(n + 1) - 1 <= h <= (n - 1)/2
"""

"""
d. For which values of n and h can the above lower and upper bounds on h be attained with equality?

For h = 0, or the case of the root being the only node.
"""


# R.8-9
"""Give a proof by induction of Proposition 8.9

Proposition 8.9: In a nonempty proper binary tree T, with n_e external nodes and n_i internal nodes, we have n_e = ni + 1
"""

# Proof by induction
# Base case:
    # Just the root.
    # The number of external nodes is 1, number of internal nodes is 0.
    # n_e = n_i + 1

# Induction step:
    # Say n_e = n_i + 1 for a certain height h.
    # Increase h by 1. For an external node, you must attach two new external nodes to it. The external node with the
    # new nodes attached becomes an internal node. Essentially, the number of external nodes increased by 2, but the
    # number of external nodes falls by one as it gets converted into an internal node (+1)
    # +2 n_e, -1 n_e, +1 n_i
    # n_e + 2 - 1 = (n_i + 1) + 1
    # n_e + 1 = n_i + 2
    # n_e = n_i + 1
    # This completes the induction step.


# R-8.10
"""
Give a direct implementation of the num_children method within the class BinaryTree.
"""


class Tree:
    """Abstract base class representing a tree structure."""

    # ------------------------------- nested Position class -------------------------------
    class Position:
        """An abstraction representing the location of a single element within a tree.

        Note that two position instaces may represent the same inherent location in a tree.
        Therefore, users should always rely on syntax 'p == q' rather than 'p is q' when testing
        equivalence of positions.
        """

        def element(self):
            """Return the element stored at this Position."""
            raise NotImplementedError('must be implemented by subclass')

        def __eq__(self, other):
            """Return True if other Position represents the same location."""
            raise NotImplementedError('must be implemented by subclass')

        def __ne__(self, other):
            """Return True if other does not represent the same location."""
            return not (self == other)  # opposite of __eq__

    # ---------- abstract methods that concrete subclass must support ----------
    def root(self):
        """Return Position representing the tree's root (or None if empty)."""
        raise NotImplementedError('must be implemented by subclass')

    def parent(self, p):
        """Return Position representing p's parent (or None if p is root)."""
        raise NotImplementedError('must be implemented by subclass')

    def num_children(self, p):
        """Return the number of children that Position p has."""
        raise NotImplementedError('must be implemented by subclass')

    def children(self, p):
        """Generate an iteration of Positions representing p's children."""
        raise NotImplementedError('must be implemented by subclass')

    def __len__(self):
        """Return the total number of elements in the tree."""
        raise NotImplementedError('must be implemented by subclass')

    # ---------- concrete methods implemented in this class ----------
    def is_root(self, p):
        """Return True if Position p represents the root of the tree."""
        return self.root() == p

    def is_leaf(self, p):
        """Return True if Position p does not have any children."""
        return self.num_children(p) == 0

    def is_empty(self):
        """Return True if the tree is empty."""
        return len(self) == 0

    def depth(self, p):
        """Return the number of levels separating Position p from the root."""
        if self.is_root(p):
            return 0
        else:
            return 1 + self.depth(self.parent(p))

    def _height1(self):  # works, but O(n^2) worst-case time
        """Return the height of the tree."""
        return max(self.depth(p) for p in self.positions() if self.is_leaf(p))

    def _height2(self, p):  # time is linear in size of subtree
        """Return the height of the subtree rooted at Position p."""
        if self.is_leaf(p):
            return 0
        else:
            return 1 + max(self._height2(c) for c in self.children(p))

    def height(self, p=None):
        """Return the height of the subtree rooted at Position p.

        If p is None, return the height of the entire tree.
        """
        if p is None:
            p = self.root()
        return self._height2(p)  # start _height2 recursion

    def __iter__(self):
        """Generate an iteration of the tree's elements."""
        for p in self.positions():  # use same order as positions()
            yield p.element()  # but yield each element

    def positions(self):
        """Generate an iteration of the tree's positions."""
        return self.preorder()  # return entire preorder iteration

    def preorder(self):
        """Generate a preorder iteration of positions in the tree."""
        if not self.is_empty():
            for p in self._subtree_preorder(self.root()):  # start recursion
                yield p

    def _subtree_preorder(self, p):
        """Generate a preorder iteration of positions in subtree rooted at p."""
        yield p  # visit p before its subtrees
        for c in self.children(p):  # for each child c
            for other in self._subtree_preorder(c):  # do preorder of c's subtree
                yield other  # yielding each to our caller

    def postorder(self):
        """Generate a postorder iteration of positions in the tree."""
        if not self.is_empty():
            for p in self._subtree_postorder(self.root()):  # start recursion
                yield p

    def _subtree_postorder(self, p):
        """Generate a postorder iteration of positions in subtree rooted at p."""
        for c in self.children(p):  # for each child c
            for other in self._subtree_postorder(c):  # do postorder of c's subtree
                yield other  # yielding each to our caller
        yield p  # visit p after its subtrees

    def breadthfirst(self):
        """Generate a breadth-first iteration of the positions of the tree."""
        if not self.is_empty():
            fringe = LinkedQueue()  # known positions not yet yielded
            fringe.enqueue(self.root())  # starting with the root
            while not fringe.is_empty():
                p = fringe.dequeue()  # remove from front of the queue
                yield p  # report this position
                for c in self.children(p):
                    fringe.enqueue(c)  # add children to back of queue


class BinaryTree(Tree):
  """Abstract base class representing a binary tree structure."""

  # --------------------- additional abstract methods ---------------------
  def left(self, p):
    """Return a Position representing p's left child.

    Return None if p does not have a left child.
    """
    raise NotImplementedError('must be implemented by subclass')

  def right(self, p):
    """Return a Position representing p's right child.

    Return None if p does not have a right child.
    """
    raise NotImplementedError('must be implemented by subclass')

  # ---------- concrete methods implemented in this class ----------
  def sibling(self, p):
    """Return a Position representing p's sibling (or None if no sibling)."""
    parent = self.parent(p)
    if parent is None:                    # p must be the root
      return None                         # root has no sibling
    else:
      if p == self.left(parent):
        return self.right(parent)         # possibly None
      else:
        return self.left(parent)          # possibly None

  def children(self, p):
    """Generate an iteration of Positions representing p's children."""
    if self.left(p) is not None:
      yield self.left(p)
    if self.right(p) is not None:
      yield self.right(p)

  def inorder(self):
    """Generate an inorder iteration of positions in the tree."""
    if not self.is_empty():
      for p in self._subtree_inorder(self.root()):
        yield p

  def _subtree_inorder(self, p):
    """Generate an inorder iteration of positions in subtree rooted at p."""
    if self.left(p) is not None:          # if left child exists, traverse its subtree
      for other in self._subtree_inorder(self.left(p)):
        yield other
    yield p                               # visit p between its subtrees
    if self.right(p) is not None:         # if right child exists, traverse its subtree
      for other in self._subtree_inorder(self.right(p)):
        yield other

  # override inherited version to make inorder the default
  def positions(self):
    """Generate an iteration of the tree's positions."""
    return self.inorder()                 # make inorder the default

  def num_children(self, p):
      num_children = 0
      for child in self.children(p):
          num_children += 1
      return num_children

  # Implemented above!


# R-8.11
"""Find the value of arithmetic expression associated with each subtree of hte binary tree of Figure 8.8"""


# 3 + 1                     # = 4
# (3 + 1) * 3               # = 12
# 9 - 5                     # = 4
# (9 - 5) + 2               # = 6
# ((3 + 1) * 3) / ((9 -5) + 2)      # = 12 / 6 = 2
# 7 - 4                     # = 3
# 3 * (7 - 4)               # = 9
# ((3 * (7 - 4)) + 6        # = 15
# (((3 + 1) * 3) / ((9 -5) + 2)) - (((3 * (7 - 4)) + 6))        = 2 - 15 = -13


# R-8.12
"""Draw an arithmetic expression tree that has four external nodes, storing the numbers 1, 5, 6 and 7 (with each number
stored in a distinct external node, but not necessarily in this order), and has three internal nodes, each storing an
operator {+, -, x, /}, so that hte value of the root is 21. The operators may return and act on fractions, and an 
operator may be used more than once."""

# 6 / (1 = 5/7)

"""
    /
6       -
    1       /   
        5       7
"""


# R-8.13

"""Draw a binary tree representation of the following arithmeti expression: 

(((5 + 2) * (2 - 1)) / ((2 + 9) + ((7 -2) - 1)) * 8)"""

"""
                                                *
                            /                                       8
            *                                   +
    +               -                   +                   -
5       2       2       1           2       9           -       1
                                                    7       2
"""


# R-8.14
"""Justify Table 8.2, summarizing the running time of the methods of a tree represented with a linked structure, 
by providing, for each method, a description of its implementation, and an analysis of its running time."""


# len, is_empty is O(1)
    # Justification: Since this is stored as a property of the tree itself, it has an O(1) retrieval time.

# root, parent, is_root, is_leaf are O(1)
    # Justification: For root, you need only check if the element's parent property is set to None.
    # Justification: For parent, the parent is stored as a property of the position.
    # Justification: For is_leaf, the children are stored as a property of the position.

# children(p) is O(cp + 1) where c is the number of children.
    # Justification: With all the children of a node stored in a collection, iterating over that collection is O(n).

# depth(p): O(dp + 1) where d is the number of ancestors.
    # Justification: Justified in the book.

# height(p): O(n)
    # Justification: You need to iterate over all the elements in the tree to find the maximum depth. The height is
    # equal to the maximum depth.

# add_root, add_left, add_right, replace, delete, attach are O(1)
    # Justification: Since you are only working on one node, and at most 2-3 of its neighbours with a constant number
    # of actions, the run time is O(1)


# R-8.15
"""The LinkedBinaryTree class provides only nonpublic versions of the update methods discussed on page 319. Implement a
simple subclass named MutableLinkedBinaryTree that provides public wrapper functions for each of the inherited nonpublic
update methods."""

class MutableLinkedBinaryTree(LinkedBinaryTree):
    """
    >>> bt = MutableLinkedBinaryTree()
    >>> bt.add_root(5)
    >>> bt.root().element() == 5
    True
    """
    def add_root(self, e):
        return self._add_root(e)

    def add_left(self, p, e):
        return self._add_left(p, e)

    def add_right(self, p, e):
        return self._add_right(p, e)

    def replace(self, p, e):
        return self._replace(p, e)

    def delete(self, p):
        return self._delete(p)

    def attach(self, p, t1, t2):
        self._attach(p, t1, t2)


# R-8.16
"""
Let T be a binary tree with n nodes, and let f() be the level numbering funcion of the positions of T, as given in 
Section 8.3.2, of each position in a binary tree T.

a) Show that for every position p of T, f(p) <= 2^n - 2
b) Show an example of a binary tree with seven nodes that attains the above upper bound on f(p) for some position p.
"""

# a) Show that for every position p of T, f(p) <= 2^n - 2

"""
PROOF BY INDUCTION

BASE CASE 
    
    n = 1, or just the root. This has, according to Section 8.3.2, f(p) = 0.
    f(p) = 0 <= 2^n - 2 = 2^(1) - 2 = 0
    0 <= 0
    
    This proves the base case.
    
INDUCTION STEP

    There would be one extra node if a left child was added.
    The left child of f(p) has a level number of 2f(p) + 1. 
    
    2f(p) + 1 <= 2^(n+1) - 2
    2f(p) + 1 <= 2*(2^n) - 2
    2(2^n - 2) + 1 <= 2*(2^n) - 2  because f(p) <= 2^n - 2
    2*2^n - 4 + 1 <= 2*(2^n) - 2
    2*2^n - 3 <= 2*2^n - 2
    
    This completes the induction step for left children
    
    For right children, assuming no left child is added...
    The right child of f(p) has a level number of 2f(p) + 2
    
    2f(p) + 2 <= 2^(n+1) - 2
    2f(p) + 2 <= 2*2^n - 2
    2(2^n - 2) + 2 <= 2*2^n - 2
    2*2^n - 2 <= 2*2^n - 2
    
    This completes the induction step for right children.
"""

# b) Show an example of a binary tree with seven nodes that attains the above upper bound of f(p) for position p.

"""
    0
        2
            6
                14
                    30
                        62
                            126

This binary tree has a maximum level number of 126. With 7 nodes, it's upper bound would be


126 <= 2^n - 2
126 <= 2^7 - 2
126 <= 128 - 2
126 <= 126  
"""


# R-8.17

"""Show how to use the Euler tour traversal to compute the level number f(p), as defined in Section 8.3.2, of each
position in a binary tree T."""

class LevelNumberTour(BinaryEulerTour):
    class TourNotCompleteError(Exception):
        pass

    def __init__(self, tree):
        super().__init__(tree)
        self._count = 0

    def level_number(self, p):
        if len(self.tree()) != self._count:
            raise self.TourNotCompleteError('You need to conduct an tour of your tree before you can retrieve a '
                                            'level number.')
        return p.element()._level_number

    def _hook_previsit(self, p, d, path):
        maximum_number = 2*(d+1) - 2
        path_length = len(path) - 1
        level_number = maximum_number
        for index in path:
            if index == 0:  # left child
                level_number -= 2**path_length
            path_length -= 1
        p.element().set_level_number(level_number)
        self._count += 1


# R-8.18
"""Let T be a binary tree with n positions that is realized with an array representation A, and let f() be the level
numbering function of the positions of T, as given in Section 8.3.2. Give pseudocode descriptions of each methods
root, parent, left, right, is_leaf, and is_root."""

class ArrayBinaryTree:
    # init:
        # tree = []

    # root
        # get tree[0] // f(0)

    # left(p)
        # return f((p * 2) + 1)

    # right(p)
        # return f((p * 2) + 2)

    # parent(p)
        # return f(int((p - 1) / 2))

    # is_leaf(p)
        # return len(tree) > left(p)

    # is_root(f)
        # return f(0) == f(p)
    pass

# R-8.19
"""
Our definition of the level number function f(p) as given in Section 8.3.2 began with the root having number 0. Some
authors prefer to use a level number g(p) in which the root is assigned number 1, because it simplifies the arithmetic 
for finding neighbouring positions. Redo Exercise R-8.18, but assuming we use a level number g(p) in which the root is
assigned number 1.
"""

# If root is 1, that means its left child is 2 and right child 3.
# The left child of (2) would have to be 4, and right child would have to be 5.
# The left child of (3) would then be 6, and right child would be 7.
# The left child is 2g(p) and right child 2g(p) + 1
# The parent is floor(g(p) / 2)


    # root
        # return g(1)

    # left(p)
        # return g(p * 2)

    # right(p)
        # return g((p * 2) + 1)

    # parent(p)
        # return g(int(p / 2))

    # is_leaf(p)
        # return len(tree) + 1 > left(p)

    # is_root(p)
        # return g(1) === g(p)


# R-8.20
"""
Draw a binary tree T that simultaneously satisfies the following:
    * Each internal node of T stores a single character.
    * A preorder traversal of T yields EXAMFUN
    * An inorder traversal of T yields MAFXUEN
"""

# yield p
# for children in p:
#   inorder(children)


# if left_child:
#   inorder(left_child)
# yield p
# if right_child:
#   inorder(right_child)

"""
                E
            X       N
        A       U
    M       F
    
Preorder:   E -> X, N
            X -< A. U
            A -> M, F
            M
            F
            U
            N
            
Inorder:    ...E, X, A, M
            M
            A
            ...F
            F
            X
            ...U
            U
            E
            B
"""


# R-8.21
"""
In what order are positions visited during a preorder traversal of the tree of Figure 8.8?
"""

# 1st: -
# 2nd: /
# 3rd: X
# 4th: +
# 5th: 3
# 6th: 1
# 7th: 3
# 8th: +
# 9th: -
# 10th: 9
# 11th: 5
# 12th: 2
# 13th: +
# 14th: *
# 15th: 3
# 16th: -
# 17th: 7
# 18th: 4
# 19th: 6


# R-8.22
"""
In what order are positions visited during a postorder traversal of the tree of Figure 8.8?
"""

# 1st: 3
# 2nd: 1
# 3rd: +
# 4th: 3
# 5th: *
# 6th: 9
# 7th: 5
# 8th: -
# 9th: 2
# 10th: +
# 11th: /
# 12th: 3
# 13th: 7
# 14th: 4
# 15th: -
# 16th: *
# 17th: 6
# 18th: +
# 19th: -


# R-8.23
"""
Let T be an ordered tree with more than one node. Is it possible that the preorder traversal of T visits the nodes in 
the same order as the postorder traversal of T? If so, give an example; otherwise, explain why this cannot occur. Likewise,
is it possible that the preorder traversal of T visits the nodes in the reverse order of the postorder traversal of T? 
If so, give an example; otherwise explain why this cannot occur.
"""

"""If it has more than one node, they can never be the same for the simple reason that in a preorder traversal the root
is visited first, whereas in a postorder traversal, the root is visited last.

If we reverse the order of a postorder traversal, it is indeed possible that they may be equal. The example where we
have an ordered tree with just the root and one child. In a preorder traversal, the root is visited first, and then the
child. In a postorder traversal, the child is visited first, then the root. Reversing the postorder traversal would
result in the root being visited first, and then the child. This is identical to the preorder traversal.
"""
