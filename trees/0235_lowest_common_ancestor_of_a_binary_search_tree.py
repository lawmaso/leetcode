from __future__ import annotations

class TreeNode:
    val: int
    left: TreeNode | None = None
    right: TreeNode | None = None

    def __init__(self, val: int = 0):
        self.val = val

class Solution:
    """
    Given a binary search tree (BST), find
    the lowest common ancestor (LCA) node of
    two given nodes in the BST.

    According to the definition of LCA on
    Wikipedia: “The lowest common ancestor is defined
    between two nodes p and q as the lowest node in T
    that has both p and q as descendants (where we allow
    a node to be a descendant of itself).”
    """

    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        """
        Initial approach: create parent mapping

        Use the parent mapping to find the earliest common
        parent of p and q

        Relies on TreeNode being hashable into dict keys

        T: O(n)
        S: O(n + h) = O(n)
        """
        parent_map = dict()

        def build_parent_map(node: TreeNode | None, parent: TreeNode | None = None):
            nonlocal parent_map

            if not node:
                return

            parent_map[node] = parent
            build_parent_map(node.left, node)
            build_parent_map(node.right, node)

        build_parent_map(root)

        # parents seen from p or q
        seen = set()

        # start from either p or q
        curr = p
        while curr:
            seen.add(curr)
            curr = parent_map[curr]

        curr = q
        while curr:
            if curr in seen:
                return curr
            
            # NOTE: no need to add the node since p defines
            # possible ancestors
            curr = parent_map[curr]

        return None

    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        """
        Approach: iterative search for the pivot node

        Look for pivot node using BST property

        The LCA will be where the nodes split into different
        subtrees

        T: O(h)
        S: O(1)
        """
        vals = [p.val, q.val]
        mn, mx = min(vals), max(vals)

        curr = root
        while curr:
            # both in the right subtree
            if mn > curr.val:
                curr = curr.right
                continue
            # both in the left subtree
            elif mx < curr.val:
                curr = curr.left
                continue

            # mn <= curr.val and mx >= curr.val
            # i.e., curr is the pivot where they split
            # i.e., the lowest common ancestor of p and q
            return curr

        # no lca exists
        return None

"""
ex1:

Input: root = [6,2,8,0,4,7,9,null,null,3,5], p = 2, q = 8
Output: 6
Explanation: The LCA of nodes 2 and 8 is 6.

                6
            2       8
        0     4    7    9
             3 5
"""
