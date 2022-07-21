from ch8.expression_tree import ExpressionTree


def array_to_linked_binary_tree(array_representation):
    # Root = 0
    # Left = 2 f(p) + 1
    # Right = 2 f(p) + 2
    t = LinkedBinaryTree2()
    positions_array = [None]*len(array_representation)
    if len(array_representation):
        root = t._add_root(array_representation[0])
        positions_array[0] = root
    for index, element in enumerate(array_representation):
        if index == 0 or element is None:
            continue
        parent = (index - 1) // 2
        if index % 2: # Left child
            position = t._add_left(positions_array[parent], element)
        else:
            position = t._add_right(positions_array[parent], element)
        positions_array[index] = position
    return t


"""
            1
        2         3
    4     5     6  9
         7 8
"""

"""
Array representation index
            0
        1         2
    3     4     5  6
         9 10 
"""

def array_to_tree_test():
    """
    >>> array_representation = [1, 2, 3, 4, 5, 6, 9, None, None, 7, 8]
    >>> treed = array_to_linked_binary_tree(array_representation)
    >>> for x in treed.preorder(): print(x.element())
    1
    2
    4
    5
    7
    8
    3
    6
    9
    """
    pass

# C-8.31
"""
Define the internal path length, I(T), of a tree T to be the sum of the depths of all the internal positions in T.
Likewise, define the external path length, E(T), of a tree T to be the sum of the depths of all external positions in
T. Show that if T is a proper binary tree with n positions, then E(T) = I(T) + n - 1
"""
from ch8.binary_tree import BinaryTree
from ch8.euler_tour import EulerTour, BinaryEulerTour
from ch8.linked_binary_tree import LinkedBinaryTree
from ch8.tree import Tree

"""
----------

Induction

Base cases:
Start with the root. In this case I(T) = 0 and E(T) = 0, simply because the depth of the root is 0.

Give the root two children (in acccordance with the definition of a proper binary tree)
I(T) = 0  (because the root, the only internal node, has zero depth)                        0
E(T) = 2  or (2*1)                                                                      0       0
E(T) = I(T) + n - 1 = 0 + 3 - 1 = 2 holds true

Add another two children to the left child of the root.                                 
I(T) = 1                                                                                    0
E(T) = (2*2) + (2 - 1)  (because one external node is now an internal node)  = 5          0     0
E(T) = I(T) + n - 1 = 1 + 5 - 1 = 5  holds true                                         0   0   

Add another two children to the leftmost child of the tree                              O
I(T) = 1 + (2*1) = 3                                                               0       0
E(T) = (3*2) + (5 - 2) = 9                                                      0    0     
E(T) = I(T) + n - 1 = 3 + 7 - 1 = 9                                           0   0
holds true


---------
Induction:
Every time you add d+1 to I(T), you get n+2 more nodes, and E(T) grows by (d+1)*2 thanks to the addition of the two nodes, 
but you also subtract by d because of the conversion of one external node to internal.

E(T)_1, I(T)_1 and n_1 are the original values, and E(T)_2, I(T)_2 and n_2 are the new values after adding another depth...

I(T)_2 = I(T)_1 + d
E(T)_2 = E(T)_1 + (d+1)*2 - d = E(T)_1 + 2d + 2 - d = E(T)_1 + d + 2
n_2 = n_1 + 2

E(T)_1 = I(T)_1 + n_1 - 1
Add d*1 to I(T)...
E(T)_2 = I(T)_1 + d + n_2 - 1
E(T)_1 + d + 2 = I(T)_1 + d + n_1 + 2 - 1
E(T)_1 + d + 2 = I(T)_1 + n_1 + d + 1
E(T)_1 = I(T)_1 + n_1 - 1

This is E(T) = I(T) + n - 1

This completes the induction step and the proof.
"""

# C-8.32
"""
Let T be a (not necessarily proper) binary tree with n nodes, and let D be the sum of the depths of all the external
nodes of T. Show that if T has the minimum number of external nodes possible, then D is O(n) and if T has the maximum
number of nodes possible, then D is O(n log n)
"""

"""
By the properties defined in Proposition 8.8
1 <= n_e <= 2^h
h + 1 <= n <= 2^(h+1) - 1

In the case where there are a minimum number of external nodes, 1, you would have a straight line from the root
to its descendants. The sum of the depths of all the external nodes in this case is simply equal to the depth, and
the relation between n and the depth is h + 1 <= n, or n = d + 1.

D = d, n = d + 1
d = n - 1
D = n - 1

This is O(n)

In the case where there are a maximum number of external nodes, 2^h, you would have a complete and proper binary tree.
The sum of the depths of all the external nodes would simply be d * 2^h, because all the external nodes would have the same
depths in this scenario. You would also have the maximum number of nodes, 2^(h+1) - 1, or n = 2^(d+1) - 1 where d is the
maximum depth.

D = d * 2^d, n = 2^(d+1) - 1
n - 1 = 2^(d+1)
log(n - 1) = d + 1
d = log(n - 1) - 1

D = d * 2^d
D = (log(n - 1) - 1) * 2^(log(n-1)-1)
D = (log(n-1) - 1) * 2^(log(n-1)) / 2^1
D = (log(n-1) - 1) * ( n-1 / 2 )
D = ( (log(n - 1) - 1) * (n - 1) ) / 2
D = (nlog(n-1) - log(n-1) - n + 1) / 2

This is O(nlog n) because cn log n >= nlog(n-1), and -log(n-1) and -n only further detract from it asymptotically.
"""

# C-8.33
"""Let T be a (possibly improper) binary tree with n nodes, and let D be the sum of the depths of all the external nodes
of T. Describe a configuration for T such that D is omega(n^2). Such a tree would be the worst case for the asymptotic
running time of method height1 (Code Fragment 8.4)"""

# Ω(n^2) means that it is higher than n^2. An example of where this might happen is where you convert only one
# external node with the maximum depth into an internal node and give it two children. Such a tree might look like this

"""
                                            X
                            X                               X
                X                   X
            X       X
        X       X
     X     X
   X   X
  X X
 X X
"""

# In this tree, for every new level of depth added (d+1), D loses d-1, but gains 2d. For every new level of depth added
# D = D_o - (d-1) + 2d = D_o - d + 1 + 2d = D_o + d + 1
# We know d grows with O(n) as in d = 0, 1, 2, 3, 4, 5...
# That means D grows 1 + 2 + 3 + 4 + 5.... as the depth grows. This is the classic Gaussian sum which is O(n^2)
# The +1 is O(n), 1 + 1 + 1... it depends on the depth.

# Overall, if you want to know D at a certain depth
# D_1 = D_0 + d + 1, where d = 1
# D_2 = D_1 + d + 1 = D_0 + d_1 + 1 + d_2 + 1, where d_1 = 1 and d_2 = 2
# (Gaussian sum) + d
# D = d(d+1)/2 + d
# D = (d^2 + d) / 2 + d
# D = (d^2 + 3d) / 2

# (d^2 + 3d) / 2 >= cd^2 where c = 1/2 and d_0 > 1
# This proves that D is omega(n^2)

# This is also the worst-case run time for _height1. _height1 only executes its recursion if it encounters a leaf,
# and its run time is O(d_p + 1). This kind of binary tree maximizes the number of leafs and also maximizes the depth,
# making it the worst case run time for _height1.

# C-8.34
"""
For a tree T, let n_i denote the number of its internal nodes, and let n_e denote the number of its external nodes.
Show that if every internal node in T has exactly 3 children, then n_e = 2n_i + 1
"""

# Proof by induction

# Base case: just the root. In this case, the number of internal nodes is zero, and the number of external nodes is 1.
# n_e = 2(n_i) + 1 = 2(0) + 1 = 0 + 1
# n_e = 1
# This proves the base case.

# Induction step: Convert the root to an internal node by adding 3 children.
# n_i += 1
# n_e loses the root as an external node, but now the root internal node now gives it three more external nodes.
# n_e = (n_e0 - 1) + 3 = n_e0 + 2

# n_e0 = 2(n_i - 1) + 1 = 2n_i - 2 + 1 = 2n_i - 1

# n_e = n_e0 + 2 = 2n_i - 1 + 2 = 2n_i + 1
# n_e = 2n_i + 1

# This completes the induction step.


# C-8.35
"""
Two ordered trees T' and T'' are said to be isomoprhic if one of the following holds:

* Both T' and T'' are empty.
* The roots of T' and T'' have the same number k >= 0 of subtrees, and the ith such subtree of T' is isomorphic to the 
ith such subtree of T'' for i = 1, ..., k

Design an algorithm that tests whether two given ordered trees are isomorphic. What is the running time of your algorithm?
"""

"""
These are isomorphic
            1
        2         3
    4     5     6
         7 8
"""

"""
            1
        3          2
          6    4      5
                    8   7
"""

"""
These are not isomorphic
                X 
        X               X
    X                X      X
                   X   X       X

                X
        X               X
     X     X               X
         X               X    X    
"""

