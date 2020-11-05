"""
https://leetcode.com/problems/count-complete-tree-nodes/

Given a complete binary tree, count the number of nodes.

Note:

Definition of a complete binary tree from Wikipedia:
In a complete binary tree every level, except possibly the last, 
is completely filled, and all nodes in the last level are as far 
left as possible. It can have between 1 and 2h nodes inclusive at 
the last level h.

Example:

Input: 
    1
   / \
  2   3
 / \  /
4  5 6

Output: 6
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    # perfect binary tree: all levels are filled to the max
    # complete binary tree: all levels except maybe the last one, is filled to the max
    def countNodes(self, root: TreeNode) -> int:
        if root is None:
            return 0
        depth_left = self.calculate_depth(root.left)
        depth_right = self.calculate_depth(root.right)
        # left is perfect binary tree, right is complete binary tree
        if depth_left == depth_right:
            return pow(2, depth_left) + self.countNodes(root.right)
        # left is complete binary tree, right is perfect binary tree
        else:
            return pow(2, depth_right) + self.countNodes(root.left)
        

    def calculate_depth(self, node):
            if node is None:
                return 0
            else:
                return 1 + self.calculate_depth(node.left)