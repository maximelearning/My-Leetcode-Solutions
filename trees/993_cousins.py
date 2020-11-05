"""
In a binary tree, the root node is at depth 0,
and children of each depth k node are at depth k+1.

Two nodes of a binary tree are cousins if they
have the same depth, but have different parents.

We are given the root of a binary tree with unique
values, and the values x and y of two different nodes in the tree.

Return true if and only if the nodes corresponding
to the values x and y are cousins.

Example 1:
            1
           / \
          2   3
         /
        4
Input: root = [1,2,3,4], x = 4, y = 3
Output: false

Example 2:
            1
           / \
          2   3
           \   \
            4   5
Input: root = [1,2,3,null,4,null,5], x = 5, y = 4
Output: true

Example 3:
            1
           / \
          2   3
           \
            4
Input: root = [1,2,3,null,4], x = 2, y = 3
Output: false
"""


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isCousins(self, root: TreeNode, x: int, y: int) -> bool:
        def traversal(node, lvl, parent):
            if node is None:
                return
            elif node.val == x or node.val == y:
                if parent:
                    self.parent_lvl.append((parent.val, lvl))
                else:
                    self.parent_lvl.append((None, lvl))
            traversal(node.left, lvl + 1, node)
            traversal(node.right, lvl + 1, node)

        self.parent_lvl = []
        traversal(root, 0, None)
        parent1, lvl1 = self.parent_lvl[0]
        parent2, lvl2 = self.parent_lvl[1]
        # Case where one of the target nodes is the root
        if parent1 is None or parent2 is None:
            return False
        if parent1 == parent2 or lvl1 != lvl2:
            return False
        return True
