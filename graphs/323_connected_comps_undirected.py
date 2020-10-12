import collections
"""
https://leetcode.com/problems/number-of-connected-components-in-an-undirected-graph/

Given n nodes labeled from 0 to n - 1 and a list of undirected edges 
(each edge is a pair of nodes), write a function to find the number of 
connected components in an undirected graph.

Example 1:
Input: n = 5 and edges = [[0, 1], [1, 2], [3, 4]]
     0          3
     |          |
     1 --- 2    4 
Output: 2

Example 2:
Input: n = 5 and edges = [[0, 1], [1, 2], [2, 3], [3, 4]]
     0           4
     |           |
     1 --- 2 --- 3
Output:  1

Note:
You can assume that no duplicate edges will appear in edges. 
Since all edges are undirected, [0, 1] is the same as [1, 0] 
and thus will not appear together in edges.
"""


class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        def bfs(v, visited, adj):
            q = collections.deque()
            q.append(v)
            while q:
                u = q.popleft()
                visited[u] = 1
                for neigh in adj[u]:
                    if visited[neigh] == 0:
                        q.append(neigh)
        adj = {x: [] for x in range(n)}  # convert edges list into dictionary
        for e in edges:
            adj[e[0]].append(e[1])
            adj[e[1]].append(e[0])
        visited = [0 for i in range(n)]  # 1 means it is marked visited
        res = 0
        for v in range(0, n):  # visit all vertices, and bfs only unvisited vertices
            if visited[v] == 0:
                bfs(v, visited, adj)
                res += 1
        return res
