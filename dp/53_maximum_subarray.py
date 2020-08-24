# https://leetcode.com/problems/maximum-subarray/

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