def is_isomorphic(t1, p1, t2, p2):
    """
    >>> l1 = LinkedBinaryTree()
    >>> l1_root = l1._add_root(1)
    >>> l1_0 = l1._add_left(l1_root, 2)
    >>> l1_1 = l1._add_right(l1_root, 3)
    >>> l1_00 = l1._add_left(l1_0, 4)
    >>> l1_01 = l1._add_right(l1_0, 5)
    >>> l1_010 = l1._add_left(l1_01, 7)
    >>> l1_011 = l1._add_right(l1_01, 8)
    >>> l1_10 = l1._add_right(l1_1, 6)
    >>> l2 = LinkedBinaryTree()
    >>> l2_root = l2._add_root(1)
    >>> l2_0 = l2._add_left(l2_root, 3)
    >>> l2_01 = l2._add_right(l2_0, 6)
    >>> l2_1 = l2._add_right(l2_root, 2)
    >>> l2_10 = l2._add_left(l2_1, 4)
    >>> l2_11 = l2._add_right(l2_1, 5)
    >>> l2_110 = l2._add_left(l2_11, 8)
    >>> l2_111 = l2._add_right(l2_11, 7)
    >>> is_isomorphic(l1, l1.root(), l2, l2.root())
    True
    >>> l2_1100 = l2._add_left(l2_110, 9)
    >>> is_isomorphic(l1, l1.root(), l2, l2.root())
    False
    """
    if p1 is None and p2 is None:
        return True
    elif p1 is None or p2 is None:
        return False

    p1_num_children = t1.num_children(p1)
    p2_num_children = t2.num_children(p2)
    if p1_num_children != p2_num_children:
        return False

    isomorphic_subtrees = []  # might have to switch to a tuple
    for child1 in t1.children(p1):
        for index, child2 in enumerate(t2.children(p2)):
            if index in isomorphic_subtrees or not is_isomorphic(t1, child1, t2, child2):
                continue
            else:
                isomorphic_subtrees.append(index)
                break
    return len(isomorphic_subtrees) == p1_num_children


"""
The worst case running time of this algorithm is O(n^2). When comparing the trees, the worst case would be that the trees
are mirrored, so that a node that is to the left child to the root of the subtree A (call it node 0) is isomorphic to the last right child on subtree A (call it node N).
In this case, we would have to go through N iterations to get to node N.
The second left child on subtree A at position 1 would be isomorphic to node N - 1 on subtree B, and so on.
In that case it would take N - 1 iterations, and so on.
This is  the familiar sum n, n-1, n-2 ... 1, 0, which sums to O(n^2).
"""


# C-8.36
"""
Show that there are more than 2^n improper binary trees with n internal nodes such that no pair are isomoprhic.
"""

"""
Note: The question must've meant "more than or equal to 2^n"
Base case: Just one internal node. In this case, only the root can be the internal node. It can have either one child 
(left/right would be isomorphic) or two children. These are the two possible ways it could be structured. 2^(1) = 2
That proves the base case.

Induction step: Any time you convert an external node to an internal node, you create two possibilities: one child or two 
children for said internal node. 

Taking into account that there were two possibilities in the previous step, that means each two possibilities can beget 
two new isomorphic possibilities each. Over many steps, this is 2 * 2 * 2 * 2... = 2^n.  

"""

# C-8.37
"""If we exclude isomorphic trees, exactly how many PROPER binary trees exist with exactly 4 leaves"""

"""
4 leaves = 4 external nodes
h + 1 <= n_e <= 2^h

One example of a 4-leaf tree is a complete tree with a height of 2. There are no trees isomorphic to this. This
is the minimum height you need to get a 4 leaf tree. n_e <= 2^h --> 4 <= 2^2 

And a tree of height 3 is the maximum height you can have if you want 4 external nodes on a proper tree. 

        X
      X   X
    X   X
   X X
   
You can swap left or right children, but they are all isomorphic to this tree if the height is 3.

        X
    X       X
  X   X
     X X


        X
    X       X
          X   X
        X  X
        
and so on...


Therefore there are only two types of trees that have 4 external nodes. 
"""

# C-8.38
"""Add support in LinkedBinaryTree for a method, delete_subtree(p), that removes the entire subtree rooted at position
p, making sure to maintain the count on the size of the tree. What is the running time of your implementation?"""

# By "maintain the count on the size of the tree", I assume that to mean the count should be accurate.
# That means we need to count the number of nodes.

# Fastest way to count this would be some kind of preorder traversal counting the number of nodes, then just delete the tree.
# This would take O(n) time.
# Alternatively, we could recur on the deleted subtree until it is all deleted. The size would modify itself.
# This would also take O(n) time, but O(2n) time in the worst case. Count method is faster.

"""
            1
        2         3
    4     5     6  9
         7 8
"""



class LinkedBinaryTree2(LinkedBinaryTree):
    def delete_subtree(self, p):
        for c in self.children(p):
            self.delete_subtree(c)
        self._delete(p)

    def _swap(self, p, q):
        root = self.root()
        if root in (p, q):
            raise ValueError(f'The {"first" if p == root else "second"} node is the root of the tree. Cannot perform swap.')

        for position in (p, q):
            cursor = position
            while cursor != self.root():
                cursor = self.parent(cursor)
                if cursor == q or cursor == p:
                    raise ValueError(f"{'The second' if cursor == q else 'The first'} node is an ancestor of the other. "
                                     f"Cannot perform swap.")

        p_node = self._validate(p)
        q_node = self._validate(q)

        p_node_is_left_child = p_node._parent._left == p_node
        q_node_is_left_child = q_node._parent._left == q_node

        if p_node_is_left_child:
            p_node._parent._left = q_node
        else:
            p_node._parent._right = q_node

        if q_node_is_left_child:
            q_node._parent._left = p_node
        else:
            q_node._parent._right = p_node

        p_node._parent, q_node._parent = q_node._parent, p_node._parent

    def preorder_next(self, p):
        if self.num_children(p) > 0:
            return self.left(p) or self.right(p)
        else:
            if self.parent(p) is not None:
                p_is_left_child = self.left(self.parent(p)) == p
                if p_is_left_child and self.sibling(p) is not None:
                    return self.sibling(p)
                elif not p_is_left_child or (p_is_left_child and self.sibling(p) is None):
                    # If it's a right child or lone left child, we need to go up the tree until we get to a left child
                    # with sibling, meaning there is still a right subtree to traverse through
                    node_is_left_child = False
                    node_has_sibling = False
                    node = p
                    while not node_is_left_child or (node_is_left_child and not node_has_sibling):
                        node = self.parent(node)
                        if self.parent(node) is None:
                            return None
                        node_is_left_child = self.left(self.parent(node)) == node
                        node_has_sibling = self.sibling(node) is not None
                        
                    return self.sibling(node)
                else:
                    return None


    def inorder_next(self, p):
        if not self.is_root(p) and self.right(p) is None:
            p_is_left_child = self.left(self.parent(p)) == p
            if p_is_left_child:
                return self.parent(p)
            elif not p_is_left_child:
                # Keep going up until there's a left child with (right) sibling to traverse through.
                node = p
                node_is_left_child_and_has_sibling = False
                while not node_is_left_child_and_has_sibling:
                    if self.is_root(node):
                        return None
                    node_is_left_child_and_has_sibling = node == self.left(self.parent(node)) \
                                                         and self.sibling(node) is not None
                    node = self.parent(node)
                return node
        elif self.is_root(p) or self.right(p): # get left-most child of your right-subtree
            node = self.right(p)
            node_has_left_child = node is not None
            while node_has_left_child:
                if self.left(node):
                    node = self.left(node)
                else:
                    node_has_left_child = False
            return node
        else:
            # A left node with a sole left child.
            return self.parent(p)

    def postorder_next(self, p):
        if self.is_root(p):
            return None

        p_is_left_child = p == self.left(self.parent(p))
        if not p_is_left_child or (p_is_left_child and self.sibling(p) is None):
            return self.parent(p)


        if self.sibling(p) is not None:
            # Find the left-most-child of your sibling.
            node = self.sibling(p)
            node_has_child = self.left(node) or self.right(node)
            while node_has_child:
                node = self.left(node) or self.right(node)
                node_has_child = not self.is_leaf(node)
            return node



"""
            1
        2         3
    4     5     6
         7 8
         
Delete the subtree at 5. Size should be 5.
"""

def test_delete_subtree():
    """
    >>> l1 = LinkedBinaryTree2()
    >>> l1_root = l1._add_root(1)
    >>> l1_0 = l1._add_left(l1_root, 2)
    >>> l1_1 = l1._add_right(l1_root, 3)
    >>> l1_00 = l1._add_left(l1_0, 4)
    >>> l1_01 = l1._add_right(l1_0, 5)
    >>> l1_010 = l1._add_left(l1_01, 7)
    >>> l1_011 = l1._add_right(l1_01, 8)
    >>> l1_10 = l1._add_right(l1_1, 6)
    >>> len(l1)
    8
    >>> l1.delete_subtree(l1_01)
    >>> len(l1)
    5
    >>> try:
    ...   l1._validate(l1_010)  # should raise error
    ... except ValueError:
    ...   print("Pass")
    Pass
    >>> l1._validate(l1_0) is not None  # doesn't raise error
    True
    """
    pass


