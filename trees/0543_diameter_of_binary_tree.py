from __future__ import annotations

"""
Given the root of a binary tree, return the length of the diameter of the tree.

The diameter of a binary tree is the length of the longest path between any two nodes in a tree. This path may or may not pass through the root.

The length of a path between two nodes is represented by the number of edges between them.
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
    def diameterOfBinaryTree(self, root: TreeNode | None) -> int:
        diameter = 0

        def dfs(node: TreeNode | None) -> int:
            nonlocal diameter

            # base case; not an actual node
            if not node:
                return 0

            # get left and right heights
            left, right = dfs(node.left), dfs(node.right)
            
            # update result diameter
            diameter = max(diameter, left + right)

            # return new height for recursive case
            return 1 + max(left, right)

        dfs(root)
        return diameter

"""
ex1:

Input: root = [1,2,3,4,5]
Output: 3

        1
    2       3
  4   5

Explanation: 3 is the length of the path [4,2,1,3] or [5,2,1,3].
"""

"""
equivalent solution would be to maximize the
sum of left and right depths/heights

bottom-up dfs to get heights efficiently

T: O(n)  [visit all nodes once]
S: O(h)  [bounded between O(log(n)) and O(n); balanced v. unbalanced]
"""

