class Solution:
    def canPartition(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        if len(nums) < 2:
            return False
        sum_ = sum(nums)
        if sum_ % 2 == 1:
            return False
#         dp solution
        n = len(nums)
        dp = []
        target = sum_ // 2
        
        # for i in range(n):
        #     dp.append((target+1)*[False])
        #     dp[i][0] = True
        dp = (target+1) * [False]
        dp[0] = True
        # print(dp)
        for num in nums:
            for j in range(target, 0, -1):
                # num = nums[i]
                # dp[num][j] = dp[num-1][j]
                if j >= num:
                    dp[j] = dp[j] or dp[j-num]
                else:
                    break
        # print(dp)
        return dp[-1]
        