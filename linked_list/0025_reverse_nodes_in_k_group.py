from __future__ import annotations

class ListNode:
    val: int
    next: ListNode | None

    def __init__(self, val: int = 0, next: ListNode | None = None):
        self.val = val
        self.next = next

    def __str__(self) -> str:
        node_vals = []

        curr = self
        while curr:
            node_vals.append(str(curr.val))
            curr = curr.next

        return "[" + ",".join(node_vals) + "]"

class Solution:
    def reverseKGroup(self, head: ListNode | None, k: int) -> ListNode | None:
        """
        Brute force: flatten, reverse, connect

        T: O(n + (n // k) * k) = O(n)
        S: O(n)
        """
        if not head:
            return None

        nodes: list[ListNode] = []

        # build flattened list representation
        curr = head
        while curr:
            nodes.append(curr)
            curr = curr.next

        n = len(nodes)

        # reverse full k-groups
        for l in range(0, n, k):
            r = l + k - 1

            # not enough nodes to form k-group
            if r >= n:
                break

            while l < r:
                nodes[l], nodes[r] = nodes[r], nodes[l]
                l += 1
                r -= 1

        # update connections
        for i in range(1, n):
            nodes[i - 1].next = nodes[i]
        nodes[n - 1].next = None

        return nodes[0]

    def reverseKGroup(self, head: ListNode | None, k: int) -> ListNode | None:
        """
        Optimal approach: in-place reversal

        Reverse the k-group first. If:
            - Full k: append to ref
            - Non-full k: unreverse, append to ref

        T: O(n)
        S: O(1)
        """
        sentinel = temp = ListNode()

        curr = head
        while curr:
            prev = None
            new_tail = curr  # curr becomes the tail of the k-group

            iters = 0
            while curr and iters < k:
                next = curr.next
                curr.next = prev
                prev = curr
                curr = next

                iters += 1

            # [success] we reversed the k-group; add to result
            if iters >= k:
                temp.next = prev
                temp = new_tail
                continue

            # [fail] not enough nodes to form full k-group
            curr = prev
            prev = None

            # un-reverse the group we tried to reverse; add undo to result
            while curr:
                next = curr.next
                curr.next = prev
                prev = curr
                curr = next

            temp.next = prev
            break

        return sentinel.next

    def reverseKGroup(self, head: ListNode | None, k: int) -> ListNode | None:
        def _kth(curr: ListNode, k: int) -> ListNode | None:
            while curr and k > 0:
                curr = curr.next
                k -= 1
            return curr

        sentinel = group_prev = ListNode(next=head)

        while True:
            kth = _kth(group_prev, k)

            # not enough nodes to form k-group
            if not kth:
                break

            group_next = kth.next
            prev, curr = group_next, group_prev.next

            # reverse the k-group
            while curr != group_next:
                temp = curr.next
                curr.next = prev
                prev = curr
                curr = temp

            tail = group_prev.next  # kth became the tail of the k-group through reversal
            group_prev.next = prev  # prev is new head of the k-group
            group_prev = tail

        return sentinel.next

if __name__ == "__main__":
    soln = Solution()

    def build_list(start: int, total: int) -> ListNode | None:
        sentinel = prev = ListNode()

        for v in range(start, start + total):
            prev.next = ListNode(v)
            prev = prev.next

        return sentinel.next

    # test that non-k group isn't reversed
    head = build_list(1, 5)
    print(head)

    head = soln.reverseKGroup(head, 2)
    print(head, "\n")

    # # test that last k-group is reversed
    head = build_list(1, 6)
    print(head)

    head = soln.reverseKGroup(head, 2)
    print(head, "\n")

    head = build_list(1, 0)
    print(head)

    head = soln.reverseKGroup(head, 20)
    print(head, "\n")

    head = build_list(1, 6)
    print(head)

    head = soln.reverseKGroup(head, 6)
    print(head, "\n")
