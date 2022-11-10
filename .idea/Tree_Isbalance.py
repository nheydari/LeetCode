def isBalanced(self, root):
    """
    :type root: TreeNode
    :rtype: bool
    """

    def dfs(root):
        if not root:
            return [True, 0]
        left = dfs(root.left)
        right = dfs(root.right)
        bal = right[0] and left[0] and abs(right[1] - left[1]) <= 1
        return [bal, 1 + max(left[1], right[1])]

    return dfs(root)[0]