"""
Given a reference of a node in a connected undirected graph.

Return a deep copy (clone) of the graph.

Each node in the graph contains a value (int) and a list (List[Node]) of its neighbors.

class Node {
    public int val;
    public List<Node> neighbors;
}

Test case format:

For simplicity, each node's value is the same as the node's index (1-indexed).
For example, the first node with val == 1, the second node with val == 2, and so on.
The graph is represented in the test case using an adjacency list.

An adjacency list is a collection of unordered lists used to represent a finite graph.
Each list describes the set of neighbors of a node in the graph.

The given node will always be the first node with val = 1.
You must return the copy of the given node as a reference to the cloned graph.
"""

from __future__ import annotations
class Node:
    val: int
    neighbors: list[Node] | None

    def __init__(self, val: int = 0, neighbors: list[Node] | None = None):
        self.val = val
        self.neighbors = neighbors if neighbors else None

class Solution:
    def cloneGraph(self, node: Node | None) -> Node | None:
        """
        Approach: BFS + hash map

        The hash map will map original nodes (or the unique values)
        to its deep copy in the new list

        We'll have to track which nodes we've seen since we can
        get stuck in an infinite loop since the graph is undirected

        T: O(n) [BFS]
        S: O(n) [hash map]
        """
        from collections import defaultdict, deque

        if not node:
            return None

        copy = defaultdict(Node)
        q = deque([node])

        while q:
            original = q.popleft()
            dupe = copy[original]; dupe.val = original.val

            for nei in original.neighbors:
                nei_processed = nei in copy
                nei_dupe = copy[nei]

                if not nei_processed:
                    q.append(nei)
                dupe.neighbors.append(nei_dupe)

        return copy[node]
