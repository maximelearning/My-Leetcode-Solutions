# https://leetcode.com/problems/diameter-of-binary-tree/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        def traversal(node: TreeNode) -> int:
            if node is None:
                return 0
            else:
                left = traversal(node.left)
                right = traversal(node.right)
                self.result = max(self.result, left + right)
                return max(left, right) + 1
        self.result = 0
        traversal(root)
        return self.result
