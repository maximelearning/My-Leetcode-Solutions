"""
https://leetcode.com/problems/search-a-2d-matrix/

Write an efficient algorithm that searches for a value in an m x n matrix. 
This matrix has the following properties:
Integers in each row are sorted from left to right.
The first integer of each row is greater than the last integer 
of the previous row.
 

Example 1:
Input: matrix = [[1,3,5,7],
                 [10,11,16,20],
                 [23,30,34,50]], 
       target = 3
Output: true

Example 2:
Input: matrix = [[1,3,5,7],
                 [10,11,16,20],
                 [23,30,34,50]], 
       target = 13
Output: false

Example 3:
Input: matrix = [], target = 0
Output: false
"""


class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if len(matrix) == 0 or len(matrix[0]) == 0:
            return False
        row = len(matrix)
        col = len(matrix[0])
        i = 0
        j = row * col - 1
        # essence is to treat the input like a single sorted linear array
        while i <= j:
            m = int((i + j)/2)
            v = matrix[int(m / col)][m % col]
            if v == target:
                return True
            elif target < v:
                j = m - 1
            else:
                i = m + 1
        return False
