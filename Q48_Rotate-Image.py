class Solution:
    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """
        m_shape = len(matrix)
        x_shape = y_shape = m_shape
    #     transpose
        for i in range(x_shape):
            for j in range(i, y_shape):
                if j > i:
                    matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
    #     change col
        for col in range(int(x_shape/2)):
            for row in range(m_shape):
                matrix[row][col], matrix[row][x_shape-col-1] = matrix[row][x_shape-col-1], matrix[row][col]
        # return matrix