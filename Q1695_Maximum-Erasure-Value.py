class Solution:
    def maximumUniqueSubarray(self, nums: List[int]) -> int:
        # brute O(N^2)
        num2ids = {}
        sum_dp = [0]
        duplicate_idx = 0
        res = 0
        for i, num in enumerate(nums):
            sum_dp += [num+sum_dp[-1]]
            if num not in num2ids:
                num2ids[num] = i
            else:
                duplicate_idx = max(duplicate_idx, num2ids[num]+1)
                num2ids[num] = i
            res = max(res, sum_dp[-1]-sum_dp[duplicate_idx])
        return res