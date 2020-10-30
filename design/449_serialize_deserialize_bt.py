"""
https://leetcode.com/problems/serialize-and-deserialize-bst/

Serialization is converting a data structure or 
object into a sequence of bits so that it can be 
stored in a file or memory buffer, or transmitted 
across a network connection link to be reconstructed 
later in the same or another computer environment.

Design an algorithm to serialize and deserialize a 
binary search tree. There is no restriction on how 
your serialization/deserialization algorithm should 
work. You need to ensure that a binary search tree 
can be serialized to a string, and this string can 
be deserialized to the original tree structure.

The encoded string should be as compact as possible.

Example 1:

Input: root = [2,1,3]
Output: [2,1,3]
Example 2:

Input: root = []
Output: []

Constraints:

The number of nodes in the tree is in the range [0, 104].
0 <= Node.val <= 104
The input tree is guaranteed to be a binary search tree.
"""


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Codec:

    def serialize(self, root: TreeNode) -> str:
        """Encodes a tree to a single string.
        """
        # Preorder traversal, where all the nodes are
        # codes with their values, separated by commas,
        # and nulls are "-" and return on nulls.
        def traversal(node):
            if node is None:
                self.res += "-,"
                return
            self.res += str(node.val) + ","
            traversal(node.left)
            traversal(node.right)
        self.res = ""
        traversal(root)
        return self.res[0:len(self.res) - 1]

    def deserialize(self, data: str) -> TreeNode:
        """Decodes your encoded data to tree.
        """
        # Do a preorder traversal, building the the
        # tree from left to right of the string, keeping a global index
        # of the next element in the string, which is also
        # the next element in the current stack frame.
        def traversal():
            if self.data[self.index] == "-":
                self.index += 1
                return None
            else:
                node = TreeNode(self.data[self.index])
                self.index += 1
                node.left = traversal()
                node.right = traversal()
            return node
        self.data = data.split(",")
        self.index = 0
        return traversal()


# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# tree = ser.serialize(root)
# ans = deser.deserialize(tree)
# return ans
