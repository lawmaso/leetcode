class Solution:
    def initial_longest_consecutive(self, nums: list[int]) -> int:
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

"""
initial approach: sort

since elements can be out of order, sort entire list
and determine the longest sequence via counting while diffs
are 1

skip duplicates

T: O(nlog(n))
S: O(1)/O(n) [depends on sort algorithm]

ex: [100,4,200,1,3,2]

[1, 2, 3, 4, 100, 200]
              i
length = 4

4 + 1 != 100; reset
length = 0

ex: [1, 2, 3, 4]
length=4
"""
