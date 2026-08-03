from __future__ import annotations

class TreeNode:
    val: int
    left: TreeNode | None
    right: TreeNode | None

    def __init__(self, val: int = 0, left: TreeNode | None = None, right: TreeNode | None = None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def invertTree(self, root: TreeNode | None) -> TreeNode | None:
        if not root:
            return None

        # propogate to children nodes
        left = self.invertTree(root.left)
        right = self.invertTree(root.right)

        # invert at this level
        root.left, root.right = right, left
        
        return root

"""
recursion: bottom-up dfs

    2
1       3

1/2: no children
at 2: root.left, root.right  root.right, root.left


T: O(n)  [each node visited once]
S: O(h)  [height of tree; between O(log(n)) and O(n)]
"""

