def diameterOfBinaryTree(self, root):
    """
    :type root: TreeNode
    :rtype: int
    """
    diam = [0]

    def LenghtTree(root):
        if not root:
            return -1
        left = LenghtTree(root.left)
        right = LenghtTree(root.right)
        diam[0] = max(diam[0], 2 + right + left)
        return 1 + max(left, right)

    LenghtTree(root)
    return diam[0]