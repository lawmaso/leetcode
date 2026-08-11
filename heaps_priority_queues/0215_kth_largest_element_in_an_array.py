"""
Given an integer array nums and an integer k, return the kth
largest element in the array.

Note that it is the kth largest element in the sorted order,
not the kth distinct element.

Can you solve it without sorting?
"""

class Solution:
    def findKthLargest(self, nums: list[int], k: int) -> int:
        """
        Brute force: sort

        T: O(nlog(n))
        S: O(n)  [sorting algorithm]
        """
        nums.sort()
        return nums[len(nums) - k]  # (n-1) - (k+1)

    def findKthLargest(self, nums: list[int], k: int) -> int:
        """
        Optimal approach: min heap of size k

        The kth largest will become the root of the heap

        T: O(nlog(k))
        S: O(n)
        """
        import heapq
        heap = []

        for n in nums:
            # push value to heap
            heapq.heappush(heap, n)

            # stabilize heap length back to k
            if len(heap) > k:
                heapq.heappop(heap)

        return heap[0]
