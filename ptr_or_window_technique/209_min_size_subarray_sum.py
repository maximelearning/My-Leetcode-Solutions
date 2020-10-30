"""
https://leetcode.com/problems/minimum-size-subarray-sum/

Given an array of n positive integers and a positive integer s, 
find the minimal length of a contiguous subarray of which the sum ≥ s. 
If there isn't one, return 0 instead.

Example: 

Input: s = 7, nums = [2,3,1,2,4,3]
Output: 2
Explanation: the subarray [4,3] has the minimal length under the problem constraint.
"""


class Solution:
    def minSubArrayLen(self, s: int, nums: List[int]) -> int:
        res = len(nums) + 1
        L = 0
        curS = 0
        # Basically if our window's sum is >= than s,
        # then we increment L until the sum falls below. Only
        # taking the min whenever it is suitable to do so (when curS >= s)
        # curS always represents the sum of the window L:R+1
        for R in range(len(nums)):
            curS += nums[R]
            while curS >= s:
                res = min(res, R - L + 1)
                curS -= nums[L]
                L += 1
        return res if res <= len(nums) else 0
