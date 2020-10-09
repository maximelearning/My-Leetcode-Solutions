import collections
"""
https://leetcode.com/problems/course-schedule/

There are a total of numCourses courses 
you have to take, labeled from 0 to numCourses-1.

Some courses may have prerequisites, 
for example to take course 0 you have to 
first take course 1, which is expressed as a pair: [0,1]

Given the total number of courses and a list 
of prerequisite pairs, is it possible for you 
to finish all courses?
 
Example 1:
Input: numCourses = 2, prerequisites = [[1,0]]
Output: true
Explanation: There are a total of 2 courses to take. 
             To take course 1 you should have finished course 0. So it is possible.

Example 2:
Input: numCourses = 2, prerequisites = [[1,0],[0,1]]
Output: false
Explanation: There are a total of 2 courses to take. 
             To take course 1 you should have finished course 0, and to take course 0 you should
             also have finished course 1. So it is impossible.
"""


class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        incoming = [0] * numCourses  # number of incoming edges
        # outgoing[y][x] is True if edge exists from y to x
        outgoing = [[0 for i in range(numCourses)] for j in range(numCourses)]
        ordering = []
        q = collections.deque()
        for pair in prerequisites:
            x, y = pair
            incoming[x] += 1
            outgoing[y][x] = True
        for i, j in enumerate(incoming):
            if j == 0:
                q.append(i)
        while len(q) > 0:  # Topological Sort
            u = q.popleft()
            ordering.append(u)
            for v, truth in enumerate(outgoing[u]):
                if truth:
                    incoming[v] -= 1
                    if incoming[v] == 0:
                        q.append(v)
        return len(ordering) == numCourses
