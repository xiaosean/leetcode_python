class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        n = len(nums)
        if n < 1:
            return None
        last_num = nums[0]-1
        idx = 0
        while idx < len(nums):
            num = nums[idx]
            if num == last_num:
                idx -= 1
                del nums[idx]
            last_num = num
            idx += 1
            