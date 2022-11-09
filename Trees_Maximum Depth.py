def maxDepth(self, root):
    """
    :type root: TreeNode
    :rtype: int
    """
    if not root:
        return 0
    return max(self.maxDepth(root.right) + 1, self.maxDepth(root.left) + 1)