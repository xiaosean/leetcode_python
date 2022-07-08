class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        if len(s1) + len(s2) != len(s3):
            return False
        dp = [[0]*(len(s2)+1) for _ in range(len(s1)+1)]
        for i in range(len(s1)):
            dp[i+1][0] = dp[i][0] + (s3[dp[i][0]]==s1[i])
        for j in range(len(s2)):
            dp[0][j+1] = dp[0][j] + (s3[dp[0][j]]==s2[j])
        for i in range(1, len(s1)+1):
            for j in range(1, len(s2)+1):
                dp[i][j] = max(dp[i-1][j] + (s3[dp[i-1][j]] == s1[i-1]), dp[i][j-1] + (s3[dp[i][j-1]] == s2[j-1]))
        return dp[-1][-1] == len(s3)
                    