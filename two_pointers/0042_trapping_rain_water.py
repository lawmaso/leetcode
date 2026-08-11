"""
Given n non-negative integers representing an elevation
map where the width of each bar is 1, compute how much
water it can trap after raining.

Example 1:
Input: height = [0,1,0,2,1,0,1,3,2,1,2,1]
Output: 6
Explanation: The above elevation map (black section) is represented by
array [0,1,0,2,1,0,1,3,2,1,2,1].

       X
   X   XX X
_X_XX_XXXXXX
  + +++  +
     +
In this case, 6 units of rain water (blue section)
are being trapped.

Example 2:
Input: height = [4,2,0,3,2,5]
Output: 9

     X
X    X
X  X X
XX XXX
XX_XXX
 ++++
 ++ +
  +
  +
"""

class Solution:
    def trap(self, height: list[int]) -> int:
        """
        Optimal: prefix and suffix maximum heights

        limit (max height) = min(left_max, right_max)

        Then, for each i we can only add max(0, limit - height[i])
            limit - height[i] = available "box" to add water into

        T: O(n)
        S: O(n)
        """
        n = len(height)
        prefix = [0] * n
        suffix = [0] * n

        # build prefix (left to right)
        p = 0
        for i in range(n):
            prefix[i] = p
            p = max(p, height[i])

        # build suffix (right to left)
        p = 0
        for i in range(n - 1, -1, -1):
            suffix[i] = p
            p = max(p, height[i])

        trapped = 0
        for i in range(n):
            limit = min(prefix[i], suffix[i])
            trapped += max(0, limit - height[i])

        return trapped

    def trap(self, height: list[int]) -> int:
        """
        Optimal+: two pointers

        No need to actually determine the true left/right max

        Being a lowerbound already gives us enough information
        to determine how much water can be trapped at an index

        T: O(n)
        S: O(1)
        """
        n = len(height)
        trapped = 0

        l, r = 0, n - 1
        left_max, right_max = height[l], height[r]

        while l < r:
            if left_max < right_max:
                l += 1
                left_max = max(left_max, height[l])
                trapped += left_max - height[l]
            else:
                r -= 1
                right_max = max(right_max, height[r])
                trapped += right_max - height[r]

        return trapped

if __name__ == "__main__":
    soln = Solution()

    for height, exp in [
        [[0,1,0,2,1,0,1,3,2,1,2,1], 6],
        [[4,2,0,3,2,5], 9]  
    ]:
        res = soln.trap(height)
        print("height:", height)
        print("res:", res, "|", "exp:", exp)

        assert res == exp
        print()
