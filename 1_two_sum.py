# https://leetcode.com/problems/two-sum/

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        value_to_index = {}
        for c, v in enumerate(nums):
            if target - v in value_to_index.keys():
                return [c, value_to_index[target - v]]
            else:
                value_to_index[v] = c
        return [None, None]
