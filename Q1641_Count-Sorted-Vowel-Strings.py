class Solution:
    def countVowelStrings(self, n: int) -> int:
        if n == 0:
            return 0
        dp = [1, 1, 1, 1, 1]
        for i in range(n-1):
            next_dp = [1]
            for j in range(1, 5):
                next_dp += [next_dp[-1]+dp[j]]
            dp = next_dp
        return sum(dp)