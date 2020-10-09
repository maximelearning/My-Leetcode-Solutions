"""
https://leetcode.com/problems/sum-of-root-to-leaf-binary-numbers/

You are given the root of a binary tree where each node has a value 0 or 1.  
Each root-to-leaf path represents a binary number starting with the most 
significant bit.  For example, if the path is 0 -> 1 -> 1 -> 0 -> 1, 
then this could represent 01101 in binary, which is 13.
For all leaves in the tree, consider the numbers represented 
by the path from the root to that leaf.
Return the sum of these numbers. The answer is 
guaranteed to fit in a 32-bits integer.

Example 1:
Input: root = [1,0,1,0,1,0,1]
Output: 22
Explanation: (100) + (101) + (110) + (111) = 4 + 5 + 6 + 7 = 22

Example 2:
Input: root = [0]
Output: 0

Example 3:
Input: root = [1]
Output: 1

Example 4:
Input: root = [1,1]
Output: 3
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def sumRootToLeaf(self, root):
        def dfs(node, prefix):
            if node:
                prefix = node.val + (prefix << 1)
                if node.left or node.right:
                    return dfs(node.left, prefix) + dfs(node.right, prefix)
                else:
                    return prefix
            else:
                return 0
        return dfs(root, 0)
