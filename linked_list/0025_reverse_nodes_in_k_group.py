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
    print(head)