# C-8.39
"""Add support in LinkedBinaryTree for a method _swap(p,q) that has the effect of restructuring the tree so that the node
references by p takes the place of node referenced by q, and vice versa. Make sure to properly handle the case when the 
nodes are adjacent.

Adjacent: Connected
"""

"""
            1
        2         3
    4     5     6
         7 8
"""

def swap_test():
    """
    >>> l1 = LinkedBinaryTree2()
    >>> l1_root = l1._add_root(1)
    >>> l1_0 = l1._add_left(l1_root, 2)
    >>> l1_1 = l1._add_right(l1_root, 3)
    >>> l1_00 = l1._add_left(l1_0, 4)
    >>> l1_01 = l1._add_right(l1_0, 5)
    >>> l1_010 = l1._add_left(l1_01, 7)
    >>> l1_011 = l1._add_right(l1_01, 8)
    >>> l1_10 = l1._add_right(l1_1, 6)
    >>> # Scenario 1: One of the nodes is a root
    >>> try:
    ...   l1._swap(l1_root, l1_10)
    ... except ValueError as e:
    ...   print(e)
    The first node is the root of the tree. Cannot perform swap.
    >>> # Scenario 2: One node is the ancestor of another.
    >>> try:
    ...   l1._swap(l1_0, l1_011)
    ... except ValueError as e:
    ...   print(e)
    The first node is an ancestor of the other. Cannot perform swap.
    >>> try:
    ...   l1._swap(l1_011, l1_0)
    ... except ValueError as e:
    ...   print(e)
    The second node is an ancestor of the other. Cannot perform swap.
    >>> # Scenario 3: Successful swap
    >>> l1._swap(l1_1, l1_01)
    >>> l1._make_position(l1_root._node._right) == l1_1
    False
    >>> l1._make_position(l1_root._node._right) == l1_01
    True
    >>> l1._make_position(l1_0._node._right) == l1_1
    True
    >>> l1._make_position(l1_0._node._right) == l1_01
    False
    """
    pass

# C-8.40
"""
We can simplify parts of our LinkedBinaryTree implementation if we make use of a single sentinel node, referenced as the
_sentinel member of the tree instance, such that the sentinel is the parent of the real root of the tree, and the root
is referenced as the left child of the sentinel. Furthermore, the sentinel will take the place of None as the value of the
_left or _right member for a node without such a child. Give a new implementation of the update methods _delete and _attach,
assuming such a representation.

Notes;

It's just ONE sentinel node. This sentinel node has the root as it's left child. This sentinel is also referenced as the
children of leaf nodes.

Hint: Avoid conditionals where possible.
"""

class LinkedBinaryTreeWithSentinels(LinkedBinaryTree):
    def __init__(self):
        super().__init__()
        self._sentinel = self._Node(None)
        self._sentinel._left = self._root

    def root(self):
        return self._sentinel._left

    def left(self, p):
        return super().left(p) if not None else self._sentinel

    def right(self, p):
        return super().right(p) if not None else self._sentinel

    def _add_root(self, e):
        root = super()._add_root(e)
        self._sentinel._left = root._node

    def _delete(self, p):
        node = self._validate(p)
        if self.num_children(p) == 2:
            raise ValueError('Position has two children')

        child = node._left if node._left else node._right  # might be None
        if child is not None:  # i.e. it has one child
            child._parent = node._parent  # child's grandparent becomes parent
        parent = node._parent
        if node is parent._left:
            parent._left = child
        else:
            parent._right = child
        self._size -= 1
        node._parent = node  # convention for deprecated node
        return node._element

    def _attach(self, p, t1, t2):
        node = self._validate(p)
        if not self.is_leaf(p):
          raise ValueError('position must be leaf')
        if not type(self) is type(t1) is type(t2):    # all 3 trees must be same type
          raise TypeError('Tree types must match')
        self._size += len(t1) + len(t2)
        if not t1.is_empty():         # attached t1 as left subtree of node
          # Your sentinel needs to become the new tree's sentinel
          # But first, make sure your root's parent is the other tree's leaf instead.
          t1._root._parent = node
          node._left = t1._root
          t1._sentinel = self._sentinel
          t1._root = None             # set t1 instance to empty
          t1._size = 0
        if not t2.is_empty():         # attached t2 as right subtree of node
          t2._root._parent = node
          node._right = t2._root
          t2._sentinel = self._sentinel
          t2._root = None             # set t2 instance to empty
          t2._size = 0


# C-8.41
"""
Describe how to clone a LinkedBinaryTree instance representing a proper binary tree, with use of the _attach method

Hint: Recursion may be helpful.
"""

"""
            1
        2         3
    4     5     6  9
         7 8
"""

def clone_proper_tree(p1, p2=None, main_leaf=None, main_tree=None):
    """
    >>> l1 = LinkedBinaryTree2()
    >>> l1_root = l1._add_root(1)
    >>> l1_0 = l1._add_left(l1_root, 2)
    >>> l1_1 = l1._add_right(l1_root, 3)
    >>> l1_00 = l1._add_left(l1_0, 4)
    >>> l1_01 = l1._add_right(l1_0, 5)
    >>> l1_010 = l1._add_left(l1_01, 7)
    >>> l1_011 = l1._add_right(l1_01, 8)
    >>> l1_10 = l1._add_left(l1_1, 6)
    >>> l1_11 = l1._add_right(l1_1, 9)
    >>> new_tree = clone_proper_tree(l1.root())
    >>> len(l1) == len(new_tree)
    True
    >>> l1_tour = iter(l1.inorder())
    >>> l2_tour = iter(new_tree.inorder())
    >>> they_are_the_same = False
    >>> for node in  l1_tour:
    ...  node2 = next(l2_tour)
    ...  #print(f'{node.element(), node2.element()}')  # for debugging
    ...  if node.element() == node2.element():
    ...    they_are_the_same = True
    ...  else:
    ...    they_are_the_same = False
    ...    break
    >>> they_are_the_same
    True
    """
    # Base case: no tree
        # Create a tree with just the root
    # Other case: have tree, no new children to clone.
    # Other case: have tree, with two new children to clone.

    if main_tree is None:
        main_tree = LinkedBinaryTree2()
        if p1 is None:
            return main_tree
        main_tree._add_root(p1.element())
        main_leaf = main_tree.root()
        clone_proper_tree(p1._node._left, p1._node._right, main_leaf, main_tree)
        return main_tree
    elif p1 is None or p2 is None:
        pass
    else:
        p1_tree = LinkedBinaryTree2()
        p1_tree._add_root(p1._element)
        p2_tree = LinkedBinaryTree2()
        p2_tree._add_root(p2._element)
        main_tree._attach(main_leaf, p1_tree, p2_tree)
        if p1._left:  # By definition of proper tree, if at least one child exists, both exist
            main_leaf_left = main_tree.left(main_leaf)
            clone_proper_tree(p1._left, p1._right, main_leaf_left, main_tree)
        if p2._left:
            main_leaf_right = main_tree.right(main_leaf)
            clone_proper_tree(p2._left, p2._right, main_leaf_right, main_tree)


# C-8.42
"""
Describe how to clone a LinkedBinaryTree instance representing a (not necessarily proper) binary tree, with use of
the _add_left and _add_right methods.


            1
        2         3
    4     5     6
         7 8
"""

def clone_improper_tree(p1, p2=None, main_leaf=None, main_tree=None):
    """
    >>> l1 = LinkedBinaryTree2()
    >>> l1_root = l1._add_root(1)
    >>> l1_0 = l1._add_left(l1_root, 2)
    >>> l1_1 = l1._add_right(l1_root, 3)
    >>> l1_00 = l1._add_left(l1_0, 4)
    >>> l1_01 = l1._add_right(l1_0, 5)
    >>> l1_010 = l1._add_left(l1_01, 7)
    >>> l1_011 = l1._add_right(l1_01, 8)
    >>> l1_10 = l1._add_left(l1_1, 6)
    >>> new_tree = clone_improper_tree(l1.root())
    >>> len(l1) == len(new_tree)
    True
    >>> l1_tour = iter(l1.inorder())
    >>> l2_tour = iter(new_tree.inorder())
    >>> they_are_the_same = False
    >>> for node in  l1_tour:
    ...  node2 = next(l2_tour)
    ...  #print(f'{node.element(), node2.element()}')  # for debugging
    ...  if node.element() == node2.element():
    ...    they_are_the_same = True
    ...  else:
    ...    they_are_the_same = False
    ...    break
    >>> they_are_the_same
    True
    """
    if main_tree is None:
        main_tree = LinkedBinaryTree()
        if p1 is None:  # empty tree
            return main_tree
        main_tree._add_root(p1.element())
        main_leaf = main_tree.root()
        clone_improper_tree(p1._node._left, p1._node._right, main_leaf, main_tree)
        return main_tree
    else:

        # p1 and p2 are of type node
        if p1 is not None:
            main_tree._add_left(main_leaf, p1._element)
        if p2 is not None:
            main_tree._add_right(main_leaf, p2._element)

        #main_tree._attach(main_leaf, p1_tree, p2_tree)
        if p1 is not None and (p1._left or p1._right):  # By definition of proper tree, if at least one child exists, both exist
            main_leaf_left = main_tree.left(main_leaf)
            clone_improper_tree(p1._left, p1._right, main_leaf_left, main_tree)
        if p2 is not None and (p2._left or p2._right):
            main_leaf_right = main_tree.right(main_leaf)
            clone_improper_tree(p2._left, p2._right, main_leaf_right, main_tree)

