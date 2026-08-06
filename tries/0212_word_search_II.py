from __future__ import annotations

"""
Given an m x n board of characters and a list of strings
words, return all words on the board.

Each word must be constructed from letters of sequentially
adjacent cells, where adjacent cells are horizontally or
vertically neighboring. The same letter cell may not be
used more than once in a word
"""

class Solution:
    def findWords(self, board: list[list[str]], words: list[str]) -> list[str]:
        """
        Brute force: dfs for each word from each position

        T: O(mn * w * 3^L)
        S: O(L)
        """
        m, n = len(board), len(board[0])
        dirs = [(-1,0), (0,1), (1,0), (0,-1)]

        def dfs(r: int, c: int, i: int, word: str, seen: set[tuple[int, int]]) -> bool:
            # base case [success]
            if i >= len(word):
                return True

            # base case [failure]
            if not (
                0 <= r < m and
                0 <= c < n and
                board[r][c] == word[i]
            ):
                return False

            # look for next portion of the word
            for dr, dc in dirs:
                nr, nc = r + dr, c + dc

                if (
                    0 <= nr < m and
                    0 <= nc < n and
                    (nr, nc) not in seen
                ):
                    seen.add((nr, nc))

                    if dfs(nr, nc, i + 1, word, seen):
                        return True

                    seen.remove((nr, nc))

            return False

        res = set()

        for r in range(m):
            for c in range(n):
                for word in words:
                    seen = {(r, c)}
                    if dfs(r, c, 0, word, seen):
                        res.add(word)

        return list(res)

if __name__ == "__main__":
    soln = Solution()

    board = [["o","a","a","n"],["e","t","a","e"],["i","h","k","r"],["i","f","l","v"]]
    words = ["oath","pea","eat","rain"]

    res = soln.findWords(board, words)
    print(res)

    board = [["a","b"],["c","d"]]
    words = ["abcb"]

    res = soln.findWords(board, words)
    print(res)
