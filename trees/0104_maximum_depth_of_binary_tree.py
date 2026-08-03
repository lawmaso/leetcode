from __future__ import annotations

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

class TreeNode:
    val: int
    left: TreeNode | None
    right: TreeNode | None

    def __init__(self, val: int = 0, left: TreeNode | None = None, right: TreeNode | None = None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def recursive_maxDepth(self, root: TreeNode | None) -> int:
        if not root:
            return 0

        return 1 + max(
            self.maxDepth(root.left),
            self.maxDepth(root.right)
        )

    def iterative_maxDepth(self, root: TreeNode | None) -> int:
        from collections import deque

        if not root:
            return 0

        self.res = 0  # store in the class
        
        q = deque([(root, 1)])
        while q:
            node, depth = q.popleft()

            # update best depth (if it applies)
            self.res = max(self.res, depth)

            # only append valid paths
            if node.left:  q.append((node.left, depth + 1))
            if node.right: q.append((node.right, depth + 1))

        return self.res


"""
iterative bfs

depth = 0

explore paths to leafs, keeping track
of current depth

maximize the depth to get the result

T: O(n)
S: O(n)
"""

