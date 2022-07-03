class Solution:
    def wiggleMaxLength(self, nums: List[int]) -> int:
        diff_list = []
        dp = [0] * (len(nums)-1)
        positive_idx, negative_idx = None, None
        longest = 0
        for idx, (x, y) in enumerate(zip(nums[:-1], nums[1:])):
            diff = y-x
            if diff > 0:
                positive_idx = idx
                if negative_idx is not None:
                    dp[idx] = dp[negative_idx] + 1
                else:
                    dp[idx] = 1
            elif diff < 0:
                negative_idx = idx
                if positive_idx is not None:
                    dp[idx] = dp[positive_idx] + 1
                else:
                    dp[idx] = 1
        return max(dp)+1 if len(nums) > 1 else len(nums)