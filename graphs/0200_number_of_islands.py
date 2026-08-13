"""
Given an m x n 2D binary grid grid which represents a
map of '1's (land) and '0's (water), return the number
of islands.

An island is surrounded by water and is formed by connecting
adjacent lands horizontally or vertically. You may assume all
four edges of the grid are all surrounded by water.

Example 1:

Input: grid = [
  ["1","1","1","1","0"],
  ["1","1","0","1","0"],
  ["1","1","0","0","0"],
  ["0","0","0","0","0"]
]
Output: 1

11110
11010
11000
00000

Example 2:

Input: grid = [
  ["1","1","0","0","0"],
  ["1","1","0","0","0"],
  ["0","0","1","0","0"],
  ["0","0","0","1","1"]
]
Output: 3

11000
11000
00100
00011
"""

class Solution:
    def numIslands(self, grid: list[list[str]]) -> int:
        """
        Approach: BFS

        Expand the frontier while land cells are reachable
        4-directionally

        T: O(mn)
        S: O(mn)
        """
        from collections import deque

        m, n = len(grid), len(grid[0])
        dirs = [(0,-1), (-1,0), (0,1), (1,0)]
        LAND, WATER = "1", "0"

        def bfs(sr: int, sc: int):
            grid[sr][sc] = WATER
            q = deque([(sr, sc)])

            while q:
                r, c = q.popleft()

                for dr, dc in dirs:
                    nr, nc = r + dr, c + dc
                    if (
                        0 <= nr < m and
                        0 <= nc < n and
                        grid[nr][nc] == LAND
                    ):
                        grid[nr][nc] = WATER
                        q.append((nr, nc))

        islands = 0
        for r in range(m):
            for c in range(n):
                if grid[r][c] == LAND:
                    bfs(r, c)
                    islands += 1

        return islands

if __name__ == "__main__":
    soln = Solution()

    for grid, expected in [
        ([
            ["1","1","1","1","0"],
            ["1","1","0","1","0"],
            ["1","1","0","0","0"],
            ["0","0","0","0","0"]
        ], 1),
        ([
            ["1","1","0","0","0"],
            ["1","1","0","0","0"],
            ["0","0","1","0","0"],
            ["0","0","0","1","1"]
        ], 3)
    ]:
        for row in grid:
            print("".join(row))
        print("-" * 10)
        res = soln.numIslands(grid)


        print("res      =", res)
        print("expected =", expected, "\n")

        assert res == expected
