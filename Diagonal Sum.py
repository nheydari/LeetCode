def diagonalSum(self, mat):
    """
    :type mat: List[List[int]]
    :rtype: int
    """
    R = len(mat)
    sum_diag = 0
    print(R)
    for i in (range(R)):
        sum_diag += mat[i][i]
        sum_diag += mat[i][R - i - 1]
    if R % 2 != 0:
        sum_diag -= mat[R // 2][R // 2]
    return sum_diag