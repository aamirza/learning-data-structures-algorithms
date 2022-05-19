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

# In this, for every new level of depth added (d+1), D loses d-1, but gains 2d. For every new level of depth added
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
