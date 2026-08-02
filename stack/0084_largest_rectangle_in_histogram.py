"""
Given an array of integers heights representing
the histogram's bar height where the width of
each bar is 1, return the area of the largest
rectangle in the histogram.

Input: heights = [2,1,5,6,2,3]
Output: 10

Explanation: The above is a histogram where width of each bar is 1.
The largest rectangle is shown in the red area, which has an area = 10 units.
"""

class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        n = len(heights)
        res = 0

        for i in range(n):
            # expand left
            l = i
            while l > 0 and heights[l - 1] >= heights[i]:
                l -= 1
            
            # expand right
            r = i
            while r < n - 1 and heights[r + 1] >= heights[i]:
                r += 1

            # determine max histogram area
            res = max(res, heights[i] * (r - l + 1))

        return res

"""

brute force: just try every possible histogram

at each point, expand as far left and right to get max
(greedy expansion)

ex1:

   X
  XX
  XX
  XX X
X XXXX
XXXXXX

expand only while >= heights are in the direction

at i=0: l=0, r=0, area = h * (r - l + 1) = 2
at i=1: l=0, r=5, area = 1 * (6) = 6
at i=2: l=2, r=3, area = 5 * (2) = 10
at i=3: l=3, r=3, area = 6
at i=4: l=2, r=5, area = 8
at i=5: l=5, r=5, area = 3

T: O(n^2)  [worst-case; ~n expansion cost per each of n columns]
S: O(1)
"""

