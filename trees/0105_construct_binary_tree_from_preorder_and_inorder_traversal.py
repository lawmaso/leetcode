from __future__ import annotations

class TreeNode:
    val: int
    left: TreeNode | None = None
    right: TreeNode | None = None

    def __init__(self, val: int = 0):
        self.val = val

class Solution:
    """
    You are given two integer arrays preorder and inorder.

    preorder is the preorder traversal of a binary tree
    inorder is the inorder traversal of the same tree
    Both arrays are of the same size and consist of unique values.

    Rebuild the binary tree from the preorder and inorder traversals and return its root.

    ex1:

    Input: preorder = [3,9,20,15,7], inorder = [9,3,15,20,7]
    Output: [3,9,20,null,null,15,7]
    """

    def buildTree(self, preorder: list[int], inorder: list[int]) -> TreeNode | None:
        """
        preorder: 
            3; then construction becomes ambiguous

            look for 3 in inorder, then:
                all nodes left are in the left subtree: [9]
                all nodes right are in the right subtree: [15, 20, 7]
        
                maybe some sort of pointers

            p=9, i=9

                3
            9       20
                  15   7

            p=20; [15, 20, 7]
                20
            15      7

        start pre at index 0 [start at root]
        look for that node in inorder

        i=0 [preorder index]
        j=1 [inorder index]

        node = TreeNode(val=3)
        left = dfs(i + 1)
        right = dfs()

        [9, 3, 15, 20, 7]
            ^
        
        pre += 1; preorder[pre] = 9
        continue looking for preorder[pre] in inorder

        [9, 3, 15, 20, 7]
         ^
        
        once preorder[pre] == inorder[ino], construct node

        dfs further

        T: O(n^2)               [indexing into inorder at each node]
        S: O(n^2 + h) = O(n^2)  [slicing]
        """
        if not all([preorder, inorder]):
            return None

        root_val = preorder[0]
        mid = inorder.index(root_val)

        # root node
        root = TreeNode(root_val)

        # child subtrees
        root.left = self.buildTree(preorder[1:mid + 1], inorder[:mid])
        root.right = self.buildTree(preorder[mid + 1:], inorder[mid + 1:])

        return root

    def buildTree(self, preorder: list[int], inorder: list[int]) -> TreeNode | None:
        """
        Optimal: DFS w/ hash map

        Recursive dfs with hash map of values
        to indices for faster lookups into inorder

        T: O(n)
        S: O(n)
        """
        n = len(preorder)
        index = {v: i for i, v in enumerate(inorder)}  # index[v] = index of v in inorder

        self.pre = 0  # start at root node
        def dfs(l: int, r: int) -> TreeNode | None:
            if l > r:
                return None

            root_val = preorder[self.pre]
            mid = index[root_val]
            self.pre += 1

            root = TreeNode(val=root_val)
            root.left = dfs(l, mid - 1)
            root.right = dfs(mid + 1, r)

            return root

        return dfs(0, n - 1)

"""
Preorder: root, left, right
Inorder:  left, root, right

root_val = preorder[p]
index = inorder[root_val]
    left of index  = left subtree of root
    right of index = right subtree of root
"""
