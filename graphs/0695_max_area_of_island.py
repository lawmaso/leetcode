"""
You are given an m x n binary matrix grid. An island is a
group of 1's (representing land) connected 4-directionally
(horizontal or vertical.) You may assume all four edges of
the grid are surrounded by water.

The area of an island is the number of cells with a value 1 in the island.

Return the maximum area of an island in grid. If there is no island, return 0.
"""

class Solution:
    def maxAreaOfIsland(self, grid: list[list[int]]) -> int:
        """
        Approach: BFS from land to determine size

        We just choose the maximum of all island sizes

        T: O(mn)
            - We process each position exactly once
        S: O(mn)
            - The queue can have at most mn nodes
        """
        from collections import deque

        m, n = len(grid), len(grid[0])
        dirs = [(-1,0), (0,1), (1,0), (0,-1)]
        WATER, LAND = 0, 1


        # bfs1: size tracks cells when they are discovered/enqueued
        def bfs1(sr: int, sc: int) -> int:
            grid[sr][sc] = WATER

            q = deque([(sr, sc)])
            size = len(q)

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
                        size += 1

            return size

        # bfs2: size tracks cells when they are processed/dequeued.
        def bfs2(sr: int, sc: int) -> int:
            grid[sr][sc] = WATER

            q = deque([(sr, sc)])
            size = 0

            while q:
                r, c = q.popleft()
                size += 1

                for dr, dc in dirs:
                    nr, nc = r + dr, c + dc
                    if (
                        0 <= nr < m and
                        0 <= nc < n and
                        grid[nr][nc] == LAND
                    ):
                        grid[nr][nc] = WATER
                        q.append((nr, nc))

            return size

        max_area = 0
        for r in range(m):
            for c in range(n):
                if grid[r][c] == LAND:
                    max_area = max(max_area, bfs1(r, c))

        return max_area

if __name__ == "__main__":
    soln = Solution()

    for grid, expected in [
        ([
            [0,0,1,0,0,0,0,1,0,0,0,0,0],
            [0,0,0,0,0,0,0,1,1,1,0,0,0],
            [0,1,1,0,1,0,0,0,0,0,0,0,0],
            [0,1,0,0,1,1,0,0,1,0,1,0,0],
            [0,1,0,0,1,1,0,0,1,1,1,0,0],
            [0,0,0,0,0,0,0,0,0,0,1,0,0],
            [0,0,0,0,0,0,0,1,1,1,0,0,0],
            [0,0,0,0,0,0,0,1,1,0,0,0,0]
        ], 6),
        ([[0,0,0,0,0,0,0,0]], 0)
    ]:
        res = soln.maxAreaOfIsland(grid)
        print("res =", res, "|", "expected =", expected)
