# https://leetcode.com/problems/longest-common-subsequence/

class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        memo = [[0 for j in range(len(text2) + 1)]
                for i in range(len(text1) + 1)]
        for i in range(len(text1)):
            for j in range(len(text2)):
                if text1[i] == text2[j]:
                    memo[i + 1][j + 1] = memo[i][j] + 1
                else:
                    memo[i + 1][j + 1] = max(memo[i][j + 1], memo[i + 1][j])
        return memo[len(text1)][len(text2)]
