# https://leetcode.com/problems/longest-substring-without-repeating-characters/

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
