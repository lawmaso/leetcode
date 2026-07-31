"""
You are given an array of integers nums and an
integer target, return indices of the two numbers
such that they add up to target.

You may assume that each input would have exactly
one solution, and you may not use the same element
twice.

You can return the answer in any order.
"""

class Solution:
    def brute_two_sum(self, nums: list[int], target: int) -> list[int]:
        n = len(nums)

        for i in range(n):
            for j in range(i + 1, n):
                if nums[i] + nums[j] == target:
                    return [i, j]

        # should never reach here; solution is guaranteed
        raise ValueError("no pair found")


"""
want two distinct indices s.t. they sum to target

order doesn't matter, so we can just exhaust all index
pairs (i, j) s.t. i != j

T: O(n^2)
S: O(1)
"""
