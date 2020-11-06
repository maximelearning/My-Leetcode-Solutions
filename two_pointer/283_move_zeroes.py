"""
https://leetcode.com/problems/move-zeroes/

Given an array nums, write a function to move all 0's 
to the end of it while maintaining the relative order 
of the non-zero elements.

Example:

Input: [0,1,0,3,12]
Output: [1,3,12,0,0]
Note:

You must do this in-place without making a copy of the array.
Minimize the total number of operations.
"""


class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # EXPLANATION:
        # We will iterate from left to right
        # We will bunch up our zeroes as we go along the path
        # When we see a non-zero value, we will switch it
        #   with the left most zero in our bunched up zeroes
        #   
        # [0,1,0,3] start, we increment num_zeroes by 1 since index 0 has a 0
        # [1,0,0,3] switched index 0 and 1, since index 1 was a 0.
        # [1,0,0,3] increment num_zeroes by 1 again, since index 2 is a 0
        # [1,3,0,0] now we switch index 3 with the left most 0 (index 1)
        num_zeroes = 0
        for i in range(len(nums)):
            if nums[i] == 0:
                num_zeroes = num_zeroes + 1
            elif num_zeroes > 0:
                nums[i], nums[i - num_zeroes] = nums[i - num_zeroes], nums[i]