# C-8.43
"""
We can define a binary tree representation T' for an ordered general tree T as follows (see Fig. 8.23):
* For each position p of T, there is an associated position p' of T'.
* If p is a leaf of T, then p' in T' does not have a left child; otherwise the left child of p' is q, where q is the 
first child of p in T.
* If p has a sibling q ordered immediately after it in T, then q' is the right child of p' in T; otherwise p' does not 
have a right child.

Questions below.
"""

# C-8.43a
"""
a. Is a preorder traversal of T' equivalent to a preorder traversal of T?
"""

"""
Preorder traversal of T: A -> B -> E -> F -> C -> D -> G
Preorder traversal of T': A -> B -> E -> F -> C -> D -> G

In the case of Fig. 8.23, it is.

It should be the case in all trees, because if p is a leaf in T, then it does not have any children to iterate through
in a preorder traversal. The same p' in T' would have only siblings to iterate through (as children), which is the same
order as a preorder traversal of p/T.

If p did have children, then they are also children of either p' or the descendants of p', in the same order as a preorder
traversal of p/T.
"""

# C-8.43b
"""
b. Is a postorder traversal of T' equivalent to a postorder traversal of T?
"""

"""
Postorder traversal of T: E -> F -> B -> C -> G -> D -> A
Postorder traversal of T': F

No, it is not. In the case of Fig. 8.23, the first element returned in T would be E, but the first element returned in
T' would be F.
"""

# C-8.43c
"""
c. Is an inorder traversal of T' equivalent to one of the standard traversals of T? If so, which one?
"""

"""
In-order traversal of T': E -> F -> B -> C -> G -> D -> A

The inorder traversal of T' is equivalent to a preorder traversal of T.
"""

# C-8.44
"""
Give an efficient algorithm that computes and prints, for every position p of a tree T, the element of p followed by
the height of p's subtree.
"""

# An postorder traversal sounds like the fastest way to do this.
"""
            1
        2         3
    4     5     6
         7 8
"""

class GetHeightAndElement(EulerTour):
    def _hook_postvisit(self, p, d, path, results):
        if len(results) == 0:
            height = 0
        else:
            height = max(results) + 1
        print(f'({p.element()}, {height})')
        return height


def get_height_and_element(tree):
    """
    >>> l1 = LinkedBinaryTree2()
    >>> l1_root = l1._add_root(1)
    >>> l1_0 = l1._add_left(l1_root, 2)
    >>> l1_1 = l1._add_right(l1_root, 3)
    >>> l1_00 = l1._add_left(l1_0, 4)
    >>> l1_01 = l1._add_right(l1_0, 5)
    >>> l1_010 = l1._add_left(l1_01, 7)
    >>> l1_011 = l1._add_right(l1_01, 8)
    >>> l1_10 = l1._add_left(l1_1, 6)
    >>> _ = GetHeightAndElement(l1).execute()
    (4, 0)
    (7, 0)
    (8, 0)
    (5, 1)
    (2, 2)
    (6, 0)
    (3, 1)
    (1, 3)
    """
    # Do a post order traversal
    # If yield without entering for-loop, yield 0 along with element.
    #
    pass

# This algorithm runs in O(n) time.

# C-8.45
"""
Give an O(n)-time algorithm for computing the depths of all positions of a tree T, where n is the number of nodes of T.
"""


class GetDepthsAndElements(EulerTour):
    def _hook_postvisit(self, p, d, path, results):
        print(f'({p.element()}, {d})')


"""
            1
        2         3
    4     5     6
         7 8
"""

def get_depth_and_positions():
    """
    >>> l1 = LinkedBinaryTree2()
    >>> l1_root = l1._add_root(1)
    >>> l1_0 = l1._add_left(l1_root, 2)
    >>> l1_1 = l1._add_right(l1_root, 3)
    >>> l1_00 = l1._add_left(l1_0, 4)
    >>> l1_01 = l1._add_right(l1_0, 5)
    >>> l1_010 = l1._add_left(l1_01, 7)
    >>> l1_011 = l1._add_right(l1_01, 8)
    >>> l1_10 = l1._add_left(l1_1, 6)
    >>> GetDepthsAndElements(l1).execute()
    (4, 2)
    (7, 3)
    (8, 3)
    (5, 2)
    (2, 1)
    (6, 2)
    (3, 1)
    (1, 0)
    """


# C-8.46
"""
The path length of a tree T is the sum of the depths of all positions in T. Describe a linear-time method for computing
the path length of a tree T.
"""

# An euler tour would work best

"""
            1
        2         3
    4     5     6
         7 8
"""

"""
            14
       11         3
    2     8     2
         3 3
"""

class PathLength(EulerTour):
    def _hook_postvisit(self, p, d, path, results):
        return d + sum(results)

def get_path_length(tree):
    """
    >>> l1 = LinkedBinaryTree2()
    >>> l1_root = l1._add_root(1)
    >>> l1_0 = l1._add_left(l1_root, 2)
    >>> l1_1 = l1._add_right(l1_root, 3)
    >>> l1_00 = l1._add_left(l1_0, 4)
    >>> l1_01 = l1._add_right(l1_0, 5)
    >>> l1_010 = l1._add_left(l1_01, 7)
    >>> l1_011 = l1._add_right(l1_01, 8)
    >>> l1_10 = l1._add_left(l1_1, 6)
    >>> PathLength(l1).execute()
    14
    """


# C-8.47
"""The balance factor of an internal position p of a proper binary tree is the difference between the heights of the 
right and left subtrees of p. Show how to specialize the Euler tour traversal to print the balance factors of all
the internal nodes of a proper binary tree."""

"""
            1
        2         3
    4     5     6  9
         7 8
"""

"""
Heights
            3
       2         1
    0     1     0 0
         0 0
"""

"""
Balance factor
            1
       1         0
    0     0     0 0
         0 0
"""

class BalanceFactor(EulerTour):
    def _hook_postvisit(self, p, d, path, results):
        if len(results) == 0:
            balance_factor = 0
            height = 0
        else:
            balance_factor = abs(results[0][0] - results[1][0])
            height = -1
            for result in results:
                if result[0] > height:
                    height = result[0]
            height += 1
        print(f'Element: {p.element()}, Height: {height}, Balance Factor: {balance_factor}')
        return [height, balance_factor]

def balance_factor_test():
    """
    >>> l1 = LinkedBinaryTree2()
    >>> l1_root = l1._add_root(1)
    >>> l1_0 = l1._add_left(l1_root, 2)
    >>> l1_1 = l1._add_right(l1_root, 3)
    >>> l1_00 = l1._add_left(l1_0, 4)
    >>> l1_01 = l1._add_right(l1_0, 5)
    >>> l1_010 = l1._add_left(l1_01, 7)
    >>> l1_011 = l1._add_right(l1_01, 8)
    >>> l1_10 = l1._add_left(l1_1, 6)
    >>> l1_11 = l1._add_right(l1_1, 9)
    >>> _ = BalanceFactor(l1).execute()
    Element: 4, Height: 0, Balance Factor: 0
    Element: 7, Height: 0, Balance Factor: 0
    Element: 8, Height: 0, Balance Factor: 0
    Element: 5, Height: 1, Balance Factor: 0
    Element: 2, Height: 2, Balance Factor: 1
    Element: 6, Height: 0, Balance Factor: 0
    Element: 9, Height: 0, Balance Factor: 0
    Element: 3, Height: 1, Balance Factor: 0
    Element: 1, Height: 3, Balance Factor: 1
    """
    pass


# C-8.48
"""
Given a proper binary tree T, define the reflection of T to be the binary tree T' such that each node v in T is also in
T', but the left child of v in T is v's right child in T' and the right child of v in T is v's left child in T'.

Show that a preorder traversal of a proper binary tree T is the same as the postorder traversal of T's reflection, but
in reverse order.
"""

"""
Original
            1
        2         3
    4     5     6  9
         7 8
"""

"""
Mirror
            1
        3         2
    9     6     5   4
               8 7     
"""

"""
Preorder of T: 1 -> 2 -> 4 -> 5 -> 7 -> 8 -> 3 -> 6 -> 9
Postorder of T': 9 -> 6 -> 3 -> 8 -> 7 -> 5 -> 4 -> 2 -> 1
"""


