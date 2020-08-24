import collections
# https://leetcode.com/problems/course-schedule/


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
