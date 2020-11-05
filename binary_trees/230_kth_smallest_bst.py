"""
https://leetcode.com/problems/kth-smallest-element-in-a-bst/

Given a binary search tree, write a 
function kthSmallest to find the kth smallest element in it.

Example 1:
Input: root = [3,1,4,null,2], k = 1
   3
  / \
 1   4
  \
   2
Output: 1

Example 2:
Input: root = [5,3,6,2,4,null,null,1], k = 3
       5
      / \
     3   6
    / \
   2   4
  /
 1
Output: 3
"""

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def kthSmallest(self, root: TreeNode, k: int) -> int:
        def traversal(node, arr):
            if node is None:
                return
            traversal(node.left, arr)
            # inorder traversal, append THEN check
            arr.append(node.val)
            if len(arr) == k:   # found the kth element, return
                self.res = arr[k-1]
                return
            if len(arr) > k:    # already found, prune this branch
                return
            traversal(node.right, arr)
        arr = []
        self.res = -1
        traversal(root, arr)
        return self.res