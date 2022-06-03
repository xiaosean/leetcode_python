class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        self.mat = matrix
        self.rows, self.cols = len(matrix), len(matrix[0])
        self.dp = [[0]*self.cols for i in range(self.rows)]
        
        # a[i, j] = a[i-1, j]+a[i, j-1]-a[i-1, j-1]
        for i in range(self.rows):
            for j in range(self.cols):
                self.dp[i][j] += self.mat[i][j]
                if i>0:
                    self.dp[i][j] += self.dp[i-1][j]
                if j > 0:
                    self.dp[i][j] += self.dp[i][j-1]
                if i>0 and j >0:
                    self.dp[i][j] -= self.dp[i-1][j-1]
    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        sum_ = self.dp[row2][col2]
        if row1-1 >= 0:
            sum_ -= self.dp[row1-1][col2]
        if col1-1 >= 0:
            sum_ -= self.dp[row2][col1-1]
        if row1-1 >= 0 and col1-1 >= 0:
            sum_ += self.dp[row1-1][col1-1]
        return sum_


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)