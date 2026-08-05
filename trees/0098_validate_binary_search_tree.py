from __future__ import annotations

class TreeNode:
    val: int
    left: TreeNode | None = None
    right: TreeNode | None = None

    def __init__(self, val: int = 0):
        self.val = val

class Solution:
    """
    Given the root of a binary tree, determine if it is a valid binary search tree (BST).

    A valid BST is defined as follows:

    The left subtree of a node contains only nodes with keys strictly less than the node's key.
    The right subtree of a node contains only nodes with keys strictly greater than the node's key.
    Both the left and right subtrees must also be binary search trees.
    """

    def isValidBST(self, root: TreeNode | None) -> bool:
        """
        brute force: inorder traversal

        convert tree to list of values
        then check that it's increasing

        T: O(n)
        S: O(n + h) = O(n)
        """

        vals = []

        def dfs(node: TreeNode | None):
            if not node:
                return

            dfs(node.left)
            vals.append(node.val)
            dfs(node.right)

        dfs(root)
        return all(vals[i - 1] < vals[i] for i in range(1, len(vals)))

    def isValidBST(self, root: TreeNode | None) -> bool:
        """
        recursive dfs with bounds 
        
        after each node is processed, the value becomes
        the new boundary

        if left, val is the new upper bound
        if right, val is the new lower bound

        to validate, we just need to check all values
        are within the range (lo, hi)

        T: O(n)
        S: O(h)
        """

        def dfs(
            node: TreeNode | None,
            lo: float | int = float("-inf"),
            hi: float | int = float("inf")
        ) -> bool:
            if not node:
                return True

            return (
                lo < node.val < hi and
                dfs(node.left, lo, node.val) and
                dfs(node.right, node.val, hi)
            )

        return dfs(root)

"""
ex1:

[2, 1, 3]

        2
    1       3
[1,2,3]+ (pass)

ex2:

[5,1,4,null,null,3,6]

            5
        1       4
              3   6

[1,5,3,4,6]- (pass)
   |-|
"""

"""
ex1 [optimal]: [2,1,3]
        2
    1       3

2 in [-inf, inf]+
1 in [-inf, 2]+
3 in [2, inf]+

ex2 [optimal]: [5,1,4,null,null,3,6]
            5
        1       4
              3   6

5 in [-inf, inf]+
1 in [-inf, 5]+
4 in [5, inf]-  <-> invalidates entire tree
"""
