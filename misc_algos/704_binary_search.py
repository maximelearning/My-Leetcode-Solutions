"""
https://leetcode.com/problems/binary-search/

Given a sorted (in ascending order) integer array nums 
of n elements and a target value, write a function to 
search target in nums. If target exists, then return 
its index, otherwise return -1.

Example 1:
Input: nums = [-1,0,3,5,9,12], target = 9
Output: 4
Explanation: 9 exists in nums and its index is 4

Example 2:
Input: nums = [-1,0,3,5,9,12], target = 2
Output: -1
Explanation: 2 does not exist in nums so return -1
"""


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        i = 0
        j = len(nums) - 1
        while i <= j:
            mid = int((i + j)/2)
            if target < nums[mid]:
                j = mid - 1
            elif target > nums[mid]:
                i = mid + 1
            else:
                return mid
        return -1
