"""
Given two binary trees and imagine that when you put one 
of them to cover the other, some nodes of the two trees are 
overlapped while the others are not.

You need to merge them into a new binary tree. The merge rule 
is that if two nodes overlap, then sum node values up as the new 
value of the merged node. Otherwise, the NOT null node will be used 
as the node of new tree.

Example 1:
Input: 
	Tree 1                     Tree 2                  
          1                         2                             
         / \                       / \                            
        3   2                     1   3                        
       /                           \   \                      
      5                             4   7                  
Output: 
Merged tree:
	     3
	    / \
	   4   5
	  / \   \ 
	 5   4   7

Note: The merging process must start from the root nodes of both trees.
"""


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def mergeTrees(self, t1: TreeNode, t2: TreeNode) -> TreeNode:
        def traversal(node1, node2):
            if node1 is None and node2 is None:
                return None
            elif node1 is None:
                return node2
            elif node2 is None:
                return node1
            node = TreeNode(node1.val + node2.val)
            node.left = traversal(node1.left, node2.left)
            node.right = traversal(node1.right, node2.right)
            return node
        node = traversal(t1, t2)
        return node