def mirror_tree(tree, p=None):
    """
    >>> l1 = LinkedBinaryTree2()
    >>> l1_root = l1._add_root(1)
    >>> l1_0 = l1._add_left(l1_root, 2)
    >>> l1_1 = l1._add_right(l1_root, 3)
    >>> l1_00 = l1._add_left(l1_0, 4)
    >>> l1_01 = l1._add_right(l1_0, 5)
    >>> l1_010 = l1._add_left(l1_01, 7)
    >>> l1_011 = l1._add_right(l1_01, 8)
    >>> l1_10 = l1._add_left(l1_1, 6)
    >>> l1_11 = l1._add_right(l1_1, 9)
    >>> mirrored_tree = clone_proper_tree(l1.root())
    >>> mirror_tree(mirrored_tree)
    >>> for p in mirrored_tree.postorder():
    ...   print(p.element())
    9
    6
    3
    8
    7
    5
    4
    2
    1
    >>> regular_tree_preorder = [x.element() for x in l1.preorder()]
    >>> mirrored_tree_postorder = [x.element() for x in mirrored_tree.postorder()]
    >>> regular_tree_preorder[-1::-1] == mirrored_tree_postorder
    True
    """
    if p is None:
        p = tree.root()
    if tree.num_children(p) != 0:
        tree._swap(tree.left(p), tree.right(p))
        for child in tree.children(p):
            mirror_tree(tree, child)

# C-8.49
"""Let the rank of a position p during a traversal be defined such that the first element visited has rank 1, the second
element visited has rank 2, and so on. For each position p in a tree T, let pre(p) be the rank of p in a preorder 
traversal of T, let post(p) be the rank of p in a postorder traversal of T, let depth(p) be the depth of p, and let 
desc(p) be the number of descendants of p, including p itself. Derive a formula defining post(p) in terms of desc(p),
depth(p), and pre(p), for each node p in T."""

"""
Original
            1
        2         3
    4     5     6  9
         7 8
"""

"""
Post-order rank
            9
        5         8
    1     4     6  7
         2 3
"""

"""
Descendants rank (might have to +1 everything if it's inclusive)
            8
        4         2
    0     2     0  0
         0 0
"""


"""
Depth rank
            0
        1         1
    2     2     2  2
         3 3
"""

"""
Preorder rank
            1
        2         7
    3     4     8  9
         5 6
"""
# Postorder     Desc    Depth   Preorder
#       1       0       2       3
#       2       0       3       5
#       3       0       3       6
#       4       2       2       4
#       5       4       1       2
#       6       0       2       8
#       7       0       2       9
#       8       2       1       7
#       9       8       0       1

"""
Notes:
* We know if the depth is 0 and preorder is 1 (the root), postorder will always equal desc(p) + pre(p)
* An observable pattern for those with desc(p) = 0 (leaves) is that post(p) = pre(p) - depth(p)
# desc(p) + pre(p) - depth(p) ? 
        # It works!
"""


# Formula is post(p) = desc(p) + pre(p) - depth(p)


# C-8.50
"""
Design algorithms for the following operations for a binary tree T:
* preorder_next(p): Return the position visited after p in a preorder traversal of T (or None if p is the last node visited).
* inrder_next(p): Return the poition visited after p in an inorder traversal of T (or none if p is the last node visited)
* postorder_next(p): Return the position visited after p in a postorder traversal of T (or None if p is the last node visited)
"""

"""
            1
        2         3
    4     5      6  10
         7 8      9
                 11
                12
               13 
"""

def next_tests():
    """
    >>> l1 = LinkedBinaryTree2()
    >>> l1_root = l1._add_root(1)
    >>> l1_0 = l1._add_left(l1_root, 2)
    >>> l1_1 = l1._add_right(l1_root, 3)
    >>> l1_00 = l1._add_left(l1_0, 4)
    >>> l1_01 = l1._add_right(l1_0, 5)
    >>> l1_010 = l1._add_left(l1_01, 7)
    >>> l1_011 = l1._add_right(l1_01, 8)
    >>> l1_10 = l1._add_left(l1_1, 6)
    >>> l1_100 = l1._add_right(l1_10, 9)
    >>> l1_11 = l1._add_right(l1_1, 10)
    >>> l1_1000 = l1._add_left(l1_100, 11)
    >>> l1_10000 = l1._add_left(l1_1000, 12)
    >>> l1_100000 = l1._add_left(l1_10000, 13)
    >>> p = l1.root()
    >>> p.element()
    1
    >>> p = l1.preorder_next(p)
    >>> p.element()
    2
    >>> p = l1.root()
    >>> while p is not None:
    ...     print(p.element())
    ...     p = l1.preorder_next(p)
    1
    2
    4
    5
    7
    8
    3
    6
    9
    11
    12
    13
    10
    >>> p = l1_00  # first node in an inorder traversal.
    >>> while p is not None:
    ...   print(p.element())
    ...   p = l1.inorder_next(p)
    4
    2
    7
    5
    8
    1
    6
    13
    12
    11
    9
    3
    10
    >>> p = l1_00  # first node in a postorder traversal
    >>> while p is not None:
    ...   print(p.element())
    ...   p = l1.postorder_next(p)
    4
    7
    8
    5
    2
    13
    12
    11
    9
    6
    10
    3
    1
    """
    pass


#C-8.51
"""
To implement the preorder method of the LinkedBinaryTree class, we relied on the convenience of Python's generator syntax
and the yield statement. Give an alternative implementation of preorder that returns an explicit instance of a nested 
iterator class.
"""

class LinkedBinaryTreeWithIteratorClasses(LinkedBinaryTree2):
    class _PreorderIterator:
        def __init__(self, tree):
            self._tree = tree
            self._k = -1

        def __iter__(self):
            return self

        def __next__(self):
            if self._k == -1:
                self._k = self._tree.root()
                return self._k
            self._k = self._tree.preorder_next(self._k)
            if self._k is None:
                raise StopIteration()
            return self._k

    def get_preorder_iterator(self):
        return self._PreorderIterator(self)


def iterator_class_test():
    """
    >>> l1 = LinkedBinaryTreeWithIteratorClasses()
    >>> l1_root = l1._add_root(1)
    >>> l1_0 = l1._add_left(l1_root, 2)
    >>> l1_1 = l1._add_right(l1_root, 3)
    >>> l1_00 = l1._add_left(l1_0, 4)
    >>> l1_01 = l1._add_right(l1_0, 5)
    >>> l1_010 = l1._add_left(l1_01, 7)
    >>> l1_011 = l1._add_right(l1_01, 8)
    >>> l1_10 = l1._add_left(l1_1, 6)
    >>> l1_100 = l1._add_right(l1_10, 9)
    >>> l1_11 = l1._add_right(l1_1, 10)
    >>> l1_1000 = l1._add_left(l1_100, 11)
    >>> l1_10000 = l1._add_left(l1_1000, 12)
    >>> l1_100000 = l1._add_left(l1_10000, 13)
    >>> generator = l1.get_preorder_iterator()
    >>> next(generator).element()
    1
    >>> next(generator).element()
    2
    >>> for x in generator:
    ...  print(x.element())
    4
    5
    7
    8
    3
    6
    9
    11
    12
    13
    10
    """
    pass

#C-8.52
"""
Algorithm preorder_draw draws a binary tree T by assigning x- and y- coordinates to each position p such that x(p) is
the number of nodes preceding p in the preorder traversal of T and y(p) is the depth of p in T.

a. Show that the drawing of T produced by preorder_draw has no pairs of crossing edges.
"""

# Hint: use induction

# Base case: just the root.
# There are no edges in this case.

# Base case 2: Root with left child.
# Since there is just one edge, it can't cross with another edge.


# Base case 3: Root with right child.
# These two don't cross, being on the same depth, but the right child coming after the left child.
"""
    0   1   2
0   Root
1       L   R
"""

# Induction step: Add one new node to either L or R.
# This won't create crossing edges. Any node added to L would precede R in a preorder traversal. It would be on a new
# depth, avoiding it crossing with R or any of R's descendants.

# C-8.52b
"""
b. Redraw the binary tree of Figure 8.22 using preorder_draw
"""

class BinaryPreorderLayout(BinaryEulerTour):
    """Class for computing (x,y) coordinates for each node of a binary tree."""
    def __init__(self, tree):
        super().__init__(tree)           # must call the parent constructor
        self._count = 0                  # initialize count of processed nodes

    def _hook_previsit(self, p, d, path):
        p.element().setX(self._count)
        p.element().setY(d)
        self._count += 1


class Coordinate:
    def __init__(self, x=0, y=0):
        self._x = x
        self._y = y

    def setX(self, x):
        self._x = x

    def setY(self, y):
        self._y = y

    def getX(self):
        return self._x

    def getY(self):
        return self._y


def draw(T):
    DISTANCE_BETWEEN_NUMBERS = 4
    toprow = ''
    for number in range(len(T)):
            str_number = str(number)
            additional_string = (DISTANCE_BETWEEN_NUMBERS-len(str_number))*' ' + str_number
            toprow += additional_string
    print(toprow)
    # Then we do a breadth-first traversal.
    depth_row = ''
    breadthfirst = T.breadthfirst()

    coordinate = next(breadthfirst)
    tree_traversed = False
    while not tree_traversed:
        depth = coordinate.element().getY()
        depth_str = str(depth)
        while coordinate.element().getY() == depth:
            mark_position = (coordinate.element().getX()+1) * DISTANCE_BETWEEN_NUMBERS
            depth_str += ' ' * (mark_position-(len(depth_str) + 1))
            depth_str += 'X' if T.is_leaf(coordinate) else 'O'
            try:
                coordinate = next(breadthfirst)
            except StopIteration:
                tree_traversed = True
                break
        print(depth_str)


