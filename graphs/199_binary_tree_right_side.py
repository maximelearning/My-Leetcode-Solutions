# https://leetcode.com/problems/binary-tree-right-side-view/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: TreeNode) -> List[int]:
        if root is None:
            return []
        res = [root.val]
        self.traverse(root, res, 1)
        return res

    def traverse(self, node: TreeNode, res: List[int], depth: int):
        if node is None:
            return
        if depth > len(res):
            res.append(node.val)
        self.traverse(node.right, res, depth + 1)
        self.traverse(node.left, res, depth + 1)
