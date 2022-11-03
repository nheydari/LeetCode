def rotate(self, matrix):
    """
    :type matrix: List[List[int]]
    :rtype: None Do not return anything, modify matrix in-place instead.
    """
    R = len(matrix)
    C = len(matrix[0])
    for i in range(R // 2 + R % 2):
        for j in range(C // 2):
            # flip diagonally
            tmp = matrix[i][j]
            matrix[i][j] = matrix[C - j - 1][i]
            matrix[C - j - 1][i] = matrix[C - i - 1][C - j - 1]
            matrix[C - i - 1][C - j - 1] = matrix[j][C - i - 1]
            matrix[j][C - i - 1] = tmp