"""
Given a string s containing just the
characters '(', ')', '{', '}', '[' and ']',
determine if the input string is valid.

An input string is valid if:
- Open brackets must be closed by the same type of
brackets.
- Open brackets must be closed in the correct order.
- Every close bracket has a corresponding open bracket
of the same type.
"""

class Solution:
    def is_valid(self, s: str) -> bool:
        pairs = ["()", "[]", "{}"]

        while any(pair in s for pair in pairs):
            for p in pairs:
                s = s.replace(p, "")

        return s == ""

"""
brute: replace all adjacent pairs

string will flatten to the empty string if valid

worst-case, fully nested


"[({})]", length = 6 = n

pop {}
pop ()
pop []

3 pops == (n / 2) pops
so in worst-case; there are n/2 pops ~= n pops
    each with approximate cost of n
~n*n

space is O(n) since each replace allocates a new string

T: O(n^2)
S: O(n)
"""

