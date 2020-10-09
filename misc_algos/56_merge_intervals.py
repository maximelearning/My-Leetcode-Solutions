# https://leetcode.com/problems/merge-intervals/

"""
Given a collection of intervals, merge all overlapping intervals.

Example 1:
Input: intervals = [[1,3],[2,6],[8,10],[15,18]]
Output: [[1,6],[8,10],[15,18]]
Explanation: Since intervals [1,3] and [2,6] 
overlaps, merge them into [1,6].

Example 2:
Input: intervals = [[1,4],[4,5]]
Output: [[1,5]]
Explanation: Intervals [1,4] and [4,5] 
are considered overlapping.
"""


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
