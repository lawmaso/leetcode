"""
Given the root of a binary tree, return its maximum
depth.

A binary tree's maximum depth is the number of nodes
along the longest path from the root node down to the
farthest leaf node.
"""

"""
recursive bottom-up dfs

if node is null: return 0

return 1 + max(depth(left), depth(right))
    - include 1 for the current node (inclusive)
    - take max of either since we want to maximize

T: O(n) [visit each node]
S: O(h) [recursion stack; between O(log(n)) and O(n)]
"""

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
    def maxDepth(self, root: TreeNode | None) -> int:
        if not root:
            return 0

        return 1 + max(
            self.maxDepth(root.left),
            self.maxDepth(root.right)
        )

