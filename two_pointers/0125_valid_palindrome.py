"""
A phrase is a palindrome if, after converting all
uppercase letters into lowercase letters and removing
all non-alphanumeric characters, it reads the same
forward and backward. Alphanumeric characters include
letters and numbers.

Given a string s, return true if it is a palindrome, or false otherwise.
"""

class Solution:
    def isPalindrome(self, s: str) -> bool:
        """
        Brute force: build out list of alphanumeric characters

        Two pointer on the list to check that the list
        is palindromic

        ex:
        race a car
        lst = [r,a,c,e,a,c,a,r]
            + + + - - + + +
            the middle a and e don't match; not a palindrome

        T: O(n)
        S: O(n)
        """
        lst = []

        # build out list
        for char in s:
            if char.isalnum():
                lst.append(char.lower())  # normalize appends

        # check if the list is palindromic
        l, r = 0, len(lst) - 1
        while l < r:
            if lst[l] != lst[r]:
                return False
            l += 1
            r -= 1

        return True

    def isPalindrome(self, s: str) -> bool:
        """
        Optimal: remove additional space via in-place traversal

        Still two pointers, just skips over non-relevant
        characters (i.e., non-alphanumeric)

        T: O(n)
        S: O(1)
        """
        n = len(s)
        l, r = 0, n - 1

        # check alpnumeric normalized pairs
        while l < r:
            # shift l to next alphanumeric (rightward)
            while l < r and not s[l].isalnum():
                l += 1
            
            # shift r to next alphanumeric (leftward)
            while l < r and not s[r].isalnum():
                r -= 1

            # l and r pointers overlap
            if l >= r:
                break

            if s[l].lower() != s[r].lower():
                return False

            l += 1
            r -= 1

        return True
