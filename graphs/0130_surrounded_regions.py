"""
You are given an m x n matrix board containing letters 'X' and 'O',
capture regions that are surrounded:

Connect: A cell is connected to adjacent cells horizontally or vertically.
Region: To form a region connect every 'O' cell.
Surround: A region is surrounded if none of the 'O' cells in that region are on the edge of the board. Such regions are completely enclosed by 'X' cells.
To capture a surrounded region, replace all 'O's with 'X's in-place within the original board. You do not need to return anything.

 
Example 1:

Input: board = [["X","X","X","X"],["X","O","O","X"],["X","X","O","X"],["X","O","X","X"]]

Output: [["X","X","X","X"],["X","X","X","X"],["X","X","X","X"],["X","O","X","X"]]

XXXX
XOOX
XXOX
XOXX

XXXX
XXXX
XXXX
XOXX
"""

class Solution:
    marker: str = "*"

    def solve(self, board: list[list[str]]):
        """
        Approach: BFS from edges

        BFS from O positions on the edge to capture the
        O positions that should remain unchanged. We must
        change these Os to another character that is neither X nor O

        Any Os remaining are the positions that should be flipped to
        be Xs

        T: O(mn)
        S: O(mn) [queue]
        """
        from collections import deque

        m, n = len(board), len(board[0])
        dirs = [(0,-1), (-1,0), (0,1), (1,0)]
        q = deque([])
        X, O = "X", "O"

         # left and right cols
        for r in range(m):
            if board[r][0] == O: q.append((r, 0)); board[r][0] = self.marker
            if board[r][n - 1] == O: q.append((r, n - 1)); board[r][n - 1] = self.marker

        # top and bottom rows
        for c in range(1, n - 1):
            if board[0][c] == O: q.append((0, c)); board[0][c] = self.marker
            if board[m - 1][c] == O: q.append((m - 1, c)); board[m-1][c] = self.marker

        # invariant: for all (r, c) in the queue, board[r][c] = self.marker
        while q:
            r, c = q.popleft()

            for dr, dc in dirs:
                nr, nc = r + dr, c + dc

                if (
                    0 <= nr < m and
                    0 <= nc < n and
                    board[nr][nc] == O
                ):
                    board[nr][nc] = self.marker
                    q.append((nr, nc))

        # now, all non-surrounded regions are marked with our marker

        # first, flip all non-marked Os to Xs (surrounded regions)
        for r in range(m):
            for c in range(n):
                if board[r][c] == O:
                    board[r][c] = X

        # then, flip all marked Os back to Os
        for r in range(m):
            for c in range(n):
                if board[r][c] == self.marker:
                    board[r][c] = O

        # NOTE: the order in which we flip matters since flipping marked positions
        # back to Os first will ambiguate them with the other Os that are part of a
        # surrounded region
        return

    def printBoard(self, board: list[list[str]]):
        for row in board:
            print("".join(row))
        print()

if __name__ == "__main__":
    soln = Solution()

    board = [["X","X","X","X"],["X","O","O","X"],["X","X","O","X"],["X","O","X","X"]]

    soln.printBoard(board)
    soln.solve(board)
    soln.printBoard(board)
