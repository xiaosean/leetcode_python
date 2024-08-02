class Solution:
    def minSwaps(self, nums: List[int]) -> int:
        total_ones = sum(nums)
        n = len(nums)
        dp = [0]*n*2
        for idx in range(2*n):
            x = nums[idx%n]
            dp[idx] = dp[idx-1]+x
            if idx >= total_ones:
                dp[idx] -= nums[(idx-total_ones)%n]
        return total_ones-max(dp)