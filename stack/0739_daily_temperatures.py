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

"""
brute force: check for larger from each

double for-loop

T: O(n^2)
S: O(n)   [output]
"""

