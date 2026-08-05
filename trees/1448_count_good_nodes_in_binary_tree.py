from __future__ import annotations

class TreeNode:
    val: int
    left: TreeNode | None = None
    right: TreeNode | None = None

    def __init__(self, val: int = 0):
        self.val = val

class Solution:
    """
    Given a binary tree root, a node X in
    the tree is named good if in the path
    from root to X there are no nodes with a
    value greater than X.

    Return the number of good nodes in the binary
    tree.

    ex1:
    Input: root = [3,1,4,3,null,1,5]
    Output: 4

    Explanation: Nodes in blue are good.
    Root Node (3) is always a good node.
    Node 4 -> (3,4) is the maximum value in the path starting from the root.
    Node 5 -> (3,4,5) is the maximum value in the path
    Node 3 -> (3,1,3) is the maximum value in the path.
    """

    def goodNodes(self, root: TreeNode | None) -> int:
        """
        tree:
                3+
            1       4+
        3+         1  5+

        no nodes in the path greater than x
            -> for all n, n.val <= x

            so argmax of path <= x

        iterative bfs from the root

        keep track of the max, then check that the current node
        is <= that max
            if true, then increase good count
            else, skip

            in both cases, update max

        T: O(n)  [bfs]
        S: O(n)  [worst-case; last level ~= n/2 leaves]
        """

        from collections import deque

        if not root:
            return 0

        good_count = 0

        q = deque([(root, root.val)])  # (node, path_max)
        while q:
            node, path_max = q.popleft()

            if path_max <= node.val:
                good_count += 1

            path_max = max(path_max, node.val)

            if node.left:  q.append((node.left, path_max))
            if node.right: q.append((node.right, path_max))

        return good_count

"""
dry-run of ex1:

        3
    1       4
3          1  5

+: count as good node
-: exclude from count

q = [
    (3n, 3)+
    (1n, 3)-
    (4n, 4)+
    (3n, 3)+
    (1n, 4)-
    (5n, 4)+
]

res = 4; pass

ex2:
Input: [3,3,null,4,2]
Output: 3

        3
    3
4       2

q = [
    (3n, 3)+
    (3n, 3)+
    (4n, 3)+
    (2n, 3)-
]

res = 3; pass
"""
