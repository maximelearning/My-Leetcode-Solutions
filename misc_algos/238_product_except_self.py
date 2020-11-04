"""
https://leetcode.com/problems/product-of-array-except-self/

Given an array nums of n integers where n > 1,  
return an array output such that output[i] is 
equal to the product of all the elements of nums 
except nums[i].

Example:
Input:  [1,2,3,4]
Output: [24,12,8,6]

Constraint: It's guaranteed that the product of the elements 
of any prefix or suffix of the array (including the whole array) fits in a 32 bit integer.
Note: Please solve it without division and in O(n).

Follow up:
Could you solve it with constant space complexity? 
(The output array does not count as extra space for 
the purpose of space complexity analysis.)

res[0] = 1
res[i] = product from 0 to i - 1


"""


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        res = [0 for i in range(n)]
        p = 1
        # res[i] will be the product of elements from
        # 0 to i-1, aka the prefix product. In other words,
        # the product to the left of any given element.
        for i in range(0, n):
            res[i] = p
            p = nums[i] * p
        p = 1
        # now we build a running suffix product, aka the product
        # to the right of a given element, to multiply to
        # each of our prefix products, and simply store in res.
        for j in range(n - 1, -1, -1):
            res[j] = res[j] * p
            p = nums[j] * p
        return res
