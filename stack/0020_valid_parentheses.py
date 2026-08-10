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
    def isValid(self, s: str) -> bool:
        """
        Brute force: replace all adjacent pairs

        String will flatten to the empty string if valid

        Worst-case, fully nested

        "[({})]", length = 6 = n

        pop {}
        pop ()
        pop []

        3 pops == (n / 2) pops
        so in worst-case; there are n/2 pops ~= n pops
            each with approximate cost of n
        ~n*n

        Space is O(n) since each replace allocates a new string

        T: O(n^2)
        S: O(n)
        """
        pairs = ["()", "[]", "{}"]

        while any(pair in s for pair in pairs):
            for p in pairs:
                s = s.replace(p, "")

        return s == ""

    def isValid(self, s: str) -> bool:
        """
        Optimal: stack

        If char is not an ending bracket, append to stack

        Once we reach a closing bracket, we check the stack
        to ensure the previous char pushed matches for the pair
        to be valid

        T: O(n)
        S: O(n)
        """
        clopen = {"]": "[", ")": "(", "}": "{"}

        stack = []
        for char in s:
            if char not in clopen:
                stack.append(char)
                continue

            # stack empty or last char doesn't match
            if not stack or stack.pop() != clopen[char]:
                return False

            # continue loop; no need to do anything after check

        return not stack
