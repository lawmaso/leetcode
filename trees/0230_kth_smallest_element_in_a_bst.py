from __future__ import annotations

class TreeNode:
    val: int
    left: TreeNode | None = None
    right: TreeNode | None = None

    def __init__(self, val: int = 0):
        self.val = val

class Solution:
    """
    Given the root of a binary search tree, and
    an integer k, return the kth smallest value
    (1-indexed) of all the values of the nodes in the tree.
    """

    def kthSmallest(self, root: TreeNode | None, k: int) -> int:
        """
        brute force: inorder dfs

        build out values list and just
        return vals[k - 1]

        T: O(n)
        S: O(n)
        """

        vals = []
        def dfs(node: TreeNode | None):
            if not node:
                return

            dfs(node.left)
            vals.append(node.val)
            dfs(node.right)

        dfs(root)
        return vals[k - 1]

"""
ex1 [brute]:

[3,1,4,null,2], k = 1

[1, 2, 3, 4]
returns 1 (pass+)
"""
