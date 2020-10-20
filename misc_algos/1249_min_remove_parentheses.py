"""
https://leetcode.com/problems/minimum-remove-to-make-valid-parentheses/

Given a string s of '(' , ')' and lowercase English characters. 

Your task is to remove the minimum number of parentheses 
( '(' or ')', in any positions ) so that the resulting 
parentheses string is valid and return any valid string.

Formally, a parentheses string is valid if and only if:

It is the empty string, contains only lowercase characters, or
It can be written as AB (A concatenated with B), where A and B are valid strings, or
It can be written as (A), where A is a valid string.
 
Example 1:
Input: s = "lee(t(c)o)de)"
Output: "lee(t(c)o)de"
Explanation: "lee(t(co)de)" , "lee(t(c)ode)" would also be accepted.

Example 2:
Input: s = "a)b(c)d"
Output: "ab(c)d"

Example 3:
Input: s = "))(("
Output: ""
Explanation: An empty string is also valid.

Example 4:
Input: s = "(a(b(c)d)"
Output: "a(b(c)d)"
"""


class Solution:
    def minRemoveToMakeValid(self, s):
        """
        We can always remove ")" based on the stack. But not
        necessarily "(" until we are finished. In that case, 
        save the indices of "(", to be removed at the very end.
        """
        res = list(s)
        stack = []  # record indices of "(" only
        i = 0
        for c in res:
            if c == "(":
                stack.append(i)  # append the INDICE of "("
            elif c == ")":
                if len(stack) == 0:  # actually change to ""
                    res[i] = ""
                else:  # otherwise pop the indice of the last "("
                    stack.pop()
            i += 1
        # remove the remaining "("
        while stack:
            res[stack.pop()] = ""
        return "".join(res)
