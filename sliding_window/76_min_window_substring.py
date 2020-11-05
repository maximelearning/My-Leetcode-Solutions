"""
https://leetcode.com/problems/minimum-window-substring/

Given two strings s and t, return the minimum window in s 
which will contain all the characters in t. If there is no such 
window in s that covers all characters in t, return the empty string "".

Note that If there is such a window, it is guaranteed that 
there will always be only one unique minimum window in s.
Also t can have repeating characters.

Example 1:
Input: s = "ADOBECODEBANC", t = "ABC"
Output: "BANC"

Example 2:
Input: s = "a", t = "a"
Output: "a"
 
Constraints:

1 <= s.length, t.length <= 105
s and t consist of English letters.
"""

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        n = len(s)
        m_target = len(t)
        d = {}
        for c in t:
            d[c] = d.get(c, 0) + 1
        left = 0
        cur_best = ""
        min_len = float('inf')
        for right in range(n):
            c = s[right]
            if c in d:
                # decrement the length of the target size, tracks whether
                # we have seen all the characters in our window or not
                if d[c] > 0:
                    m_target = m_target - 1
                # can have negative counts, since we might
                # add back the counts later to move left forward
                d[c] = d[c] - 1
            # while we have all t's characters are in our window
            while m_target == 0:
                # update our best
                if min_len > right - left + 1:
                    cur_best = s[left:right+1]
                    min_len = right - left + 1
                left_c = s[left]
                # if the left character is a target character
                if left_c in d:
                    # increment its count in d
                    d[left_c] = d[left_c] + 1
                    # if that count then becomes positive, we then have
                    # a window that is invalid after moving left forward by one.
                    # So we increment the required characters by 1.
                    if d[left_c] > 0:
                        m_target = m_target + 1
                left = left + 1
        return cur_best