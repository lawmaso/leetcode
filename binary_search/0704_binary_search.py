class Solution:
    def search(self, nums: list[int], target: int) -> int:
        l, r = 0, len(nums) - 1

        # need l <= r in case l and r overlap on target
        # ex: singleton case [1], target=1
        while l <= r:
            m = l + (r-l) // 2
            mid_val = nums[m]

            if mid_val == target:
                return m
            elif mid_val < target:  # search right space
                l = m + 1
            else:  # search left space
                r = m - 1

        return -1

"""
brute force: linear search

but to improve, we can utilize the fact the
list is sorted and apply binary search

basically, split list each time

~= log(n) splits -> gets us a result of target being
existent or not

start two pointers at left and right, get middle index

(l + r) // 2 -> potential overflow
    = l//2 + r//2 - l//2 + l//2 (add 0)
    = l + (r - l) // 2

avoid overflow via substraction

compare middle against target:
    if < target: search right space
    if > target: search left space
    if == target: return index
"""
