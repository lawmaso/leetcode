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

    def searchMatrix(self, matrix: list[list[int]], target: int) -> bool:
        m, n = len(matrix), len(matrix[0])

        left, right = 0, m * n - 1
        while left <= right:
            mid = left + (right-left) // 2
            
            r = mid // n  # "number of full columns"
            c = mid % n   # "column"

            mid_val = matrix[r][c]
            if mid_val == target:
                return True
            elif mid_val < target:  # too small, search rightward
                left = mid + 1
            else:  # too large, search leftward
                right = mid - 1

        return False

"""
brute force: just linear search

T: O(mn)
S: O(1)
"""

"""
optimal: flatten matrix and binary search on regular list

matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 3

1 3 5 7 10 11 16 20 23 30 34 60
l                            r

need a way to get from (r, c) indexing to flattened

for any [r][c], flat_index = (n * r) + c

or to get from flat index to [r][c]:
    r = flat_index // n  (full columns)
    c = flat_index % n   (column)

T: O(log(mn))
S: O(1)
"""

