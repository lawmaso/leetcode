from __future__ import annotations

class TreeNode:
    val: int
    left: TreeNode | None = None
    right: TreeNode | None = None

    def __init__(self, val: int = 0):
        self.val = val

class Solution:
    """
    Given two integer arrays inorder and postorder
    where inorder is the inorder traversal of a
    binary tree and postorder is the postorder traversal
    of the same tree, construct and return the binary tree.

    ex1:
    inorder = [9,3,15,20,7], postorder = [9,15,7,20,3]

            3
        9      20
             15   7
    """

    def buildTree(self, inorder: list[int], postorder: list[int]) -> TreeNode | None:
        """
        inorder:   left, curr, right
        postorder: left, right, curr
            reversed: curr, right, left
            
        inorder:         left, curr, right
        postorder[::-1]: curr, right, left

        approach: reverse postorder so earlier nodes come
        first in out dfs

        then use inorder to recursively construct the left and right
        subtrees to add to the current node
        """
        if not all([inorder, postorder]):
            return None

        n = len(inorder)
        index = {v: i for i, v in enumerate(inorder)}
        p = n - 1

        def dfs(l: int, r: int) -> TreeNode | None:
            nonlocal p

            if l > r:
                return None

            val = postorder[p]; p -= 1
            mid = index[val]

            root = TreeNode(val=val)

            # important: build right first since postorder
            # reversed has the ordering: curr, right, left
            # this updates nonlocal p properly
            root.right = dfs(mid + 1, r)
            root.left = dfs(l, mid - 1)

            return root

        return dfs(0, n - 1)
