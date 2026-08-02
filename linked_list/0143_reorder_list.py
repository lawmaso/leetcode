"""
You are given the head of a singly linked-list. The list can be represented as:

L0 → L1 → … → Ln - 1 → Ln
Reorder the list to be on the following form:

L0 → Ln → L1 → Ln - 1 → L2 → Ln - 2 → …
You may not modify the values in the list's nodes. Only nodes themselves may be changed.
"""

from __future__ import annotations
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reorderList(self, head: ListNode | None) -> None:
        if not head: return None

        nodes = []

        curr = head
        while curr:
            nodes.append(curr)
            curr = curr.next

        seq = []

        l, r = 0, len(nodes) - 1
        while l <= r:
            if l == r:
                seq.append(nodes[l])
                break

            seq.append(nodes[l])
            seq.append(nodes[r])

            l += 1
            r -= 1

        # splice together the list
        for i in range(1, len(seq)):
            seq[i - 1].next = seq[i]
        seq[-1].next = None  # remove old ref (since it's now the tail)

        return seq[0]  # == head

def create_linked_list(lst: list[int]) -> ListNode | None:
    if not lst:
        return None

    head = temp = ListNode(val=lst[0])
    for i in range(1, len(lst)):
        temp.next = ListNode(val=lst[i])
        temp = temp.next

    return head

if __name__ == "__main__":
    linked_list = create_linked_list([1, 2, 3, 4])
    
    soln = Solution()
    soln.reorderList(linked_list)

    curr = linked_list
    while curr:
        print(curr.val)
        curr = curr.next

"""
brute force

append all nodes into a list [L0, L1, ... Ln]

utilize list to form the ordering L0, Ln, ...

then splice them together in one-pass

return L0

left and right pointers: l and r
    append l then r

if l == r, append either just once and break

T: O(n)
S: O(n)
"""

