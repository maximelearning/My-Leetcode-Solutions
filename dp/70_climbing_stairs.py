# https://leetcode.com/problems/climbing-stairs/

"""
You are climbing a stair case. It takes n steps to reach to the top.
Each time you can either climb 1 or 2 steps. 
In how many distinct ways can you climb to the top?

Example 1:
Input: 2
Output: 2
Explanation: There are two ways to climb to the top.
1. 1 step + 1 step
2. 2 steps

Example 2:
Input: 3
Output: 3
Explanation: There are three ways to climb to the top.
1. 1 step + 1 step + 1 step
2. 1 step + 2 steps
3. 2 steps + 1 step

"""


class Solution:
    def climbStairs(self, n: int) -> int:
        memo = [0 for i in range(n + 1)]
        return self.helper(0, n, memo)

    def helper(self, x: int, n: int, memo: List[int]) -> int:
        if x == n:
            return 1
        elif x > n:
            return 0
        if memo[x] == 0:
            memo[x] = self.helper(x + 1, n, memo) + self.helper(x + 2, n, memo)
        return memo[x]
