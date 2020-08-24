import collections
# https://leetcode.com/problems/is-graph-bipartite/


class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        colors = {}
        queue = collections.deque()
        for i in range(len(graph)):  # Incase of disconnected graph
            if i in colors.keys():
                continue
            queue.append(i)
            colors[i] = 1
            while len(queue) > 0:  # BFS
                j = queue.popleft()
                neighbors = graph[j]
                for k in neighbors:
                    if k not in colors.keys():
                        colors[k] = -colors[j]
                        queue.append(k)
                    elif colors[k] == colors[j]:
                        return False
        return True
