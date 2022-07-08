class Solution:
    def candy(self, ratings: List[int]) -> int:
        if not ratings:
            return 0
        ratings = [ratings[0]] + ratings + [ratings[-1]]
        n = len(ratings)
        dp = [1]*len(ratings)
        for i in range(1, n):
            if ratings[i]-ratings[i-1]>0:
                dp[i] = dp[i-1] + 1
        for i in range(n-1, 0, -1):
            if ratings[i-1]-ratings[i]>0:
                dp[i-1] = max(dp[i] + 1, dp[i-1])
        return sum(dp[1:-1])