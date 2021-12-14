class Solution:
    def rob(self, nums: List[int]) -> int:
        # dfs with 3 mode: cooldown, take and wait
            # do until no numbers
            # each turn, if it is not cooldown period, we can choose take or wait
#         def house_robber(nums, res=0, cooldown=False):
#             if not nums:
#                 return res
#             if cooldown:
#                 # skip this number
#                 return house_robber(nums[1:], res=res, cooldown=False)
#             take = house_robber(nums[1:], res=res+nums[0], cooldown=True)
#             wait = house_robber(nums[1:], res=res, cooldown=False)
#             return max(take, wait)
#         return house_robber(nums)
        n = len(nums)
        dp = [0] * (n+2)
        for idx, num in enumerate(nums):
            shift_idx = 2 
            # take or cooldown or wait
            # take
            dp[idx+shift_idx] = max(dp[idx] + num, dp[idx+1])
        return dp[-1]