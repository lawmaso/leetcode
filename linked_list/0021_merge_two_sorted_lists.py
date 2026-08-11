from __future__ import annotations

class ListNode:
    val: int
    next: ListNode | None

    def __init__(self, val: int = 0, next: ListNode | None = None):
        self.val = val
        self.next = next

class Solution:
    def mergeTwoLists(self, list1: ListNode | None, list2: ListNode | None) -> ListNode | None:
        """
        Brute force: add all nodes to a list in sorted order,
        then splice them together by pointing them in sequential order
            i.e., i -> i + 1 -> ... -> n - 1

        T: O(n)
        S: O(n)
        """
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
    
    def mergeTwoLists(self, list1: ListNode | None, list2: ListNode | None) -> ListNode | None:
        """
        Optimal: in-place splicing

        Build out new list by comparing values at each point

        T: O(n)
        S: O(1)
        """
        if not list1: return list2
        if not list2: return list1

        sentinel = temp = ListNode()  # sentinel head
        l1, l2 = list1, list2

        while l1 and l2:
            if l1.val <= l2.val:
                temp.next = l1
                l1 = l1.next
            else:
                temp.next = l2
                l2 = l2.next

            # update temp to be last added node
            temp = temp.next
        
        # append remaining of non-exhausted list
        temp.next = l1 or l2

        # return newly formed list
        return sentinel.next
