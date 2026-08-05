from __future__ import annotations

class TreeNode:
    val: int
    left: TreeNode | None = None
    right: TreeNode | None = None

    def __init__(self, val: int = 0):
        self.val = val

class Solution:
    """
    Given the root of a binary search tree, and
    an integer k, return the kth smallest value
    (1-indexed) of all the values of the nodes in the tree.
    """

    def kthSmallest(self, root: TreeNode | None, k: int) -> int:
        """
        brute force: inorder dfs

        build out values list and just
        return vals[k - 1]

        T: O(n)
        S: O(n)
        """

        vals = []
        def dfs(node: TreeNode | None):
            if not node:
                return

            dfs(node.left)
            vals.append(node.val)
            dfs(node.right)

        dfs(root)
        return vals[k - 1]

    def kthSmallest(self, root: TreeNode | None, k: int) -> int:
        """
        optimal: prune the search tree based on k

        need to somehow get the sizes of the subtrees
            -> bottom-up dfs

            3
        1       4
          2
        
          
        2, k=1 -> 1, k=0; return 1
            
        so subtract 1 from k and check when it becomes 0
        -> k=0 implies we are at the kth node

        ex2:
        [5,3,6,2,4,null,null,1], k = 3

                    5
                  3   6
                2  4
               1

        1,k=3->2
        2,k=2->1
        3,k=1->0+ [found result]
        ...

        T: O(n)
        S: O(h)
        """

        def dfs(node: TreeNode | None) -> int:
            nonlocal k

            # base case
            if not node:
                return -1

            res = dfs(node.left)

            # found kth smallest in the left subtree
            if res != -1:
                return res

            # check if this node is the kth smallest
            k -= 1
            if k == 0:
                return node.val

            # kth smallest exists in the right subtre
            return dfs(node.right)

        return dfs(root)

"""
ex1 [brute]:

[3,1,4,null,2], k = 1

[1, 2, 3, 4]
returns 1 (pass+)
"""

"""
ex2 [optimal]:
[5,3,6,2,4,null,null,1], k = 6

            5
        3   6
      2  4
    1

1, k=6->5
2, k=4
3, k=3
4, k=2
5, k=1
6, k=0+ [result]

passes
"""
