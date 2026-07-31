"""
Given an array of strings strs, group the anagrams
together. You can return the answer in any order.

Example 1:

Input: strs = ["eat","tea","tan","ate","nat","bat"]
Output: [["bat"],["nat","tan"],["ate","eat","tea"]]

Explanation:

There is no string in strs that can be rearranged to form "bat".
The strings "nat" and "tan" are anagrams as they can be rearranged to form each other.
The strings "ate", "eat", and "tea" are anagrams as they can be rearranged to form each other.

Example 2:

Input: strs = [""]
Output: [[""]]

Example 3:
Input: strs = ["a"]
Output: [["a"]]
"""

class Solution:
    def brute_is_anagram(self, strs: list[str]) -> list[list[str]]:
        n = len(strs)
        groups = dict()
        parent = list(range(n))

        def pair_anagram(a: str, b: str) -> bool:
            if len(a) != len(b):
                return False
            
            offset = ord("a")
            a_count = [0] * 26
            b_count = [0] * 26

            for i in range(len(a)):
                a_count[ord(a[i]) - offset] += 1
                b_count[ord(b[i]) - offset] += 1

            return a_count == b_count

        for i in range(n):
            # i should always be the group representative
            if i != parent[i]:
                continue
            
            groups[i] = [strs[i]]

            for j in range(i + 1, n):
                if pair_anagram(strs[i], strs[j]):
                    parent[j] = i
                    groups[i].append(strs[j])

        print(groups.items())

        return list(groups.values())


"""
brute force: check all pairs

when checking a pair, assume i is the group representative.
if i is not it's own representative, then it was already examined and
grouped with other strings

groups should be in a sort of map, keyed by their
representative's index

return list(map.values())

T: O(n^2)
S: O(n)
"""
