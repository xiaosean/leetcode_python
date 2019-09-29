class Solution:
    def findLengthOfLCIS(self, nums: List[int]) -> int:
        if not nums:
            return 0
        max_count = 1
        count = 1
        max_val = nums[0]
        for num in nums[1:]:
            if num > max_val:
                max_val = num
                count += 1
                max_count = max(max_count, count)
            else:
                max_val = num
                count = 1
        return max_count
                