"""
Given an integer array nums, return an array answer such
that answer[i] is equal to the product of all the elements
of nums except nums[i].

The product of any prefix or suffix of nums
is guaranteed to fit in a 32-bit integer.

You must write an algorithm that runs in O(n)
time and without using the division operation.
"""

class Solution:
    def initial_product_except_self(self, nums: list[int]) -> list[int]:
        n = len(nums)

        prefix = [1] * n  # prefix[i] = product of left exluding i
        suffix = [1] * n  # suffix[i] = product of right excluding i

        # build left product
        p = 1
        for i in range(n):
            prefix[i] = p
            p *= nums[i]

        # build right product
        p = 1
        for i in range(n - 1, -1, -1):
            suffix[i] = p
            p *= nums[i]

        # build out result using prefixes and suffixes
        res = []
        for i in range(n):
            res.append(prefix[i] * suffix[i])

        return res

"""
at any point, we just want the left and right product
from that point

ex: [1, 2, 3, 4]

left_prod:  [1 (base), 1, 2, 6]
right_prod: [24, 12, 4, 1 (base)]

then result is just element-wise product of both

prefixing and suffixing products

T: O(n)
S: O(n)
"""