def preorder_draw(T):
    BinaryPreorderLayout(T).execute()
    draw(T)

        # Initialize empty string
        # Add the depth of the coordinate
        # Then use the x-coordinate to determine where it should be on the line. Mark with O for non-leaf and X for leaf.


# First set coordinates on all the elements, then do a breadth-first traversal to draw it out.

def draw_test():
    """"
    >>> l1 = LinkedBinaryTree()
    >>> l1_root = l1._add_root(Coordinate())
    >>> l1_0 = l1._add_left(l1_root, Coordinate())
    >>> l1_00 = l1._add_left(l1_0, Coordinate())
    >>> l1_01 = l1._add_right(l1_0, Coordinate())
    >>> l1_000 = l1._add_left(l1_00, Coordinate())
    >>> l1_001 = l1._add_right(l1_00, Coordinate())
    >>> l1_0010 = l1._add_left(l1_001, Coordinate())
    >>> l1_0011 = l1._add_right(l1_001, Coordinate())
    >>> l1_1 = l1._add_right(l1_root, Coordinate())
    >>> l1_10 = l1._add_left(l1_1, Coordinate())
    >>> l1_11 = l1._add_right(l1_1, Coordinate())
    >>> l1_100 = l1._add_left(l1_10, Coordinate())
    >>> l1_101 = l1._add_right(l1_10, Coordinate())
    >>> BinaryPreorderLayout(l1).execute()
    >>> l1_root.element().getX()
    0
    >>> l1_01.element().getX()
    7
    >>> l1_01.element().getY()  # It works!
    2
    >>> preorder_draw(l1)
       0   1   2   3   4   5   6   7   8   9  10  11  12
    0  O
    1      O                           O
    2          O                   X       O           X
    3              X   O                       X   X
    4                      X   X
    """
    pass


# C-8.53
"""
Redo the previous problem for the algorithm postorder_draw that is similar to preorder_draw except that it assigns x(p)
to be the number of nodes preceding position p in the postorder traversal.
"""

class BinaryPostorderLayout(BinaryEulerTour):
    """Class for computing (x,y) coordinates for each node of a binary tree."""
    def __init__(self, tree):
        super().__init__(tree)           # must call the parent constructor
        self._count = 0                  # initialize count of processed nodes

    def _hook_postvisit(self, p, d, path, results):
        p.element().setX(self._count)
        p.element().setY(d)
        self._count += 1


def postorder_draw(T):
    BinaryPostorderLayout(T).execute()
    draw(T)

def draw_postorder_test():
    """"
    >>> l1 = LinkedBinaryTree()
    >>> l1_root = l1._add_root(Coordinate())
    >>> l1_0 = l1._add_left(l1_root, Coordinate())
    >>> l1_00 = l1._add_left(l1_0, Coordinate())
    >>> l1_01 = l1._add_right(l1_0, Coordinate())
    >>> l1_000 = l1._add_left(l1_00, Coordinate())
    >>> l1_001 = l1._add_right(l1_00, Coordinate())
    >>> l1_0010 = l1._add_left(l1_001, Coordinate())
    >>> l1_0011 = l1._add_right(l1_001, Coordinate())
    >>> l1_1 = l1._add_right(l1_root, Coordinate())
    >>> l1_10 = l1._add_left(l1_1, Coordinate())
    >>> l1_11 = l1._add_right(l1_1, Coordinate())
    >>> l1_100 = l1._add_left(l1_10, Coordinate())
    >>> l1_101 = l1._add_right(l1_10, Coordinate())
    >>> BinaryPostorderLayout(l1).execute()
    >>> l1_root.element().getY()
    0
    >>> l1_01.element().getY()
    2
    >>> l1_000.element().getX()  # First element in a postorder
    0
    >>> l1_0010.element().getX()  # Second element in a postorder
    1
    >>> postorder_draw(l1)
       0   1   2   3   4   5   6   7   8   9  10  11  12
    0                                                  O
    1                          O                   O
    2                  O   X               O   X
    3  X           O               X   X
    4      X   X
    """
    pass


# C-8.54
"""
Design an algorithm for drawing general trees, using a style similar to the inorder traversal approach for drawing
binary trees.
"""

# When doing a preorder traversal, get the number of children each node has.
# Queue to do a preorder/"inorder" traversal of the first half, and then an "inorder" traversal of the parent
# before coming back around to the other half of the children nodes.
# What for children nodes with children?
# Children should be dealt with first. Think of it like a preorder/inorder traversal.

# Don't we have a formula for calculating postorder traversal given the preorder traversal and depth?
# Might not be able to do Euler tour for this one, since none work.

class GeneralTreeLayout(EulerTour):
    def __init__(self, tree):
        super().__init__(tree)
        self._count = 0

    def _tour(self, p, d, path):
        """Perform tour of subtree rooted at Position p.

        p        Position of current node being visited
        d        depth of p in the tree
        path     list of indices of children on path from root to p
        """
        path = None
        results = None
        num_children, children_to_traverse = self._hook_previsit(p, d, path)  # "pre visit" p
        if num_children:
            i = 0
            t_children = self._tree.children(p)
            while i < children_to_traverse:
                child = next(t_children)
                i += 1
                self._tour(child, d+1, path)
        # Do an invisit--this is where you print the current value
        self._hook_invisit(p, d)

        if num_children:
            while i < num_children:
                child = next(t_children)
                i += 1
                self._tour(child, d+1, path)

    def _hook_invisit(self, p, d):
        p.element().setX(self._count)
        p.element().setY(d)
        self._count += 1

    def _hook_previsit(self, p, d, path):
        num_children = self._tree.num_children(p)
        if num_children > 0:
            half_children = num_children // 2
            if half_children == 0:
                half_children = 1
            return (num_children, half_children)
        return (0, 0)


class TreeWithChildren(Tree):
    class _Node:
        __slots__ = '_element', '_parent', '_children'

        def __init__(self, element, parent=None, children=None):
            self._element = element
            self._parent = parent
            self._children = [] if not isinstance(children, list) else children

    class Position(BinaryTree.Position):
        """An abstraction representing the location of a single element."""

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

    # ------------------------------- utility methods -------------------------------
    def _validate(self, p):
        """Return associated node, if position is valid."""
        if not isinstance(p, self.Position):
            raise TypeError('p must be proper Position type')
        if p._container is not self:
            raise ValueError('p does not belong to this container')
        if p._node._parent is p._node:  # convention for deprecated nodes
            raise ValueError('p is no longer valid')
        return p._node

    def _make_position(self, node):
        """Return Position instance for given node (or None if no node)."""
        return self.Position(self, node) if node is not None else None

    # -------------------------- tree constructor --------------------------
    def __init__(self):
        """Create an initially empty binary tree."""
        self._root = None
        self._size = 0

    def __len__(self):
        """Return the total number of elements in the tree."""
        return self._size

    # ---------- abstract methods that concrete subclass must support ----------
    def root(self):
        """Return Position representing the tree's root (or None if empty)."""
        return self._make_position(self._root)

    def parent(self, p):
        """Return Position representing p's parent (or None if p is root)."""
        node = self._validate(p)
        self._make_position(node._parent)

    def num_children(self, p):
        """Return the number of children that Position p has."""
        node = self._validate(p)
        return len(node._children)

    def children(self, p):
        """Generate an iteration of Positions representing p's children."""
        node = self._validate(p)
        for child in node._children:
            yield self._make_position(child)

    def ith_child_node(self, i, p):
        node = self._validate(p)
        if len(node._children) > i:
            raise IndexError("Index of child is out of bounds")
        return self._make_position(node._children[i])

    def _add_root(self, e):
        if self._root is not None:
            raise ValueError('Root exists')
        self._size = 1
        self._root = self._Node(e)
        return self._make_position(self._root)

    def _add_child(self, p, e):
        node = self._validate(p)
        self._size += 1
        node._children.append(self._Node(e, node))  # node is its parent
        return self._make_position(node._children[len(node._children)-1])


def general_tree_draw_test():
    """
    >>> t = TreeWithChildren()  # Recreating the structure of Figure 8.2
    >>> t_root = t._add_root(Coordinate())
    >>> t.root() == t_root
    True
    >>> t_0 = t._add_child(t_root, Coordinate())
    >>> t_1 = t._add_child(t_root, Coordinate())
    >>> t_2 = t._add_child(t_root, Coordinate())
    >>> t_3 = t._add_child(t_root, Coordinate())
    >>> t_10 = t._add_child(t_1, Coordinate())
    >>> t_11 = t._add_child(t_1, Coordinate())
    >>> t_110 = t._add_child(t_11, Coordinate())
    >>> t_111 = t._add_child(t_11, Coordinate())
    >>> t_112 = t._add_child(t_11, Coordinate())
    >>> t_1120 = t._add_child(t_112, Coordinate())
    >>> t_1121 = t._add_child(t_112, Coordinate())
    >>> t_1122 = t._add_child(t_112, Coordinate())
    >>> t_1123 = t._add_child(t_112, Coordinate())
    >>> t_30 = t._add_child(t_3, Coordinate())
    >>> t_31 = t._add_child(t_3, Coordinate())
    >>> t_32 = t._add_child(t_3, Coordinate())
    >>> general_tree_inorder_draw(t)
       0   1   2   3   4   5   6   7   8   9  10  11  12  13  14  15  16
    0                                              O
    1  X       O                                       X       O
    2      X           O                                   X       X   X
    3              X       X           O
    4                          X   X       X   X
    """

