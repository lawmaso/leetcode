from __future__ import annotations

class ListNode:
    val: int
    next: ListNode | None

    def __init__(self, v: int = 0, next: ListNode | None = None):
        self.val = val
        self.next = next

class Solution:
    def brute_hasCycle(self, head: ListNode | None) -> bool:
        seen = set()  # nodes

        curr = head
        while curr:
            if curr in seen:
                return True
            seen.add(curr)
            curr = curr.next

        return False

    def hasCycle(self, head: ListNode | None) -> bool:
        slow = fast = head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

            if slow == fast:
                return True

        return False

"""
brute force: use set to track if a node was seen already

this should work since if no cycle exists, then our iterations
would just stop. and if a cycle exists, then our seen set would tell
us, to which we can conclude a cycle exists

assumes we can hash list nodes

T: O(n)
S: O(n)
"""

"""
optimal: utilize slow and fast pointers

since fast grows at twice the rate of slow, if a cycle exists,
then fast will reach slow eventually

continue while fast and fast.next are non-null
update both accordingly:
    - slow = slow.next
    - fast = fast.next.next

T: O(n)
S: O(1)  [just pointers]
"""

