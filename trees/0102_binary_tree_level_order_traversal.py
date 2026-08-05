from __future__ import annotations

class TreeNode:
    val: int
    left: TreeNode | None = None
    right: TreeNode | None = None

    def __init__(self, val: int = 0):
        self.val = val

class Solution:
    """
    Given the root of a binary tree, return 
    the level order traversal of its nodes'
    values. (i.e., from left to right, level by level).

    
    ex1:

    Input: root = [3,9,20,null,null,15,7]
    Output: [[3],[9,20],[15,7]]
    
            3
        9       20
              15  7

    [3] [9] [15, 7]

    ignore nulls
    """

    def levelOrder(self, root: TreeNode | None) -> list[list[int]]:
        """
        iterative bfs

        append the frontier of the queue
        at each iteration of the bfs

        T: O(n)
        S: O(n)
        """

        from collections import deque

        if not root:
            return []

        res = []
        q = deque([root])

        while q:
            frontier = []

            # get all nodes of the frontier
            for _ in range(len(q)):
                node = q.popleft()

                # add value to the frontier
                frontier.append(node.val)

                # append non-null nodes to the queue
                # NOTE: append left -> right to order levels
                if node.left:  q.append(node.left)
                if node.right: q.append(node.right)

            # after the frontier is collected, append to the result
            res.append(frontier)

        return res

