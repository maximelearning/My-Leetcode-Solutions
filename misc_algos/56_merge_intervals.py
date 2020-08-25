# https://leetcode.com/problems/merge-intervals/

class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        result = []
        for i in sorted(intervals, key=lambda x: x[0]):
            if len(result) > 0 and result[-1][1] >= i[0]:
                merged = [result[-1][0], max(result[-1][1], i[1])]
                result.pop()
                result.append(merged)
            else:
                result.append(i)
        return result


"""
===================================
|result[-1][0]       result[-1][1]|
===================================
                ===============================
                |i[0]                     i[1]|
                ===============================
Since we know the starting indices for the intervals
are sorted, we only need to compare the ending value of 
the previously processed interval with the next 
interval's starting value.
result[-1][0] is always <= i[0]
"""
