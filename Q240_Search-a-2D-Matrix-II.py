class Solution:
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        if matrix is None:
            return False
        row_shape = len(matrix)
        if row_shape == 0:
            return False
        col_shape = len(matrix[0])
        if col_shape == 0:
            return False
        if target < matrix[0][0] or target > matrix[row_shape-1][col_shape-1]:
            return False
            
        down, right = 0, col_shape-1
        
        while right >= 0 and down < row_shape:
            if target == matrix[down][right]:
                return True
            if target < matrix[down][right]:
                right -= 1
            else:
                down += 1
            
        return False
        