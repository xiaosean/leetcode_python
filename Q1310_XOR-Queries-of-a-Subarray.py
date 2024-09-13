class Solution:
    def xorQueries(self, arr: List[int], queries: List[List[int]]) -> List[int]:
        dp = [0]
        ans = 0
        for num in arr:
            ans = ans ^ num
            dp += [ans]
        res = []
        for l, r in queries:
            res += [dp[l]^dp[r+1]]
        return res

