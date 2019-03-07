class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        row = []
        col = []
        if len(matrix) == 0:
            return
        if len(matrix[0]) == 0:
            return
        h, w = len(matrix), len(matrix[0])
        
        for i in range(h):
            for j in range(w):
                if matrix[i][j] == 0:
                    row += [i]
                    col += [j]
        row = list(set(row))
        col = list(set(col))
        for i in row:
            for j in range(w):
                matrix[i][j] = 0
        for i in col:
            for j in range(h):
                matrix[j][i] = 0