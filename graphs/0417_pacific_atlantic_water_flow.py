"""
There is an m x n rectangular island that borders both the
Pacific Ocean and Atlantic Ocean. The Pacific Ocean touches
the island's left and top edges, and the Atlantic Ocean touches
the island's right and bottom edges.

The island is partitioned into a grid of square cells. You are
given an m x n integer matrix heights where heights[r][c] represents
the height above sea level of the cell at coordinate (r, c).

The island receives a lot of rain, and the rain water can flow to
neighboring cells directly north, south, east, and west if the neighboring
cell's height is less than or equal to the current cell's height. Water
can flow from any cell adjacent to an ocean into the ocean.

Return a 2D list of grid coordinates result where result[i] = [ri, ci]
denotes that rain water can flow from cell (ri, ci) to both the Pacific
and Atlantic oceans.
"""

"""
Ex:

[[1,2,2,3,5],[3,2,3,4,4],[2,4,5,3,1],[6,7,1,4,5],[5,1,1,2,4]]

1  2  2  3   5+
3  2  3  4+  4+
2  4  5+ 3   1
6+ 7+ 1  4   5
5+ 1  1  2   4

[[0,4],[1,3],[1,4],[2,2],[3,0],[3,1],[4,0]]
"""

from collections import deque

class Solution:
    def pacificAtlantic(self, heights: list[list[int]]) -> list[list[int]]:
        """
        Approach: BFS from the oceans

        Parellel BFS from each ocean. Mark the result of each BFS
        through a 2D boolean matrix
            ocean[r][c] = (r, c) can be reached by ocean

        Expand BFS frontier while the neighboring height is >= the current
        height since we are flipping the problem (i.e., going from the ocean inward
        as opposed to land to ocean)

        Then just return the element-wise conjunction of both
        matrices to get those positions

        T: O(mn)
        S: O(mn)
        """
        m, n = len(heights), len(heights[0])
        dirs = [(0,-1), (-1,0), (0,1), (1,0)]

        q_pacific, mat_pacific = self._getQueueAndMatrix(m, n, "pacific")
        q_atlantic, mat_atlantic = self._getQueueAndMatrix(m, n, "atlantic")

        # independent bfs from each ocean
        for q, matrix in [
            [q_pacific, mat_pacific],
            [q_atlantic, mat_atlantic]
        ]:
            while q:
                r, c = q.popleft()

                for dr, dc in dirs:
                    nr, nc = r + dr, c + dc
                    if (
                        0 <= nr < m and
                        0 <= nc < n and
                        not matrix[nr][nc] and
                        heights[nr][nc] >= heights[r][c]
                    ):
                        matrix[nr][nc] = True
                        q.append((nr, nc))

        # get all positions where both oceans could be reached
        return [
            [r, c]
            for r in range(m)
            for c in range(n)
            if mat_pacific[r][c] and mat_atlantic[r][c]
        ]

    def _getQueueAndMatrix(self, m: int, n: int, ocean: str) -> tuple[deque[tuple[int, int]], list[list[bool]]]:
        q = deque([])
        matrix = [[False] * n for _ in range(m)]

        if ocean == "pacific":
            # left and top
            for r in range(m):    q.append((r, 0)); matrix[r][0] = True
            for c in range(1, n): q.append((0, c)); matrix[0][c] = True
        elif ocean == "atlantic":
            # right and bottom
            for r in range(m):     q.append((r, n - 1)); matrix[r][n - 1] = True
            for c in range(n - 1): q.append((m - 1, c)); matrix[m - 1][c] = True
        else:
            raise ValueError(f"unknown ocean type '{ocean}' recieved")

        return q, matrix

if __name__ == "__main__":
    soln = Solution()

    for heights, expected in [
        (
            [[1,2,2,3,5],[3,2,3,4,4],[2,4,5,3,1],[6,7,1,4,5],[5,1,1,2,4]],
            [[0,4],[1,3],[1,4],[2,2],[3,0],[3,1],[4,0]]
        ),
        (
            [[1]],
            [[0,0]]
        )
    ]:
        res = soln.pacificAtlantic(heights)

        print("res      = ", sorted(res))
        print("expected = ", sorted(expected), "\n")

        assert sorted(res) == sorted(expected)
