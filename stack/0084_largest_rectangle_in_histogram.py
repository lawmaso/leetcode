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
    def brute_largestRectangleArea(self, heights: list[int]) -> int:
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

    def largestRectangleArea(self, heights: list[int]) -> int:
        n = len(heights)
        res = 0

        stack = []  # (index, height)
        for i, h in enumerate(heights):
            leftmost = i

            # previous height is larger (expansion ends)
            while stack and stack[-1][-1] > h:
                prev_i, prev_h = stack.pop()
                leftmost = prev_i

                # area of previous histogram being expanded just before i
                res = max(res, prev_h * ((i - 1) - prev_i + 1))

            stack.append((leftmost, h))

        # account for fully expanded histograms
        while stack:
            i, h = stack.pop()
            res = max(res, h * ((n-1) - i + 1))

        return res

"""
dry-run of v2 (optimal):

   X
  XX
  XX
  XX X
X XXXX
XXXXXX

stack = [
    (0,2),  a=2
    (0,1),
    (2,5),  a=10
    (3,6),  a=6
    (2,2),
    (5,3)
]

    2 > 1:
    0, 2 = st.pop()
    a = 2 * (0-0+1) = 2
    
    6 > 2:
    3, 6 = st.pop()
    a = 6 * (3-3+1) = 6

    5 > 2:
    2, 5 = st.pop()
    a = 5 * (3-2+1) = 10

reverse order: (left to right)
0,1 = st.pop(); a = 1 * (6) = 6
2,2 = st.pop(); a = 2 * (5-2+1) = 8
5,3 = st.pop(); a = 3 * (5-5+1) = 5

passes
"""


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

"""
optimization: utilize stack to compute areas iteratively

# (index, height)
stack = [
    (0, 2)+
    (0, 1)-
    (2, 5)+
    (2, 5)+
    (2, 2)-
    (5, 3)-
]

-: not explicitly computed (fully expandable to the end)
+: computed throughout iterations

compute iteratively (+) when a lower height is reached further down
(i.e., it kind of cuts off the higher height from expanding further)

res = arg_max (h * (r - l + 1))

at end, stack will have the fully expandable histograms,
so we'll need one last loop to compute areas

T: O(n)  [going through all of heights]
S: O(n)  [worst-case: strictly increasing heights]
"""

