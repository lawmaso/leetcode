class Solution:
    def longestConsecutive(self, nums: list[int]) -> int:
        """
        Initial approach: sort

        Since elements can be out of order, sort entire list
        and determine the longest sequence via counting while diffs
        are 1

        Skip duplicates

        T: O(nlog(n))
        S: O(1)/O(n) [depends on sort algorithm]
        """
        if not nums:
            return 0

        nums.sort()
        res = 1

        length = 0
        for i in range(len(nums)):
            # skip duplicates
            if i > 0 and nums[i - 1] == nums[i]:
                continue
            # nums[i] connects to nums[i - 1]
            elif i > 0 and nums[i - 1] + 1 == nums[i]:
                length += 1
                res = max(res, length)
                continue

            length = 1

        return res

    def longestConsecutive(self, nums: list[int]) -> int:
        """
        Optimal: count from entrypoints in a sequence

        No need to sort after hashing the list into a set of values
        to check if the subsequent value(s) exist, just check that
        (v + i) is in the set and increase length

        Casting to set is also simpler as we avoid checking for duplicates
        explicitly

        T: O(n) [building set + main loop]
        S: O(n) [set]
        """
        n = len(nums)
        unique = set(nums)  # unique nums

        res = 0
        for val in unique:
            # val an entrypoint for a sequence; prev doesn't exist
            if (val - 1) not in unique:
                length = 1

                # while next value in sequence exists; increase length
                while (val + length) in unique:
                    length += 1

                res = max(res, length)

        return res

"""
[brute force] ex: [100,4,200,1,3,2]

[1, 2, 3, 4, 100, 200]
              i
length = 4

4 + 1 != 100; reset
length = 0

ex: [1, 2, 3, 4]
length=4
"""
