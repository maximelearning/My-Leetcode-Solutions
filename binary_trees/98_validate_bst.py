"""
https://leetcode.com/problems/validate-binary-search-tree/

Given a binary tree, determine if it is a valid binary search tree (BST).

Assume a BST is defined as follows:

The left subtree of a node contains only nodes with keys less than the node's key.
The right subtree of a node contains only nodes with keys greater than the node's key.
Both the left and right subtrees must also be binary search trees.
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        inorder = []
        self.traversal(inorder, root)
        if len(inorder) <= 1:
            return True
        for i in range(len(inorder) - 1):
            if inorder[i] >= inorder[i + 1]:
                return False
        return True

    def traversal(self, inorder: List[int], node: TreeNode) -> None:
        if node is None:
            return
        else:
            self.traversal(inorder, node.left)
            inorder.append(node.val)
            self.traversal(inorder, node.right)
