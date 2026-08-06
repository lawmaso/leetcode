from __future__ import annotations

"""
A trie (pronounced as "try") or prefix tree
is a tree data structure used to efficiently
store and retrieve keys in a dataset of strings.
There are various applications of this data structure,
such as autocomplete and spellchecker.

Implement the Trie class:
    - Trie() Initializes the trie object.
    - void insert(String word)
        Inserts the string word into the trie.
    - boolean search(String word)
        Returns true if the string word is in the trie (i.e., was inserted before), and false otherwise.
    - boolean startsWith(String prefix)
        Returns true if there is a previously inserted string word that has the prefix prefix, and false otherwise.

ex1:
Input
["Trie", "insert", "search", "search", "startsWith", "insert", "search"]
[[], ["apple"], ["apple"], ["app"], ["app"], ["app"], ["app"]]
Output
[null, null, true, false, true, null, true]

Explanation
Trie trie = new Trie();
trie.insert("apple");
trie.search("apple");   // return True
trie.search("app");     // return False
trie.startsWith("app"); // return True
trie.insert("app");
trie.search("app");     // return True

a*
p*
p*+
l*
e*+

+: inserted word
*: valid prefix

apple is a word, but app is not
only after insertion should a string be a word
"""

class TrieNode:
    children: dict[str, TrieNode]
    is_word: bool

    def __init__(self):
        self.children = dict()
        self.is_word = False

    def insert(self, s: str):
        curr = self

        # parse chars to connect the nodes
        for char in s:
            # char is not a child of curr yet
            if char not in curr.children:
                curr.children[char] = TrieNode()

            # move to the next character
            curr = curr.children[char]

        # now, curr is the last character node, mark it as a word
        curr.is_word = True

        """
        ex:
        root = TrieNode()
        root.insert("a")
        root -> a (is_word=True)
        """

class Trie:
    root: TrieNode

    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str):
        self.root.insert(word)

    def search(self, word: str, allowPrefix: bool = False) -> bool:
        curr = self.root

        for char in word:
            if char not in curr.children:
                return False
            curr = curr.children[char]

        return allowPrefix or curr.is_word

    def startsWith(self, prefix: str) -> bool:
        return self.search(prefix, allowPrefix=True)

if __name__ == "__main__":
    trie = Trie() 
    trie.insert("apple")
    assert trie.search("apple")    # return True
    assert not trie.search("app")  # return False
    assert trie.startsWith("app")  # return True
    trie.insert("app") 
    assert trie.search("app")      # return True
