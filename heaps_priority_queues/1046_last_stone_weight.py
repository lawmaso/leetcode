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
