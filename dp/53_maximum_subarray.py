# https://leetcode.com/problems/maximum-subarray/

"""
Given an integer array nums, find the contiguous subarray 
(containing at least one number) which has the 
largest sum and return its sum.

Follow up: If you have figured out the O(n) solution, 
try coding another solution using the divide and conquer approach, 
which is more subtle.

Example 1:
Input: nums = [-2,1,-3,4,-1,2,1,-5,4]
Output: 6
Explanation: [4,-1,2,1] has the largest sum = 6.
"""


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        memo = [0] * len(nums)  # max subarray ending at given index
        memo[0] = nums[0]
        maximum = nums[0]
        for i in range(1, len(nums)):
            memo[i] = max(nums[i], memo[i-1] + nums[i])
            maximum = max(memo[i], maximum)
        return maximum
