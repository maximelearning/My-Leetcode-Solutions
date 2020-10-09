# https://leetcode.com/problems/longest-substring-without-repeating-characters/

"""
Given a string s, find the length of the longest 
substring without repeating characters.

Example 1:
Input: s = "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3.

Example 2:
Input: s = "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.

Example 3:
Input: s = "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3.
Notice that the answer must be a substring, 
"pwke" is a subsequence and not a substring.
"""


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left = 0
        maximum = 0
        seen = {}
        for right in range(len(s)):
            char = s[right]
            if char not in seen:
                maximum = max(right - left + 1, maximum)
            else:
                if seen[char] >= left:
                    left = seen[char] + 1
                else:
                    maximum = max(right - left + 1, maximum)
            seen[char] = right
        return maximum
