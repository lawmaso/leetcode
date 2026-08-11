"""
You are given an array of integers stones where stones[i] is
the weight of the ith stone.

We are playing a game with the stones. On each turn, we choose
the heaviest two stones and smash them together. Suppose the heaviest
two stones have weights x and y with x <= y. The result of this smash is:

If x == y, both stones are destroyed, and
If x != y, the stone of weight x is destroyed, and the stone of weight y has new weight y - x.
At the end of the game, there is at most one stone left.

Return the weight of the last remaining stone. If there are no stones left, return 0.
"""

class Solution:
    def lastStoneWeight(self, stones: list[int]) -> int:
        """
        Brute force: sort + simulation

        T: O(n * nlog(n)) = O(n^2 * log(n))
            O(n): ~n stone smashes [worst-case]
            O(nlog(n)): resort list after smashes
        S: O(n)  [auxiliary space used by sorting algorithm]
        """

        while len(stones) >= 2:
            stones.sort()

            # get top two stones
            y, x = stones.pop(), stones.pop()

            # both get destroyed
            if x == y:
                continue

            stones.append(y - x)  # new stone after smash

        return stones[0] if stones else 0

    def lastStoneWeight(self, stones: list[int]) -> int:
        """
        Optimal approach: max heap

        T: O(n + n * log(n)) = O(nlog(n))
            O(n): building heap
            O(nlog(n)): ~n pops/pushes; each cost log(n)
        S: O(n)
        """
        import heapq

        # negate stones to simulate max heap
        heap = [-stone for stone in stones]
        heapq.heapify(heap)

        # simulate game
        while len(heap) >= 2:
            y, x = heapq.heappop(heap), heapq.heappop(heap)

            if x == y:
                continue

            # append new stone
            # new weight is (-y) - (-x) == x - y
            # but we need to negate again: -(x - y) == y - x
            heapq.heappush(heap, y - x)

        # unnegate the last stone (if exists)
        return -heap[0] if heap else 0
