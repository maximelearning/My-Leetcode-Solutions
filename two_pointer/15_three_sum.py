"""
https://leetcode.com/problems/3sum/

Given an array nums of n integers, are there 
elements a, b, c in nums such that a + b + c = 0? 
Find all unique triplets in the array which gives the sum of zero.
Notice that the solution set must not contain duplicate triplets.

Example 1:
Input: nums = [-1,0,1,2,-1,-4]
Output: [[-1,-1,2],[-1,0,1]]

Example 2:
Input: nums = []
Output: []

Example 3:
Input: nums = [0]
Output: []
"""


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []
        for l in range(len(nums) - 2):
            if l > 0 and nums[l] == nums[l-1]:
                continue
            m = l + 1
            r = len(nums) - 1
            while m < r:
                s = nums[l] + nums[m] + nums[r]
                if s < 0:
                    m += 1
                elif s > 0:
                    r -= 1
                else:
                    res.append([nums[l], nums[m], nums[r]])
                    # To not create duplicates, skip over
                    while m < r and nums[m] == nums[m+1]:
                        m += 1
                    while m < r and nums[r] == nums[r-1]:
                        r -= 1
                    m += 1
                    r -= 1
        return res
