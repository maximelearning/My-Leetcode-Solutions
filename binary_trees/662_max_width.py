def widthOfBinaryTree(self, root: TreeNode) -> int:
    def traversal(node, arr, lvl):
        if node is None:
            if len(arr) - 1 < lvl:
                arr.append([])
            arr[lvl].append(1)
        else:
            if len(arr) - 1 < lvl:
                arr.append([])
            arr[lvl].append(1)
            traversal(node.left, arr, lvl + 1)
            traversal(node.right, arr, lvl + 1)

    levels = []
    traversal(root, levels, 0)
    m = 0
    for e in levels:
        m = max(m, len(e))
    return m
