def countBits(self, n):
    """
    :type n: int
    :rtype: List[int]
    """
    ans = [0] * (n + 1)
    for i in range(n + 1):
        j = i
        while j > 0:
            ans[i] = ans[i] + j % 2
            j = j >> 1
    return ans