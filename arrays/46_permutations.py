"""
https://leetcode.com/problems/permutations/

Given a collection of distinct integers, return all possible permutations.

Example:

Input: [1,2,3]
Output:
[
  [1,2,3],
  [1,3,2],
  [2,1,3],
  [2,3,1],
  [3,1,2],
  [3,2,1]
]
"""


class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        def dfs(cur, path, res):
            if not cur:
                res.append(path)
            else:
                for i in range(len(cur)):
                    dfs(cur[:i] + cur[i+1:], path + [cur[i]], res)
        res = []
        dfs(nums, [], res)
        return res
