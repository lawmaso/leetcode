"""
You are given a m x n 2D grid initialized with these three possible values:
    -1: A water cell that can not be traversed.
    0: A treasure chest.
    INF: A land cell that can be traversed.
        We use the integer 2^31 - 1 = 2147483647 to represent INF.

Fill each land cell with the distance to its nearest treasure chest.
If a land cell cannot reach a treasure chest then the value should remain INF.

Assume the grid can only be traversed up, down, left, or right.

Modify the grid in-place.
"""

class Solution:
    def islandsAndTreasures(self, grid: list[list[int]]):
        """
        Approach: multi-source BFS from chests

        BFS is a complete algorithm, so any INF position connected to
        a any number of treasure chests will always be given the minimum
        manhattan distance to any treasure chest

        T: O(mn)
        S: O(mn)
        """
        from collections import deque

        m, n = len(grid), len(grid[0])
        dirs = [(-1,0), (0,1), (1,0), (0,-1)]
        WATER, CHEST, INF = -1, 0, 2**31 - 1

        q = deque([])

        for r in range(m):
            for c in range(n):
                if grid[r][c] == CHEST:
                    q.append((r, c, 0))

        while q:
            r, c, prev_dist = q.popleft()

            for dr, dc in dirs:
                nr, nc = r + dr, c + dc

                if (
                    0 <= nr < m and
                    0 <= nc < n and
                    grid[nr][nc] == INF
                ):
                    grid[nr][nc] = prev_dist + 1
                    q.append((nr, nc, grid[nr][nc]))

        return
