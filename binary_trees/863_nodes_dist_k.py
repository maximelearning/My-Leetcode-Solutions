import collections
"""
https://leetcode.com/problems/all-nodes-distance-k-in-binary-tree/

We are given a binary tree (with root node root), 
a target node, and an integer value K.

Return a list of the values of all nodes that have a 
distance K from the target node.  The answer can be 
returned in any order.

Example 1:

Input: root = [3,5,1,6,2,0,8,null,null,7,4], target = 5, K = 2
                3
               / \
              5   1
             / \ / \
            6  2 0  8
              / \
             7   4

Output: [7,4,1]

Explanation: 
The nodes that are a distance 2 from the target node (with value 5)
have values 7, 4, and 1.

Note that the inputs "root" and "target" are actually TreeNodes.
The descriptions of the inputs above are just serializations of these objects.
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, K: int) -> List[int]:
        def traversal(node, adj, parent):
            if node is None:
                return
            adj[node.val] = []
            if parent:
                adj[node.val] += [parent.val]
            if node.left:
                adj[node.val] += [node.left.val]
            if node.right:
                adj[node.val] += [node.right.val]
            traversal(node.left, adj, node)
            traversal(node.right, adj, node)
        adj = {}
        traversal(root, adj, None)
        res = []
        q = collections.deque()
        q.append((target.val, K))
        visited = set()
        visited.add(target.val)
        while len(q) > 0:
            v, dist = q.popleft()
            if dist == 0:
                res.append(v)
                continue
            for u in adj[v]:
                if u not in visited:
                    q.append((u, dist - 1))
                    visited.add(u)
        return res
