class Solution:
    def PredictTheWinner(self, nums: List[int]) -> bool:
        n = len(nums)
        dp = [[0] * n for _ in range(n)]
        def minmax(nums, s, e, turn=True):
            if s >= e:
                return 0

            if dp[s+1][e]:
                point1 = turn*nums[s] -turn * dp[s+1][e]
            else:    
                point1 = turn*nums[s] + minmax(nums, s+1, e,-turn)
                
            if dp[s][e-1]:
                point2 = turn*nums[e] -turn * dp[s][e-1]
            else:
                point2 = turn*nums[e] + minmax(nums[:-1], s, e-1, -turn)
            max_val = max(turn*point1, turn*point2)
            dp[s][e] = max(turn*point1, turn*point2)    
            return turn*(dp[s][e])
        return minmax(nums, s=0, e=len(nums)-1) >= 0
