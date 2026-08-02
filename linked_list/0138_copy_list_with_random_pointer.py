"""
A linked list of length n is given such that each node
contains an additional random pointer, which could point
to any node in the list, or null.

Construct a deep copy of the list. The deep copy should
consist of exactly n brand new nodes, where each new node
has its value set to the value of its corresponding original
node. Both the next and random pointer of the new nodes should
point to new nodes in the copied list such that the pointers
in the original list and copied list represent the same list
state. None of the pointers in the new list should point to
nodes in the original list.

For example, if there are two nodes X and Y in the original
list, where X.random --> Y, then for the corresponding two nodes
x and y in the copied list, x.random --> y.

Return the head of the copied linked list.

The linked list is represented in the input/output as a
list of n nodes. Each node is represented as a pair of [val, random_index] where:

val: an integer representing Node.val
random_index: the index of the node (range from 0 to n-1) that
the random pointer points to, or null if it does not point to any node.

Your code will only be given the head of the original linked list.
"""

from __future__ import annotations

class Node:
    x: int
    next: Node | None
    random: Node | None

    def __init__(self, x: int, next: Node | None = None, random: Node | None = None):
        self.x = int(x)
        self.next = next
        self.random = random

class Solution:
    def copyRandomList(self, head: Node | None) -> Node | None:
        map = dict()      # original: copy
        map[None] = None  # map None to itself in case next or random is None

        curr = head
        while curr:
            next, random = curr.next, curr.random

            copy_curr   = map.setdefault(curr,   ListNode(curr.val))
            copy_next   = map.setdefault(next,   ListNode(next.val) if next else None)
            copy_random = map.setdefault(random, ListNode(random.val) if random else None)

            # chain curr to next and random
            copy_curr.next = copy_next
            copy_curr.random = copy_random

            curr = curr.next

        return map[head]

"""
map original nodes to copies

forward scan the original linked list

    copy_curr   = map[curr]
    copy_next   = map[curr.next]
    copy_random = map[curr.random]

    these can potentially not exist yet in the map, so handle
    the cases separately with

    copy_curr = map.setdefault(curr, ListNode())
    ...

ex:
    head = [[1,1],[2,1]]

    map = {
        None: None,
        1: copy_1,
        2: copy_2
    }

    curr = 1
        next, random = 2, 2

        copy_curr   = copy_1
        copy_next   = copy_2
        copy_random = copy_2

        copy_curr.next = copy_next
        copy_curr.random = copy_random

    curr = 2
        next, random = None, 2

        copy_curr   = copy_2
        copy_next   = None
        copy_random = copy_2

        cc.next = None
        cc.random = copy_2

    curr = None
    return ma[head]
+ looks like it passes

T: O(n)
S: O(n)
"""

