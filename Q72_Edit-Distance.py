class Solution:
    def minDistance(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: int
        """
        m = len(word1)
        n = len(word2)
        dp = [[0 for i in range(n+1)] for j in range(m+1)]
    #     i word1, j word 2
        for i in range(m+1):
            for j in range(n+1):
                # init shift count
                if i== 0:
                    dp[i][j] = j
                elif j == 0:
                    dp[i][j] = i
                # same letter don't add count
                elif word1[i-1] == word2[j-1]:
                    dp[i][j] = dp[i-1][j-1]
                else:
    #                 else condition get minimum
                    insert = dp[i][j-1]
                    delete = dp[i-1][j]
                    replace = dp[i-1][j-1]
                    dp[i][j] = 1 + min(insert, delete, replace)
        return dp[m][n]   