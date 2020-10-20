"""
https://leetcode.com/problems/partition-labels/

A string S of lowercase English letters is given. 
We want to partition this string into as many parts 
as possible so that each letter appears in at most 
one part, and return a list of integers representing 
the size of these parts.

Example 1:
Input: S = "ababcbacadefegdehijhklij"
Output: [9,7,8]
Explanation:
The partition is "ababcbaca", "defegde", "hijhklij".
This is a partition so that each letter appears in at most one part.
A partition like "ababcbacadefegde", "hijhklij" is incorrect,
because it splits S into less parts.

Note:
S will have length in range [1, 500].
S will consist of lowercase English letters ('a' to 'z') only.
"""


class Solution:
    def partitionLabels(self, S: str) -> List[int]:
        left = 0
        right = 0
        res = []
        d = {}  # last occuring
        i = 0
        # preprocess
        # record the last index for each character
        for c in S:
            d[c] = i
            i += 1
        # loop through all the characters
        for j in range(len(S)):
            c = S[j]
            # record the rightmost indice for the current substring S[left:j + 1]
            # recall that for any given substring, it's size can only be as small
            # as the rightmost occuring character of the string
            right = max(right, d[c])
            # since right is the rightmost index for the characters in the set(S[left:j+1]),
            # and we then now find that j == right, then this is a valid substring, as
            # the rightmost indices of any of S[left:j+1]'s characters is not to the right of
            # index j, if right == j. This is because of taking the max each iteration.
            if j == right:
                res.append(right - left + 1)
                left = j + 1
        return res
