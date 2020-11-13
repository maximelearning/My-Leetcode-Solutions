"""
https://leetcode.com/problems/add-strings/

Given two non-negative integers num1 and num2 
represented as string, return the sum of num1 and num2.

Note:

The length of both num1 and num2 is < 5100.
Both num1 and num2 contains only digits 0-9.
Both num1 and num2 does not contain any leading zero.
You must not use any built-in library or convert the inputs to integer directly.
"""

class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        d = {"0":0,"1":1,"2":2,"3":3,"4":4,"5":5,"6":6,"7":7,"8":8,"9":9}
        i = len(num1) - 1
        j = len(num2) - 1
        carry = 0
        res = []
        while i >= 0 or j >= 0:
            x = 0
            y = 0
            if i >= 0:
                x = d[num1[i]]
            if j >= 0:
                y = d[num2[j]]
            v = x + y + carry
            carry = v // 10
            res.append(v % 10)
            i -= 1
            j -= 1
        if carry > 0:
            res.append(carry)
        return "".join(str(i) for i in res)[::-1]