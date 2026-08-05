from __future__ import annotations

class TreeNode:
    val: int
    left: TreeNode | None = None
    right: TreeNode | None = None

    def __init__(self, val: int = 0):
        self.val = val


class Solution:
    """
    Given the roots of two binary trees root and subRoot,
    return true if there is a subtree of root with the same
    structure and node values of subRoot and false otherwise.

    A subtree of a binary tree tree is a tree that consists
    of a node in tree and all of this node's descendants. The
    tree tree could also be considered as a subtree of itself.
    """

    def _isSameTree(self, p: TreeNode | None, q: TreeNode | None) -> bool:
        if not p and not q:   return True
        elif not p or not q:  return False

        return (
            p.val == q.val and
            self._isSameTree(p.left, q.left) and
            self._isSameTree(p.right, q.right)
        )

    def isSubtree(self, root: TreeNode, subRoot: TreeNode) -> bool:
        def dfs(node: TreeNode) -> bool:
            if not node:
                return False

            if node.val == subRoot.val and self._isSameTree(node, subRoot):
                return True

            return dfs(node.left) or dfs(node.right)

        return dfs(root)

"""
ex1:

Input: root = [3,4,5,1,2], subRoot = [4,1,2]
Output: true

        3
    4       5
1       2

dfs when the value in root matches subRoot, then
just check that they are the same tree

if not, continue searching the main tree, root

T: O(n)
S: O(h)
"""

