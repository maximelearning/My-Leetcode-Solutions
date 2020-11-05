"""
https://leetcode.com/problems/spiral-matrix/

Given a matrix of m x n elements (m rows, n columns), 
return all elements of the matrix in spiral order.

Example 1:
Input:
[
 [ 1, 2, 3 ],
 [ 4, 5, 6 ],
 [ 7, 8, 9 ]
]
Output: [1,2,3,6,9,8,7,4,5]

Example 2:
Input:
[
  [1, 2, 3, 4],
  [5, 6, 7, 8],
  [9,10,11,12]
]
Output: [1,2,3,4,8,12,11,10,9,5,6,7]
"""

class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        if len(matrix) == 0:
            return []
        rowBegin = 0
        rowEnd = len(matrix) - 1
        colBegin = 0
        colEnd = len(matrix[0]) - 1
        res = []
        while rowBegin <= rowEnd and colBegin <= colEnd:

            # right
            for i in range(colBegin, colEnd + 1):
                res.append(matrix[rowBegin][i])

            # down
            rowBegin = rowBegin + 1
            for j in range(rowBegin, rowEnd + 1):
                res.append(matrix[j][colEnd])

            # left
            colEnd = colEnd - 1
            if rowBegin <= rowEnd:  # Make sure there is a row to traverse
                for k in range(colEnd, colBegin - 1, -1):
                    res.append(matrix[rowEnd][k])
                    
            # up
            rowEnd = rowEnd - 1
            if colBegin <= colEnd:  # Make sure there is a column to traverse
                for l in range(rowEnd, rowBegin - 1, -1):
                    res.append(matrix[l][colBegin])
            colBegin = colBegin + 1
            
        return res