"""
https://leetcode.com/problems/binary-tree-maximum-path-sum/

Given a non-empty binary tree, find the maximum path sum.
For this problem, a path is defined as any sequence 
of nodes from some starting node to any node in the 
tree along the parent-child connections. The path must 
contain at least one node and does not need to go through the root.

Example 1:
Input: [1,2,3]
       1
      / \
     2   3
Output: 6

Example 2:
Input: [-10,9,20,null,null,15,7]
   -10
   / \
  9  20
    /  \
   15   7
Output: 42
"""


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def maxPathSum(self, root: TreeNode) -> int:
        def traversal(node):
            if node is None:
                return 0
            left = max(0, traversal(node.left))
            right = max(0, traversal(node.right))
            self.res = max(self.res, left + right + node.val)
            return max(left, right) + node.val
        if root is None:
            return 0
        self.res = float("-inf")
        traversal(root)
        return self.res
