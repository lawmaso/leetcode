from __future__ import annotations

"""
Given a binary tree, determine if it is height-balanced.
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
    def old_isBalanced(self, root: TreeNode | None) -> bool:
        """
        want children heights to never diff by more than 1

        want abs(lh - rh) <= 1

        bottom-up augmented dfs that returns
        tuple of (valid: bool, height: int)

        T: O(n)
        S: O(h)
        """
        def dfs(node: TreeNode | None) -> tuple[bool, int]:
            if not node:
                return True, 0

            left_valid, left_height = dfs(node.left)
            right_valid, right_height = dfs(node.right)
            new_height = 1 + max(left_height, right_height)

            if not all([left_valid, right_valid]):
                return False, new_height

            # check if the subtree rooted at node is height-balanced
            diff = abs(right_height - left_height)
            return diff <= 1, new_height

        return dfs(root)[0]

    def isBalanced(self, root: TreeNode | None) -> bool:
        """
        to make the code less verbose, we can encode
        validity into the height itself as -1 since heights start at 0

        same time and space as the original solution
        """

        def dfs(node: TreeNode | None) -> int:
            if not node:
                return 0

            left_height = dfs(node.left)
            if left_height == -1:
                return left_height

            right_height = dfs(node.right)
            if right_height == -1:
                return right_height

            diff = abs(right_height - left_height)
            return 1 + max(left_height, right_height) if diff <= 1 else -1


        # if tree is balanced; all checks will pass and we'll
        # get returned a non-negative height
        return dfs(root) != -1

"""
ex1:

Input: root = [3,9,20,null,null,15,7]
Output: true

        3
    9       20
          15  7
"""

