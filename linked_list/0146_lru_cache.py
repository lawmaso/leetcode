"""
Design a data structure that follows the constraints of a Least Recently Used (LRU) cache.

Implement the LRUCache class:

LRUCache(int capacity) Initialize the LRU cache with positive size capacity.
int get(int key) Return the value of the key if the key exists, otherwise return -1.
void put(int key, int value) Update the value of the key if the key exists.
Otherwise, add the key-value pair to the cache. If the number of keys exceeds the
capacity from this operation, evict the least recently used key.
The functions get and put must each run in O(1) average time complexity.
"""

from __future__ import annotations

class LRUNode:
    key: int
    val: int
    prev: LRUNode | None
    next: LRUNode | None

    def __init__(self, key: int = -1, val: int = -1):
        self.key = key
        self.val = val
        self.prev = self.next = None

class LRUCache:
    """
    Optimal: doubly linked list

    l - r (sentinel head and tail)
        left: lru
        right: mru
    Only allow <capacity> nodes between l and r

    On put: add just before mru
        if over capacity, pop the right of the lru node

    On get: check if the key is cached

    cache[int, LRUNode]

    Achieves O(1) per operation
    """
    capacity: int
    cache: dict[int, LRUNode]
    left: LRUNode
    right: LRUNode

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = dict()
        self.left = LRUNode()
        self.right = LRUNode()

        self.left.next = self.right
        self.right.prev = self.left

    def _evict(self, node: LRUNode):
        prev, next = node.prev, node.next
        prev.next = next
        next.prev = prev

    def _use(self, node: LRUNode):
        prev, next = self.right.prev, self.right
        prev.next = next.prev = node
        node.prev = prev
        node.next = next

    def get(self, key: int) -> int:
        # check if key is in cache
        if key in self.cache:
            # since we're using this key, make it the most recently used
            # i.e., move node to be before the right sentinel
            node = self.cache[key]
            self._evict(node)
            self._use(node)

            # return the value of the node
            return node.val

        return -1  # not found

    def put(self, key: int, value: int):
        # check if cache contains key
        if key in self.cache:
            node = self.cache[key]
            node.val = value
            self._evict(node)
        else:
            node = LRUNode(key=key, val=value)
            self.cache[key] = node

        self._use(node)

        # check we're not over capacity
        if len(self.cache) > self.capacity:
            lru = self.left.next
            
            # evict from the linked list
            self._evict(lru)
        
            # to delete this node from the cache we need it's key;
            # so we'll augment LRUNode with this attribute
            del self.cache[lru.key]
