from __future__ import annotations

class ListNode:
    val: int
    next: ListNode | None

    def __init__(self, val: int = 0, next: ListNode | None = None):
        self.val = val
        self.next = next

class Solution:
    def brute_mergeTwoLists(self, list1: ListNode | None, list2: ListNode | None) -> ListNode | None:
        if not list1:
            return list2
        if not list2:
            return list1

        nodes = []
        
        # append nodes based on value order
        l1, l2 = list1, list2
        while l1 and l2:
            if l1.val <= l2.val:
                nodes.append(l1)
                l1 = l1.next
            else:
                nodes.append(l2)
                l2 = l2.next

        # handle cases when other gets exhausted
        for head in [l1, l2]:
            while head:
                nodes.append(head)
                head = head.next

        # chain together the nodes
        for i in range(1, len(nodes)):
            nodes[i - 1].next = nodes[i]

        return nodes[0]

"""
brute force: add all nodes to a list in sorted order,
then splice them together by pointing them in sequential order
    i.e., i -> i + 1 -> ... -> n - 1

T: O(n)
S: O(n)
"""

