# C-8.31
"""
Define the internal path length, I(T), of a tree T to be the sum of the depths of all the internal positions in T.
Likewise, define the external path length, E(T), of a tree T to be the sum of the depths of all external positions in
T. Show that if T is a proper binary tree with n positions, then E(T) = I(T) + n - 1
"""

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
