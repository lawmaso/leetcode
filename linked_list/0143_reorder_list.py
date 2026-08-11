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
        """
        Brute force: list -> splice

        Append all nodes into a list [L0, L1, ... Ln]

        Utilize list to form the ordering L0, Ln, ...

        Then splice them together in one-pass

        return L0

        left and right pointers: l and r
            append l then r

        if l == r, append either just once and break

        T: O(n)
        S: O(n)
        """
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

    def reorderList(self, head: ListNode | None) -> None:
        """
        Optimal: in-place splicing

        1, 2, 3, 4

        Split from half so we have partitions starting
        from the head and tail, but reverse the right portion so
        Ln appears first, then Ln-1, ..., etc.

        slow=3
        fast=null

        1,2|3,4
        1,2|4,3
        1, 2
        4, 3

        1->4->2->3

        odd case: [1, 2, 3]

        slow=2
        fast=3
        1|2,3
        1|3,2

        1
        3,2

        Say we have left and right to represent the partitions

        left_next = left.next
        right_next = right.next

        left.next = right
        if not left_next: # shouldn't connect right to left_next
            break

        right.next = left_next

        # shift
        left = left_next
        right = right_next

        T: O(n)
        S: O(1)
        """
        if not head: return None

        prev = None
        slow = fast = head
        while fast and fast.next:
            prev = slow
            slow = slow.next
            fast = fast.next.next

        #   [1]
        # p s/f; p is None [edge case]
        if not prev:
            return head

        # disconnect to form partitions
        prev.next = None

        # reverse from slow
        prev = None
        curr = slow
        while curr:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp

        left = head
        right = prev

        # splice list together in L0 -> Ln, ...
        while left and right:
            next_left = left.next
            next_right = right.next

            left.next = right

            # no next left node; don't point right to it
            if not next_left:
                break
            
            right.next = next_left

            # continue loop
            left = next_left
            right = next_right

        return head

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
