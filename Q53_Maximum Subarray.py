class Solution:
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) > 0:
            max_sum_ = nums[0]
        else:
            return None
        sum_ = 0
        for num in nums:
            sum_ += num
            if sum_ > max_sum_:
                max_sum_ = sum_
            if sum_ < 0:
                sum_ = 0

        return max_sum_
