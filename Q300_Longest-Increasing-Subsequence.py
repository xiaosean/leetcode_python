class Solution:
    def lengthOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        if n < 2:
            return n
        dp_ = [1] * n
        for idx, num in enumerate(nums):
            for i in range(idx-1, -1, -1):
                if nums[i] < nums[idx]:
                    dp_[idx] = max(dp_[idx], dp_[i]+1)
        return max(dp_)
        
        