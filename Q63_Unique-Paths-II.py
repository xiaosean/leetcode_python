class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        if not obstacleGrid:
            return 0
        m, n = len(obstacleGrid), len(obstacleGrid[0])
        dp = [[None] *(n+1) for _ in range(m+1)]
        for i in range(m+1):
            dp[i][0] = 0
        for i in range(n+1):
            dp[0][i] = 0
        dp[1][1] = 1
        if obstacleGrid[0][0] == 1:
            return 0
        for r_id in range(m):
            for c_id in range(n):
                item = obstacleGrid[r_id][c_id]
                if dp[r_id+1][c_id+1] is None:
                    if item == 1:
                        dp[r_id+1][c_id+1] = 0
                    else:
                        dp[r_id+1][c_id+1] = dp[r_id][c_id+1] + dp[r_id+1][c_id]
        return dp[-1][-1]