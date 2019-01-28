class Solution:
    def maximalSquare(self, matrix):
        """
        :type matrix: List[List[str]]
        :rtype: int
        """
        if len(matrix) < 1 or len(matrix[0]) < 1:
            return 0
        r_size, c_size = len(matrix), len(matrix[0])
        dp_mat = [[0] * (c_size+1) for _ in range(r_size+1)]
        max_length = 0
        for r_idx in range(r_size):
            for c_idx in range(c_size):
                if matrix[r_idx][c_idx] == "1":
                    dp_mat[r_idx+1][c_idx+1] = min(min(dp_mat[r_idx+1][c_idx], dp_mat[r_idx][c_idx])
                                                   , dp_mat[r_idx][c_idx+1]) + 1
                    max_length = max(max_length, dp_mat[r_idx+1][c_idx+1])  
        return max_length**2