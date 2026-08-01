"""
Given an array of integers temperatures represents the daily temperatures,
return an array answer such that answer[i] is the number of days you have
to wait after the ith day to get a warmer temperature.
If there is no future day for which this is possible, keep answer[i] == 0 instead.


Example 1:
Input: temperatures = [73,74,75,71,69,72,76,73]
Output: [1,1,4,2,1,1,0,0]

73 -> 74: 1-0 = 1
74 -> 75: 2-1 = 1
71 -> 72: 
69 -> 72:

Example 2:
Input: temperatures = [30,40,50,60]
Output: [1,1,1,0]

Example 3:
Input: temperatures = [30,60,90]
Output: [1,1,0]
"""


class Solution:
    def brute_dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n = len(temperatures)
        res = [0] * n

        for i, temp in enumerate(temperatures):
            for j in range(i + 1, n):
                if temperatures[j] > temp:
                    res[i] = j - i
                    break

        return res

    def dailyTemperatures(self, temperatures: list[int]) -> list[int]:
        n = len(temperatures)

        stack = []  # (index, temp)
        res = [0] * n

        for curr_index, temp in enumerate(temperatures):
            # update previous temps if curr temp is warmer
            while stack and stack[-1][-1] < temp:
                prev_index, _ = stack.pop()
                res[prev_index] = curr_index - prev_index

            # add this temp to stack
            stack.append((curr_index, temp))

        return res

"""
brute force: check for larger from each

double for-loop

T: O(n^2)
S: O(n)   [output]
"""

"""
optimal: utilize stack

if prev stack push has a lower temp than the current,
we can update the days until warmer length for those in the stack
that have a lower temperature


temperatures with no greater temp in the future will remain
in the stack

to account for indexes for the computation, augment the stack
entries as a tuple (index, temp)

T: O(n)
S: O(n)  [strictly decreasing; worst-case]
"""
