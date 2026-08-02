"""
Given the head of a linked list, remove
the nth node from the end of the list and
return its head.
"""

from __future__ import annotations
class ListNode:
    val: int
    next: ListNode | None

    def __init__(self, val: int = 0, next: ListNode | None = None):
        self.val = val
        self.next = next

class Solution:
    def brute_removeNthFromEnd(self, head: ListNode | None, n: int) -> ListNode | None:
        nodes = [ListNode(next=head)]  # sentinel at index 0

        curr = head
        while curr:
            nodes.append(curr)
            curr = curr.next

        i = len(nodes) - n
        nodes[i - 1].next = nodes[i + 1] if i + 1 < len(nodes) else None

        return nodes[0].next

"""
brute force: convert nodes to list form, and
rechain at the pivot

edge case: nth node is n, so the list won't have
a left node to chain

so add a sentinel at the front to make indexing cleaner

ex:
Input: head = [1,2,3,4,5], n = 2
Output: [1,2,3,5]

nodes = [x, 1, 2, 3, 4, 5]
6-2 = 4

ex: [1, 2]

nodes = [x, 1, 2], n=1
3-1 = 2

so nodes[i + 1] can be out of bounds

ex: [1], n=1

[x, 1]
i = 2-1 = 1
nodes[0].next = None since i + 1 >= len(nodes)
+

ex: [1, 2, 3], n=3

[x, 1, 2, 3]
i = 4-3 = 1
x.next = 2

x -> 2 -> 3
returns x.next
+

T: O(n)
S: O(n)
"""

