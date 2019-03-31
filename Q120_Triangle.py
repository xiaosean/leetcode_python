class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        n = len(triangle)
        dp = []
        for depth in range(n-1, -1, -1):
            depth_min = []
            for i in range(len(triangle[depth])):
                bottom_sum = 0
                if dp:
                    bottom_sum = min(dp[i], dp[i+1]) 
                depth_min += [bottom_sum + triangle[depth][i]]
            dp = depth_min
        return min(dp)