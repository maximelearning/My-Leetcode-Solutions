"""
https://leetcode.com/problems/palindromic-substrings/

Given a string, your task is to count how 
many palindromic substrings in this string.

The substrings with different start indexes 
or end indexes are counted as different substrings 
even they consist of same characters.

Example 1:
Input: "abc"
Output: 3
Explanation: Three palindromic strings: "a", "b", "c".
 

Example 2:
Input: "aaa"
Output: 6
Explanation: Six palindromic strings: "a", "a", "a", "aa", "aa", "aaa".
 

Note:
The input string length won't exceed 1000.
"""

class Solution:
    def countSubstrings(self, s: str) -> int:
        def extendPalindrome(s, i, j):
            res = 0
            while i < len(s) and j < len(s) and i >= 0 and j >= 0 and s[i] == s[j]:
                res += 1
                i -= 1
                j += 1
            return res
        res = 0
        for i in range(len(s)):
            res += extendPalindrome(s, i, i)
            res += extendPalindrome(s, i, i + 1)
        return res