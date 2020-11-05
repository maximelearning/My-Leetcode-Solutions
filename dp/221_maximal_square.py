"""
https://leetcode.com/problems/maximal-square/

Given a 2D binary matrix filled with 0's and 1's, 
find the largest square containing only 1's and return its area.

Example:
Input: 

1 0 1 0 0
1 0 1 1 1
1 1 1 1 1
1 0 0 1 0

Output: 4
"""


class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        if len(matrix) <= 0 or matrix is None:
            return 0
        maximum = 0
        row = len(matrix)
        col = len(matrix[0])
        dp = [[0 for j in range(0, col)] for i in range(0, row)]
        for i in range(0, row):
            for j in range(0, col):
                if i == 0 and j == 0 and matrix[i][j] == '1':  # base case
                    dp[i][j] = 1
                elif matrix[i][j] == '1':
                    # geometry insight, take min since there are 3 possible
                    # squares and whether this corner is part of a square is only
                    # as good as the weakest of the 3 links around it, since a single 0
                    # disrupts the entire square
                    dp[i][j] = min(dp[i-1][j-1], dp[i-1][j], dp[i][j-1]) + 1
                else:
                    dp[i][j] = 0  # since it breaks
                maximum = max(maximum, dp[i][j])
        return maximum*maximum
