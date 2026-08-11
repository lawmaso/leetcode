from __future__ import annotations

class TreeNode:
    val: int
    left: TreeNode | None = None
    right: TreeNode | None = None

    def __init__(self, val: int = 0):
        self.val = val

class Solution:
    """
    Given the roots of two binary trees p and q, write a function to check if they are the same or not.

    Two binary trees are considered the same if they are structurally identical, and the nodes have the same value.
    """

    def isSameTree(self, p: TreeNode | None, q: TreeNode | None) -> bool:
        """
        Recursive DFS

        Base case(s): one is null while the other isn't; false
                      values aren't equivalent; false
                      both null; true

        Recursive case: continue on children structurally

        dfs(p.left, q.left) and dfs(p.right, q.right)

        T: O(n)
        S: O(h)
        """
        if not p and not q: return True
        elif not p:         return False
        elif not q:         return False

        return all([
            p.val == q.val,
            self.isSameTree(p.left, q.left),
            self.isSameTree(p.right, q.right)
        ])

    def isSameTree(self, p: TreeNode | None, q: TreeNode | None) -> bool:
        """
        Approach: iterative BFS

        Queue with tuples of (left, right), initially append
        (p, q) to the queue

        At each iteration, check that left and right are valid and 
        their values match

        Any mismatch: not the same tree

        After BFS finishes, result is always true since checks passes
        """
        from collections import deque

        q = deque([(p, q)])
        while q:
            l, r = q.popleft()

            # continue bfs if nodes are null
            if not l and not r:
                continue

            # structural/value mismatch
            if not l or not r or l.val != r.val:
                return False

            q.append((l.left, r.left))
            q.append((l.right, r.right))

        return True
