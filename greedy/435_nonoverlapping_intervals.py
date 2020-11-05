"""
https://leetcode.com/problems/non-overlapping-intervals/

Given a collection of intervals, find the minimum number 
of intervals you need to remove to make the rest of the 
intervals non-overlapping.

Example 1:
Input: [[1,2],[2,3],[3,4],[1,3]]
Output: 1
Explanation: [1,3] can be removed and the rest of intervals are non-overlapping.

Example 2:
Input: [[1,2],[1,2],[1,2]]
Output: 2
Explanation: You need to remove two [1,2] to make the rest of intervals non-overlapping.

Example 3:
Input: [[1,2],[2,3]]
Output: 0
Explanation: You don't need to remove any of the intervals since they're already non-overlapping.

Note:
You may assume the interval's end point is always bigger than its start point.
Intervals like [1,2] and [2,3] have borders "touching" but they don't overlap each other.
"""

class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        # Key is to sort by the earliest end times, since 
        # that allows us to maximize the number of non-overlapping
        # intervals to the right of the current interval.
        intervals.sort(key=lambda x: x[1])
        res = 0
        end = float('-inf')
        for interval in intervals:
            s = interval[0]
            e = interval[1]
            if s >= end:
                end = e
            else:
                res += 1
        return res