def general_tree_inorder_draw(t):
    GeneralTreeLayout(t).execute()
    draw(t)

"""
   0   1   2   3   4   5   6   7   8   9  10  11  12  13  14  15  16  17
0                                                O
1   X       O                                        X       O    
2       X           O                                    X       X   X
3               X       X           O
4                           X   X       X    X
"""


# C-8.55
"""
Exercise P-4.27 described the walk function of the os module. This function performs a traversal of the implicit tree 
represented by the file system. Read the formal documentation for the function, and in partiuclar its use of an optional
Boolean parameter named topdown. Describe how its behaviour relates to tree traversal algorithms described in this 
chapter.
"""

# https://docs.python.org/3/library/os.html

# When topdown is set to true, the return value for a directory is generated before the return value for any of its
# subdirectories.

# When topdown is set to false, the return value for a directory is generated after all the return values of its
# subdirectories.

# This is akin to doing a preorder traversal when topdown is set to True, and doing a postorder traversal when
# topdown is set to False.

# C-8.56
"""
The indented parenthetic representation of a tree T is a variation of the parenthetic representation of T (see
Code Fragment 8.25) that uses indentation and line breaks as illustrated in Figure 8.24. Give an algorithm that prints
this representation of a tree.
"""

class IndentedParentheticRepresentation(EulerTour):
    def _hook_previsit(self, p, d, path):
        statement = ''
        statement += ' '*2*d
        statement += p.element()
        if not self._tree.is_leaf(p):
            statement += ' ('
        print(statement)

    def _hook_postvisit(self, p, d, path, results):
        if not self._tree.is_leaf(p):
            statement = ' '*2*d + ')'
            print(statement)

def indent_parenthetic_test():
    """
    >>> t = TreeWithChildren()
    >>> t_root = t._add_root("Sales")
    >>> t_0 = t._add_child(t_root, "Domestic")
    >>> t_1 = t._add_child(t_root, "International")
    >>> t_10 = t._add_child(t_1, "Canada")
    >>> t_11 = t._add_child(t_1, "S. America")
    >>> t_12 = t._add_child(t_1, "Overseas")
    >>> t_120 = t._add_child(t_12, "Africa")
    >>> t_121 = t._add_child(t_12, "Europe")
    >>> t_122 = t._add_child(t_12, "Asia")
    >>> t_123 = t._add_child(t_12, "Australia")
    >>> IndentedParentheticRepresentation(t).execute()
    Sales (
      Domestic
      International (
        Canada
        S. America
        Overseas (
          Africa
          Europe
          Asia
          Australia
        )
      )
    )
    """


# C-8.57
"""
Let T be a binary tree with n positions. Define a Roman position to be a position p in T, such that the number of 
descendants in p's left subtree differ from the number of descendants in p's right subtree by at most 5.

Describe a linear-time method for finding each position p of T, such that p is not a Roman position, but all of p's
descendants are Roman.
"""

# If p isn't Roman, that means the size of the left and right subtree differ by more than 5.
# If p is Roman, that means the size of the left and right subtree are somewhat equal (less than 5)

"""
Easy solution: Do an Euler tour of the tree. Bubble up the number of descendants of each subtree and compare.
Set has_roman_descendant to be True by default, and set it to false when it's no longer true.
Set is_roman to be something else. If is_roman is false and has_roman_descendant is true, then add it to a list. 
"""

class FindTheRomans(BinaryEulerTour):
    def _hook_previsit(self, p, d, path):
        # During the previsit, we don't actually do anything.
        pass

    def _hook_invisit(self, p, d, path):
        pass

    def _hook_postvisit(self, p, d, path, results):
        # We can return both the boolean value of it being Roman, and whether it has Roman descendants, and
        # the number of descendants.
        no_of_descendants = 0
        is_roman = False
        are_all_descendants_roman = False
        is_leaf_node = results[0] is None and results[1] is None
        if is_leaf_node:
            no_of_descendants = 1  # just the node itself
            is_roman = True
            are_all_descendants_roman = True
        else:
            left_node_descendants = 0 if results[0] is None else results[0][0]
            left_node_is_roman = True if results[0] is None else results[0][1]
            left_node_descendants_are_all_roman = True if results[0] is None else results[0][2]
            right_node_descendants = 0 if results[1] is None else results[1][0]
            right_node_is_roman = True if results[1] is None else results[1][1]
            right_node_descendants_are_all_roman = True if results[1] is None else results[1][2]

            if abs(left_node_descendants - right_node_descendants) <= 5:
                is_roman = True
            if left_node_descendants_are_all_roman and right_node_descendants_are_all_roman and left_node_is_roman and right_node_is_roman:
                are_all_descendants_roman = True
            no_of_descendants = 1 + left_node_descendants + right_node_descendants
        if not is_roman and are_all_descendants_roman:
            print(f'{p.element()} is non-Roman with all Roman descendants. It has {left_node_descendants} left descendants and {right_node_descendants} right descendants.')
        return (no_of_descendants, is_roman, are_all_descendants_roman)


"""
                          A
                B                 C
            D       E           F
        G     H       I
      J  K   L M
    N  

B will be the only non-Roman position with all Roman descendants.
"""

"""
Array representation index
                          0
                1                 2
            3       4           5
        7     8       10
    15   16  17 18
   31  
"""




def roman_test():
    """
    >>> array_representation = [None]*32
    >>> letter = ord('A')
    >>> indexes = (0, 1, 2, 3, 4, 5, 7, 8, 10, 15, 16, 17, 18, 31)
    >>> for index in indexes:
    ...   array_representation[index] = chr(letter)
    ...   letter += 1
    >>> t =  array_to_linked_binary_tree(array_representation)
    >>> _ = FindTheRomans(t).execute()
    B is non-Roman with all Roman descendants. It has 8 left descendants and 2 right descendants.
    """
    pass

# C-8.58
"""
Let T be a tree with n positions. Define the lowest common ancestor (LCA) between two positions p and q as the lowest
position in T that has both p and q as descendants (where we allow a position to be a descendant of itself). Given two
positions p and q, describe an efficient algorithm for finding the LCA of p and q. What is the running time of your
algorithm?
"""

def get_ancestors(T, p):
    ancestors = []
    node = p
    while node is not None:
        ancestors.append(node)
        node = T.parent(node)
    return ancestors

def lowest_common_ancestors(T, p, q):
    p_ancestors = get_ancestors(T, p)
    q_node = q
    while q_node is not None:
        if q_node in p_ancestors:
            return q_node
        q_node = T.parent(q_node)

"""
            1
        2         3
    4     5      6  10
         7 8      9    17
                 11
                12
               13
               
LCA between 13 and 6 is 6
LCA between 13 and 10 is 3 
LCA between 4 and 11 is 1
"""


def lowest_common_ancestor_test():
    """
    >>> l1 = LinkedBinaryTree2()
    >>> l1_root = l1._add_root(1)
    >>> l1_0 = l1._add_left(l1_root, 2)
    >>> l1_1 = l1._add_right(l1_root, 3)
    >>> l1_00 = l1._add_left(l1_0, 4)
    >>> l1_01 = l1._add_right(l1_0, 5)
    >>> l1_010 = l1._add_left(l1_01, 7)
    >>> l1_011 = l1._add_right(l1_01, 8)
    >>> l1_10 = l1._add_left(l1_1, 6)
    >>> l1_100 = l1._add_right(l1_10, 9)
    >>> l1_11 = l1._add_right(l1_1, 10)
    >>> l1_1000 = l1._add_left(l1_100, 11)
    >>> l1_10000 = l1._add_left(l1_1000, 12)
    >>> l1_100000 = l1._add_left(l1_10000, 13)
    >>> lowest_common_ancestors(l1, l1_100000, l1_10).element()
    6
    >>> lowest_common_ancestors(l1, l1_100000, l1_11).element()
    3
    >>> lowest_common_ancestors(l1, l1_00, l1_1000).element()
    1
    """



# The worst case running time of this algorithm is O(d(p) * d(q)) where d(p) and d(q) are the depths of p and q
# respectively.


# C-8.59
"""
Let T be a binary tree with n positions, and, for any positions p in T, let d_p denote the dpeth of p in T. The distance
between p and q in T is d_p + d_q - 2d_a, where a is the lowest common ancestor (LCA) of p and q. 

The diameter of T is the maximum distance between two positions in T. Describe an efficient algorithm for finding the
diameter of T. What is the running time of your algorithm?
"""

