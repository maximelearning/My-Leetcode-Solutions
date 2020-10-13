import heapq
"""
https://leetcode.com/problems/meeting-rooms-ii/

Given an array of meeting time intervals consisting of start 
and end times [[s1,e1],[s2,e2],...] (si < ei), find the minimum 
number of conference rooms required.

Example 1:

Input: [[0, 30],[5, 10],[15, 20]]
Output: 2
"""


class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        if intervals is None or len(intervals) <= 0:
            return 0
        intervals.sort(key=lambda x: x[0])
        heap = []  # ending times, free rooms
        heapq.heappush(heap, intervals[0][1])
        for i in intervals[1:]:
            if i[0] >= heap[0]:
                heapq.heappop(heap)
            heapq.heappush(heap, i[1])

        return len(heap)
