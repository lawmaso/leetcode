"""
Given an array of integers nums containing n + 1
integers where each integer is in the range [1, n] inclusive.

There is only one repeated number in nums, return this repeated number.

You must solve the problem without modifying the array nums and using
only constant extra space.
"""

class Solution:
    def findDuplicate(self, nums: list[int]) -> int:
        """
        Approach: modify list

        When a value is negative, we've marked it before,
        so we can conclude that the duplicate is the index

        ex: [1,3,4,2,2]

        [1, -3, -4, -2, -2]
                        ^
                        val = abs(-2) = 2
                        nums[2] < 0; conclude 2 was already seen
        return 2
        +

        T: O(n)
        S: O(1)
        """
        for i in range(len(nums)):
            val = abs(nums[i])

            if nums[val] < 0:
                return val

            nums[val] *= -1

    def findDuplicate(self, nums: list[int]) -> int:
        """
        Optimal: simulate linked list

        T: O(n)
        S: O(1)
        """
        slow = fast = 0

        # phase 1: 
        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]

            # break at the intersection of slow and fast
            # NOTE: this intersection is not necessarily the duplicate
            if slow == fast:
                break

        # phase 2: find duplicate (i.e., the entry point of the cycle)
        slow2 = 0
        while True:
            slow = nums[slow]
            slow2 = nums[slow2]

            if slow == slow2:
                return slow

"""
Brute force v1: use a set

Doesn't meet space requirements

T: O(n)
S: O(n)

Brute force 2: sort then check adjacent

T: O(nlog(n))
S: O(1)
"""
