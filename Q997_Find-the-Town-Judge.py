class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        # find one guy be trusted - count: n-1
        # that guy doesn't trust every one
        # count each guys trust or not, pick the count equals n-1 and make sure no one > n-1
        dp = [0] * (n+1)
        count_map = [0] * (n+1)
        for people, be_trust in trust:
            dp[be_trust] += 1
            count_map[people] += 1
        res = -1
        for i in range(1, n+1):
            if dp[i] >= n:
                return -1
            elif dp[i] == n-1 and count_map[i]==0:
                if res != -1:
                    return -1
                res = i
        return res