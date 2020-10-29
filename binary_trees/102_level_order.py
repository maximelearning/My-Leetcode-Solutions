import collections
"""
https://leetcode.com/problems/binary-tree-level-order-traversal/

Given a binary tree, return the level order traversal of its nodes' values. 
(ie, from left to right, level by level).

For example:
Given binary tree [3,9,20,null,null,15,7],
    3
   / \
  9  20
    /  \
   15   7
return its level order traversal as:
[
  [3],
  [9,20],
  [15,7]
]
"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        if root is None:
            return []
        res = []
        queue = collections.deque()
        queue.append((root, 1))
        while queue:
            node, lvl = queue.popleft()
            if len(res) < lvl:
                res.append([node.val])
            else:
                res[lvl - 1].append(node.val)
            if node.left:
                queue.append((node.left, lvl + 1))
            if node.right:
                queue.append((node.right, lvl + 1))
        return res
