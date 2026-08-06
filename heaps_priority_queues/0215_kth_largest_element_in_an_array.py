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