# The diameter of a tree is the largest of the following quantities:
    # The diameter of T's left subtree
    # The diameter of T's right subtree
    # the longest path between leaves that goes through the root of T.

class Height:
    def __init__(self):
        self.h = 0


def diameter(T, p=-1, height=Height()):
    if T.root() is None:
        return 0
    if p == -1:
        p = T.root()

    left_height = Height()
    right_height = Height()

    left_subtree_diameter = diameter(T, T.left(p), left_height) if T.left(p) else 0
    right_subtree_diameter = diameter(T, T.right(p), right_height) if T.right(p) else 0

    height.h = max(left_height.h, right_height.h) + 1

    return max(left_height.h + right_height.h, max(left_subtree_diameter, right_subtree_diameter))


def diameter_test():
    """
    >>> l1 = LinkedBinaryTree2()
    >>> l1_root = l1._add_root(1)
    >>> l1_0 = l1._add_left(l1_root, 2)
    >>> l1_1 = l1._add_right(l1_root, 3)
    >>> l1_00 = l1._add_left(l1_0, 4)
    >>> l1_01 = l1._add_right(l1_0, 5)
    >>> l1_010 = l1._add_left(l1_01, 7)
    >>> l1_011 = l1._add_right(l1_01, 8)
    >>> l1_10 = l1._add_left(l1_1, 6)
    >>> l1_100 = l1._add_right(l1_10, 9)
    >>> l1_11 = l1._add_right(l1_1, 10)
    >>> l1_1000 = l1._add_left(l1_100, 11)
    >>> l1_10000 = l1._add_left(l1_1000, 12)
    >>> l1_100000 = l1._add_left(l1_10000, 13)
    >>> diameter(l1)
    9
    """
    pass



#C-8.60
"""
Suppose each position of a binary tree T is labelled with its value f(p) in a level numbering of T. Design a fast
method for determining f(a) for the lowest common ancestor (LCA), a, of two positions p and q in T, given f(p)
and f(q). You do not need to find position a, just value f(a)
"""

# Position 97 and 42
# floor((97-1)/2) = 48
# floor((48-1)/2) = 23
# floor((23-1)/2) = 11
# floor((11-1)/2) = 5
# floor((5-1)/2) = 2
# floor((2-1)/2) = 0

# floor((42-1)/2) = 20
# floor((20-1)/2) = 9
# floor((9-1)/2) = 4
# floor((4-1)/2) = 1
# floor((1-1)/2) = 0



def find_lowest_common_ancestor(p, q):
    # You would need to check first if they are in the same tree. But I won't be doing that here.
    if p == q:
        return p
    elif p == 0 or q == 0:
        return 0

    if p > q:
        return find_lowest_common_ancestor((p-1)//2, q)
    else:
        return find_lowest_common_ancestor(p, (q-1)//2)


def lca_test():
    """
    >>> find_lowest_common_ancestor(97, 42)
    0
    >>> find_lowest_common_ancestor(13, 14)
    6
    >>> find_lowest_common_ancestor(13, 28)
    13
    """
    pass


# C-8.61
"""
Give an alternative implementation of the build_expression_tree method of the ExpressionTree class that relies on
recursion to perform an implicit Euler tour of the tree that is being built.
"""

# Build expression tree:
    # Start with an empty stack
    # For t in tokens (tokens is a string of all the expressions):
        # If t in +-x*
            # Push expression onto the stack.
        # Else If t is not in the above, and also not parenthesis
            # Push onto the stack as an instance of the ExpressionTree class
        # Else If t is a closing parenthesis
            # Do 3 pops
                # First pop is the right subtree
                # Second pop is the operator
                # Third pop is the left subtree
            # Push back onto stack as an instance of an Expression tree
        # Opening parenthesis are ignored
    # Return by popping the one remaining element in the stack
        # We have only element in the stack because the closing parenthesis if statement combines them all into one

"""
                /
        x               +
    +       4       -       2
3       1       9       5
"""


def _max_index_of_tree(T):
    return len(T) - 1


def _expand_tree_to_cursor(T, cursor):
    # Say you want to go up to cursor 5, but have a tree the size of 1 (a single "None")
    # Cursor up to 5 means we need a size of 6.  Size+1 in other words.
    # How do we get a size of 1 to a size of 6? By adding 5 more nones.
    desired_size = cursor + 1
    size_increase = desired_size - len(T)
    if size_increase > 0:
        T.extend([None] * size_increase)


# (((3+1)x4)/((9-5)+2))


"""
                /
        X               +
    +       4       -       2
3       1       9       5

"""

class Index():
    def __init__(self):
        self.i = 0

    def __repr__(self):
        return f'{self.i}'

    def value(self):
        return self.i

    def increase(self):
        self.i += 1


def build_expression_tree2(expression, tree=None, i=0, stack=None):
    # (((3+1)*4)/((9-5)+2))
    # (a+(b+c))
    if i == 0:
        i = Index()
    if i.value() >= len(expression):
        return tree


    if stack is None:
        stack = []

    if expression[i.value()] == '(':
        i.increase()
        left_subtree = build_expression_tree2(expression, tree, i, stack)  # might return an ExpressionTree or tuple of (operator, left, right)
        if isinstance(left_subtree, ExpressionTree):
            subtree = left_subtree
        else:
            subtree = ExpressionTree(*left_subtree)

        if i.value() <= len(expression):
            stack.append(subtree)
            right_subtree = build_expression_tree2(expression, tree, i, stack) # might return an ExpressionTree or tuple of (operator, left, right)
            if isinstance(right_subtree, ExpressionTree):
                subtree = right_subtree
            elif right_subtree is not None:
                subtree = ExpressionTree(*right_subtree)
        return subtree
    elif expression[i.value()] in '+-*x/':
        operator = expression[i.value()]
        left = stack.pop()
        i.increase()
        right = build_expression_tree2(expression, tree, i, stack)
        return (operator, left, right)
    elif expression[i.value()] in ')':
        i.increase()
        return stack.pop()
    elif expression[i.value()] not in '()':
        # We're at a. So far we have ExpressionTree(build_expression_tree(expression, tree, i))
        stack.append(ExpressionTree(expression[i.value()]))
        i.increase()
        return build_expression_tree2(expression, tree, i, stack)


def test_expression_tree():
    """
    >>> expression_tree = build_expression_tree2('(((3+1)x4)/((9-5)+2))')
    >>> print(expression_tree)
    (((3+1)x4)/((9-5)+2))
    """
    pass


# C-8.62
"""
Note that the build_expression_tree function of the ExpressionTree class is written in such a way that a leaf token
can be any string; for example, it parses the expression '(a*(b+c))'. However, within the evaluate method, an error would
occur when attempting to convert a leaf token to a number. Modify the evaluate method to accept an optional Python
dictionary that can be used to map such string variables to numeric values, with a syntax such as T.evaluate({'a': 3,
'b':1, 'c':5}). In this way, the same algebraic expression can be evaluated using different values.
"""

class ExpressionTreeAlgebaricEvaluation(ExpressionTree):
    def evaluate_algebraically(self, values=None):
        return self._evaluate_recur_algebraically(self.root(), values)

    def _evaluate_recur_algebraically(self, p, values):
        def _evaluate_recur(self, p):
            """Return the numeric result of subtree rooted at p."""
            # if p is in values, replace p with the value.
            if p.element() in values:
                p._element = values[p.element()]
            if self.is_leaf(p):
                return float(p.element())  # we assume element is numeric
            else:
                op = p.element()
                left_val = self._evaluate_recur(self.left(p))
                right_val = self._evaluate_recur(self.right(p))
                if op == '+':
                    return left_val + right_val
                elif op == '-':
                    return left_val - right_val
                elif op == '/':
                    return left_val / right_val
                else:  # treat 'x' or '*' as multiplication
                    return left_val * right_val

# Created new class to demonstrate on here (__file__ = c.py), but modified the original ExpressionTree class as well.


"""
    +
a       +
       b  c
"""


"""
        N
    +
a       +
       b c
"""

def algebraic_evaluate_test():
    """
    >>> tree = build_expression_tree2('(a+(b+c))')
    >>> tree.evaluate({'a': 3, 'b': 1, 'c': 5})
    9.0
    >>> tree2 = build_expression_tree2('(a*((2*(b+5))-3))')
    >>> tree2.evaluate({'a': 4, 'b': 5})
    68.0
    """
    pass


# C-8.63
"""
Implement a postfix method of the ExpressionTree class that produces the postfix notation for the given expression.
"""

class ExpressionTreePostfix(ExpressionTree):
    def postfix(self):
        postfix_string = ''
        for p in self.postorder():
            postfix_string += f'{p.element()} '
        postfix_string.strip()
        print(postfix_string)

"""
            /
    *            4
  +    -
 5 2  8 3
"""


def postfix_test():
    """
    >>> tree = build_expression_tree2("(((5+2)*(8-3))/4)")
    >>> print(tree)
    (((5+2)*(8-3))/4)
    >>> tree.postfix()
    5 2 + 8 3 - * 4 /
    """
    pass
