"""
Given an integer array nums, return all the triplets
[nums[i], nums[j], nums[k]] such that i != j, i != k,
and j != k, and nums[i] + nums[j] + nums[k] == 0.

Notice that the solution set must not contain duplicate
triplets.
"""

class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        """
        Brute force: try all triplets

        Use a set and custom hash to avoid duplicates
        that could also be out of order

        T: O(n^3)
        S: O(m)   [where m is the number of unique triplets]

        C(n, k) := n!/k!(n - k)!

        C(n, 3) := n!/3!(n - 3)!
                := n(n-1)(n-2)(n-3)!/3!(n - 3)!
                := n(n-1)(n-2)/6
            ~= n^3
        """
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

    def threeSum(self, nums: list[int]) -> list[list[int]]:
        """
        Optimal: sort first then two pointer

        First, we fix i at some point, then do a two pointer
        on j and k in the remaining indices

        j and k will be looking for the negation of i

        T: O(nlog(n) + n^2) = O(n^2)
        S: O(1)
        """
        n = len(nums)
        res = []

        nums.sort()

        for i, val in enumerate(nums):
            # no way to form sum of 0
            if val > 0:
                break

            # skip duplicates
            if i > 0 and val == nums[i - 1]:
                continue

            l, r = i + 1, n - 1
            while l < r:
                triplet = [val, nums[l], nums[r]]
                total = sum(triplet)

                if total == 0:
                    res.append(triplet)

                    # we only need to update one of the pointers
                    # to prevent duplicates
                    l += 1
                    while l < r and nums[l] == nums[l - 1]:
                        l += 1

                elif total < 0:  # increase sum
                    l += 1
                else:  # decrease sum
                    r -= 1

        return res
