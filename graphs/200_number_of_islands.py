"""
https://leetcode.com/problems/number-of-islands/

Given a 2d grid map of '1's (land) and '0's (water), 
count the number of islands. An 
island is surrounded by water and is 
formed by connecting adjacent lands horizontally 
or vertically. You may assume 
all four edges of the grid are all surrounded by water.

Example 1:
Input: grid = [
  ["1","1","1","1","0"],
  ["1","1","0","1","0"],
  ["1","1","0","0","0"],
  ["0","0","0","0","0"]
]
Output: 1

Example 2:
Input: grid = [
  ["1","1","0","0","0"],
  ["1","1","0","0","0"],
  ["0","0","1","0","0"],
  ["0","0","0","1","1"]
]
Output: 3
"""


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0
        num = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == "1":
                    self.dfs(grid, i, j)
                    num += 1
        return num

    def dfs(self, grid: List[List[str]], i: int, j: int) -> None:
        if i >= len(grid) or j >= len(grid[0]) or i < 0 or j < 0 or grid[i][j] == "0":
            return
        else:
            grid[i][j] = "0"
            self.dfs(grid, i - 1, j)
            self.dfs(grid, i, j - 1)
            self.dfs(grid, i + 1, j)
            self.dfs(grid, i, j + 1)
