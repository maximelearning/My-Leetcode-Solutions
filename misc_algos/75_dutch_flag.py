"""
https://leetcode.com/problems/sort-colors/

Given an array nums with n objects colored red, white, 
or blue, sort them in-place so that objects of the same 
color are adjacent, with the colors in the order red, white, and blue.

Here, we will use the integers 0, 1, and 2 to represent 
the color red, white, and blue respectively.

Follow up:
Could you come up with a one-pass algorithm using only O(1) constant space?
 
Example 1:
Input: nums = [2,0,2,1,1,0]
Output: [0,0,1,1,2,2]

Example 2:
Input: nums = [2,0,1]
Output: [0,1,2]

Example 3:
Input: nums = [0]
Output: [0]

Example 4:
Input: nums = [1]
Output: [1]
"""


class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        i = 0
        j = 0
        k = len(nums) - 1
        n = len(nums)
        while j <= k:
            c = nums[j]
            if c == 0:
                nums[i], nums[j] = nums[j], nums[i]
                i += 1
                j += 1
            elif c == 1:
                j += 1
            else:
                nums[k], nums[j] = nums[j], nums[k]
                k -= 1


"""
 0       i       j       k      n
================================
| zeros | ones  | mixed | twos |
================================

0 <= zeroes <= i - 1
i <= ones <= j - 1
j <= mixed <= k - 1
k <= twos <= n - 1
"""
