# https://leetcode.com/problems/valid-parentheses/

class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        dict = {"]": "[", "}": "{", ")": "("}
        for char in s:
            if char in dict.keys():
                if len(stack) == 0 or dict[char] != stack.pop():
                    return False
            else:
                stack.append(char)
        return len(stack) == 0
