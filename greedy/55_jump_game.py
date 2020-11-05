"""
https://leetcode.com/problems/jump-game/

Given an array of non-negative integers, you are 
initially positioned at the first index of the array.

Each element in the array represents your 
maximum jump length at that position.

Determine if you are able to reach the last index.

Example 1:
Input: nums = [2,3,1,1,4]
Output: true
Explanation: Jump 1 step from index 0 to 1, then 3 steps to the last index.

Example 2:
Input: nums = [3,2,1,0,4]
Output: false
Explanation: You will always arrive at index 3 no matter what. 
Its maximum jump length is 0, which makes it impossible to reach the last index.
 
Constraints:

1 <= nums.length <= 3 * 10^4
0 <= nums[i][j] <= 10^5
"""

class Solution:
    def canJump(self, nums: List[int]) -> bool:
        n = len(nums)
        max_reach = 0
        # greedy since our max_reach allows us to get to any 
        # index from 0 to max_reach
        for i in range(n):
            # there is no path from 0 to i
            if max_reach < i:
                return False
            # we found a path from 0 to n - 1
            elif max_reach >= n - 1:
                return True
            # either our current reach is the furthest, 
            # or i + the next jump is
            # note: we know we can reach i, since if we couldn't
            #       then we would've failed in the above cases
            max_reach = max(max_reach, nums[i] + i)
        return max_reach >= n - 1