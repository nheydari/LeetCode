def isSameTree(self, p, q):
    """
    :type p: TreeNode
    :type q: TreeNode
    :rtype: bool
    """
    if not p and not q:
        return True
    if not p or not q or p.val != q.val:
        return False
    if p.val == q.val:
        return self.isSameTree(p.right, q.right) and self.isSameTree(p.left, q.left)