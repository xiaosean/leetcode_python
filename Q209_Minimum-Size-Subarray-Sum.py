class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        # 2 pointer solutions
        cnt, sum_, start = len(nums)+1, 0, 0
        for end, num in enumerate(nums):
            sum_ += num
            while sum_ >= target:
                cnt = min(cnt, end-start+1)
                sum_ -= nums[start]
                start += 1
        return cnt if cnt <= len(nums) else 0
                