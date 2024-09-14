class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        MAX = max(nums)
        count = 0
        res = 0
        for num in nums:
            if num == MAX:
                count += 1
                res = max(res, count)
            else:
                count = 0
        return res