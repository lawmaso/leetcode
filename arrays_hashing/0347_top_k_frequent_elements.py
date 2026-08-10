"""
Given an integer array nums and an integer k, return
the k most frequent elements. You may return the answer
in any order.

Example 1:

Input: nums = [1,1,1,2,2,3], k = 2
Output: [1,2]

Example 2:

Input: nums = [1], k = 1
Output: [1]

Example 3:

Input: nums = [1,2,1,2,1,2,3,1,3,2], k = 2
Output: [1,2]

Follow up: Your algorithm's time complexity must be better
than O(n log n), where n is the array's size.
"""

class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        """
        Initial approach: heap

        ex1:
        1: 3+
        2: 2+
        3: 1-

        counts = [3, 2, 1] -> counts[:k]

        Max count of a single value can be the length of the array,
        which is just len(nums) = n

        Build out max heap with entries (count, value), then pop k times

        T: O(n + klog(n))
            build heap: n
            pops: klog(n)
        S: O(n)
        """

        import heapq

        n = len(nums)
        heap = []

        # count value frequencies
        counts = dict()
        for val in nums:
            if val not in counts:
                counts[val] = 0
            counts[val] += 1

        # build out heap structure
        for val, count in counts.items():
            heap.append((-count, val))  # negate for max heap
        heapq.heapify(heap)

        # get result by popping top k from heap
        res = []
        for _ in range(k):
            res.append(heapq.heappop(heap)[1])
        return res

    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        """
        Optimal: counting sort

        Notice that the max count of any element can be
        at most n (the length of the list)

        Utilize frequency list to count; allow indexing from 0 (trivial)
        to the max, which is len(nums)

        Length of freq list is then: len(nums) - 0 + 1 = len(nums) + 1

        After building the list out, we can build out the result from
        the highest frequencies to lowest, until we hit the threshold k

        T: O(n)
        S: O(n)
        """
        n = len(nums)

        freq = [[] for _ in range(n + 1)]
        counts = dict()
        for val in nums:
            if val not in counts:
                counts[val] = 0
            counts[val] += 1

        for val, count in counts.items():
            freq[count].append(val)

        res = []
        for i in range(len(freq) - 1, -1, -1):
            for val in freq[i]:
                res.append(val)
                if len(res) == k:
                    return res

        # should never reach here if k is bounded properly
        return res
