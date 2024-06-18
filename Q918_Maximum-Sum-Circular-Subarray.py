class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        cur_sum, cur_positive, cur_negative, max_positive,max_negative = 0, 0, 0, nums[0], nums[0]
        for idx, num in enumerate(nums):
            cur_sum += num
            cur_positive = max(cur_positive+num, num)
            max_positive = max(max_positive, cur_positive)
            cur_negative = min(cur_negative+num, num)
            max_negative = min(max_negative, cur_negative)
        return max(max_positive, cur_sum-max_negative) if max_positive>0 else max_positive