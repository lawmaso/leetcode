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
"""


class Solution:
    def initial_top_k_frequent(self, nums: list[int], k: int) -> list[int]:
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

"""
initial approach: heap

ex1:
1: 3+
2: 2+
3: 1-

counts = [3, 2, 1] -> counts[:k]

max count of a single value can be the length of the array,
which is just len(nums) = n

build out max heap with entries (count, value), then pop k times

T: O(n + klog(n))
    build heap: n
    pops: klog(n)
S: O(n)
"""
