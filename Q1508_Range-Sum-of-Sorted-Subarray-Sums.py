class Solution:
    def rangeSum(self, nums: List[int], n: int, left: int, right: int) -> int:
        dp = []
        res = []
        for num in nums:
            for i in range(len(dp)):
                dp[i] += num
                res += [dp[i]]
            res += [num]
            dp += [num]
        res.sort()
        res = res[:int(n*(n+1)/2)]
        return sum(res[left-1:right])%(10**9+7)