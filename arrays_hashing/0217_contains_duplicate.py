"""
Given an integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct.

Example 1:

Input: nums = [1,2,3,1]
Output: true
Explanation: The element 1 occurs at the indices 0 and 3.

Example 2:

Input: nums = [1,2,3,4]
Output: false

Explanation: All elements are distinct.

Example 3:

Input: nums = [1,1,1,3,3,4,3,2,4,2]
Output: true
"""


class Solution:
    def containsDuplicate(self, nums: list[int]) -> bool:
        """
        Brute force: check every pair of elements of the list

        T: O(n^2)
        S: O(1)
        """
        n = len(nums)

        for i in range(n):
            for j in range(i + 1, n):
                if nums[i] == nums[j]:
                    return True

        return False

    def containsDuplicate(self, nums: list[int]) -> bool:
        """
        Optimal: utilize hashset to track seen elements

        T: O(n)
        S: O(n)
        """
        seen = set()

        for n in nums:
            if n in seen:
                return True
            seen.add(n)

        return False


"""
Dry runs:

1, 2, 3, 1
seen = {}
     = {1}, {1, 2}, {1, 2, 3}, then 1 is found
"""
