"""
You are given an m x n grid where each cell can have one of three values:

0 representing an empty cell,
1 representing a fresh orange, or
2 representing a rotten orange.

Every minute, any fresh orange that is 4-directionally
adjacent to a rotten orange becomes rotten.

Return the minimum number of minutes that must elapse until
no cell has a fresh orange. If this is impossible, return -1.
"""

class Solution:
    def orangesRotting(self, grid: list[list[int]]) -> int:
        """
        Approach: multi-source BFS from rotten fruit
        
        Expand the frontier each iteration of the BFS, while
        increasing the time elapsed

        T: O(mn)
        S: O(mn)
        """
        from collections import deque

        m, n = len(grid), len(grid[0])
        dirs = [(0,-1), (-1,0), (0,1), (1,0)]
        EMPTY, FRESH, ROTTEN = list(int(v) for v in range(3))

        fresh = 0
        q = deque()

        for r in range(m):
            for c in range(n):
                cell = grid[r][c]

                if cell == FRESH:
                    fresh += 1
                elif cell == ROTTEN:
                    q.append((r, c))

        minute = 0
        while q and fresh > 0:
            # expand the (rotten) frontier
            for _ in range(len(q)):
                r, c = q.popleft()

                for dr, dc in dirs:
                    nr, nc = r + dr, c + dc
                    if (
                        0 <= nr < m and
                        0 <= nc < n and
                        grid[nr][nc] == FRESH
                    ):
                        grid[nr][nc] = ROTTEN
                        q.append((nr, nc))
                        fresh -= 1

            minute += 1

        return minute if fresh == 0 else -1


if __name__ == "__main__":
    soln = Solution()

    for grid, expected in [
        ([[2,1,1],[1,1,0],[0,1,1]], 4),
        ([[2,1,1],[0,1,1],[1,0,1]], -1),
        ([[0,2]], 0)
    ]:
        res = soln.orangesRotting(grid)
        print("res =", res, "|", "expected =", expected)

        assert res == expected
