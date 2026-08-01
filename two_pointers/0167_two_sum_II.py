class Solution:
    def brute_two_sum(self, numbers: list[int], target: int) -> list[int]:
        n = len(numbers)

        for i in range(n):
            for j in range(i + 1, n):
                if numbers[i] + numbers[j] == target:
                    return [i + 1, j + 1]

        raise ValueError("no pair found")

    def opt_two_sum(self, numbers: list[int], target: int) -> list[int]:
        seen = dict()  # val: index

        for i, n in enumerate(numbers):
            complement = target - n

            if complement in seen:
                return [seen[complement] + 1, i + 1]

            seen[n] = i

        raise ValueError("no pair found")

    def two_sum(self, numbers: list[int], target: int) -> list[int]:
        n = len(numbers)
        l, r = 0, n - 1

        while l < r:
            sum_ = numbers[l] + numbers[r]

            if sum_ == target:
                return [l + 1, r + 1]
            elif sum_ < target:  # increase case
                l += 1
            else:                # decrease case
                r -= 1

        raise ValueError("no pair found")

"""
brute force: check every pair and see if
             one sums to target

T: O(n^2)
S: O(1)
"""

"""
optimization: store each seen value in a mapping to its index

if a value needs the stored value, then we have a solution

T: O(n)
S: O(n)  [doesn't meet requirements]
"""

"""
optimal: use sorted property with two pointers

start left at 0 and right at n - 1

curr_sum = nums[left] + nums[right]

depending on sum, we can then guide the some closer towards target
if curr_sum is too small, shift left to increase sum
if curr_sum is too large, shift right to decrease sum

to avoid using the same value twice, condition will be left < right

T: O(n)
S: O(1)
"""
