from __future__ import annotations

class TreeNode:
    val: int
    left: TreeNode | None = None
    right: TreeNode | None = None

    def __init__(self, val: int = 0):
        self.val = val

class Solution:
    """
    Given the roots of two binary trees p and q, write a function to check if they are the same or not.

    Two binary trees are considered the same if they are structurally identical, and the nodes have the same value.
    """

    def isSameTree(self, p: TreeNode | None, q: TreeNode | None) -> bool:
        """
        recursion (dfs)

        base case(s): one is null while the other isn't; false
                      values aren't equivalent; false
                      both null; true

        recursive case: continue on children structurally

        dfs(p.left, q.left) and dfs(p.right, q.right)

        T: O(n)
        S: O(h)
        """
        
        if not p and not q: return True
        elif not p:         return False
        elif not q:         return False

        return all([
            p.val == q.val,
            self.isSameTree(p.left, q.left),
            self.isSameTree(p.right, q.right)
        ])

