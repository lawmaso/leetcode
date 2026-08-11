from __future__ import annotations

class ListNode:
    val: int
    next: ListNode | None

    def __init__(self, v: int = 0, next: ListNode | None = None):
        self.val = v
        self.next = next

class Solution:
    def hasCycle(self, head: ListNode | None) -> bool:
        """
        Brute force: use set to track if a node was seen already

        This should work since if no cycle exists, then our iterations
        would just stop. and if a cycle exists, then our seen set would tell
        us, to which we can conclude a cycle exists

        Assumes we can hash list nodes

        T: O(n)
        S: O(n)
        """
        seen = set()  # nodes

        curr = head
        while curr:
            if curr in seen:
                return True
            seen.add(curr)
            curr = curr.next

        return False

    def hasCycle(self, head: ListNode | None) -> bool:
        """
        Optimal: utilize slow and fast pointers

        Since fast grows at twice the rate of slow, if a cycle exists,
        then fast will reach slow eventually

        Continue while fast and fast.next are non-null

        Update both accordingly:
            - slow = slow.next
            - fast = fast.next.next

        T: O(n)
        S: O(1)  [just pointers]
        """
        slow = fast = head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

            if slow == fast:
                return True

        return False
