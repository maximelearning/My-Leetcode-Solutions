# https: // leetcode.com/problems/subarray-sum-equals-k/

class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        res = 0
        summation = 0
        table = {0: 1}  # Does this running sum exist?
        for x in nums:
            summation += x
            res += table.get(summation-k, 0)
            table[summation] = table.get(summation, 0) + 1
        return res
