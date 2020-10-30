"""
https://leetcode.com/problems/path-sum/

Given a binary tree and a sum, determine if the tree has 
a root-to-leaf path such that adding up all the values along 
the path equals the given sum.

Note: A leaf is a node with no children.

Example:
Given the below binary tree and sum = 22,
      5
     / \
    4   8
   /   / \
  11  13  4
 /  \      \
7    2      1
return true, as there exist a root-to-leaf path 5->4->11->2 which sum is 22.
"""


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def hasPathSum(self, root: TreeNode, target: int) -> bool:
        def traversal(node, s):
            if node is None:
                return False
            s -= node.val
            # leaf
            if node.left is None and node.right is None and s == 0:
                return True
            return traversal(node.left, s) or traversal(node.right, s)

        if root is None:
            return False
        return traversal(root, target)
