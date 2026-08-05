from __future__ import annotations

class TreeNode:
    val: int
    left: TreeNode | None = None
    right: TreeNode | None = None

    def __init__(self, val: int = 0):
        self.val = val

class Solution:
    """
    Given the root of a binary tree,
    imagine yourself standing on the
    right side of it, return the values
    of the nodes you can see ordered from
    top to bottom.

    ex1:
    Input: root = [1,2,3,null,5,null,4]
    Output: [1,3,4]

            1
        2       3
           5       4

    [1, 3, 4]

    last node in each level
    """

    def rightSideView(self, root: TreeNode | None) -> list[int]:
        """
        iterative bfs

        append the value of the last
        node of the frontier

        from left to right, append non-null childnre
            append left child then right child to ensure
            ordering is respected

        T: O(n)
        S: O(n)
        """
        
        from collections import deque

        if not root:
            return []

        q = deque([root])
        res = []

        while q:
            n = len(q)

            for i in range(n):
                node = q.popleft()

                # append valid child nodes
                if node.left:  q.append(node.left)
                if node.right: q.append(node.right)


                # check if last value
                if i == n - 1:
                    res.append(node.val)

        return res

