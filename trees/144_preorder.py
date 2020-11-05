"""
Given the root of a binary tree, return the preorder traversal of its nodes' values.

Example 1:
Input: root = [1,null,2,3]
            1
             \
              2
             /
            3
Output: [1,2,3]

Example 2:
Input: root = []
Output: []

Example 3:
Input: root = [1]
Output: [1]

Example 4:
            1
           /
          2
Input: root = [1,2]
Output: [1,2]

Example 5:
            1
             \
              2
Input: root = [1,null,2]
Output: [1,2]

Constraints:

    The number of nodes in the tree is in the range [0, 100].
    -100 <= Node.val <= 100

Follow up:

Recursive solution is trivial, could you do it iteratively?
"""


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def preorderTraversal(self, root: TreeNode) -> List[int]:
        stack = []
        res = []
        while True:
            while root:
                stack.append(root.right)
                res.append(root.val)
                root = root.left
            if len(stack) == 0:
                return res
            root = stack.pop()
        return res
