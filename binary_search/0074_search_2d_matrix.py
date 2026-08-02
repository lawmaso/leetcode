"""
You are given an m x n integer matrix matrix with the following two properties:

Each row is sorted in non-decreasing order.
The first integer of each row is greater than the last integer of the previous row.
Given an integer target, return true if target is in matrix or false otherwise.

You must write a solution in O(log(m * n)) time complexity.
"""

class Solution:
    def brute_searchMatrix(self, matrix: list[list[int]], target: int) -> bool:
        m, n = len(matrix), len(matrix[0])

        for r in range(m):
            for c in range(n):
                if matrix[r][c] == target:
                    return True

        return False

"""
brute force: just linear search

T: O(mn)
S: O(1)
"""

