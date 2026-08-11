from __future__ import annotations

"""
Given an m x n board of characters and a list of strings
words, return all words on the board.

Each word must be constructed from letters of sequentially
adjacent cells, where adjacent cells are horizontally or
vertically neighboring. The same letter cell may not be
used more than once in a word
"""

class TrieNode:
    children: dict[str, TrieNode]
    is_word: bool
    word: str

    def __init__(self):
        self.children = dict()
        self.is_word = False
        self.word = ""

    def insert(self, s: str):
        curr = self

        for char in s:
            if char not in curr.children:
                curr.children[char] = TrieNode()
            curr = curr.children[char]

        curr.is_word = True
        curr.word = s

class Trie:
    root: TrieNode

    def __init__(self, words: list[str] = list()):
        self.root = TrieNode()
        for word in words:
            self.insert(word)

    def insert(self, s: str):
        self.root.insert(s)

class Solution:
    def findWords(self, board: list[list[str]], words: list[str]) -> list[str]:
        """
        Brute force: DFS for each word from each position

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

    def findWords(self, board: list[list[str]], words: list[str]) -> list[str]:
        """
        Optimal approach: trie + DFS

        T: O(mn * 3^L + W)
            O(mn * 3^L): grid search + DFS
            O(W): building trie
        S: O(W + L)
            O(W): trie nodes
            O(L): recursion stack from DFS

        W: sum(len(words))
        L: max(len(w) for w in words)
        """
        m, n = len(board), len(board[0])
        dirs = [(-1,0), (0,1), (1,0), (0,-1)]
        trie = Trie(words)

        res = []

        def dfs(r: int, c: int, parent: TrieNode, seen: set[tuple[int, int]]):
            char = board[r][c]
            if char not in parent.children:
                return

            curr = parent.children[char]

            # base case: found a word
            if curr.is_word:
                res.append(curr.word)

                # instead of using an explicit set, once this word is found,
                # just mark the node flag as not a word; so this base case is
                # never reached for this word again
                curr.is_word = False
                
                # NOTE: don't return early, this could be a prefix
                # of another word (e.g., oat and oatmeal)
                # return

            for dr, dc in dirs:
                nr, nc = r + dr, c + dc

                # check in bounds and not already seen
                if (
                    0 <= nr < m and
                    0 <= nc < n and
                    (nr, nc) not in seen
                ):
                    seen.add((nr, nc))
                    dfs(nr, nc, curr, seen)
                    seen.remove((nr, nc))

        for r in range(m):
            for c in range(n):
                dfs(r, c, trie.root, {(r, c)})

        return res

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
