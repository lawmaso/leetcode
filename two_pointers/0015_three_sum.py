"""
Given an integer array nums, return all the triplets
[nums[i], nums[j], nums[k]] such that i != j, i != k,
and j != k, and nums[i] + nums[j] + nums[k] == 0.

Notice that the solution set must not contain duplicate
triplets.
"""

class Solution:
    def brute_three_sum(self, nums: list[int]) -> list[list[int]]:
        n = len(nums)

        seen = set()  # triplet hashes
        res = []

        # examine all triplets
        for i in range(n):
            for j in range(i + 1, n):
                for k in range(j + 1, n):
                    triplet = [nums[i], nums[j], nums[k]]
                    triplet_hash = "".join([str(v) for v in sorted(triplet)])
                    
                    if sum(triplet) == 0 and triplet_hash not in seen:
                        res.append(triplet)
                        seen.add(triplet_hash)

        return res

"""
brute force: try all triplets

use set and custom hash to avoid duplicates
that could also be out of order

T: O(n^3)
S: O(m)   [where m is the number of unique triplets]

C(n, k) := n!/k!(n - k)!

C(n, 3) := n!/3!(n - 3)!
        := n(n-1)(n-2)(n-3)!/3!(n - 3)!
        := n(n-1)(n-2)/6
    ~= n^3
"""

