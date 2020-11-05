"""
https://leetcode.com/problems/max-consecutive-ones-ii/

Given a binary array, find the maximum number of 
consecutive 1s in this array if you can flip at most one 0.

Example 1:
Input: [1,0,1,1,0]
Output: 4
Explanation: Flip the first zero will get the the maximum number of consecutive 1s.
    After flipping, the maximum number of consecutive 1s is 4.

Note:
    The input array will only contain 0 and 1.
    The length of input array is a positive integer and will not exceed 10,000
"""


class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        m = 0
        # prev must be -1 because
        # there may or may not be a 0 at the beginning
        # in which case our max calculation could be wrong.
        # so -1 for prev cancels out with the + 1
        prev = -1
        cur = 0
        for n in nums:
            if n == 0:
                prev, cur = cur, 0
            else:
                cur += 1
            m = max(m, prev + 1 + cur)
        return m
