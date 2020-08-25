# https://leetcode.com/problems/climbing-stairs/

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
