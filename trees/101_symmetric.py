"""
https://leetcode.com/problems/symmetric-tree/

Given a binary tree, check whether it is a mirror of 
itself (ie, symmetric around its center).

For example, this binary tree [1,2,2,3,4,4,3] is symmetric:
    1
   / \
  2   2
 / \ / \
3  4 4  3
 

But the following [1,2,2,null,3,null,3] is not:
    1
   / \
  2   2
   \   \
   3    3
"""


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        def traversal(node1, node2):
            if node1 is None and node2 is None:
                return True
            elif node1 is None or node2 is None:
                return False
            else:
                return node1.val == node2.val and traversal(node1.left, node2.right) and traversal(node1.right, node2.left)
        if root is None:
            return True
        return traversal(root.left, root.right)
