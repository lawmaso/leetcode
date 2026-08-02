from __future__ import annotations

class ListNode:
    val: int
    next: ListNode | None

    def __init__(self, val: int = 0, next: ListNode | None = None):
        self.val = val
        self.next = next

class Solution:
    def brute_reverseList(self, head: ListNode | None) -> ListNode | None:
        values = []

        curr = head
        while curr:
            values.append(curr.val)
            curr = curr.next

        reverse = temp = ListNode()  # sentinel head
        for i in range(len(values) - 1, -1, -1):
            temp.next = ListNode(val=values[i])
            temp = temp.next

        return reverse.next


"""
brute force: append all values to a list, then
build out the new linked list starting from the back to the front

ex: empty list
curr = None; while curr never iterates
return reverse.next = None
+

ex: [1,2]
values = [1,2]

reverse -> 2 -> 1 -> None
return reverse.next = 2->1->None
+

T: O(n)
S: O(n)
"""

