"""
You are given an array of k linked-lists lists, each
linked-list is sorted in ascending order.

Merge all the linked-lists into one
sorted linked-list and return it.
"""

from __future__ import annotations
class ListNode:
    val: int

    def __init__(self, val: int = -1, next: ListNode | None = None):
        self.val = val
        self.next = next

class Solution:
    def _merge(self, l1: ListNode | None, l2: ListNode | None) -> ListNode | None:
        sentinel = temp = ListNode()

        while l1 and l2:
            if l1.val <= l2.val:
                temp.next = l1
                l1 = l1.next
            else:
                temp.next = l2
                l2 = l2.next

            temp = temp.next

        # attach remaining nodes
        temp.next = l1 or l2

        return sentinel.next

    def mergeKLists(self, lists: list[ListNode | None]) -> ListNode | None:
        if not lists:
            return None

        base = lists[0]
        for i in range(1, len(lists)):
            base = self._merge(base, lists[i])

        return base

"""
brute force: merge 1-by 1

ex:
lists = [[1,4,5],[1,3,4],[2,6]]

1st: 1,1,3,4,4,5
2nd: 1,1,2,3,4,4,5,6

in general, say each list is length n

1st: (n) + n
2nd: (n + n) + n
3rd: (n + n + n) + n
...
(k - 1)th: (k-1)(n) + n = n[k-1 + 1] = n*k

taking the sum:
    sum [i=1, k-1] of [i*n + n] = sum [i=1, k-1] of [n(i + 1)]
    = n * sum[i=1, k-1] (i + 1)
    = n * [sum[i=1, k-1] [i] + (k-1)]
    = n * [(k-1)(k)/2 + (k-1)]
    = n(k-1) * [k/2 + 1]
   ~= n * k^2

guassian sum formula: sum[i=1,n] = n(n+1)/2

to actually implement this solution, define a helper to
merge the linked lists

T: O(n * k^2)
S: O(1) [in-place merges]
"""

