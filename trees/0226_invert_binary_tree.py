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
    def recursive_invertTree(self, root: TreeNode | None) -> TreeNode | None:
        if not root:
            return None

        # propagate to children nodes
        left = self.invertTree(root.left)
        right = self.invertTree(root.right)

        # invert at this level
        root.left, root.right = right, left
        
        return root
    
    def iterative_invertTree(self, root: TreeNode | None) -> TreeNode | None:
        from collections import deque

        if not root:
            return None

        q = deque([root])
        while q:
            node = q.popleft()

            # swap children
            node.left, node.right = node.right, node.left

            # continue on non-null children
            if node.left:  q.append(node.left)
            if node.right: q.append(node.right)

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

"""
iterative: bfs

ex:
[2,1,3]

    2
1       3

queue = [(root, left, right)]
head, l, r = queue.popleft()

... [continue on children]

on second thought, we don't need the queue to have left and right
children as that's already a given inside of the node in each tuple
entry

T: O(n)  [visit each node]
S: O(n)  [queue length at last level ~= n/2]
"""

