# https: // leetcode.com/problems/subarray-sum-equals-k/

"""
Given an array of integers and an integer k, you need 
to find the total number of continuous subarrays whose sum equals to k.

Example 1:
Input:nums = [1,1,1], k = 2
Output: 2
"""


class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        res = 0
        summation = 0
        table = {0: 1}  # Does this running sum exist?
        for x in nums:
            summation += x
            # if the running sum - target value = a running sum that
            # we have already encountered, then we have an additional subarray
            # occurrence
            res += table.get(summation-k, 0)
            # record the running sum
            table[summation] = table.get(summation, 0) + 1
        return res
