"""
https://leetcode.com/problems/subtree-of-another-tree/

Given two non-empty binary trees s and t, check 
whether tree t has exactly the same structure and 
node values with a subtree of s. A subtree of s is 
a tree consists of a node in s and all of this node's 
descendants. The tree s could also be considered as a subtree of itself.

Example 1:
Given tree s:
     3
    / \
   4   5
  / \
 1   2
Given tree t:
   4 
  / \
 1   2
Return true, because t has the same structure and node values with a subtree of s.

Example 2:
Given tree s:
     3
    / \
   4   5
  / \
 1   2
    /
   0
Given tree t:
   4
  / \
 1   2
Return false. 
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def isSubtree(self, s: TreeNode, t: TreeNode) -> bool:
        if s is None:  # prevent accessing a NoneType
            return False
        elif self.traversal(s, t):
            return True
        else:  # check if the subtree is rooted at any other node
            return self.isSubtree(s.left, t) or self.isSubtree(s.right, t)

    def traversal(self, s, t):
        if s is None and t is None:  # terminates successfully
            return True
        elif s is None or t is None:  # false if one node is None, other None isn't
            return False
        elif s.val == t.val:  # continue traversing to check if matching
            return self.traversal(s.left, t.left) and self.traversal(s.right, t.right)
        else:
            return False  # two non-null nodes with differing values
