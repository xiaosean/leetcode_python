class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        h, w = len(points), len(points[0])
        dp = [[0]*w for _ in range(h)]
        for i in range(h-1):
            temp = dp[i][-1]
            for j in range(w-2,-1,-1):
                points[i][j] = max(points[i][j+1]-1, points[i][j])
            for j in range(w):
                points[i][j] = max(points[i][j], points[i][j-1]-1 if j else 0)
                points[i+1][j] += points[i][j]
            
        return max(points[-1])