from __future__ import annotations

"""
Design a data structure that supports
adding new words and finding if a string
matches any previously added string.

Implement the WordDictionary class:
    - WordDictionary()
        Initializes the object.
    - void addWord(word)
        Adds word to the data structure, it can
        be matched later.
    - bool search(word)
        Returns true if there is any string in the data
        structure that matches word or false otherwise.
        word may contain dots '.' where dots can be
        matched with any letter.

ex:
wordDictionary = WordDictionary()
wordDictionary.addWord("bad")
wordDictionary.addWord("dad")
wordDictionary.addWord("mad")
wordDictionary.search("pad")  # return False
wordDictionary.search("bad")  # return True
wordDictionary.search(".ad")  # return True
wordDictionary.search("b..")  # return True

    [root]
    | | |
    b d m
    \|/
    a
    |
    d
"""

class TrieNode:
    children: dict[str, TrieNode]
    is_word: bool

    def __init__(self):
        self.children = dict()
        self.is_word = False

    def insert(self, word: str):
        curr = self

        for char in word:
            if char not in curr.children:
                curr.children[char] = TrieNode()
            curr = curr.children[char]

        curr.is_word = True

class Trie:
    root: TrieNode  # sentinel root

    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str):
        self.root.insert(word)

    def search(self, word: str) -> bool:
        n = len(word)

        def dfs(curr: TrieNode, i: int = 0) -> bool:
            if i >= n:
                # able to reach the end of the word

                return curr.is_word
                # NOTE: we can't just return true; we need
                # to ensure that this was actually an inserted
                # word, which would be flagged with .is_word=True

            char = word[i]

            # at period chars, just try any path
            if char == ".":
                # NOTE: go through the actual node values since we
                # can choose any when we reach a period (i.e., "wildcard")
                return any(
                    dfs(child, i + 1)
                    for child in curr.children.values()
                )

            # non-period character exists as a connection to curr
            elif char in curr.children:
                return dfs(curr.children[char], i + 1)

            return False

        return dfs(self.root)

class WordDictionary:
    """
    Approach: prefix tree + DFS

    DFS handles the case where we need
    to match a dot with any letter
    """
    trie: Trie

    def __init__(self):
        self.trie = Trie()

    def addWord(self, word: str):
        self.trie.insert(word)

    def search(self, word: str) -> bool:
        return self.trie.search(word)


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)

if __name__ == "__main__":
    wordDictionary = WordDictionary()

    wordDictionary.addWord("bad")
    wordDictionary.addWord("dad")
    wordDictionary.addWord("mad")

    assert not wordDictionary.search("pad")  # return False
    assert wordDictionary.search("bad")      # return True
    assert wordDictionary.search(".ad")      # return True
    assert wordDictionary.search("b..")      # return True
