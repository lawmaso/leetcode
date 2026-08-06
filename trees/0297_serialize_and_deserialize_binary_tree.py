from __future__ import annotations

class TreeNode:
    val: int
    left: TreeNode | None = None
    right: TreeNode | None = None

    def __init__(self, val: int = 0):
        self.val = val

"""
Serialization is the process of converting
a data structure or object into a sequence
of bits so that it can be stored in a file
or memory buffer, or transmitted across a
network connection link to be reconstructed
later in the same or another computer environment.

Design an algorithm to serialize and deserialize
a binary tree. There is no restriction on how your
serialization/deserialization algorithm should work.
You just need to ensure that a binary tree can be
serialized to a string and this string can be
deserialized to the original tree structure.

Clarification: The input/output format is the
same as how LeetCode serializes a binary tree.
You do not necessarily need to follow this format,
so please be creative and come up with different
approaches yourself.
"""

class Codec:
    """
    Approach: preorder traversal with null markers
    to ensure determinism with child pointers

    T: O(n)
    S: O(n)
    """
    null: str

    def __init__(self, null: str = "*"):
        self.null = null

    def serialize(self, root: TreeNode | None) -> str:
        vals = []

        def dfs(node: TreeNode | None):
            if not node:
                vals.append(self.null)
                return

            vals.append(str(node.val))
            dfs(node.left)
            dfs(node.right)

        dfs(root)
        return ",".join(vals)
        

    def deserialize(self, data: str) -> TreeNode | None:
        """
        Approach: reconstruct the tree from
        the preorder traversal

        T: O(n)
        S: O(n)
        """
        vals = iter(data.split(","))

        def dfs() -> TreeNode | None:
            val = next(vals)

            if val == self.null:
                return None

            node = TreeNode(int(val))
            node.left = dfs()
            node.right = dfs()

            return node

        return dfs()


if __name__ == "__main__":
    soln = Codec()

    tree = TreeNode(val=0)
    tree.left = TreeNode(val=-1)
    tree.right = TreeNode(val=1)

    data = soln.serialize(tree)
    print(data)

    copy = soln.deserialize(data)

    assert copy.val == tree.val
    assert copy.left.val == tree.left.val
    assert copy.right.val == tree.right.val