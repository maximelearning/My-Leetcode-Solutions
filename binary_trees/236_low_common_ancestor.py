"""
https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-tree/

Given a binary tree, find the lowest common ancestor 
(LCA) of two given nodes in the tree.

According to the definition of LCA on Wikipedia: 
“The lowest common ancestor is defined between 
two nodes p and q as the lowest node in T that 
has both p and q as descendants (where we allow 
a node to be a descendant of itself).”

Example 1:
                  3 
                /   \
               5     1 
              / \    / \
             6   2  0   8 
                /  \
               7    4 
Input: root = [3,5,1,6,2,0,8,null,null,7,4], p = 5, q = 1
Output: 3
Explanation: The LCA of nodes 5 and 1 is 3.

Example 2:
                  3 
                /   \
               5     1 
              / \    / \
             6   2  0   8 
                /  \
               7    4 
Input: root = [3,5,1,6,2,0,8,null,null,7,4], p = 5, q = 4
Output: 5
Explanation: The LCA of nodes 5 and 4 is 5, since a node can be a descendant of itself according to the LCA definition.

Example 3
Input: root = [1,2], p = 1, q = 2
Output: 1
"""


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        def traversal(node, p, q):
            if node is None:
                return None
            # if a node matches, we don't care about going any deeper
            elif node == p or node == q:
                return node
            left = traversal(node.left, p, q)
            right = traversal(node.right, p, q)
            if left and right:
                return node
            elif left:
                return left
            elif right:
                return right
        return traversal(root, p, q)
