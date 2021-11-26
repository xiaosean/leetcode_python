class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        if not obstacleGrid:
            return 0
        n, m = len(obstacleGrid), len(obstacleGrid[0])
        paths = [[1]*m for _ in range(n)]
        # quick check if have a row or column are all 1
        obstacle_flag = False
        for i in range(n):
            if obstacleGrid[i][0] == 1:
                obstacle_flag = True
            if obstacle_flag:
                paths[i][0] = 0
        obstacle_flag = False
        for i in range(m):
            if obstacleGrid[0][i] == 1:
                obstacle_flag = True
            if obstacle_flag:
                paths[0][i] = 0
        for i in range(n):
            for j in range(m):
                if obstacleGrid[i][j] == 1:
                    paths[i][j] = 0
                elif i > 0 and j > 0:
                    paths[i][j] = paths[i-1][j] + paths[i][j-1]
        return paths[-1][-1]
                
                
        