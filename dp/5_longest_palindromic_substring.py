"""
https://leetcode.com/problems/longest-palindromic-substring/

Given a string s, return the longest palindromic substring in s.

Example 1:
Input: s = "babad"
Output: "bab"
Note: "aba" is also a valid answer.

Example 2:
Input: s = "cbbd"
Output: "bb"

Example 3:
Input: s = "a"
Output: "a"

Example 4:
Input: s = "ac"
Output: "a"
"""


class Solution:
    def longestPalindrome(self, s: str) -> str:
        if len(s) == 0:
            return ""
        palindrome = s[:1]
        for i in range(len(s) - 1):
            p1 = self.expandPalindrome(s, i, i)  # odd
            if len(p1) > len(palindrome):
                palindrome = p1
            if s[i] == s[i + 1]:
                p2 = self.expandPalindrome(s, i, i + 1)  # even
                if len(p2) > len(palindrome):
                    palindrome = p2
        return palindrome

    def expandPalindrome(self, s: str, i: int, j: int) -> str:
        while i >= 0 and j < len(s) and s[i] == s[j]:
            i -= 1
            j += 1
        return s[i+1:j]
