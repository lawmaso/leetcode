"""
You are given an integer array height of length n.
There are n vertical lines drawn such that the
two endpoints of the ith line are (i, 0) and (i, height[i]).

Find two lines that together with the x-axis form a
container, such that the container contains the most water.

Return the maximum amount of water a container can store.

Notice that you may not slant the container.

Example 1:
Input: height = [1,8,6,2,5,4,8,3,7]
Output: 49

Explanation: The above vertical lines are represented
by array [1,8,6,2,5,4,8,3,7]. In this case, the max area
of water (blue section) the container can contain is 49.


Example 2:
Input: height = [1,1]
Output: 1
"""

class Solution:
    def maxArea(self, height: list[int]) -> int:
        """
        Brute force: for each left, check all possible areas

        Assuming index l is the left

        For all l:
            res = arg_max [min(heights[l], heights[r]) * (r - l)]

        T: O(n^2)
        S: O(1)
        """
        n = len(height)
        res = 0

        for l in range(n):
            for r in range(l + 1, n):
                h = min(height[l], height[r])
                res = max(res, h * (r - l))

        return res

    def maxArea(self, height: list[int]) -> int:
        """
        Optimal: greedy expansion using two pointers

        left and right

        Expanding inwards -> width decreases, so attempt to increase height

        For l or r, choose to update the minimum one
            If l and r have the same height, choose either
                Choose left for determinism/standard

        T: O(n)
        S: O(1)
        """
        n = len(height)
        res = 0

        # start at boundaries
        l, r = 0, n - 1
        while l < r:
            h = min(height[l], height[r])
            res = max(res, h * (r - l))

            # expand l inwards
            if height[l] <= height[r]:
                l += 1
            # expand r inwards
            else:
                r -= 1

        return res
