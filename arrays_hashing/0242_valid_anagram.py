"""
Given two strings s and t, return true if t is an anagram of s, and false otherwise.

Example 1:

Input: s = "anagram", t = "nagaram"
Output: true

Example 2:

Input: s = "rat", t = "car"
Output: false

Follow up: What if the inputs contain Unicode characters? How would you adapt your solution to such a case?
"""

class Solution:
    def initial_is_anagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        offset = ord("a")
        s_count = [0] * 26
        t_count = [0] * 26

        # can choose either length since they're equal
        for i in range(len(t)):
            s_count[ord(s[i]) - offset] += 1
            t_count[ord(t[i]) - offset] += 1

        return s_count == t_count

    def follow_up_is_anagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        s_count = dict()
        t_count = dict()

        for i in range(len(t)):
            cs, ct = s[i], t[i]

            if cs not in s_count:
                s_count[cs] = 0
            if ct not in t_count:
                t_count[ct] = 0

            s_count[cs] += 1
            t_count[ct] += 1

        return s_count == t_count

"""
approach: 

assumption: all characters are lowercase english letters

store each string char count in a list[int] where len = 26

then count each by normalizing the ascii code to its appropriate index

a -> 0
b -> 1
...
char -> ord(char) - ord("a")

then just check that each list is equal

T: O(n)
S: O(n)

dry-run:

ex:
s, t = abba, bbaa
expect true

s_count = [2, 2, ...]
t_count = [2, 2, ...]

s_count equals t_count; test passes

ex:
s, t = a, b
expect false

s_count = [1, 0]
t_count = [0, 1]

s_count != t_count; test passes
"""


"""
follow-up: not just lowercase english

to adapt the current solution, we'd need a way to generalize to
be able to store the count for any character. can't just use a subset
of the ascii codes in a list since they can be largely disconnected
with no way to normalize them to the same baseline.

solution: use a hash map s.t. keys are the character and values are the counts
in the string

this way we don't rely on explcit indexing, but hashing of the specific char
to efficiently update+get the count


T: O(n)
S: O(n)
"""

