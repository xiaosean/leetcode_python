class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        # knapsack
        dp = [1] + [0]*target
        for i in range(1, target+1):
            for num in nums:
                if i >= num and dp[i-num]:
                    dp[i] += dp[i-num]
        return dp[-1]