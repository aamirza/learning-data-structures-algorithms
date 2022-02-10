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
