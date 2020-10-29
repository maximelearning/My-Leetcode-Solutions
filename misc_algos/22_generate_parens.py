"""
https://leetcode.com/problems/generate-parentheses/

Given n pairs of parentheses, write a function to 
generate all combinations of well-formed parentheses.

Example 1:
Input: n = 3
Output: ["((()))","(()())","(())()","()(())","()()()"]

Example 2:
Input: n = 1
Output: ["()"]
"""


class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        def gen(s, left, right):
            if len(s) == 2 * n:
                self.res.append(s)
                return
            # append lefts
            if left < n:
                gen(s + "(", left + 1, right)
            # only append rights if more lefts
            if right < left:
                gen(s + ")", left, right + 1)
        self.res = []
        gen("", 0, 0)
        return self.res
