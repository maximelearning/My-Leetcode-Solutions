"""
https://leetcode.com/problems/set-matrix-zeroes/

Given an m x n matrix. If an element is 0, set 
its entire row and column to 0. Do it in-place.

Follow up:

A straight forward solution using O(mn) space is probably a bad idea.
A simple improvement uses O(m + n) space, but still not the best solution.
Could you devise a constant space solution?

Example 1:
Input: matrix = [[1,1,1],
                 [1,0,1],
                 [1,1,1]]
Output: [[1,0,1],
         [0,0,0],
         [1,0,1]]

Example 2:
Input: matrix = [[0,1,2,0],
                 [3,4,5,2],
                 [1,3,1,5]]
Output: [[0,0,0,0],
         [0,4,5,0],
         [0,3,1,0]]
"""


class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        rows = len(matrix)
        cols = len(matrix[0])
        if rows == 0:
            return
        elif matrix is None:
            return
        # Determine whether our flag row and flag column need to be zeroed later
        isRowZero = False
        isColZero = False
        for i in range(rows):
            if matrix[i][0] == 0:
                isRowZero = True
                break
        for j in range(cols):
            if matrix[0][j] == 0:
                isColZero = True
                break
        # Mark the first row and first column elements with a 0
        # if that column/row will be zeroed
        for i in range(1, rows):
            for j in range(1, cols):
                if matrix[i][j] == 0:
                    matrix[i][0] = 0
                    matrix[0][j] = 0
        # Zero out the rows/columns that are marked,
        # do not zero out the flag row/columns
        for i in range(1, rows):
            if matrix[i][0] == 0:
                for j in range(cols):
                    matrix[i][j] = 0
        for i in range(1, cols):
            if matrix[0][i] == 0:
                for j in range(rows):
                    matrix[j][i] = 0
        # Now we zero out the flag row or column
        # if we need to
        if isRowZero:
            for i in range(rows):
                matrix[i][0] = 0
        if isColZero:
            for i in range(cols):
                matrix[0][i] = 0
