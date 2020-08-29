# https://leetcode.com/problems/binary-tree-maximum-path-sum/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
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
