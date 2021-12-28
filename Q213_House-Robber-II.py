class Solution:
    def rob(self, nums: List[int]) -> int:
        def rob_helper(nums):
            dp1, dp2 = 0, 0
            for num in nums:
                dp1, dp2 = dp2, max(dp1 + num, dp2)
            return dp2
        return max(rob_helper(nums[:-1]), rob_helper(nums[1:]), nums[0])