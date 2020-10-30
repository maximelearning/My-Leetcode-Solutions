"""
https://leetcode.com/problems/max-consecutive-ones-iii/

Given an array A of 0s and 1s, we may change up to K values from 0 to 1.
Return the length of the longest (contiguous) subarray that contains only 1s. 
 
Example 1:
Input: A = [1,1,1,0,0,0,1,1,1,1,0], K = 2
Output: 6
Explanation: 
[1,1,1,0,0,1,1,1,1,1,1]
Bolded numbers were flipped from 0 to 1.  The longest subarray is underlined.

Example 2:
Input: A = [0,0,1,1,0,0,1,1,1,0,1,1,0,0,0,1,1,1,1], K = 3
Output: 10
Explanation: 
[0,0,1,1,1,1,1,1,1,1,1,1,0,0,0,1,1,1,1]
Bolded numbers were flipped from 0 to 1.  The longest subarray is underlined.

Note:
1 <= A.length <= 20000
0 <= K <= A.length
A[i] is 0 or 1 
"""


class Solution:
    def longestOnes(self, A: List[int], K: int) -> int:
        n = len(A)
        cur_k = 0
        m = 0
        L = 0
        # Essence: Increment R, and if the cur_k is > K, then we need to move the left
        # pointer of our window forward until cur_k is <= K.
        for R in range(n):
            if A[R] == 0:
                cur_k += 1
            while cur_k > K:
                if A[L] == 0:
                    cur_k -= 1
                L += 1
            m = max(m, R - L + 1)
        return m
