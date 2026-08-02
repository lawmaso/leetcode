"""
You are given two non-empty linked lists representing
two non-negative integers. The digits are stored in reverse
order, and each of their nodes contains a single digit. Add
the two numbers and return the sum as a linked list.

You may assume the two numbers do not contain any leading
zero, except the number 0 itself.
"""

from __future__ import annotations
class ListNode:
    val: int
    next: ListNode | None

    def __init__(self, val: int = 0, next: ListNode | None = None):
        self.val = val
        self.next = next

class Solution:
    def brute_addTwoNumbers(self, l1: ListNode | None, l2: ListNode | None) -> ListNode | None:
        v1 = v2 = 0

        p = 0  # current power
        curr = l1
        while curr:
            v1 += curr.val * (10 ** p)
            
            curr = curr.next
            p += 1

        p = 0
        curr = l2
        while curr:
            v2 += curr.val * (10 ** p)

            curr = curr.next
            p += 1

        total = v1 + v2
        if total == 0:
            return ListNode(val=0)

        sentinel = temp = ListNode()

        while total:
            temp.next = ListNode(val=(total % 10))  # get last digit
            temp = temp.next

            total //= 10

        return sentinel.next

    def addTwoNumbers(self, l1: ListNode | None, l2: ListNode | None) -> ListNode | None:
        sentinel = temp = ListNode()
        carry = 0

        # loop while we need to add a digit
        while l1 or l2 or carry:
            v1 = l1.val if l1 else 0
            v2 = l2.val if l2 else 0
            
            total = v1 + v2 + carry

            temp.next = ListNode(val=(total % 10))  # get last digit
            carry = total // 10                     # carry over (if any)

            temp = temp.next
            if l1: l1 = l1.next
            if l2: l2 = l2.next

        # return newly formed list
        return sentinel.next

"""
l1 = [2,4,3], l2 = [5,6,4]

brute: actual sum -> list

 243
+564
----
 807

t.next = ListNode(val=(n % 10))
t = t.next
n //= 10

T: O(n1 + n2)
S: O(n1 + n2)
"""

"""
optimal: one-pass across both

T: O(n1 + n2)
S: O(n1 + n2)
"""

