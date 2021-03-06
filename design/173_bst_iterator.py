"""
https://leetcode.com/problems/binary-search-tree-iterator/

Implement an iterator over a binary search tree (BST). 
Your iterator will be initialized with the root node of a BST.

Calling next() will return the next smallest number in the BST.

Example:
          7
         / \
        3   15
            / \
           9  20
BSTIterator iterator = new BSTIterator(root);
iterator.next();    // return 3
iterator.next();    // return 7
iterator.hasNext(); // return true
iterator.next();    // return 9
iterator.hasNext(); // return true
iterator.next();    // return 15
iterator.hasNext(); // return true
iterator.next();    // return 20
iterator.hasNext(); // return false

Note: IMPORTANT!!!!!!!

next() and hasNext() should run in average O(1) time and uses O(h) memory, 
where h is the height of the tree.

You may assume that next() call will always be valid, that is, there 
will be at least a next smallest number in the BST when next() is called.
"""


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class BSTIterator:

    def __init__(self, root: TreeNode):
        self.stack = []
        self.__fillStack(root)

    def next(self) -> int:
        """
        @return the next smallest number
        """
        node = self.stack.pop()
        self.__fillStack(node.right)
        return node.val

    def hasNext(self) -> bool:
        """
        @return whether we have a next smallest number
        """
        if len(self.stack) > 0:
            return True
        return False

    # Maintains an average of O(h) space, where h is the height of the tree
    def __fillStack(self, node):
        while node:
            self.stack.append(node)
            node = node.left


# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()
